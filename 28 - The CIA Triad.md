---
tags: [THM, pre-security, attacks-defenses, CIA-triad, room]
platform: TryHackMe
type: room
module: "Attacks and Defenses"
module_number: 7
room_number: 28
status: "⬜"
url: https://tryhackme.com/room/theciatriad
difficulty: Easy
---

# 🔐 The CIA Triad

> [!abstract] Summary
> The CIA Triad — Confidentiality, Integrity, Availability — is the foundational model for information security. Every security control, attack, and defense can be mapped to one or more of these three pillars.

**Path:** [[Pre Security (New)]] > [[Attacks and Defenses]] > The CIA Triad

---

## 📖 The Three Pillars

### Confidentiality
**Definition:** Ensuring information is accessible **only to those authorized** to access it.

**Threats:** Unauthorized access, data breaches, eavesdropping, insider threats
**Controls:** Encryption, access control, authentication, need-to-know policies

**Examples:**
- Encrypting a database so only authorized users can read it
- Using HTTPS to prevent traffic interception
- Role-based access control (RBAC)

---

### Integrity
**Definition:** Ensuring information is **accurate and unmodified** by unauthorized parties.

**Threats:** Data tampering, MitM attacks, malware modification, corruption
**Controls:** Hashing, digital signatures, version control, checksums, audit logs

**Examples:**
- Hashing a downloaded file to verify it wasn't tampered with
- Digital signatures on software packages
- Database transaction logs

---

### Availability
**Definition:** Ensuring systems and data are **accessible when needed** by authorized users.

**Threats:** DDoS attacks, ransomware, hardware failure, natural disasters
**Controls:** Redundancy, backups, load balancing, DDoS protection, disaster recovery

**Examples:**
- Redundant servers so one failure doesn't take down a service
- Daily backups to recover from ransomware
- CDN to absorb DDoS traffic

---

## CIA vs Common Attacks

| Attack | C | I | A |
|--------|---|---|---|
| Data breach | ✗ | | |
| SQL Injection | ✗ | ✗ | |
| Ransomware | | ✗ | ✗ |
| DDoS | | | ✗ |
| MitM | ✗ | ✗ | |
| Malware | ✗ | ✗ | ✗ |

---

## Extended Models

### Parkerian Hexad (extends CIA)
Adds: **Possession/Control**, **Authenticity**, **Utility**

### AAA (Authentication, Authorization, Accounting)
- **Authentication** — verifying identity (who are you?)
- **Authorization** — verifying permissions (what can you do?)
- **Accounting/Auditing** — tracking actions (what did you do?)

---

## 🔑 Key Takeaways
- Every security decision maps to protecting Confidentiality, Integrity, or Availability
- Use CIA to frame the impact of any vulnerability or attack
- Security controls should address all three pillars

## 🔗 Related Notes
- [[29 - Cryptography Concepts]] · [[Defensive Security Intro]] · [[22 - Operating System Security]]
- [[CIA Triad]] · [[Encryption]] · [[DDoS]] · [[Access Control]]
