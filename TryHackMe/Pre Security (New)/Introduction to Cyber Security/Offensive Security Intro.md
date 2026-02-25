---
tags:
  - THM
  - pre-security
  - offensive-security
  - room
platform: TryHackMe
type: room
module: Introduction to Cyber Security
module_number: 1
room_number: 1
status: ⬜
url: https://tryhackme.com/room/offensivesecurityintro
difficulty: Easy
---
# 🗡️ Offensive Security Intro

> [!abstract] Summary
> Introduction to the offensive side of cybersecurity. Learn what ethical hacking means, how hackers think, and get a first taste of hacking a fake banking application using a command-line tool.

**Path:** [[Pre Security (New)]] > [[Introduction to Cyber Security]] > [[TryHackMe/Pre Security (New)/Introduction to Cyber Security/Offensive Security Intro]]

---

## 🎯 Learning Objectives
- Understand what offensive security means
- Learn the difference between offensive and defensive security
- Perform a first basic web application hack
- Understand the concept of bug bounty

---

## 📖 Key Concepts

### What is Offensive Security?
Offensive security consists of **attacking systems** to find vulnerabilities before malicious hackers do. The goal is to think like an attacker in order to better defend systems.

Common offensive security roles:
- **Penetration Tester** — tests systems with client permission
- **Red Teamer** — simulates full adversary attacks
- **Bug Bounty Hunter** — finds vulnerabilities and reports them for reward

### Offensive vs Defensive Security
| Offensive (Red Team) | Defensive (Blue Team) |
|---|---|
| Attacks systems | Defends systems |
| Finds vulnerabilities | Patches vulnerabilities |
| Thinks like an attacker | Monitors and responds |
| Pen testing, exploitation | SOC, SIEM, incident response |

### The Hacker Mindset
- Always ask: *"What can go wrong here?"*
- Look for unintended uses of features
- Think about what data could be exposed or manipulated

---

## 🛠️ Tools & Commands

### GoBuster — Directory Brute-Forcing
Used to find hidden pages/directories on a web server by brute-forcing URLs.

```bash
gobuster dir -u http://TARGET_URL -w /path/to/wordlist.txt
```

| Flag | Description |
|------|-------------|
| `dir` | Directory/file brute-force mode |
| `-u` | Target URL |
| `-w` | Path to wordlist |

**Example:**
```bash
gobuster dir -u http://fakebank.thm -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

> [!tip] Key Insight
> Many web applications have hidden pages (admin panels, test pages, backup files) that are not linked anywhere but still accessible if you know the URL. GoBuster automates finding these.

---

## 🔑 Key Takeaways
- Offensive security = ethical hacking with permission
- Tools like GoBuster can reveal hidden attack surfaces
- The same skills used to attack are used to defend
- Always operate within legal and ethical boundaries

---

## 🔗 Related Notes
- [[TryHackMe/Pre Security (New)/Introduction to Cyber Security/Defensive Security Intro]] — the other side of the coin
- [[Careers in Cyber]] — offensive career paths
- [[Become a Hacker]] — deeper dive into hacking
- [[Penetration Testing]] · [[Bug Bounty]] · [[GoBuster]]
