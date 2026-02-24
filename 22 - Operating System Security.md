---
tags: [THM, pre-security, operating-systems, security, room]
platform: TryHackMe
type: room
module: "Operating Systems Basics"
module_number: 5
room_number: 22
status: "⬜"
url: https://tryhackme.com/room/operatingsystemsecurity
difficulty: Easy
---

# 🔒 Operating System Security

> [!abstract] Summary
> Covers how operating systems are secured — authentication, access control, patching, logging, and common OS-level attacks like privilege escalation and credential theft.

**Path:** [[Pre Security (New)]] > [[Operating Systems Basics]] > Operating System Security

---

## 📖 Key Concepts

### Authentication in OS

| Method | Description |
|--------|-------------|
| **Password** | Knowledge-based; vulnerable to brute force/reuse |
| **SSH Keys** | Cryptographic key pair; much stronger than passwords |
| **MFA/2FA** | Second factor (app, SMS, hardware token) |
| **Biometrics** | Fingerprint, face recognition |
| **Smart Card** | Physical token + PIN |

**Password Storage:**
- Linux: hashed in `/etc/shadow` (SHA-512)
- Windows: hashed in SAM database (NTLM hash)

> [!warning] Never store passwords in plaintext! Both shadow and SAM files can be attacked with tools like hashcat or John the Ripper.

---

### Access Control

**Principle of Least Privilege:** Grant only the minimum access needed.

**Linux Permissions:** rwx model (see [[20 - Linux CLI Basics]])

**Windows NTFS ACLs:** Fine-grained permissions per user/group

**sudo / UAC:** Controlled privilege escalation mechanisms

---

### Common OS Security Vulnerabilities

| Attack | Description |
|--------|-------------|
| **Privilege Escalation** | Moving from low to high privilege (SUID, UAC bypass, kernel exploit) |
| **Credential Dumping** | Extracting passwords/hashes from memory (Mimikatz on Windows) |
| **Persistence** | Maintaining access after reboot (cron jobs, Registry Run keys, services) |
| **Kernel Exploits** | Exploiting kernel vulnerabilities for ring-0 access (Dirty COW, EternalBlue) |
| **Password Attacks** | Brute force, dictionary attack, credential stuffing |

---

### Patching & Updates
- **Unpatched vulnerabilities** are the #1 cause of successful exploits
- CVEs (Common Vulnerabilities and Exposures) track known vulnerabilities
- **EternalBlue** (CVE-2017-0144) — unpatched SMB vulnerability exploited by WannaCry ransomware

```bash
# Linux — Update system
sudo apt update && sudo apt upgrade -y

# Windows — Check Windows Update via PowerShell
Get-WindowsUpdate
```

---

### Logging & Auditing

**Linux logs:**
```bash
/var/log/syslog          # General system log
/var/log/auth.log        # Authentication events
/var/log/apache2/access.log  # Web server
journalctl -xe           # Systemd journal
```

**Windows logs (Event Viewer):**
| Log | Key Events |
|-----|-----------|
| Security | 4624 (logon), 4625 (failed logon), 4648 (explicit credential use) |
| System | Service start/stop, crashes |
| Application | App errors |
| PowerShell | 4104 (script block logging) |

---

### Hardening Checklist

**Linux:**
- [ ] Disable root SSH login (`PermitRootLogin no` in `/etc/ssh/sshd_config`)
- [ ] Use SSH keys instead of passwords
- [ ] Remove unused packages and services
- [ ] Set proper file permissions
- [ ] Enable auditd for logging
- [ ] Configure UFW/iptables firewall

**Windows:**
- [ ] Enable Windows Defender + Firewall
- [ ] Keep Windows Updated
- [ ] Disable unused services
- [ ] Enforce strong password policy
- [ ] Enable PowerShell ScriptBlock logging
- [ ] Use LAPS for local admin passwords

---

## 🔑 Key Takeaways
- Authentication, access control, and patching are the pillars of OS security
- Privilege escalation is the primary goal after initial access in pen testing
- Logging is essential — defenders detect attacks through logs
- Least privilege reduces the blast radius of any compromise

## 🔗 Related Notes
- [[19 - Windows Basics]] · [[20 - Linux CLI Basics]] · [[21 - Windows CLI Basics]]
- [[Privilege Escalation]] · [[Credential Dumping]] · [[Persistence]] · [[CVE]] · [[Patching]]
