---
tags: [THM, cyber-security-101, defensive-security, incident-response, room]
platform: TryHackMe
type: room
module: "10 - Defensive Security"
module_number: 10
room_number: 41
status: "⬜"
url: https://tryhackme.com/room/incidentresponsefundamentals
difficulty: Easy
---

# 🚨 Incident Response Fundamentals

> [!abstract] Summary
> Learn the Incident Response lifecycle — the structured approach to handling security breaches. Covers PICERL, containment strategies, playbooks, and post-incident activities.

**Path:** [[Cyber Security 101]] > Module 10 > Incident Response Fundamentals

## 🎯 Learning Objectives
- Know the IR lifecycle (PICERL)
- Understand containment vs eradication
- Use IR playbooks
- Document incidents properly

## 📖 Key Concepts

### PICERL Framework
| Phase | Action |
|-------|--------|
| **P**reparation | Policies, playbooks, tools, training |
| **I**dentification | Detect and confirm incident |
| **C**ontainment | Stop spread — short and long-term |
| **E**radication | Remove malware, close attacker access |
| **R**ecovery | Restore systems to production |
| **L**essons Learned | Post-incident review, improve |

### Containment Strategies
**Short-term:** Isolate host · block C2 IPs · disable accounts · kill processes

**Long-term:** Patch other systems · reset all credentials · deploy additional monitoring

> [!warning] **Preserve before you clean.** Take forensic images of compromised systems before eradication. Once cleaned, evidence is gone.

### Eradication
- Remove malware and malicious files
- Delete attacker-created accounts
- Patch exploited vulnerabilities
- Remove persistence (scheduled tasks, registry Run keys, cron jobs)

### Recovery
- Restore from **verified clean** backups
- Monitor closely for re-infection
- Gradually restore services with validation

### IR Playbooks
Pre-written step-by-step procedures per incident type: Ransomware · Phishing · Insider Threat · DDoS

## 🔑 Key Takeaways
- **PICERL** — memorise it, it's on every security exam and interview
- Contain first, eradicate second — stop the spread before cleaning
- Preserve forensic evidence before remediation
- Lessons Learned closes the loop — every incident should improve defences

## 🔗 Related Notes
- [[CS101-40 - Digital Forensics Fundamentals]] · [[CS101-39 - SOC Fundamentals]]
- [[Incident Response]] · [[PICERL]] · [[Playbooks]] · [[Forensics]]
