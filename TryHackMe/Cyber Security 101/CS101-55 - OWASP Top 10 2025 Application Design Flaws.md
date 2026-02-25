---
tags: [THM, cyber-security-101, OWASP, web-hacking, SSRF, injection, room]
platform: TryHackMe
type: room
module: "14 - OWASP Top 10 (2025)"
module_number: 14
room_number: 55
status: "⬜"
url: https://tryhackme.com/room/owasptop102025
difficulty: Easy
---

# 🕷️ OWASP Top 10 2025: Application Design Flaws

> [!abstract] Summary
> OWASP 2025 categories A02, A03, A06, A10 — Cryptographic Failures, Injection, Vulnerable Components, and SSRF. Design-level vulnerabilities at the architecture layer.

**Path:** [[Cyber Security 101]] > Module 14 > OWASP Top 10 2025: Application Design Flaws

## 📖 Key Concepts

### A02 — Cryptographic Failures
HTTP instead of HTTPS · weak algorithms (MD5, DES) · hardcoded keys · unencrypted sensitive data

```bash
nmap --script ssl-enum-ciphers -p 443 target.com   # Check TLS config
```

**Prevention:** TLS 1.2+ everywhere · AES-256-GCM · bcrypt for passwords

### A03 — Injection
```bash
# SQL Injection
' OR 1=1--

# Command Injection
127.0.0.1; whoami

# XSS
<script>alert(document.cookie)</script>
```

**Prevention:** Parameterised queries · input validation · WAF

### A06 — Vulnerable and Outdated Components
Log4Shell (CVE-2021-44228) — millions of servers running unpatched Log4j.

```bash
npm audit   # Node.js
pip-audit   # Python
```

**Prevention:** Dependency tracking (SBOM) · regular patching · vulnerability advisories

### A10 — SSRF (Server-Side Request Forgery)
Server makes requests on attacker's behalf — reaches internal services.

```
# Payloads
http://127.0.0.1/admin
http://169.254.169.254/latest/meta-data/   ← AWS credentials!
```

**Prevention:** Whitelist allowed URLs · block private/loopback ranges

> [!warning] SSRF against cloud environments (AWS/GCP/Azure) can leak IAM credentials from the metadata service — leading to full cloud account compromise.

## 🔑 Key Takeaways
- A02: TLS everywhere, strong crypto, no hardcoded keys
- A03: Parameterised queries defeat SQLi — the most impactful single fix
- A06: Log4Shell showed scale of unpatched component risk — track your dependencies
- A10 SSRF: metadata endpoint `169.254.169.254` is the first thing to test

## 🔗 Related Notes
- [[CS101-54 - OWASP Top 10 2025 IAAA Failures]] · [[CS101-56 - OWASP Top 10 2025 Insecure Data Handling]]
- [[CS101-32 - SQL Fundamentals]] · [[SSRF]] · [[Injection]] · [[OWASP Top 10]]
