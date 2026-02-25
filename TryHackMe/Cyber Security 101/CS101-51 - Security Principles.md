---
tags: [THM, cyber-security-101, career, security-principles, room]
platform: TryHackMe
type: room
module: "13 - Build Your Cyber Security Career"
module_number: 13
room_number: 51
status: "⬜"
url: https://tryhackme.com/room/securityprinciples
difficulty: Easy
---

# 🔐 Security Principles

> [!abstract] Summary
> Foundational security principles — CIA Triad, Defence in Depth, Zero Trust, least privilege, and common security models. The theoretical backbone behind every security control.

**Path:** [[Cyber Security 101]] > Module 13 > Security Principles

## 🎯 Learning Objectives
- Understand the CIA Triad
- Apply least privilege and separation of duties
- Understand Defence in Depth and Zero Trust
- Know common security models (Bell-LaPadula, Biba)

## 📖 Key Concepts

### CIA Triad
| Pillar | Goal | Attack Example | Control |
|--------|------|---------------|---------|
| **Confidentiality** | Only authorised access | Data breach | Encryption, access control |
| **Integrity** | Data not unauthorised modified | SQLi, MitM | Hashing, signatures |
| **Availability** | Systems accessible when needed | DDoS, ransomware | Redundancy, backups |

### Core Principles
**Least Privilege** — minimum access needed to perform the role.

**Separation of Duties** — no single person controls a complete critical process (e.g. code writer ≠ deployer).

**Defence in Depth** — multiple overlapping layers. Compromise of one ≠ full compromise.
```
Internet → Firewall → IDS → DMZ → Internal Firewall → Servers → Encryption
```

**Zero Trust** — "Never trust, always verify." No implicit trust based on network location.

### Security Models
| Model | Protects | Rule |
|-------|---------|------|
| **Bell-LaPadula** | Confidentiality | No read up, no write down |
| **Biba** | Integrity | No read down, no write up |

### Common Frameworks
| Framework | Purpose |
|-----------|---------|
| **NIST CSF** | Identify · Protect · Detect · Respond · Recover |
| **ISO 27001** | Information Security Management System |
| **CIS Controls** | 18 prioritised security controls |

> [!tip] NIST CSF maps directly to SOC team functions. If an interviewer asks "how do you approach security?" — NIST CSF is a structured answer.

## 🔑 Key Takeaways
- CIA Triad is the foundation — every control maps to one or more pillars
- Least privilege reduces blast radius of any compromise
- Zero Trust is the modern architecture — assume breach
- Defence in Depth ensures no single point of failure

## 🔗 Related Notes
- [[CS101-52 - Careers in Cyber]] · [[TryHackMe/Cyber Security 101/Untitled/Defensive Security Intro]]
- [[CIA Triad]] · [[Zero Trust]] · [[Least Privilege]] · [[NIST CSF]] · [[Defence in Depth]]
