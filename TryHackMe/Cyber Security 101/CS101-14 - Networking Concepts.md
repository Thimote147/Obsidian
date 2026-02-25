---
tags: [THM, cyber-security-101, networking, OSI, TCP-IP, room]
platform: TryHackMe
type: room
module: "05 - Networking"
module_number: 5
room_number: 14
status: "⬜"
url: https://tryhackme.com/room/networkingconcepts
difficulty: Easy
---

# 🌐 Networking Concepts

> [!abstract] Summary
> Foundational networking — the OSI and TCP/IP models, IP addressing, subnetting, TCP vs UDP, and packet encapsulation. The mandatory base for all network-based security work.

**Path:** [[Cyber Security 101]] > Module 5 > Networking Concepts

## 🎯 Learning Objectives
- Explain the OSI and TCP/IP models
- Understand IP addressing and subnetting
- Differentiate TCP and UDP
- Describe packet encapsulation

## 📖 Key Concepts

### OSI Model (7 Layers)
| # | Layer | Examples | PDU |
|---|-------|----------|-----|
| 7 | Application | HTTP, DNS, FTP | Data |
| 6 | Presentation | SSL/TLS, JPEG | Data |
| 5 | Session | NetBIOS, RPC | Data |
| 4 | Transport | TCP, UDP | Segment |
| 3 | Network | IP, ICMP | Packet |
| 2 | Data Link | Ethernet, ARP | Frame |
| 1 | Physical | Cables, Wi-Fi | Bits |

> [!tip] Mnemonic (bottom→top): **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way

### TCP/IP Model (4 layers)
Application → Transport → Internet → Network Access

### IP Addressing
**Private ranges (RFC 1918):**
```
10.0.0.0/8        (10.x.x.x)
172.16.0.0/12     (172.16-31.x.x)
192.168.0.0/16    (192.168.x.x)
127.0.0.1         (loopback)
```

### Subnetting
`192.168.1.0/24` → 256 addresses (254 usable)
`/25` → 128 per subnet · `/30` → 4 (point-to-point)

### TCP vs UDP
| | TCP | UDP |
|-|-----|-----|
| Connection | 3-way handshake | Connectionless |
| Reliability | Guaranteed | Best effort |
| Use | HTTP, SSH, FTP | DNS, DHCP, VoIP |

**TCP 3-way handshake:** SYN → SYN-ACK → ACK

### Encapsulation
Each layer adds headers as data moves down the stack:
`[ETH][IP][TCP][DATA][ETH trailer]`

## 🔑 Key Takeaways
- OSI layers describe where attacks happen — exploit targets specific layers
- TCP = reliable; UDP = fast
- Private IPs don't route on the internet
- Wireshark shows each encapsulation layer

## 🔗 Related Notes
- [[CS101-15 - Networking Essentials]] · [[CS101-18 - Wireshark The Basics]]
- [[OSI Model]] · [[TCP]] · [[UDP]] · [[IP Addressing]] · [[Subnetting]]
