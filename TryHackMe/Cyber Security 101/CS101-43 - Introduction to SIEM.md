---
tags: [THM, cyber-security-101, security-solutions, SIEM, room]
platform: TryHackMe
type: room
module: "11 - Security Solutions"
module_number: 11
room_number: 43
status: "⬜"
url: https://tryhackme.com/room/introductiontosiem
difficulty: Easy
---

# 📊 Introduction to SIEM

> [!abstract] Summary
> Learn SIEM fundamentals — how it aggregates logs, correlates events, generates alerts, and enables security investigations at scale.

**Path:** [[Cyber Security 101]] > Module 11 > Introduction to SIEM

## 🎯 Learning Objectives
- Understand SIEM architecture and data sources
- Know how correlation rules generate alerts
- Navigate a SIEM for investigation
- Know popular SIEM platforms

## 📖 Key Concepts

### SIEM Architecture
```
Log Sources → Normalisation → Storage → Correlation Engine → Alerts → Dashboard
     ↑
Firewalls · AD · Endpoints · IDS · Web servers · Cloud
```

### Normalisation
Converts different log formats into a unified schema:
```
Windows Event 4625 + Linux auth.log "Failed password"
→ {type: "auth_failure", user: "admin", src_ip: "x.x.x.x"}
```

### Correlation Rules
```
IF: 5 failed logins (4625) from same IP within 60s
THEN: Alert "Brute Force" — Medium

IF: Login success (4624) after 10+ failures from same IP
THEN: Alert "Brute Force Success" — Critical
```

### Popular SIEM Platforms
| SIEM | Type |
|------|------|
| **Splunk** | Commercial — market leader |
| **Microsoft Sentinel** | Cloud-native (Azure) |
| **Elastic SIEM** | Open-source |
| **Wazuh** | Open-source |
| **IBM QRadar** | Commercial enterprise |

### Investigation Workflow
1. Alert fires → analyst opens alert
2. Review correlated events
3. Pivot to raw logs for context
4. Query related IOCs
5. True Positive → escalate · False Positive → tune + close

> [!tip] Learning Splunk or Elastic is a strong career move. Both offer free tiers and learning paths (Splunk Fundamentals, Elastic training).

## 🔑 Key Takeaways
- SIEM = centralised log storage + real-time correlation + alerting
- Correlation rules turn raw logs into actionable alerts
- Normalisation enables cross-source correlation
- False positive tuning is ongoing — alert fatigue kills SOC effectiveness

## 🔗 Related Notes
- [[CS101-42 - Logs Fundamentals]] · [[CS101-39 - SOC Fundamentals]]
- [[SIEM]] · [[Splunk]] · [[Elastic]] · [[Correlation Rules]]
