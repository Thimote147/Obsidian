---
tags: [THM, cyber-security-101, OSINT, research, room]
platform: TryHackMe
type: room
module: "01 - Start Your Cyber Security Journey"
module_number: 1
room_number: 3
status: "⬜"
url: https://tryhackme.com/room/searchskills
difficulty: Easy
---

# 🔍 Search Skills

> [!abstract] Summary
> Learn to efficiently search the Internet and use specialized search engines and technical documentation. Essential OSINT and research skills every security professional needs.

**Path:** [[Cyber Security 101]] > Module 1 > Search Skills

## 🎯 Learning Objectives
- Use advanced Google search operators
- Use specialized security search engines (Shodan, Censys, FOFA)
- Navigate technical documentation effectively
- Apply OSINT techniques for recon

## 📖 Key Concepts

### Google Dorking (Advanced Operators)
```
"exact phrase"           → Exact match
site:example.com         → Limit to domain
filetype:pdf             → Specific file type
intitle:"admin panel"    → In page title
inurl:login              → In URL
-keyword                 → Exclude term
cache:example.com        → Cached version
```

**Security examples:**
```
site:github.com "password" filetype:env
intitle:"index of" "backup"
filetype:log inurl:admin
```

### Specialized Search Engines
| Tool | Purpose |
|------|---------|
| **Shodan** | Search engine for Internet-connected devices (IoT, servers, cameras) |
| **Censys** | Internet-wide scanning — certificates, open ports, services |
| **FOFA** | Chinese alternative to Shodan |
| **GreyNoise** | Context on mass scanners and internet noise |
| **VirusTotal** | Scan files/URLs/IPs for malware |

### Technical Documentation
| Resource | Use |
|----------|-----|
| **CVE Details** | Look up CVE vulnerability details |
| **NVD** (nvd.nist.gov) | National Vulnerability Database |
| **Exploit-DB** | Public exploits and PoCs |
| **GTFOBins** | Linux binary exploitation (priv esc) |
| **LOLBAS** | Windows living-off-the-land binaries |
| **HackTricks** | Comprehensive pen testing wiki |

### OSINT Framework
Structured approach to finding public information:
- **Passive** recon: no direct target contact (Shodan, WHOIS, LinkedIn)
- **Active** recon: direct interaction (Nmap, port scanning)

## 🛠️ Commands
```bash
# WHOIS lookup
whois tryhackme.com

# DNS enumeration
dig tryhackme.com ANY
dnsrecon -d tryhackme.com

# theHarvester — email/subdomain OSINT
theHarvester -d tryhackme.com -b google
```

## 🔑 Key Takeaways
- Google dorking reveals sensitive exposed files and pages
- Shodan finds internet-connected devices — critical for external recon
- OSINT gathers intelligence without touching the target
- CVE/Exploit-DB are essential for finding and researching vulnerabilities

## 🔗 Related Notes
- [[TryHackMe/Cyber Security 101/Untitled/Offensive Security Intro]] · [[CS101-23 - Nmap The Basics]]
- [[OSINT]] · [[Shodan]] · [[Google Dorking]] · [[CVE]] · [[Exploit-DB]]
