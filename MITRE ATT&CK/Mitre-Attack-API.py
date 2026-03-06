#!/usr/bin/env python3
"""
MITRE ATT&CK Sigma Coverage Dashboard

Scans a Sigma rules directory, extracts attack.TXXXX and cve.* tags,
compares them against the official MITRE ATT&CK Enterprise matrix, and generates:
  1. HTML visual matrix (ATT&CK Navigator style)  → coverage_dashboard.html
  2. Markdown report   (Obsidian-compatible)       → coverage_report.md
  3. Terminal CLI summary                          → stdout

Tactic order, names, and all technique data are fetched dynamically from the
official MITRE CTI STIX bundle — nothing is hardcoded.

Dependencies:
  pip install pyyaml requests
"""

import sys
import json
import re
import html as html_lib
from pathlib import Path
from collections import defaultdict
from datetime import datetime

try:
    import yaml
    import requests
except ImportError:
    sys.exit("Missing dependencies. Run:\n  pip install pyyaml requests")


# ═══════════════════════════════════════════════════════════════════════════════
#  CONFIGURATION  ← edit here
# ═══════════════════════════════════════════════════════════════════════════════

SIGMA_RULES_DIR = "/opt/cso/sigma-rules"   # path to your sigma rules

OUTPUT_DIR  = Path(__file__).parent
CACHE_FILE  = OUTPUT_DIR / "attack_data_cache.json"
HTML_OUTPUT = OUTPUT_DIR / "coverage_dashboard.html"
MD_OUTPUT   = OUTPUT_DIR / "coverage_report.md"

STIX_URL = (
    "https://raw.githubusercontent.com/mitre/cti/master/"
    "enterprise-attack/enterprise-attack.json"
)


# ═══════════════════════════════════════════════════════════════════════════════
#  1. LOAD ATT&CK DATA  (cached locally after first fetch)
# ═══════════════════════════════════════════════════════════════════════════════

def load_attack_data():
    """Fetch (or load from local cache) the MITRE ATT&CK Enterprise STIX bundle."""
    if CACHE_FILE.exists():
        print(f"[cache] Loading ATT&CK data from {CACHE_FILE.name} ...")
        return json.loads(CACHE_FILE.read_text())
    print("[net]   Fetching ATT&CK STIX bundle from MITRE CTI GitHub ...")
    r = requests.get(STIX_URL, timeout=90)
    r.raise_for_status()
    data = r.json()
    CACHE_FILE.write_text(json.dumps(data))
    print(f"[cache] Saved to {CACHE_FILE}")
    return data


def parse_attack_matrix(stix_data):
    """
    Parse the STIX bundle and extract:
      tactics    — ordered list of dicts: {stix_id, id (TA####), name, short_name}
                   ordered via the x-mitre-matrix object (canonical MITRE order)
      techniques — dict[tech_id] = {id, name, tactics, is_sub, parent_id}

    Nothing is hardcoded: tactic order and names come from the STIX data itself.
    """
    objects = stix_data["objects"]

    # ── Step A: collect x-mitre-tactic objects keyed by STIX ID ──────────────
    stix_tactic_map = {}
    for obj in objects:
        if obj.get("type") == "x-mitre-tactic":
            stix_tactic_map[obj["id"]] = obj

    # ── Step B: find x-mitre-matrix → gives canonical tactic order ───────────
    tactic_order_refs = []
    for obj in objects:
        if obj.get("type") == "x-mitre-matrix":
            tactic_order_refs = obj.get("tactic_refs", [])
            break   # enterprise matrix is first (and only) one we need

    # ── Step C: build ordered tactics list ───────────────────────────────────
    tactics = []
    for stix_id in tactic_order_refs:
        tac_obj = stix_tactic_map.get(stix_id)
        if not tac_obj:
            continue
        refs   = tac_obj.get("external_references", [])
        tac_id = next(
            (r["external_id"] for r in refs if r.get("source_name") == "mitre-attack"),
            None,
        )
        tactics.append({
            "stix_id":    stix_id,
            "id":         tac_id,          # e.g. TA0001
            "name":       tac_obj["name"], # e.g. "Initial Access"
            "short_name": tac_obj.get("x_mitre_shortname", ""),  # e.g. "initial-access"
        })

    # ── Step D: parse attack-pattern (technique / sub-technique) objects ──────
    techniques = {}
    for obj in objects:
        if obj.get("type") != "attack-pattern":
            continue
        if obj.get("x_mitre_deprecated") or obj.get("revoked"):
            continue
        refs    = obj.get("external_references", [])
        tech_id = next(
            (r["external_id"] for r in refs if r.get("source_name") == "mitre-attack"),
            None,
        )
        if not tech_id or not tech_id.startswith("T"):
            continue
        tactic_phases = [
            p["phase_name"]
            for p in obj.get("kill_chain_phases", [])
            if p.get("kill_chain_name") == "mitre-attack"
        ]
        is_sub    = obj.get("x_mitre_is_subtechnique", False)
        parent_id = tech_id.rsplit(".", 1)[0] if is_sub and "." in tech_id else None
        techniques[tech_id] = {
            "id":        tech_id,
            "name":      obj["name"],
            "tactics":   tactic_phases,   # list of short_names, e.g. ["initial-access"]
            "is_sub":    is_sub,
            "parent_id": parent_id,
        }

    return tactics, techniques


# ═══════════════════════════════════════════════════════════════════════════════
#  2. LOAD SIGMA RULES
# ═══════════════════════════════════════════════════════════════════════════════

def load_sigma_rules(sigma_dir):
    """
    Walk sigma_dir recursively, parse every .yml file, extract tags.
    Returns:
      coverage        — dict[tech_id]      → list of rule titles
      cves            — dict[cve_id]       → list of rule titles
      tactic_coverage — dict[tactic_short] → list of rule titles
      total, errors   — int
    """
    coverage        = defaultdict(list)
    cves            = defaultdict(list)
    tactic_coverage = defaultdict(list)
    total = errors  = 0

    sigma_path = Path(sigma_dir)
    if not sigma_path.exists():
        print(f"[warn]  Sigma directory not found: {sigma_dir}")
        print("[warn]  Running in demo mode — coverage will be empty.")
        return coverage, cves, tactic_coverage, 0, 0

    for yml_file in sigma_path.rglob("*.yml"):
        total += 1
        try:
            text = yml_file.read_text(encoding="utf-8", errors="ignore")
            docs = list(yaml.safe_load_all(text))
            rule = next((d for d in docs if isinstance(d, dict)), None)
            if not rule:
                continue
            rule_id   = str(rule.get("id", "")).strip()
            rule_name = rule.get("title", yml_file.stem)
            rule_entry = (rule_id, rule_name)
            for tag in rule.get("tags", []) or []:
                tag = str(tag).lower().strip()
                # attack.tXXXX  or  attack.tXXXX.XXX
                if re.match(r"^attack\.t\d{4}(\.\d{3})?$", tag):
                    tech_id = tag[len("attack."):].upper()
                    coverage[tech_id].append(rule_entry)
                # attack.tactic_name  →  initial_access, defense_evasion, …
                elif tag.startswith("attack."):
                    tactic = tag[len("attack."):].replace("_", "-")
                    tactic_coverage[tactic].append(rule_name)
                # cve.YYYY-NNNNN
                elif re.match(r"^cve\.\d{4}-\d+$", tag):
                    cve_id = "CVE-" + tag[4:].upper()
                    cves[cve_id].append(rule_entry)
        except Exception:
            errors += 1

    return coverage, cves, tactic_coverage, total, errors


# ═══════════════════════════════════════════════════════════════════════════════
#  3. HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

def cell_style(count):
    """Return (background_color, text_color) based on rule count."""
    if count == 0: return "#2d2d3a", "#555"
    if count == 1: return "#7b6000", "#ffd54f"
    if count <= 3: return "#1b5e20", "#a5d6a7"
    if count <= 6: return "#2e7d32", "#c8e6c9"
    return                "#1565c0", "#bbdefb"


def coverage_stats(techniques, coverage):
    covered = sum(1 for tid in techniques if coverage[tid])
    total   = len(techniques)
    pct     = round(covered / total * 100, 1) if total else 0.0
    return covered, total, pct


def _group_by_tactic(techniques):
    """Returns (tactic_techs, subtechs) dicts keyed by tactic short_name / parent_id."""
    tactic_techs = defaultdict(list)
    subtechs     = defaultdict(list)
    for tech in techniques.values():
        if tech["is_sub"]:
            if tech["parent_id"]:
                subtechs[tech["parent_id"]].append(tech)
        else:
            for tac in tech["tactics"]:
                tactic_techs[tac].append(tech)
    for tac in tactic_techs:
        tactic_techs[tac].sort(key=lambda t: t["id"])
    for pid in subtechs:
        subtechs[pid].sort(key=lambda t: t["id"])
    return tactic_techs, subtechs


# ═══════════════════════════════════════════════════════════════════════════════
#  4. HTML DASHBOARD
# ═══════════════════════════════════════════════════════════════════════════════

def generate_html(tactics, techniques, coverage, cves, sigma_dir, total_rules, errors):
    tactic_techs, subtechs = _group_by_tactic(techniques)
    covered, total_techs, pct = coverage_stats(techniques, coverage)
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M")

    def _tooltip(tid, name, rules):
        tip = f"{tid}: {name}\nRules ({len(rules)}):"
        for r in rules[:15]:
            rid, rname = r
            prefix = f"[{rid[:8]}] " if rid else ""
            tip += f"\n  • {prefix}{rname}"
        if len(rules) > 15:
            tip += f"\n  … and {len(rules) - 15} more"
        return html_lib.escape(tip)

    def _sub_cell(st):
        count    = len(coverage[st["id"]])
        bg, fg   = cell_style(count)
        name_esc = html_lib.escape(st["name"])
        tip      = _tooltip(st["id"], st["name"], coverage[st["id"]])
        interactive = (
            f' data-tid="{st["id"]}" data-name="{name_esc}" data-clickable="1"'
            f' onclick="showRulesPanel(this)"'
        ) if count > 0 else ""
        return (
            f'<div class="subtechnique" style="background:{bg};color:{fg}" title="{tip}"{interactive}>'
            f'<span class="tid">{st["id"]}</span>'
            f'<span class="sname">{name_esc}</span>'
            f'<span class="badge">{count}</span>'
            f'</div>'
        )

    def _tech_cell(tech):
        tid      = tech["id"]
        rules    = coverage[tid]
        count    = len(rules)
        bg, fg   = cell_style(count)
        name_esc = html_lib.escape(tech["name"])
        tip      = _tooltip(tid, tech["name"], rules)
        interactive = (
            f' data-tid="{tid}" data-name="{name_esc}" data-clickable="1"'
            f' onclick="showRulesPanel(this)"'
        ) if count > 0 else ""
        sub_html = ""
        if tid in subtechs:
            sub_html = (
                '<div class="subtechs">'
                + "".join(_sub_cell(s) for s in subtechs[tid])
                + "</div>"
            )
        return (
            f'<div class="technique" style="background:{bg};color:{fg}" title="{tip}"{interactive}>'
            f'<div class="tech-header">'
            f'<span class="tid">{tid}</span>'
            f'<span class="tname">{name_esc}</span>'
            f'<span class="badge">{count}</span>'
            f'</div>{sub_html}</div>'
        )

    # ── Matrix columns (ordered by tactics list from STIX) ───────────────────
    columns_html = ""
    for tac in tactics:
        short    = tac["short_name"]
        techs    = tactic_techs.get(short, [])
        tac_cov  = sum(1 for t in techs if coverage[t["id"]])
        cells    = "".join(_tech_cell(t) for t in techs)
        columns_html += (
            f'<div class="tactic-col">'
            f'<div class="tactic-header" title="{tac["id"]}">'
            f'<div class="tactic-name">{html_lib.escape(tac["name"])}</div>'
            f'<div class="tactic-meta">{tac_cov}/{len(techs)}</div>'
            f'</div>'
            f'<div class="techniques">{cells}</div>'
            f'</div>'
        )

    # ── Legend ───────────────────────────────────────────────────────────────
    legend_items = [
        ("#2d2d3a", "#555",    "No coverage"),
        ("#7b6000", "#ffd54f", "1 rule"),
        ("#1b5e20", "#a5d6a7", "2–3 rules"),
        ("#2e7d32", "#c8e6c9", "4–6 rules"),
        ("#1565c0", "#bbdefb", "7+ rules"),
    ]
    legend_html = "".join(
        f'<div class="legend-item">'
        f'<div class="legend-box" style="background:{bg};border:1px solid {fg}"></div>'
        f'<span>{label}</span></div>'
        for bg, fg, label in legend_items
    )

    # ── CVE section ───────────────────────────────────────────────────────────
    cve_html = ""
    if cves:
        cve_rows = "".join(
            f'<tr><td><code>{cve_id}</code></td><td>{len(rules)}</td>'
            f'<td>{html_lib.escape(", ".join(r[1] for r in rules[:5]))}'
            f'{"…" if len(rules) > 5 else ""}</td></tr>'
            for cve_id, rules in sorted(cves.items())
        )
        cve_html = (
            f'<div class="section">'
            f'<h2>CVE Coverage <span class="count-badge">{len(cves)}</span></h2>'
            f'<table class="cve-table">'
            f'<thead><tr><th>CVE ID</th><th>Rules</th><th>Rule Titles</th></tr></thead>'
            f'<tbody>{cve_rows}</tbody>'
            f'</table></div>'
        )

    # Build JS rules lookup: {tid: [[rule_id, rule_name], ...]}
    rules_js_data = {
        tid: [[r[0], r[1]] for r in rules]
        for tid, rules in coverage.items()
        if rules and tid in techniques
    }
    rules_js = json.dumps(rules_js_data, ensure_ascii=False)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>MITRE ATT&amp;CK Coverage Dashboard</title>
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    background: #12121e; color: #e0e0e0; font-size: 13px;
  }}
  .header {{
    padding: 18px 28px 14px;
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    border-bottom: 2px solid #e94560;
  }}
  .header h1 {{ font-size: 1.5rem; color: #e94560; letter-spacing: .5px; margin-bottom: 4px; }}
  .header .meta {{ font-size: .78rem; color: #888; }}
  .stats {{
    display: flex; gap: 14px; padding: 14px 28px;
    background: #16213e; border-bottom: 1px solid #0f3460; flex-wrap: wrap;
  }}
  .stat-card {{
    background: #0f3460; padding: 10px 18px; border-radius: 8px;
    min-width: 120px; border-left: 3px solid #e94560;
  }}
  .stat-card .val {{ font-size: 1.7rem; font-weight: 700; color: #e94560; line-height: 1.1; }}
  .stat-card .lbl {{ font-size: .68rem; color: #aaa; text-transform: uppercase; letter-spacing: .6px; margin-top: 2px; }}
  .legend {{
    display: flex; gap: 14px; padding: 10px 28px;
    background: #16213e; border-bottom: 1px solid #0f3460;
    flex-wrap: wrap; align-items: center;
  }}
  .legend-label {{ font-size: .75rem; color: #aaa; font-weight: 600; margin-right: 4px; }}
  .legend-item {{ display: flex; align-items: center; gap: 6px; font-size: .75rem; color: #ccc; }}
  .legend-box {{ width: 22px; height: 13px; border-radius: 3px; }}
  .filter-bar {{
    padding: 10px 28px; background: #1a1a2e; border-bottom: 1px solid #222;
    display: flex; align-items: center; gap: 14px;
  }}
  .filter-bar input[type=text] {{
    background: #0f3460; border: 1px solid #1e4080; color: #e0e0e0;
    padding: 6px 12px; border-radius: 6px; font-size: .82rem; width: 240px; outline: none;
  }}
  .filter-bar input[type=text]:focus {{ border-color: #e94560; }}
  .filter-bar label {{ font-size: .78rem; color: #aaa; display: flex; align-items: center; gap: 6px; cursor: pointer; }}
  .filter-bar input[type=checkbox] {{ width: auto; accent-color: #e94560; }}
  .matrix-wrap {{ overflow-x: auto; padding: 18px 28px; }}
  .matrix {{ display: flex; gap: 5px; min-width: max-content; }}
  .tactic-col {{ width: 164px; flex-shrink: 0; }}
  .tactic-header {{
    background: linear-gradient(180deg, #0f3460 0%, #0b2a52 100%);
    border: 1px solid #e94560; border-radius: 6px 6px 0 0;
    padding: 8px 9px 6px; margin-bottom: 3px; text-align: center;
  }}
  .tactic-name {{
    font-weight: 700; font-size: .72rem; color: #e94560;
    text-transform: uppercase; letter-spacing: .4px; line-height: 1.2;
  }}
  .tactic-meta {{ font-size: .66rem; color: #888; margin-top: 2px; }}
  .techniques {{ display: flex; flex-direction: column; gap: 2px; }}
  .technique {{
    padding: 5px 7px; border-radius: 4px; cursor: default;
    border: 1px solid rgba(255,255,255,.07);
    transition: filter .12s, transform .12s; position: relative;
  }}
  .technique:hover {{ filter: brightness(1.3); transform: scaleX(1.02); z-index: 5; }}
  .technique.hidden {{ display: none; }}
  .tech-header {{ display: flex; align-items: flex-start; gap: 4px; justify-content: space-between; }}
  .tid {{
    font-weight: 700; font-family: "SF Mono","Fira Code",monospace;
    font-size: .63rem; opacity: .75; white-space: nowrap; flex-shrink: 0;
  }}
  .tname {{ flex: 1; font-size: .69rem; line-height: 1.3; word-break: break-word; }}
  .badge {{
    background: rgba(0,0,0,.35); border-radius: 10px; padding: 1px 5px;
    font-size: .62rem; font-weight: 700; flex-shrink: 0; min-width: 18px; text-align: center;
  }}
  .subtechs {{ margin-top: 3px; display: flex; flex-direction: column; gap: 1px; }}
  .subtechnique {{
    padding: 3px 6px 3px 8px; border-radius: 3px; font-size: .64rem;
    display: flex; align-items: center; gap: 4px;
    border-left: 2px solid rgba(255,255,255,.2); margin-left: 4px;
    cursor: default; transition: filter .12s;
  }}
  .subtechnique:hover {{ filter: brightness(1.3); }}
  .subtechnique .tid {{ font-size: .60rem; }}
  .sname {{ flex: 1; }}
  .section {{ padding: 20px 28px; }}
  .section h2 {{ color: #e94560; font-size: 1rem; margin-bottom: 12px; display: flex; align-items: center; gap: 10px; }}
  .count-badge {{
    background: #e94560; color: #fff; border-radius: 12px;
    padding: 2px 9px; font-size: .75rem; font-weight: 700;
  }}
  .cve-table {{ width: 100%; border-collapse: collapse; font-size: .8rem; }}
  .cve-table th {{ background: #0f3460; color: #e94560; padding: 8px 12px; text-align: left; }}
  .cve-table td {{ padding: 6px 12px; border-bottom: 1px solid #1e2a40; color: #ddd; }}
  .cve-table tr:hover td {{ background: #16213e; }}
  .cve-table code {{ font-size: .78rem; color: #ffd54f; }}
  ::-webkit-scrollbar {{ height: 6px; width: 6px; }}
  ::-webkit-scrollbar-track {{ background: #12121e; }}
  ::-webkit-scrollbar-thumb {{ background: #333; border-radius: 3px; }}
  .technique[data-clickable], .subtechnique[data-clickable] {{ cursor: pointer; }}
  .rule-panel {{
    position: fixed; right: 0; top: 0; width: 400px; height: 100vh;
    background: #1a1a2e; border-left: 2px solid #e94560;
    box-shadow: -6px 0 24px rgba(0,0,0,.6);
    z-index: 1000; display: flex; flex-direction: column;
    transform: translateX(100%); transition: transform .25s ease;
  }}
  .rule-panel.open {{ transform: translateX(0); }}
  .rule-panel-header {{
    padding: 14px 16px; background: linear-gradient(135deg, #16213e, #0f3460);
    border-bottom: 1px solid #e94560; position: sticky; top: 0;
    display: flex; align-items: flex-start; justify-content: space-between; gap: 10px;
  }}
  .rule-panel-title .ptid {{ font-size: .78rem; color: #e94560; font-weight: 700; font-family: monospace; }}
  .rule-panel-title .pname {{ font-size: .88rem; color: #e0e0e0; margin-top: 3px; line-height: 1.3; }}
  .rule-panel-close {{
    background: none; border: 1px solid #555; color: #aaa; border-radius: 4px;
    width: 26px; height: 26px; cursor: pointer; font-size: 14px; flex-shrink: 0;
    display: flex; align-items: center; justify-content: center;
  }}
  .rule-panel-close:hover {{ border-color: #e94560; color: #e94560; }}
  .rule-panel-body {{ padding: 14px 16px; overflow-y: auto; flex: 1; }}
  .rule-count {{ font-size: .73rem; color: #888; margin-bottom: 10px; text-transform: uppercase; letter-spacing: .5px; }}
  .rule-list {{ list-style: none; display: flex; flex-direction: column; gap: 7px; }}
  .rule-item {{ background: #0f3460; border-radius: 6px; padding: 8px 12px; border-left: 3px solid #e94560; }}
  .rule-item .rid {{ font-family: "SF Mono","Fira Code",monospace; font-size: .62rem; color: #777; word-break: break-all; margin-bottom: 3px; }}
  .rule-item .rname {{ font-size: .8rem; color: #ddd; line-height: 1.35; }}
</style>
</head>
<body>

<div class="header">
  <h1>MITRE ATT&amp;CK — Sigma Coverage Dashboard</h1>
  <div class="meta">
    Generated: {date_str} &nbsp;|&nbsp;
    Sigma: <code style="color:#aaa">{html_lib.escape(sigma_dir)}</code> &nbsp;|&nbsp;
    ATT&amp;CK Enterprise
  </div>
</div>

<div class="stats">
  <div class="stat-card"><div class="val">{total_rules}</div><div class="lbl">Rules Scanned</div></div>
  <div class="stat-card"><div class="val">{covered}</div><div class="lbl">Techniques Covered</div></div>
  <div class="stat-card"><div class="val">{total_techs}</div><div class="lbl">Total Techniques</div></div>
  <div class="stat-card"><div class="val">{pct}%</div><div class="lbl">Coverage Rate</div></div>
  <div class="stat-card"><div class="val">{len(cves)}</div><div class="lbl">CVEs Referenced</div></div>
  <div class="stat-card"><div class="val">{errors}</div><div class="lbl">Parse Errors</div></div>
</div>

<div class="legend">
  <span class="legend-label">Coverage:</span>
  {legend_html}
</div>

<div class="filter-bar">
  <input type="text" id="search" placeholder="Filter techniques (e.g. T1059, Phishing) ..."
         oninput="filterMatrix(this.value)">
  <label>
    <input type="checkbox" id="hide-empty" onchange="filterMatrix(document.getElementById('search').value)">
    Hide uncovered
  </label>
</div>

<div class="matrix-wrap">
  <div class="matrix" id="matrix">
    {columns_html}
  </div>
</div>

{cve_html}

<div id="rule-panel" class="rule-panel">
  <div class="rule-panel-header">
    <div class="rule-panel-title">
      <div class="ptid" id="panel-tid"></div>
      <div class="pname" id="panel-name"></div>
    </div>
    <button class="rule-panel-close" onclick="closeRulesPanel()">&#x2715;</button>
  </div>
  <div class="rule-panel-body">
    <div class="rule-count" id="panel-count"></div>
    <ul class="rule-list" id="panel-rules-list"></ul>
  </div>
</div>

<script>
const TECH_RULES = {rules_js};

function showRulesPanel(el) {{
  const tid   = el.dataset.tid;
  const name  = el.dataset.name;
  const rules = TECH_RULES[tid];
  if (!rules || rules.length === 0) return;
  document.getElementById('panel-tid').textContent   = tid;
  document.getElementById('panel-name').textContent  = name;
  document.getElementById('panel-count').textContent = rules.length + ' rule' + (rules.length !== 1 ? 's' : '');
  const list = document.getElementById('panel-rules-list');
  list.innerHTML = '';
  rules.forEach(([rid, rname]) => {{
    const li = document.createElement('li');
    li.className = 'rule-item';
    const esc = s => s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
    li.innerHTML = (rid ? '<div class="rid">' + esc(rid) + '</div>' : '') +
                   '<div class="rname">' + esc(rname) + '</div>';
    list.appendChild(li);
  }});
  document.getElementById('rule-panel').classList.add('open');
}}

function closeRulesPanel() {{
  document.getElementById('rule-panel').classList.remove('open');
}}

function filterMatrix(query) {{
  query = query.toLowerCase().trim();
  const hideEmpty = document.getElementById('hide-empty').checked;
  document.querySelectorAll('.technique').forEach(el => {{
    const text    = el.innerText.toLowerCase();
    const count   = parseInt(el.querySelector('.badge')?.textContent || '0');
    const matches = (!query || text.includes(query)) && (!hideEmpty || count > 0);
    el.classList.toggle('hidden', !matches);
  }});
}}
</script>
</body>
</html>"""

    HTML_OUTPUT.write_text(html_content, encoding="utf-8")
    print(f"[html]  Saved → {HTML_OUTPUT}")


# ═══════════════════════════════════════════════════════════════════════════════
#  5. MARKDOWN REPORT
# ═══════════════════════════════════════════════════════════════════════════════

def generate_markdown(tactics, techniques, coverage, cves, sigma_dir, total_rules):
    covered, total_techs, pct = coverage_stats(techniques, coverage)
    tactic_techs, subtechs    = _group_by_tactic(techniques)
    date_str = datetime.now().strftime("%Y-%m-%d")

    lines = [
        "# MITRE ATT&CK Sigma Coverage Report",
        "",
        f"> Generated: {date_str}  |  Source: `{sigma_dir}`",
        "",
        "## Summary",
        "",
        "| Metric | Value |",
        "|--------|-------|",
        f"| Sigma Rules Scanned | **{total_rules}** |",
        f"| Techniques Covered  | **{covered} / {total_techs}** |",
        f"| Coverage Rate       | **{pct}%** |",
        f"| CVEs Referenced     | **{len(cves)}** |",
        "",
        "## Coverage by Tactic",
        "",
    ]

    for tac in tactics:
        short     = tac["short_name"]
        techs     = sorted(tactic_techs.get(short, []), key=lambda t: t["id"])
        tac_cov   = sum(1 for t in techs if coverage[t["id"]])
        tac_total = len(techs)
        tac_pct   = round(tac_cov / tac_total * 100, 1) if tac_total else 0.0

        lines += [
            f"### {tac['name']} ({tac['id']})",
            f"Coverage: **{tac_cov}/{tac_total}** ({tac_pct}%)",
            "",
            "| Status | ID | Name | Rules | Sub-techs |",
            "|--------|----|------|-------|-----------|",
        ]

        for t in techs:
            count     = len(coverage[t["id"]])
            sub_list  = subtechs.get(t["id"], [])
            sub_cov   = sum(1 for s in sub_list if coverage[s["id"]])
            sub_total = len(sub_list)
            status    = "✅" if count > 0 else ("🟡" if sub_cov > 0 else "⬜")
            sub_info  = f"{sub_cov}/{sub_total}" if sub_total else "—"
            lines.append(f"| {status} | `{t['id']}` | {t['name']} | {count} | {sub_info} |")
            for st in sub_list:
                s_count  = len(coverage[st["id"]])
                s_status = "✅" if s_count > 0 else "⬜"
                lines.append(f"| {s_status} | `{st['id']}` | ↳ {st['name']} | {s_count} | — |")

        lines.append("")

        # Rules detail — collapsible block for covered techniques in this tactic
        covered_techs = [t for t in techs if coverage[t["id"]] or any(coverage[s["id"]] for s in subtechs.get(t["id"], []))]
        if covered_techs:
            lines += [
                "<details>",
                f"<summary>Rules detail ({sum(1 for t in techs if coverage[t['id']])} techniques covered)</summary>",
                "",
            ]
            for t in covered_techs:
                rules = coverage[t["id"]]
                if rules:
                    lines.append(f"**`{t['id']}`** {t['name']}")
                    for rid, rname in rules:
                        id_part = f"`{rid}` — " if rid else ""
                        lines.append(f"- {id_part}{rname}")
                for st in subtechs.get(t["id"], []):
                    st_rules = coverage[st["id"]]
                    if st_rules:
                        lines.append(f"  **`{st['id']}`** ↳ {st['name']}")
                        for rid, rname in st_rules:
                            id_part = f"`{rid}` — " if rid else ""
                            lines.append(f"  - {id_part}{rname}")
                lines.append("")
            lines += ["</details>", ""]

    if cves:
        lines += ["## CVE Coverage", "", "| CVE | Rules | Rule Titles |", "|-----|-------|-------------|"]
        for cve_id, rules in sorted(cves.items()):
            rule_str = ", ".join(f"`{r[1]}`" for r in rules[:3])
            if len(rules) > 3:
                rule_str += f" +{len(rules) - 3} more"
            lines.append(f"| {cve_id} | {len(rules)} | {rule_str} |")
        lines.append("")

    MD_OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"[md]    Saved → {MD_OUTPUT}")


# ═══════════════════════════════════════════════════════════════════════════════
#  6. TERMINAL OUTPUT
# ═══════════════════════════════════════════════════════════════════════════════

A = {
    "reset":  "\033[0m",  "bold": "\033[1m",
    "red":    "\033[91m", "green": "\033[92m",
    "yellow": "\033[93m", "cyan":  "\033[96m",
    "gray":   "\033[90m",
}


def _ansi_count(count):
    if count == 0: return A["gray"]
    if count == 1: return A["yellow"]
    if count <= 3: return A["green"]
    return A["cyan"]


def generate_terminal(tactics, techniques, coverage, cves, total_rules, errors):
    covered, total_techs, pct = coverage_stats(techniques, coverage)
    tactic_techs, subtechs    = _group_by_tactic(techniques)
    b, r = A["bold"], A["reset"]

    print()
    print(f"{b}{A['red']}{'═' * 68}{r}")
    print(f"  {b}MITRE ATT&CK — Sigma Coverage Dashboard{r}")
    print(f"{b}{A['red']}{'═' * 68}{r}")
    print(
        f"  Rules : {b}{total_rules}{r}  |  "
        f"Covered: {b}{covered}/{total_techs}{r}  |  "
        f"Rate: {b}{pct}%{r}  |  "
        f"CVEs: {b}{len(cves)}{r}  |  "
        f"Errors: {b}{errors}{r}"
    )
    print()

    for tac in tactics:
        short     = tac["short_name"]
        techs     = tactic_techs.get(short, [])
        tac_cov   = sum(1 for t in techs if coverage[t["id"]])
        tac_total = len(techs)
        bar_n     = int(tac_cov / tac_total * 24) if tac_total else 0
        bar       = f"{A['green']}{'█' * bar_n}{A['gray']}{'░' * (24 - bar_n)}{r}"
        pct_tac   = round(tac_cov / tac_total * 100) if tac_total else 0
        print(
            f"  {b}{A['cyan']}{tac['name']:<24}{r} "
            f"{bar}  {tac_cov:>3}/{tac_total:<3} ({pct_tac:>3}%)"
        )

    print()

    top = sorted(
        [(tid, rules) for tid, rules in coverage.items() if rules and tid in techniques],
        key=lambda x: len(x[1]),
        reverse=True,
    )[:10]
    if top:
        print(f"  {b}Top 10 most-covered techniques:{r}")
        for tid, rules in top:
            name  = techniques[tid]["name"]
            color = _ansi_count(len(rules))
            print(f"    {color}{b}{tid}{r}  {name:<45} {color}{len(rules)} rules{r}")
        print()

    uncovered = sum(
        1 for t in techniques.values()
        if not t["is_sub"] and not coverage[t["id"]]
    )
    print(f"  {A['gray']}Uncovered parent techniques: {b}{uncovered}{r}")

    if cves:
        cve_list = ", ".join(sorted(cves.keys())[:8])
        if len(cves) > 8:
            cve_list += f" … +{len(cves) - 8} more"
        print(f"  {A['gray']}CVEs referenced: {b}{cve_list}{r}")

    print()


# ═══════════════════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    stix_data          = load_attack_data()
    tactics, techniques = parse_attack_matrix(stix_data)
    print(
        f"[ok]    Loaded {len(tactics)} tactics, "
        f"{len(techniques)} techniques/sub-techniques from ATT&CK STIX bundle"
    )

    coverage, cves, tactic_coverage, total_rules, errors = load_sigma_rules(SIGMA_RULES_DIR)
    covered_count = sum(1 for v in coverage.values() if v)
    print(
        f"[ok]    Parsed {total_rules} sigma rules — "
        f"{covered_count} unique technique IDs covered — "
        f"{errors} parse errors"
    )

    generate_terminal(tactics, techniques, coverage, cves, total_rules, errors)
    generate_html(tactics, techniques, coverage, cves, SIGMA_RULES_DIR, total_rules, errors)
    generate_markdown(tactics, techniques, coverage, cves, SIGMA_RULES_DIR, total_rules)

    print(f"\n[done]  All outputs written to: {OUTPUT_DIR}\n")


if __name__ == "__main__":
    main()
