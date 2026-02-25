---
tags: [THM, cyber-security-101, defensive-tooling, CAPA, malware-analysis, room]
platform: TryHackMe
type: room
module: "12 - Defensive Security Tooling"
module_number: 12
room_number: 48
status: "⬜"
url: https://tryhackme.com/room/capabasics
difficulty: Easy
---

# 🔎 CAPA: The Basics

> [!abstract] Summary
> Learn CAPA by Mandiant — automatically identifies malicious capabilities in executables through static analysis without executing them. Maps results to MITRE ATT&CK.

**Path:** [[Cyber Security 101]] > Module 12 > CAPA: The Basics

## 🎯 Learning Objectives
- Understand what CAPA does and when to use it
- Run CAPA against suspicious executables
- Interpret CAPA output
- Map capabilities to MITRE ATT&CK

## 📖 Key Concepts

### What CAPA Detects
Network communication · File operations · Process injection · Persistence · Encryption · Anti-analysis (VM/debugger detection)

### Usage
```bash
capa malware.exe                    # Analyse binary
capa malware.exe -v                 # Verbose
capa malware.exe -j > results.json  # JSON output
capa malware.exe -r /custom/rules/  # Custom rules
```

### Sample Output
```
+----------------------------------------------------------+
| CAPABILITY                         | NAMESPACE |
+----------------------------------------------------------+
| create reverse shell               | c2        |
| inject shellcode into a process    | injection |
| connect to HTTP server             | net       |
| check for analysis tools           | anti-analysis |
+----------------------------------------------------------+

MITRE ATT&CK:
| Defense Evasion  | T1055 Process Injection
| C2               | T1071.001 HTTP
```

### When to Use
- Suspicious binary submitted for triage
- Before running in sandbox (quick capability check)
- Generating ATT&CK mappings for threat intel reports

> [!warning] **Static analysis only** — CAPA misses capabilities that are encrypted/packed at rest or generated dynamically. Use alongside sandboxing (Any.run, Cuckoo) for full picture.

## 🔑 Key Takeaways
- CAPA = instant malware triage without executing the file
- Auto-maps to MITRE ATT&CK — saves time on threat intel reports
- Free and open-source from Mandiant
- Pair with dynamic analysis for complete coverage

## 🔗 Related Notes
- [[CS101-47 - CyberChef The Basics]] · [[CS101-49 - REMnux Getting Started]]
- [[CAPA]] · [[Malware Analysis]] · [[MITRE ATT&CK]] · [[Static Analysis]]
