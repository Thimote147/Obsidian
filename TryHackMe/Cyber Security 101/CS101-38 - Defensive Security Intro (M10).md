---
tags: [THM, cyber-security-101, defensive-security, blue-team, room]
platform: TryHackMe
type: room
module: "10 - Defensive Security"
module_number: 10
room_number: 43
status: "⬜"
url: https://tryhackme.com/room/defensivesecurityintro
difficulty: Easy
---

# 🛡️ Defensive Security Intro (Module 10)

> [!abstract] Summary
> Re-examination of defensive security concepts at a deeper level — introducing SOC operations, Threat Intelligence, DFIR, and Malware Analysis as they apply to a full security programme.

**Path:** [[Cyber Security 101]] > Module 10 > Defensive Security Intro

## 📖 Key Concepts

This room revisits [[TryHackMe/Cyber Security 101/Untitled/Defensive Security Intro]] from Module 1 but in the context of the full Defensive Security module. It sets the stage for the rooms that follow.

### The Defensive Security Ecosystem
```
Prevention    → Firewalls, patching, hardening
Detection     → SIEM, IDS, EDR, log analysis
Response      → SOC analysts, IR teams, forensics
Recovery      → Backups, DR plans, business continuity
```

### Threat Intelligence (TI)
Collecting and analysing information about adversaries:
- **Strategic** — high-level, for executives
- **Tactical** — TTPs (Tactics, Techniques, Procedures) — MITRE ATT&CK
- **Operational** — specific campaign info
- **Technical** — IOCs (IPs, hashes, domains)

### MITRE ATT&CK Framework
Matrix of adversary TTPs mapped to kill chain stages:
- Reconnaissance → Resource Development → Initial Access → Execution → Persistence → Privilege Escalation → Defence Evasion → Credential Access → Discovery → Lateral Movement → Collection → Exfiltration → Impact

### Cyber Kill Chain (Lockheed Martin)
1. Reconnaissance
2. Weaponisation
3. Delivery
4. Exploitation
5. Installation
6. Command & Control (C2)
7. Actions on Objectives

> [!tip] Understanding attacker methodology (Kill Chain / ATT&CK) helps defenders anticipate and disrupt attacks at each phase.

## 🔑 Key Takeaways
- Defence is layered: prevent → detect → respond → recover
- MITRE ATT&CK maps real-world adversary behaviour — use it to guide detection
- Threat intelligence feeds the entire defensive operation

## 🔗 Related Notes
- [[TryHackMe/Cyber Security 101/Untitled/Defensive Security Intro]] · [[CS101-44 - SOC Fundamentals]]
- [[CS101-45 - Digital Forensics Fundamentals]] · [[SOC]] · [[MITRE ATT&CK]] · [[Threat Intelligence]]
