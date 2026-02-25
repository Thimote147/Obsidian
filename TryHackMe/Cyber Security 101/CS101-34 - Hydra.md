---
tags: [THM, cyber-security-101, offensive-tooling, Hydra, brute-force, room]
platform: TryHackMe
type: room
module: "09 - Offensive Security Tooling"
module_number: 9
room_number: 34
status: "⬜"
url: https://tryhackme.com/room/hydra
difficulty: Easy
---

# 💧 Hydra

> [!abstract] Summary
> Learn Hydra — the fastest online password brute-forcing tool. Attack login forms, SSH, FTP, RDP, and other services using wordlists and credential stuffing.

**Path:** [[Cyber Security 101]] > Module 9 > Hydra

## 🎯 Learning Objectives
- Brute-force SSH and FTP credentials
- Attack HTTP login forms (GET and POST)
- Use credential stuffing techniques
- Understand rate limiting and detection

## 📖 Key Concepts

### Syntax
```bash
hydra -l USER -P wordlist.txt TARGET SERVICE
hydra -L userlist.txt -P wordlist.txt TARGET SERVICE
```

### Common Services
```bash
# SSH
hydra -l admin -P rockyou.txt 10.10.10.1 ssh

# FTP
hydra -l admin -P rockyou.txt 10.10.10.1 ftp

# RDP
hydra -l administrator -P rockyou.txt 10.10.10.1 rdp

# HTTP POST login form
hydra -l admin -P rockyou.txt 10.10.10.1 http-post-form   "/login:username=^USER^&password=^PASS^:Invalid credentials"

# HTTP GET basic auth
hydra -l admin -P rockyou.txt http-get://10.10.10.1/admin
```

### Performance Options
```bash
-t 4      # 4 threads (default)
-t 16     # Faster (may cause lockouts)
-V        # Verbose (show attempts)
-f        # Stop after first valid credential
-u        # Try each user before trying next password
```

> [!warning] **Detection:** Brute-force attacks generate hundreds of failed login entries in logs (Event ID 4625 on Windows, auth.log on Linux). Most accounts lock after 3–10 failed attempts. Use `-t 1` and throttle to avoid lockouts. In real engagements, brute-force is noisy — always check for password spraying as a stealthier alternative.

### HTTP Form Syntax Breakdown
```
"/path:POST_data:failure_string"
   ↑          ↑              ↑
 URL path  ^USER^/^PASS^  Text shown on failure
```

## 🔑 Key Takeaways
- Hydra = online brute force; John/Hashcat = offline hash cracking
- Always use `-f` to stop after finding first valid cred
- HTTP form attacks require identifying the failure string
- `-V` is essential for debugging — see what's being sent

## 🔗 Related Notes
- [[CS101-24 - John the Ripper The Basics]] · [[CS101-35 - Gobuster The Basics]]
- [[CS101-33 - Burp Suite The Basics]] · [[Hydra]] · [[Brute Force]] · [[Password Attacks]]
