---
tags: [THM, cyber-security-101, offensive-security, room]
platform: TryHackMe
type: room
module: "01 - Start Your Cyber Security Journey"
module_number: 1
room_number: 1
status: "⬜"
url: https://tryhackme.com/room/offensivesecurityintro
difficulty: Easy
---

# 🗡️ Offensive Security Intro

> [!abstract] Summary
> Hack your first website (legally in a safe environment) and experience what an ethical hacker does. Introduction to offensive security using GoBuster to find hidden pages.

**Path:** [[Cyber Security 101]] > Module 1 > Offensive Security Intro

## 🎯 Learning Objectives
- Understand what offensive security means
- Hack a fake banking website using GoBuster
- Learn the difference between offensive and defensive security

## 📖 Key Concepts

### What is Offensive Security?
Attacking systems **with permission** to find vulnerabilities before malicious hackers do.

**Roles:** Penetration Tester · Red Teamer · Bug Bounty Hunter

### Offensive vs Defensive
| Offensive (Red Team) | Defensive (Blue Team) |
|---|---|
| Finds vulnerabilities | Fixes vulnerabilities |
| Attacks systems | Monitors & responds |
| Thinks like attacker | Thinks like defender |

## 🛠️ Tools & Commands

### GoBuster — Directory Brute-Forcing
```bash
gobuster dir -u http://TARGET -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```
| Flag | Description |
|------|-------------|
| `dir` | Directory/file mode |
| `-u` | Target URL |
| `-w` | Wordlist path |

> [!tip] Hidden pages (admin panels, backups) can be found by brute-forcing URLs — they exist even if not linked.

## 🔑 Key Takeaways
- Offensive security = ethical hacking with written permission
- GoBuster reveals hidden attack surface through brute force
- Same skills used to attack are used to build defenses

## 🔗 Related Notes
- [[TryHackMe/Cyber Security 101/Untitled/Defensive Security Intro]] · [[Search Skills]]
- [[CS101-39 - Gobuster The Basics]] · [[Penetration Testing]] · [[Bug Bounty]]
