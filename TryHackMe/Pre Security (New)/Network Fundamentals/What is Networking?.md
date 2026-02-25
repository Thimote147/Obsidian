---
tags:
  - THM
  - pre-security
  - networking
  - room
platform: TryHackMe
type: room
module: Network Fundamentals
module_number: 2
room_number: 4
status: ⬜
url: https://tryhackme.com/room/whatisnetworking
difficulty: Easy
---

# 🌐 What is Networking?

> [!abstract] Summary
> Introduction to the fundamental concept of computer networks — what they are, how devices communicate, the role of IP and MAC addresses, and how to use the `ping` command to test connectivity.

**Path:** [[Pre Security (New)]] > [[Network Fundamentals]] > [[What is Networking?]]

---

## 🎯 Learning Objectives
- Understand what a network is and why it exists
- Learn what the Internet is
- Understand IP addresses and MAC addresses
- Use the `ping` command to test connectivity

---

## 📖 Key Concepts

### What is a Network?
A **network** is two or more devices connected together to share data and resources. Networks can be as small as two computers in a home, or as large as the Internet.

**Why networks matter in security:**
- Networks are the primary way attackers move between systems
- Understanding networks is fundamental to both attacking and defending

---

### The Internet
The Internet is one giant network made up of millions of private and public networks connected together. It originated from **ARPANET** (Advanced Research Projects Agency Network) in the late 1960s.

---

### IP Addresses
An **IP (Internet Protocol) address** is a unique identifier assigned to every device on a network so they can find and communicate with each other.

#### IPv4
- 32-bit address written as 4 octets separated by dots
- Example: `192.168.1.100`
- Range: `0.0.0.0` to `255.255.255.255`
- ~4.3 billion addresses (now largely exhausted)

#### IPv6
- 128-bit address written in hexadecimal
- Example: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Solves the IPv4 exhaustion problem

#### Public vs Private IP Addresses
| Type | Range | Usage |
|------|-------|-------|
| Private | `10.0.0.0/8` | Internal networks |
| Private | `172.16.0.0/12` | Internal networks |
| Private | `192.168.0.0/16` | Home/office networks |
| Public | Everything else | Internet-routable |

> [!tip] Security Note
> Private IPs are not routable on the Internet. They are used internally and translated to public IPs via [[NAT]] when accessing the Internet.

---

### MAC Addresses
A **MAC (Media Access Control) address** is a **physical hardware address** burned into every network interface card (NIC).

- 48-bit address written as 6 pairs of hexadecimal: `a4:c3:f0:85:ac:2d`
- First 3 pairs = OUI (manufacturer identifier)
- Last 3 pairs = unique device identifier
- Used for communication **within** a local network (Layer 2)
- Can be **spoofed** with software tools

> [!warning] Security Note
> MAC addresses can be spoofed, so they should not be relied on as a sole authentication method.

---

### IP vs MAC — Key Difference
| | IP Address | MAC Address |
|---|---|---|
| **Layer** | Network (L3) | Data Link (L2) |
| **Scope** | Across networks | Within local network |
| **Changes?** | Yes (dynamic/static) | No (hardware-burned, but spoofable) |
| **Format** | `192.168.1.1` | `aa:bb:cc:dd:ee:ff` |

---

## 🛠️ Tools & Commands

### ping
Tests whether a device is reachable on a network by sending **ICMP Echo Request** packets and waiting for a reply.

```bash
ping <IP_ADDRESS or HOSTNAME>
```

**Examples:**
```bash
ping 192.168.1.1          # Ping a local IP
ping tryhackme.com        # Ping a domain (uses DNS to resolve)
ping -c 4 192.168.1.1     # Send exactly 4 packets (Linux)
ping -n 4 192.168.1.1     # Send exactly 4 packets (Windows)
```

**Reading ping output:**
```
PING tryhackme.com (104.26.11.229): 56 data bytes
64 bytes from 104.26.11.229: icmp_seq=0 ttl=57 time=11.2 ms
```
- `ttl` (Time to Live) — decremented at each hop; indicates distance
- `time` — round-trip latency in milliseconds

> [!tip] Security Note
> ICMP is sometimes blocked by firewalls. A non-responsive ping does not always mean the host is down.

---

### Check Your IP Address
```bash
# Linux
ip a
ifconfig

# Windows
ipconfig
```

---

## 🔑 Key Takeaways
- A network connects devices to share data — the Internet is the largest network
- IP addresses identify devices logically; MAC addresses identify them physically
- IPv4 is running out of addresses; IPv6 solves this with a vastly larger space
- `ping` is the simplest tool to test if a host is reachable

---

## 🔗 Related Notes
- [[Intro to LAN]] — deeper look at local networks
- [[OSI Model]] — how networking layers work together
- [[Packets and Frames]] — TCP/IP and how data is transported
- [[IP Address]] · [[MAC Address]] · [[ICMP]] · [[ping]]
