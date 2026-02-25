---
tags: [THM, cyber-security-101, networking, DNS, HTTP, FTP, room]
platform: TryHackMe
type: room
module: "05 - Networking"
module_number: 5
room_number: 16
status: "⬜"
url: https://tryhackme.com/room/networkingcoreprotocols
difficulty: Easy
---

# 🌐 Networking Core Protocols

> [!abstract] Summary
> Deep dive into the core TCP/IP protocols — DNS, HTTP, FTP, SMTP. Understanding these is essential for both exploitation and traffic analysis.

**Path:** [[Cyber Security 101]] > Module 5 > Networking Core Protocols

## 🎯 Learning Objectives
- Understand DNS resolution and record types
- Know HTTP request/response structure
- Understand FTP and SMTP
- Interact with protocols manually using netcat/telnet

## 📖 Key Concepts

### DNS (Port 53)
Translates domains → IP addresses.

| Record | Purpose |
|--------|---------|
| **A** | IPv4 address |
| **AAAA** | IPv6 address |
| **CNAME** | Alias |
| **MX** | Mail server |
| **TXT** | SPF, DKIM |
| **NS** | Nameservers |
| **PTR** | Reverse DNS |

```bash
nslookup tryhackme.com
dig tryhackme.com A
dig tryhackme.com MX
dig @8.8.8.8 tryhackme.com   # Use specific resolver
```

> [!warning] **DNS abuse:** tunnelling (C2 over DNS), DNS spoofing, DNS amplification DDoS. Monitor for unusual query volumes and long TXT records.

### HTTP (Port 80) / HTTPS (Port 443)
**Methods:** GET · POST · PUT · DELETE · HEAD · OPTIONS

**Status codes:** 200 OK · 301 Redirect · 401 Unauth · 403 Forbidden · 404 Not Found · 500 Server Error

```bash
# Manual HTTP with netcat
nc target.com 80
GET / HTTP/1.1
Host: target.com
```

### FTP (Port 21/20)
File transfer — **credentials transmitted in plaintext!**
```bash
ftp target.com
get filename    # Download
put filename    # Upload
```

### SMTP (Port 25/587/465)
Email sending. Can be tested manually with telnet to verify open relay.

## 🔑 Key Takeaways
- DNS is the internet's phonebook — also a frequent attack vector
- HTTP is plaintext — HTTPS encrypts with TLS
- FTP sends credentials in cleartext — use SFTP instead
- Manual protocol testing (netcat) reveals server behaviour

## 🔗 Related Notes
- [[CS101-15 - Networking Essentials]] · [[CS101-17 - Networking Secure Protocols]]
- [[CS101-18 - Wireshark The Basics]] · [[DNS]] · [[HTTP]] · [[FTP]]
