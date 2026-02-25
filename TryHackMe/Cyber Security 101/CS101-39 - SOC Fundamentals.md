---
tags: [THM, cyber-security-101, defensive-security, SOC, blue-team, room]
platform: TryHackMe
type: room
module: "10 - Defensive Security"
module_number: 10
room_number: 39
status: "⬜"
url: https://tryhackme.com/room/socfundamentals
difficulty: Easy
---

# 🖥️ SOC Fundamentals

> [!abstract] Summary
> Learn how Security Operations Centers work — team structure, tiers, technologies, and the day-to-day analyst workflow. Blueprint for entry-level SOC roles.

**Path:** [[Cyber Security 101]] > Module 10 > SOC Fundamentals

## 🎯 Learning Objectives
- Understand SOC tiers and responsibilities
- Know the alert triage workflow
- Understand key SOC technologies
- Differentiate true positives from false positives

## 📖 Key Concepts

### SOC Tiers
| Tier | Role | Responsibility |
|------|------|---------------|
| **Tier 1** | Alert Analyst | Monitor, initial triage, escalate |
| **Tier 2** | Incident Responder | Deeper investigation, containment |
| **Tier 3** | Threat Hunter | Proactive hunting, advanced threats |

### Alert Triage Workflow
```
Alert fires → True Positive or False Positive?
  ↓ TP
Severity Assessment (Critical/High/Medium/Low)
  ↓
Containment → Eradication → Recovery → Document
```

### Key SOC Technologies
| Tool | Purpose |
|------|---------|
| **SIEM** | Aggregate logs, correlate, alert |
| **EDR** | Endpoint detection & response |
| **IDS/IPS** | Network intrusion detection |
| **SOAR** | Automate response workflows |
| **Ticketing** | Track incidents (ServiceNow, Jira) |

### Incident Severity Levels
| Level | Response Time |
|-------|--------------|
| **P1 Critical** | Immediate — active breach |
| **P2 High** | < 1 hour — confirmed malware |
| **P3 Medium** | < 4 hours — suspicious activity |
| **P4 Low** | Next business day |

> [!warning] **Alert fatigue** — too many false positives cause analysts to miss real threats. Tuning SIEM rules is ongoing critical work.

## 🔑 Key Takeaways
- SOC is 24/7 — Tier 1 monitors, Tier 2 investigates, Tier 3 hunts
- SIEM is the central nervous system of the SOC
- False positive management is as important as detection

## 🔗 Related Notes
- [[CS101-38 - Defensive Security Intro]] · [[CS101-43 - Introduction to SIEM]]
- [[CS101-42 - Logs Fundamentals]] · [[SOC]] · [[SIEM]] · [[Alert Triage]]
