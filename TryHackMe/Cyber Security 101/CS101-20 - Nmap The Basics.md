---
tags: [THM, cyber-security-101, networking, Nmap, scanning, room]
platform: TryHackMe
type: room
module: "05 - Networking"
module_number: 5
room_number: 20
status: "⬜"
url: https://tryhackme.com/room/nmapthebasics
difficulty: Easy
---

# 🗺️ Nmap: The Basics

> [!abstract] Summary
> Learn Nmap — the industry-standard network scanner. Discover live hosts, find open ports, detect service versions, fingerprint OS, and run NSE scripts.

**Path:** [[Cyber Security 101]] > Module 5 > Nmap: The Basics

## 🎯 Learning Objectives
- Discover live hosts (ping sweep)
- Scan ports and identify services
- Detect versions and OS
- Use NSE scripts

## 📖 Key Concepts

### Scan Types
```bash
nmap 10.10.10.0/24           # CIDR scan
nmap -sn 10.10.10.0/24       # Ping sweep (no port scan)
nmap -sS target              # SYN scan (stealth, needs root)
nmap -sT target              # TCP connect (no root needed)
nmap -sU target              # UDP scan
nmap -p 22,80,443 target     # Specific ports
nmap -p- target              # All 65535 ports
nmap --top-ports 100 target  # Top 100 ports
nmap -Pn target              # Skip host discovery
```

### Detection
```bash
nmap -sV target              # Service versions
nmap -O target               # OS fingerprint
nmap -sC target              # Default NSE scripts
nmap -A target               # Aggressive (sV+O+sC)
nmap --script vuln target    # Vulnerability scripts
nmap --script smb-vuln-ms17-010 target  # EternalBlue check
```

### Output
```bash
nmap -oN output.txt target   # Normal
nmap -oX output.xml target   # XML
nmap -oA output target       # All formats
```

### Port States
| State | Meaning |
|-------|---------|
| open | Service listening |
| closed | Reachable, no service |
| filtered | Firewall blocking |

### Timing Templates
`-T0` paranoid · `-T1` sneaky · `-T3` normal (default) · `-T4` aggressive · `-T5` insane

> [!warning] All scans require written authorisation. Scanning without permission is illegal. `-sS` SYN scan leaves half-open connections visible in firewall logs.

## 🔑 Key Takeaways
- `-sS` SYN scan is the most common — requires root
- `-sV -sC -O` = maximum target information
- Always save output (`-oA`) — you'll need to reference it later
- Nmap is the first tool used in any engagement

## 🔗 Related Notes
- [[CS101-19 - Tcpdump The Basics]] · [[CS101-26 - Metasploit Introduction]]
- [[Nmap]] · [[Port Scanning]] · [[Reconnaissance]] · [[NSE Scripts]]
