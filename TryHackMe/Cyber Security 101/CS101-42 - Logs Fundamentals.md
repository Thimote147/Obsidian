---
tags: [THM, cyber-security-101, defensive-security, logs, SIEM, room]
platform: TryHackMe
type: room
module: "10 - Defensive Security"
module_number: 10
room_number: 42
status: "⬜"
url: https://tryhackme.com/room/logsfundamentals
difficulty: Easy
---

# 📋 Logs Fundamentals

> [!abstract] Summary
> Learn what logs are, where to find them, and how to analyse them. Logs are the primary evidence source for both real-time detection and forensic investigation.

**Path:** [[Cyber Security 101]] > Module 10 > Logs Fundamentals

## 🎯 Learning Objectives
- Understand log sources on Windows and Linux
- Read and search logs effectively
- Identify suspicious log entries
- Know critical Windows Event IDs

## 📖 Key Concepts

### Critical Windows Event IDs
| Event ID | Description |
|----------|-------------|
| **4624** | Successful logon |
| **4625** | Failed logon ← brute force |
| **4672** | Admin privilege logon |
| **4688** | Process created ← malware execution |
| **4698** | Scheduled task created ← persistence |
| **4720** | User account created |
| **4732** | User added to privileged group |
| **7045** | New service installed |

### Linux Logs
```bash
/var/log/auth.log        # SSH, sudo, su events
/var/log/syslog          # General system
/var/log/apache2/access.log  # Web server
~/.bash_history          # User commands
```

### Log Analysis Commands
```bash
# Failed SSH logins
grep "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -rn

# Windows PowerShell
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625} | Select TimeCreated, Message

# Follow live
tail -f /var/log/auth.log
```

### Web Log Analysis
```
192.168.1.1 - - [25/Feb/2026:10:00:00] "GET /admin HTTP/1.1" 403 512
```
**Suspicious patterns:** 404 floods (scanning) · 403 on admin paths · SQL keywords in URL

> [!warning] Local logs can be deleted by attackers. **Always forward logs to a centralised SIEM immediately.** Tamper-resistant centralised logging is a foundational security control.

## 🔑 Key Takeaways
- Event ID 4625 in bulk = brute force · 4688 with suspicious process = malware
- Linux auth.log records all SSH and sudo activity
- Centralise logs to prevent tampering and enable correlation
- Log analysis is the core skill for Tier 1 SOC analysts

## 🔗 Related Notes
- [[CS101-39 - SOC Fundamentals]] · [[CS101-43 - Introduction to SIEM]]
- [[Log Analysis]] · [[SIEM]] · [[Windows Event IDs]] · [[Threat Hunting]]
