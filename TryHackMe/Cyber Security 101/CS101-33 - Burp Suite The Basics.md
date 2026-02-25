---
tags: [THM, cyber-security-101, web-hacking, Burp-Suite, room]
platform: TryHackMe
type: room
module: "08 - Web Hacking"
module_number: 8
room_number: 33
status: "⬜"
url: https://tryhackme.com/room/burpsuitebasics
difficulty: Easy
---

# 🔧 Burp Suite: The Basics

> [!abstract] Summary
> Learn Burp Suite — the industry-standard web application security testing tool. Intercept requests, replay them, fuzz parameters, and analyse web traffic with Burp's powerful proxy.

**Path:** [[Cyber Security 101]] > Module 8 > Burp Suite: The Basics

## 🎯 Learning Objectives
- Configure browser proxy with FoxyProxy
- Intercept and modify requests
- Use Repeater for manual testing
- Use Intruder for fuzzing and brute force

## 📖 Key Concepts

### Burp Suite Modules
| Module | Purpose |
|--------|---------|
| **Proxy** | Intercept browser traffic |
| **Repeater** | Manually replay/modify requests |
| **Intruder** | Automated fuzzing and brute force |
| **Scanner** | Automated vulnerability detection (Pro) |
| **Decoder** | Encode/decode data |
| **Comparer** | Diff two requests/responses |

### Setup
1. Burp → Proxy → Options → 127.0.0.1:8080
2. Browser → FoxyProxy → Burp profile
3. Install Burp CA cert (for HTTPS)

### Proxy — Intercept
```
Intercept ON → browser request pauses → view/modify → Forward
Right-click → Send to Repeater / Intruder
```

### Repeater
Manual request replay with modifications. Essential for:
- Testing SQLi/XSS payloads
- Modifying cookies/headers
- Testing IDOR (change user ID)

### Intruder — Attack Types
| Type | Use |
|------|-----|
| Sniper | Single parameter, single wordlist |
| Battering Ram | Same payload in all positions |
| Pitchfork | Parallel wordlists (username+password) |
| Cluster Bomb | All combinations (brute force) |

**Brute force with Intruder:**
1. Send login request to Intruder
2. Mark `§username§` and `§password§`
3. Pitchfork: load username list + password list
4. Start attack → sort by response length/status

> [!tip] Burp Community (free) has rate-limited Intruder. Use **ffuf** or **Hydra** for faster brute force. Save Burp requests to files → use with `sqlmap -r file.txt`.

## 🔑 Key Takeaways
- Burp Proxy is the foundation — all traffic flows through it
- Repeater = manual testing, Intruder = automated testing
- Always install the CA cert for HTTPS interception
- Send to Repeater (Ctrl+R) is the most-used shortcut

## 🔗 Related Notes
- [[CS101-30 - Web Application Basics]] · [[CS101-37 - SQLMap The Basics]]
- [[CS101-34 - Hydra]] · [[Burp Suite]] · [[Web Application Testing]] · [[IDOR]]
