---
tags: [THM, pre-security, computer-fundamentals, room]
platform: TryHackMe
type: room
module: "Computer Fundamentals"
module_number: 4
room_number: 14
status: "⬜"
url: https://tryhackme.com/room/computertypes
difficulty: Easy
---
# 💻 Computer Types

> [!abstract] Summary
> Overview of the different types of computers — desktops, laptops, servers, embedded systems, mobile devices — and their roles in a networked environment.

**Path:** [[Pre Security (New)]] > [[Computer Fundamentals]] > Computer Types

---

## 📖 Key Concepts

### Types of Computers

| Type | Description | Security Relevance |
|------|-------------|-------------------|
| **Desktop** | Tower/all-in-one for home/office | Common workstation target |
| **Laptop** | Portable personal computer | High theft/loss risk; full disk encryption important |
| **Server** | High-performance, runs 24/7, serves other computers | Primary target in attacks; hosts services |
| **Embedded System** | Dedicated hardware (routers, IoT, industrial) | Often unpatched, exposed — major attack surface |
| **Mobile Device** | Smartphone/tablet | BYOD risks, app vulnerabilities, MDM |
| **Mainframe** | Enterprise, handles massive transactions | Used in banking/government |
| **Supercomputer** | Scientific computing, massive parallel processing | Password cracking, AI |

---

### Servers vs Workstations
| | Server | Workstation |
|---|---|---|
| **Purpose** | Provides services to other machines | Used directly by a person |
| **Hardware** | ECC RAM, RAID, redundant PSU | Standard consumer hardware |
| **OS** | Windows Server, Linux Server | Windows 10/11, macOS |
| **Security** | Hardened, minimal software | More software → larger attack surface |

---

### Embedded Systems & IoT
- Run minimal, specialized OS (often Linux-based)
- Often **lack security updates** — longest-lived attack surface
- Examples: routers, smart TVs, CCTV cameras, medical devices, SCADA/ICS
- **Shodan** — search engine for Internet-connected devices

> [!warning] IoT Security
> Default credentials on IoT devices are a massive risk. Mirai botnet compromised ~600,000 IoT devices using default passwords.

---

## 🔑 Key Takeaways
- Different computer types have different security concerns
- Servers are high-value targets; workstations are common initial access points
- Embedded/IoT devices are often the weakest link due to lack of patching

## 🔗 Related Notes
- [[13 - Inside a Computer System]] · [[15 - Client-Server Basics]] · [[16 - Virtualisation Basics]]
