---
tags: [THM, cyber-security-101, active-directory, windows, room]
platform: TryHackMe
type: room
module: "03 - Windows and AD Fundamentals"
module_number: 3
room_number: 10
status: "⬜"
url: https://tryhackme.com/room/winadbasics
difficulty: Easy
---

# 🏢 Active Directory Basics

> [!abstract] Summary
> Introduction to Active Directory — the cornerstone of Windows enterprise environments. Learn AD structure, users, groups, OUs, Group Policy, and Kerberos/NTLM authentication.

**Path:** [[Cyber Security 101]] > Module 3 > Active Directory Basics

## 🎯 Learning Objectives
- Understand AD purpose and domain structure
- Navigate objects: users, computers, groups, OUs
- Understand Group Policy Objects (GPOs)
- Know Kerberos and NTLM authentication flows

## 📖 Key Concepts

### AD Structure
```
Forest → Domain (corp.local) → OUs → Users/Computers/Groups
```

### High-Value Groups
| Group | Permissions |
|-------|------------|
| **Domain Admins** | Full control over domain |
| **Enterprise Admins** | Full control over forest |
| **Schema Admins** | Modify AD schema |

> [!warning] **Domain Admins = Crown Jewel.** Compromising one Domain Admin = full domain compromise. This is the ultimate objective of most Windows network attacks.

### Kerberos Authentication
1. Client → KDC: Request TGT (using password hash)
2. KDC → Client: Encrypted TGT
3. Client → KDC: Request Service Ticket using TGT
4. Service validates ticket → access granted

**Attack techniques:** Kerberoasting · Pass-the-Ticket · Golden Ticket · Silver Ticket

### NTLM (Legacy)
Challenge-response. **Attacks:** Pass-the-Hash · NTLM Relay

### Group Policy
```cmd
gpupdate /force     # Force apply GPOs
gpresult /r         # Show applied GPOs
```

## 🔑 Key Takeaways
- AD controls the entire Windows enterprise — compromise it = game over
- Kerberos is the primary auth protocol — understand for attack AND defence
- GPOs push security policy at scale — misconfigured GPOs = attack vector

## 🔗 Related Notes
- [[CS101-09 - Windows Fundamentals 3]] · [[CS101-28 - Metasploit Meterpreter]]
- [[Kerberos]] · [[NTLM]] · [[Domain Admin]] · [[GPO]] · [[Privilege Escalation]]
