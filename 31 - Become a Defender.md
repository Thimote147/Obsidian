---
tags: [THM, pre-security, attacks-defenses, defensive, room]
platform: TryHackMe
type: room
module: "Attacks and Defenses"
module_number: 7
room_number: 31
status: "⬜"
url: https://tryhackme.com/room/becomeadefender
difficulty: Easy
---

# 🛡️ Become a Defender

> [!abstract] Summary
> Consolidates all defensive knowledge from the path — defense-in-depth, incident response, monitoring, and a roadmap for developing blue team skills. Bridges Pre-Security to the SOC Level 1 path.

**Path:** [[Pre Security (New)]] > [[Attacks and Defenses]] > Become a Defender

---

## 📖 Key Concepts

### Defense-in-Depth
Multiple layers of security so that if one fails, others still protect.

```
Physical Security
      ↓
Network Security (Firewall, IDS/IPS, VPN)
      ↓
Host Security (AV, EDR, Patching)
      ↓
Application Security (WAF, Secure coding, SAST/DAST)
      ↓
Data Security (Encryption, DLP, Backups)
      ↓
Identity & Access (MFA, Least Privilege, PAM)
      ↓
Monitoring & Response (SIEM, SOC, IR)
```

---

### Security Controls Framework

| Type | Description | Example |
|------|-------------|---------|
| **Preventive** | Stop attacks from succeeding | Firewall, MFA, patching |
| **Detective** | Identify attacks in progress | IDS, SIEM alerts, logging |
| **Corrective** | Fix damage after an attack | IR, backups, reimaging |
| **Deterrent** | Discourage attackers | Warning banners, policies |

---

### Blue Team Activities

#### Threat Hunting
Proactively searching for threats that have bypassed detection tools.
- Based on threat intelligence
- Hypothesis-driven investigation
- Tools: Splunk, Elastic, Velociraptor

#### Security Monitoring & SIEM
```
Log Sources:
- Firewalls, IDS/IPS
- Windows Event Logs
- Linux syslogs
- Web server logs
- Endpoint (EDR)
     ↓
SIEM (Splunk, IBM QRadar, Microsoft Sentinel)
     ↓
Correlation Rules → Alerts
     ↓
SOC Analyst → Investigate → Triage → Escalate/Close
```

**Key Windows Event IDs to monitor:**
| Event ID | Description |
|----------|-------------|
| 4624 | Successful logon |
| 4625 | Failed logon |
| 4648 | Logon with explicit credentials |
| 4720 | User account created |
| 4732 | User added to privileged group |
| 4688 | Process created |
| 7045 | New service installed |

#### Incident Response (IR) Phases
```
1. Preparation     → IR plan, playbooks, tools, training
2. Identification  → Detect and confirm incident
3. Containment     → Isolate affected systems
4. Eradication     → Remove malware, close vulnerabilities
5. Recovery        → Restore systems to normal
6. Lessons Learned → Post-incident report, improve defenses
```

---

### Hardening Checklist Summary

**Network:**
- [ ] Firewall with default-deny policy
- [ ] Network segmentation (DMZ, VLANs)
- [ ] IDS/IPS
- [ ] Disable unused ports/services

**Endpoints:**
- [ ] AV / EDR deployed
- [ ] OS and software fully patched
- [ ] Application allowlisting
- [ ] Least privilege accounts

**Identity:**
- [ ] MFA everywhere
- [ ] Strong password policy
- [ ] Privileged Access Management (PAM)
- [ ] Regular access reviews

**Data:**
- [ ] Encryption at rest and in transit
- [ ] Regular backups (3-2-1 rule)
- [ ] DLP (Data Loss Prevention)

**Monitoring:**
- [ ] Centralized logging (SIEM)
- [ ] Alerting on key events
- [ ] Incident response plan tested

---

### 3-2-1 Backup Rule
- **3** copies of data
- **2** different storage media
- **1** offsite/cloud backup

---

### Next Steps After Pre-Security
1. **SOC Level 1** path on TryHackMe
2. Practice log analysis and threat hunting
3. Certifications: CompTIA Security+ → CySA+ → BTL1
4. Set up a home SOC lab with a free SIEM (Wazuh, Graylog)

---

## 🔑 Key Takeaways
- Defense-in-depth means no single control protects everything — layer your defenses
- Preventive, detective, and corrective controls work together
- Monitoring (SIEM) and rapid IR are the difference between a minor incident and a breach
- The Pre-Security path gives all the fundamentals needed to start a blue team career

## 🔗 Related Notes
- [[Defensive Security Intro]] · [[Careers in Cyber]] · [[30 - Become a Hacker]]
- [[SIEM]] · [[Incident Response]] · [[Threat Hunting]] · [[Defense-in-Depth]] · [[SOC]]
