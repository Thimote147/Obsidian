---
tags:
  - THM
  - pre-security
  - defensive-security
  - blue-team
  - room
platform: TryHackMe
type: room
module: Introduction to Cyber Security
module_number: 1
room_number: 2
status: ⬜
url: https://tryhackme.com/room/defensivesecurityintro
difficulty: Easy
---

# 🛡️ Defensive Security Intro

> [!abstract] Summary
> Introduction to the defensive side of cybersecurity. Learn about SOC teams, threat intelligence, DFIR, and how defenders protect systems using tools like SIEM and IDS.

**Path:** [[Pre Security (New)]] > [[Introduction to Cyber Security]] > [[Defensive Security Intro]]

---

## 🎯 Learning Objectives
- Understand what defensive security is
- Learn about Security Operations Centers (SOC)
- Understand Threat Intelligence
- Learn about Digital Forensics and Incident Response (DFIR)
- Understand Malware Analysis basics

---

## 📖 Key Concepts

### What is Defensive Security?
Defensive security focuses on **preventing, detecting, and responding** to attacks. While offensive teams simulate attacks, defensive teams work to stop them.

Two main tasks:
1. **Preventing intrusions** — security policies, patching, user awareness
2. **Detecting and responding** — monitoring, incident response, forensics

---

### Security Operations Center (SOC)
A team of security professionals that monitors networks and systems **24/7** to detect and respond to threats.

**What a SOC monitors:**
- Vulnerabilities — unpatched systems, misconfigurations
- Policy violations — e.g., someone uploading sensitive data to the cloud
- Unauthorized activity — failed logins, suspicious traffic
- Network intrusions — malware, exploits

---

### Threat Intelligence
Gathering and analyzing **information about adversaries** to better prepare defenses.

- **Threat** = potential attacker with capability and intent
- Intelligence feeds help predict and prevent attacks
- Sources: open-source (OSINT), commercial, government advisories

---

### Digital Forensics and Incident Response (DFIR)

#### Digital Forensics
Analyzing evidence after an attack to understand what happened.
- **File System Forensics** — deleted files, access times, metadata
- **Memory Forensics** — malware hiding in RAM
- **Log Analysis** — system/network logs for attack traces
- **Network Forensics** — capturing and analyzing traffic (PCAP files)

#### Incident Response (IR)
Structured approach to handling a security breach.

```
1. Preparation     → Policies, playbooks, tools in place
2. Detection       → Identify the incident
3. Containment     → Limit the damage / spread
4. Eradication     → Remove the threat
5. Recovery        → Restore normal operations
6. Lessons Learned → Improve defenses
```

---

### Malware Analysis
Understanding malicious software to better defend against it.

| Type | Description |
|------|-------------|
| **Virus** | Self-replicating code that attaches to legitimate files |
| **Trojan** | Disguised as legitimate software |
| **Ransomware** | Encrypts files and demands payment |
| **Spyware** | Silently collects user data |
| **Rootkit** | Hides its presence deep in the OS |

**Analysis approaches:**
- **Static Analysis** — examining code without running it
- **Dynamic Analysis** — running malware in a sandbox to observe behavior

---

### Key Defensive Tools

| Tool | Purpose |
|------|---------|
| **SIEM** (Security Information & Event Management) | Aggregates logs, detects anomalies, alerts |
| **IDS/IPS** (Intrusion Detection/Prevention System) | Detects/blocks suspicious network traffic |
| **EDR** (Endpoint Detection & Response) | Monitors endpoints for malicious activity |
| **Firewall** | Controls incoming/outgoing network traffic |
| **Antivirus** | Detects known malware signatures |

---

## 🔑 Key Takeaways
- Defensive security is about prevention, detection, and response
- SOC teams are the frontline of defense in organizations
- DFIR combines investigation (forensics) with rapid response (IR)
- Both offensive and defensive skills are needed to understand the full picture

---

## 🔗 Related Notes
- [[Offensive Security Intro]] — the attacking perspective
- [[Careers in Cyber]] — defensive career paths
- [[Become a Defender]] — deeper defensive skills
- [[The CIA Triad]] — core security principles
- [[SIEM]] · [[IDS]] · [[Incident Response]] · [[Malware Analysis]]
