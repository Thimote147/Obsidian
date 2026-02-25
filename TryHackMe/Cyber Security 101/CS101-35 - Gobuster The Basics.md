---
tags: [THM, cyber-security-101, offensive-tooling, Gobuster, enumeration, room]
platform: TryHackMe
type: room
module: "09 - Offensive Security Tooling"
module_number: 9
room_number: 35
status: "⬜"
url: https://tryhackme.com/room/gobusterthebasics
difficulty: Easy
---

# 🔍 Gobuster: The Basics

> [!abstract] Summary
> Learn Gobuster — a fast directory and DNS brute-forcing tool. Discover hidden paths, files, subdomains, and virtual hosts on web targets.

**Path:** [[Cyber Security 101]] > Module 9 > Gobuster: The Basics

## 🎯 Learning Objectives
- Use Gobuster for directory and file enumeration
- Enumerate DNS subdomains
- Discover virtual hosts
- Select appropriate wordlists

## 📖 Key Concepts

### Modes
```bash
gobuster dir   # Directory/file bruteforce
gobuster dns   # Subdomain enumeration
gobuster vhost # Virtual host enumeration
```

### Directory Enumeration
```bash
gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt

# With file extensions
gobuster dir -u http://target.com   -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt   -x php,html,txt,bak

# Authenticated
gobuster dir -u http://target.com -w wordlist.txt   -H "Cookie: session=abc123"

# Proxy through Burp
gobuster dir -u http://target.com -w wordlist.txt   --proxy http://127.0.0.1:8080
```

### DNS Subdomain Enumeration
```bash
gobuster dns -d target.com   -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt

# Show IP addresses
gobuster dns -d target.com -w wordlist.txt --show-ips
```

### Virtual Host Enumeration
```bash
gobuster vhost -u http://target.com   -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt   --append-domain
```

### Recommended Wordlists (SecLists)
```bash
/usr/share/seclists/Discovery/Web-Content/common.txt
/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt
/usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
```

> [!tip] Install SecLists: `sudo apt install seclists`. These wordlists are far better than basic wordlists. `directory-list-2.3-medium.txt` is the standard for CTFs.

## 🔑 Key Takeaways
- Gobuster finds hidden content — always run during web enumeration
- `-x php,html,txt` finds hidden files, not just directories
- DNS mode finds subdomains that may have less security
- SecLists > default wordlists — use them every time

## 🔗 Related Notes
- [[CS101-34 - Hydra]] · [[CS101-33 - Burp Suite The Basics]]
- [[CS101-36 - Shells Overview]] · [[Gobuster]] · [[Directory Enumeration]] · [[SecLists]]
