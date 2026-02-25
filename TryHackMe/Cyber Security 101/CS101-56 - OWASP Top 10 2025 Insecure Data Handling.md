---
tags: [THM, cyber-security-101, OWASP, web-hacking, deserialization, room]
platform: TryHackMe
type: room
module: "14 - OWASP Top 10 (2025)"
module_number: 14
room_number: 56
status: "⬜"
url: https://tryhackme.com/room/owasptop102025
difficulty: Easy
---

# 🕷️ OWASP Top 10 2025: Insecure Data Handling

> [!abstract] Summary
> OWASP 2025 categories A04, A05, A08 — Insecure Design, Security Misconfiguration, and Software/Data Integrity Failures including deserialization and supply chain attacks.

**Path:** [[Cyber Security 101]] > Module 14 > OWASP Top 10 2025: Insecure Data Handling

## 📖 Key Concepts

### A04 — Insecure Design
Security flaws in architecture, not just implementation.
- Business logic flaws (negative quantity in cart = refund)
- No threat modelling during design phase
- No rate limiting by design

**Prevention:** Threat modelling (STRIDE) · security requirements from day 1

### A05 — Security Misconfiguration
Default credentials · directory listing · verbose error messages · exposed admin panels · public S3 buckets

```bash
# Test for defaults
gobuster dir -u http://target.com -w admin-panels.txt

# Check S3 bucket
aws s3 ls s3://bucket-name --no-sign-request
```

**Prevention:** Harden defaults · disable unnecessary features · no stack traces to users

> [!warning] Misconfigured cloud storage is one of the most common breach causes. Millions of records have been exposed through public S3 buckets. Always audit cloud storage ACLs.

### A08 — Software and Data Integrity Failures

**Insecure Deserialization:**
```python
import pickle
obj = pickle.loads(user_data)   # DANGEROUS — arbitrary code execution!
```

**Supply Chain Attacks:**
- SolarWinds, XZ Utils backdoor — malicious code in dependencies
- Typosquatting — `reqeusts` instead of `requests`

**Prevention:**
- Never deserialise untrusted data
- Verify digital signatures on packages
- Dependency pinning with hash verification

## 🔑 Key Takeaways
- A04: Fix the architecture, not just the code — use threat modelling
- A05: Harden defaults, disable unused features, never expose stack traces
- A08: Never deserialise untrusted input — leads directly to RCE
- Supply chain attacks are rising — verify software integrity at every stage

## 🔗 Related Notes
- [[CS101-54 - OWASP Top 10 2025 IAAA Failures]] · [[CS101-55 - OWASP Top 10 2025 Application Design Flaws]]
- [[OWASP Top 10]] · [[Security Misconfiguration]] · [[Deserialization]] · [[Supply Chain Attacks]]
