---
tags: [THM, cyber-security-101, OWASP, web-hacking, room]
platform: TryHackMe
type: room
module: "14 - OWASP Top 10 (2025)"
module_number: 14
room_number: 54
status: "⬜"
url: https://tryhackme.com/room/owasptop102025
difficulty: Easy
---

# 🕷️ OWASP Top 10 2025: IAAA Failures

> [!abstract] Summary
> OWASP 2025 categories A01, A07, A09 — failures in the IAAA model. Covers Broken Access Control (still #1), Authentication Failures, and Security Logging gaps.

**Path:** [[Cyber Security 101]] > Module 14 > OWASP Top 10 2025: IAAA Failures

## 🎯 Learning Objectives
- Understand the IAAA model
- Exploit Broken Access Control (IDOR)
- Exploit Authentication Failures
- Understand Logging and Monitoring Failures

## 📖 Key Concepts

### IAAA Model
Identification → Authentication → Authorisation → Accountability

### A01 — Broken Access Control (Most Critical)
Users can act outside their intended permissions.

**IDOR (Insecure Direct Object Reference):**
```http
GET /api/user/1/profile    ← your data
GET /api/user/2/profile    ← someone else's data (IDOR!)
```

**Prevention:** Enforce authorisation server-side on every request. Never trust client-supplied IDs alone.

### A07 — Authentication Failures
- No MFA · weak passwords · no rate limiting · predictable session tokens

**Testing:**
```bash
# Check for brute force protection
hydra -l admin -P rockyou.txt target http-post-form "/login:user=^USER^&pass=^PASS^:Invalid"
```

**Prevention:** MFA · rate limiting · strong session tokens · proper logout (invalidate server-side)

### A09 — Security Logging and Monitoring Failures
Insufficient logging means attacks go undetected.

**Must log:** All auth events · access control failures · admin actions · API calls

> [!warning] A09 is what turns a 24-hour breach detection into a 6-month one. The average time to detect a breach is still measured in months. Centralised, tamper-resistant logging closes this gap.

## 🔑 Key Takeaways
- A01 Broken Access Control is the #1 web vulnerability — test every parameter for IDOR
- MFA defeats most authentication attacks — always enable it
- A09 failures allow attackers to operate undetected for months

## 🔗 Related Notes
- [[CS101-33 - Burp Suite The Basics]] · [[CS101-30 - Web Application Basics]]
- [[CS101-55 - OWASP Top 10 2025 Application Design Flaws]]
- [[IDOR]] · [[OWASP Top 10]] · [[MFA]] · [[Broken Access Control]]
