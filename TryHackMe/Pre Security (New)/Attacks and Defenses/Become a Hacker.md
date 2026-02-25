---
tags: [THM, pre-security, attacks-defenses, offensive, room]
platform: TryHackMe
type: room
module: "Attacks and Defenses"
module_number: 7
room_number: 30
status: "⬜"
url: https://tryhackme.com/room/becomeahacker
difficulty: Easy
---

# 🗡️ Become a Hacker

> [!abstract] Summary
> Consolidates all offensive knowledge from the path — the penetration testing methodology, attack phases, and a roadmap for developing hacking skills. Bridges Pre-Security to the Jr Penetration Tester path.

**Path:** [[Pre Security (New)]] > [[Attacks and Defenses]] > Become a Hacker

---

## 📖 Key Concepts

### What is Ethical Hacking?
Ethical hacking = **authorized** simulation of attacks to find vulnerabilities before malicious actors do.

**Types:**
- **Black Box** — no prior knowledge (simulates external attacker)
- **Grey Box** — some knowledge (e.g., credentials provided)
- **White Box** — full knowledge (code, infrastructure — most thorough)

---

### Penetration Testing Methodology

```
1. RECONNAISSANCE (Passive & Active)
   ↓
2. SCANNING & ENUMERATION
   ↓
3. EXPLOITATION
   ↓
4. POST-EXPLOITATION
   ↓
5. REPORTING
```

#### 1. Reconnaissance
**Passive:** No direct contact with target
- OSINT — Google, LinkedIn, Shodan, WHOIS, DNS records
- Tools: `theHarvester`, `maltego`, `recon-ng`

**Active:** Direct interaction with target
- Port scanning, service enumeration
- Tools: [[Nmap]]

#### 2. Scanning & Enumeration
```bash
# Nmap — core scanning tool
nmap -sV -sC -oN scan.txt TARGET      # Service version + default scripts
nmap -p- TARGET                        # All 65535 ports
nmap -sU TARGET                        # UDP scan
nmap -A TARGET                         # Aggressive (OS detect, scripts, traceroute)

# Web enumeration
gobuster dir -u http://target -w /usr/share/wordlists/dirb/common.txt
nikto -h http://target                 # Web vulnerability scanner
```

#### 3. Exploitation
- Exploit identified vulnerabilities
- Tools: Metasploit Framework, exploit-db
- Manual exploitation scripts

#### 4. Post-Exploitation
After gaining access:
```bash
whoami && id           # Who am I?
uname -a               # System info
cat /etc/passwd        # Users
sudo -l                # Sudo privileges
find / -perm -4000     # SUID binaries
ss -tulnp              # Network services
```

#### 5. Reporting
Document: scope, findings, evidence (screenshots), risk ratings, remediation recommendations

---

### Attack Categories

| Category | Examples |
|----------|---------|
| **Web Application** | SQLi, XSS, SSRF, IDOR, LFI/RFI |
| **Network** | Port scanning, MitM, sniffing |
| **OS / Privilege Escalation** | SUID abuse, sudo misconfig, kernel exploits |
| **Social Engineering** | Phishing, vishing, pretexting |
| **Password Attacks** | Brute force, credential stuffing, password spray |
| **Wireless** | WPA2 cracking, evil twin |

---

### Essential Tools Roadmap

| Phase | Tool |
|-------|------|
| Recon | Nmap, theHarvester, Shodan |
| Web | Burp Suite, FFUF, Gobuster, Nikto |
| Exploitation | Metasploit, searchsploit |
| Post-Exploit | LinPEAS, WinPEAS, BloodHound |
| Password | Hashcat, John the Ripper, Hydra |
| Forensics | Wireshark, Volatility, Autopsy |

---

### Next Steps After Pre-Security
1. **Jr Penetration Tester** path on TryHackMe
2. Practice on CTFs: TryHackMe rooms, HackTheBox, PicoCTF
3. Certifications: eJPT → OSCP
4. Build a home lab with VMs

---

## 🔑 Key Takeaways
- Ethical hacking follows a structured methodology: recon → scan → exploit → post-exploit → report
- Always operate with written authorization
- The Pre-Security path provides all the foundational knowledge needed to start hacking
- Next step: Jr Penetration Tester path

## 🔗 Related Notes
- [[TryHackMe/Pre Security (New)/Introduction to Cyber Security/Offensive Security Intro]] · [[Careers in Cyber]] · [[Become a Defender]]
- [[Penetration Testing]] · [[Nmap]] · [[Metasploit]] · [[Burp Suite]] · [[OSCP]]
