---
tags: [THM, cyber-security-101, defensive-security, blue-team, room]
platform: TryHackMe
type: room
module: "10 - Defensive Security"
module_number: 10
room_number: 38
status: "⬜"
url: https://tryhackme.com/room/defensivesecurityintro
difficulty: Easy
---

# 🛡️ Defensive Security Intro

> [!abstract] Summary
> Re-examination of defensive security at a deeper level — introducing the SOC, Threat Intelligence, DFIR, and Malware Analysis as part of a complete security programme.

**Path:** [[Cyber Security 101]] > Module 10 > Defensive Security Intro

## 📖 Key Concepts

### The Defensive Security Ecosystem
```
Prevention    → Firewalls, patching, hardening
Detection     → SIEM, IDS, EDR, log analysis
Response      → SOC analysts, IR teams, forensics
Recovery      → Backups, DR plans, business continuity
```

### Threat Intelligence (TI) Tiers
| Tier | Audience | Content |
|------|----------|---------|
| **Strategic** | Executives | High-level threat landscape |
| **Tactical** | Security teams | TTPs, MITRE ATT&CK |
| **Operational** | IR teams | Specific campaign details |
| **Technical** | Analysts | IOCs (IPs, hashes, domains) |

### MITRE ATT&CK Framework
Maps adversary TTPs to kill chain stages. Used to guide detection rule creation and IR investigations.

### Cyber Kill Chain
1. Reconnaissance → 2. Weaponisation → 3. Delivery → 4. Exploitation → 5. Installation → 6. C2 → 7. Actions on Objectives

> [!tip] Understanding attacker methodology (Kill Chain + ATT&CK) helps defenders detect and disrupt attacks at each phase rather than only at the endpoint.

## 🔑 Key Takeaways
- Defence is layered: prevent → detect → respond → recover
- MITRE ATT&CK maps real-world adversary TTPs — use it to build detection rules
- Threat intelligence feeds the entire defensive operation

## 🔗 Related Notes
- [[TryHackMe/Cyber Security 101/Untitled/Defensive Security Intro]] · [[CS101-39 - SOC Fundamentals]]
- [[MITRE ATT&CK]] · [[Threat Intelligence]] · [[SOC]] · [[Kill Chain]]
