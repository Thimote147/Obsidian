---
tags: [THM, cyber-security-101, defensive-security, blue-team, room]
platform: TryHackMe
type: room
module: "01 - Start Your Cyber Security Journey"
module_number: 1
room_number: 2
status: "⬜"
url: https://tryhackme.com/room/defensivesecurityintro
difficulty: Easy
---

# 🛡️ Defensive Security Intro

> [!abstract] Summary
> Introduction to defensive security — SOC teams, Threat Intelligence, Digital Forensics, Incident Response, and Malware Analysis. The blue team perspective.

**Path:** [[Cyber Security 101]] > Module 1 > Defensive Security Intro

## 🎯 Learning Objectives
- Understand what defensive security does
- Learn about SOC, Threat Intelligence, DFIR, Malware Analysis
- Know the key defensive tools (SIEM, IDS)

## 📖 Key Concepts

### Security Operations Center (SOC)
24/7 team monitoring for: vulnerabilities, policy violations, unauthorized activity, intrusions.

### Threat Intelligence
Gathering info about adversaries to predict and prevent attacks.
- Sources: OSINT, commercial feeds, government advisories

### DFIR
**Digital Forensics** — investigating evidence after an attack (file system, memory, logs, network).
**Incident Response** — structured response: Preparation → Detection → Containment → Eradication → Recovery → Lessons Learned

### Malware Analysis
| Type | Description |
|------|-------------|
| **Static** | Examine code without running it |
| **Dynamic** | Run in sandbox, observe behavior |

### Key Tools
| Tool | Purpose |
|------|---------|
| **SIEM** | Aggregate logs, detect anomalies, alert |
| **IDS/IPS** | Detect/block suspicious traffic |
| **EDR** | Endpoint detection & response |

## 🔑 Key Takeaways
- Defensive = prevent, detect, respond
- SOC is the frontline — monitors everything 24/7
- DFIR combines investigation with rapid response

## 🔗 Related Notes
- [[TryHackMe/Cyber Security 101/Untitled/Offensive Security Intro]] · [[CS101-44 - SOC Fundamentals]]
- [[CS101-45 - Digital Forensics Fundamentals]] · [[CS101-46 - Incident Response Fundamentals]]
- [[SIEM]] · [[IDS]] · [[Incident Response]] · [[Malware Analysis]]
