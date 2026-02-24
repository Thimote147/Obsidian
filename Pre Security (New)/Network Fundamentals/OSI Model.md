---
tags:
  - THM
  - pre-security
  - networking
  - OSI
  - room
platform: TryHackMe
type: room
module: Network Fundamentals
module_number: 2
room_number: 6
status: ⬜
url: https://tryhackme.com/room/osimodelzi
difficulty: Easy
---

# 📚 OSI Model

> [!abstract] Summary
> The OSI (Open Systems Interconnection) Model is the foundational framework that describes how data travels across a network in 7 distinct layers. Each layer has specific responsibilities and communicates only with the layers directly above and below it.

**Path:** [[Pre Security (New)]] > [[Network Fundamentals]] > [[OSI Model]]

---

## 🎯 Learning Objectives
- Understand the purpose of the OSI model
- Know all 7 layers, their roles, and associated protocols
- Understand encapsulation and de-encapsulation
- Apply the model to understand where attacks occur

---

## 📖 The 7 Layers

> [!tip] Mnemonic (Top → Bottom)
> **"All People Seem To Need Data Processing"**
> Application · Presentation · Session · Transport · Network · Data Link · Physical

---

### Layer 7 — Application
- **What it does:** Interface between network services and end-user applications
- **Protocols:** [[HTTP]], [[HTTPS]], [[FTP]], [[SMTP]], [[DNS]], [[SSH]]
- **Data unit:** Data
- **Example:** Your browser sending an HTTP request

### Layer 6 — Presentation
- **What it does:** Translates, encrypts, and compresses data
- **Responsibilities:** Data formatting, encryption (TLS/SSL), character encoding (ASCII, UTF-8)
- **Data unit:** Data
- **Example:** HTTPS encrypting data before transmission

### Layer 5 — Session
- **What it does:** Establishes, manages, and terminates sessions between devices
- **Responsibilities:** Session creation, checkpointing, synchronization
- **Data unit:** Data
- **Example:** Keeping your logged-in state on a website

### Layer 4 — Transport
- **What it does:** End-to-end communication, data segmentation, error checking
- **Protocols:** [[TCP]] (reliable), [[UDP]] (fast/unreliable)
- **Data unit:** Segments (TCP) / Datagrams (UDP)
- **Key concepts:** Port numbers, [[Three-Way Handshake]], flow control

| | TCP | UDP |
|---|---|---|
| **Connection** | Connection-oriented | Connectionless |
| **Reliability** | Guaranteed delivery | No guarantee |
| **Speed** | Slower | Faster |
| **Use case** | Web, email, file transfer | Streaming, DNS, gaming |

### Layer 3 — Network
- **What it does:** Logical addressing and routing between different networks
- **Protocols:** [[IP]] (IPv4/IPv6), [[ICMP]], [[OSPF]], [[BGP]]
- **Data unit:** Packets
- **Devices:** Routers
- **Example:** A router deciding the best path to send a packet to `8.8.8.8`

### Layer 2 — Data Link
- **What it does:** Physical addressing within a local network; error detection
- **Protocols:** [[Ethernet]], [[Wi-Fi]] (802.11), [[ARP]]
- **Data unit:** Frames
- **Devices:** Switches, Network Interface Cards (NICs)
- **Key:** Uses [[MAC Address|MAC addresses]] for delivery within LAN

#### Sub-layers:
- **MAC** (Media Access Control) — controls how devices access the medium
- **LLC** (Logical Link Control) — flow control and error checking

### Layer 1 — Physical
- **What it does:** Transmits raw bits (0s and 1s) over a physical medium
- **Media:** Ethernet cables, fiber optic, radio waves (Wi-Fi)
- **Data unit:** Bits
- **Devices:** Hubs, cables, repeaters, NICs (hardware level)

---

## 🔄 Encapsulation & De-encapsulation

### Encapsulation (Sender — top to bottom)
Each layer **adds its own header** (and sometimes trailer) to the data:

```
Application  → DATA
Transport    → [TCP Header] + DATA          = Segment
Network      → [IP Header] + Segment        = Packet
Data Link    → [Ethernet Header] + Packet + [Trailer] = Frame
Physical     → 01001010... (bits)
```

### De-encapsulation (Receiver — bottom to top)
Each layer **strips its header** and passes data up:
```
Physical → Frame → Packet → Segment → Data
```

---

## 🔒 Security Relevance by Layer

| Layer | Common Attacks |
|-------|---------------|
| 7 — Application | [[SQL Injection]], [[XSS]], [[Directory Traversal]] |
| 6 — Presentation | SSL stripping, weak cipher exploitation |
| 5 — Session | Session hijacking, cookie theft |
| 4 — Transport | [[SYN Flood]], port scanning |
| 3 — Network | IP spoofing, routing attacks |
| 2 — Data Link | [[ARP Spoofing]], MAC flooding |
| 1 — Physical | Cable tapping, jamming |

---

## 🛠️ Layer Quick Reference

| # | Layer | PDU | Address | Device | Protocol |
|---|-------|-----|---------|--------|----------|
| 7 | Application | Data | — | — | HTTP, DNS, FTP |
| 6 | Presentation | Data | — | — | TLS, ASCII |
| 5 | Session | Data | — | — | NetBIOS, RPC |
| 4 | Transport | Segment/Datagram | Port | — | TCP, UDP |
| 3 | Network | Packet | IP | Router | IP, ICMP |
| 2 | Data Link | Frame | MAC | Switch | Ethernet, ARP |
| 1 | Physical | Bit | — | Hub, Cable | — |

---

## 🔑 Key Takeaways
- The OSI model standardizes how network communication is structured in 7 layers
- Encapsulation adds headers going down; de-encapsulation removes them going up
- Each layer has specific protocols, devices, and vulnerabilities
- Understanding which layer an attack targets helps in defense and pen testing

---

## 🔗 Related Notes
- [[What is Networking?]] — IP and MAC fundamentals
- [[Intro to LAN]] — Data Link and Network layer in practice
- [[Packets and Frames]] — Transport layer deep dive (TCP/UDP)
- [[TCP]] · [[UDP]] · [[IP Address]] · [[MAC Address]] · [[ARP]] · [[Encapsulation]]
