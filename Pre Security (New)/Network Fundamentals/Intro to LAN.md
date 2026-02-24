---
tags:
  - THM
  - pre-security
  - networking
  - LAN
  - room
platform: TryHackMe
type: room
module: Network Fundamentals
module_number: 2
room_number: 5
status: ⬜
url: https://tryhackme.com/room/introtolan
difficulty: Easy
---

# 🖧 Intro to LAN

> [!abstract] Summary
> Covers Local Area Network (LAN) topologies, subnetting, the ARP protocol, and DHCP. Foundational knowledge for understanding how devices communicate within a local network.

**Path:** [[Pre Security (New)]] > [[Network Fundamentals]] > [[Intro to LAN]]

---

## 🎯 Learning Objectives
- Understand LAN topologies and their pros/cons
- Learn what subnetting is and why it's used
- Understand ARP and how devices resolve IP → MAC
- Understand DHCP and how devices get IP addresses

---

## 📖 Key Concepts

### LAN Topologies

#### Star Topology
- All devices connect to a **central switch or hub**
- Most common in modern networks
- **Pros:** Reliable — one cable failure doesn't affect others; easy to add devices
- **Cons:** Single point of failure (the switch); more cabling required

#### Bus Topology
- All devices connect to a **single backbone cable**
- **Pros:** Cheap, simple
- **Cons:** Single point of failure; collisions; hard to troubleshoot; rarely used today

#### Ring Topology
- Devices connected in a **closed loop**; data travels in one direction
- **Pros:** Easier to troubleshoot than bus
- **Cons:** One failure breaks the whole ring; rarely used today

---

### Switches vs Routers

| Device | Function |
|--------|----------|
| **Switch** | Connects devices **within** a LAN; forwards frames using MAC addresses (Layer 2) |
| **Router** | Connects **different networks** together; routes packets using IP addresses (Layer 3) |

> [!tip] Key Difference
> Switches work within a network. Routers connect networks to each other (including to the Internet).

---

### Subnetting
**Subnetting** divides a large network into smaller, more manageable sub-networks.

#### Why Subnet?
- Efficiency — only broadcast within the subnet
- Security — isolate sensitive systems (e.g., servers from workstations)
- Organization — group devices logically

#### Subnet Mask
Defines which part of an IP address is the **network** portion and which is the **host** portion.

| CIDR | Subnet Mask | # Hosts |
|------|-------------|---------|
| `/8` | `255.0.0.0` | ~16 million |
| `/16` | `255.255.0.0` | ~65,000 |
| `/24` | `255.255.255.0` | 254 |
| `/30` | `255.255.255.252` | 2 |

**Example:**
- IP: `192.168.1.100`
- Subnet: `/24` → network is `192.168.1.0`, hosts from `.1` to `.254`

#### Special Addresses in a Subnet
- **Network address** — first address (e.g., `192.168.1.0`) — identifies the subnet
- **Broadcast address** — last address (e.g., `192.168.1.255`) — sends to all hosts
- **Usable hosts** — everything in between

---

### ARP (Address Resolution Protocol)
ARP resolves an **IP address → MAC address** within a local network.

**How it works:**
```
1. Device A wants to send data to 192.168.1.5
2. A doesn't know the MAC address
3. A broadcasts: "Who has 192.168.1.5? Tell 192.168.1.1"
4. Device B (192.168.1.5) replies with its MAC address
5. A stores this in its ARP cache
```

**ARP Cache commands:**
```bash
# Linux / Mac
arp -a

# Windows
arp -a
```

> [!warning] Security Note
> **ARP Spoofing/Poisoning** — An attacker can send fake ARP replies, associating their MAC with another device's IP. This enables **Man-in-the-Middle (MitM)** attacks.

---

### DHCP (Dynamic Host Configuration Protocol)
DHCP automatically assigns IP addresses to devices joining a network.

**DHCP DORA Process:**
```
D — Discover  → Client broadcasts: "I need an IP!"
O — Offer     → Server: "Here, take 192.168.1.100"
R — Request   → Client: "I accept 192.168.1.100"
A — Acknowledge → Server: "Confirmed, it's yours"
```

**What DHCP assigns:**
- IP Address
- Subnet Mask
- Default Gateway
- DNS Server(s)
- Lease duration

> [!tip] Security Note
> **Rogue DHCP Server** — An attacker can run a fake DHCP server and assign themselves as the gateway, enabling traffic interception.

---

## 🛠️ Commands

```bash
# View ARP table
arp -a

# View network interfaces and IPs (Linux)
ip a
ip route

# Release/renew DHCP (Windows)
ipconfig /release
ipconfig /renew

# Release/renew DHCP (Linux)
sudo dhclient -r    # release
sudo dhclient       # renew
```

---

## 🔑 Key Takeaways
- Star topology is dominant in modern networks; switches are the central point
- Subnetting segments networks for efficiency, security, and organization
- ARP maps IP → MAC addresses within a LAN (vulnerable to spoofing)
- DHCP automatically assigns IP config via the DORA process

---

## 🔗 Related Notes
- [[What is Networking?]] — IP and MAC address basics
- [[OSI Model]] — where ARP and subnetting fit in the layers
- [[Packets and Frames]] — how frames are delivered using MAC addresses
- [[ARP]] · [[DHCP]] · [[Subnetting]] · [[Switch]] · [[Router]]
