---
tags:
  - THM
  - pre-security
  - networking
  - firewall
  - VPN
  - room
platform: TryHackMe
type: room
module: "Network Fundamentals"
module_number: 2
room_number: 8
status: "⬜"
url: https://tryhackme.com/room/extendingyournetwork
difficulty: Easy
---

# 🔌 Extending Your Network

> [!abstract] Summary
> Covers the technologies used to extend and secure networks — Port Forwarding, Firewalls, and VPNs. Explains how these work and their security implications.

**Path:** [[Pre Security (New)]] > [[Network Fundamentals]] > [[Extending Your Network]]

---

## 🎯 Learning Objectives
- Understand Port Forwarding and when it's used
- Learn how Firewalls work and their types
- Understand what VPNs are and how they protect privacy

---

## 📖 Key Concepts

### Port Forwarding
**Port Forwarding** allows services running on a **private/internal network** to be accessible from the **Internet** by configuring the router to redirect traffic.

**How it works:**
```
Internet User → Router (Public IP: 203.0.113.1:80)
                    ↓ Port Forward
             → Internal Server (192.168.1.10:80)
```

**Common use cases:**
- Hosting a web server at home
- Remote desktop access
- Game servers
- CCTV camera access from outside

> [!warning] Security Note
> Port forwarding exposes internal services to the Internet. Any open port is a potential attack surface. Only forward ports when necessary and ensure the service is hardened.

---

### Firewalls

A **Firewall** is a network security device (hardware or software) that **monitors and controls** incoming/outgoing traffic based on predefined security rules.

#### Types of Firewalls

| Type | How It Works | Layer |
|------|-------------|-------|
| **Stateless (Packet Filtering)** | Inspects individual packets; doesn't track connections | L3/L4 |
| **Stateful** | Tracks the state of active connections; more intelligent | L3/L4 |
| **Application Layer (WAF)** | Inspects payload/content; understands HTTP etc. | L7 |
| **Next-Gen Firewall (NGFW)** | Deep packet inspection, IDS/IPS, application awareness | L3–L7 |

#### Firewall Rules
Rules define what traffic is **allowed** or **denied** based on:
- Source/Destination IP
- Source/Destination Port
- Protocol (TCP/UDP/ICMP)
- Direction (inbound/outbound)

**Example Rule (iptables — Linux):**
```bash
# Allow established connections
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Allow SSH (port 22) from a specific IP
iptables -A INPUT -p tcp --dport 22 -s 192.168.1.0/24 -j ACCEPT

# Drop all other inbound traffic
iptables -A INPUT -j DROP
```

> [!tip] Firewall Rule Logic
> Rules are evaluated **top to bottom** — the first matching rule wins. Always end with a default-deny rule.

---

### VPN (Virtual Private Network)

A **VPN** creates an **encrypted tunnel** between a device and a VPN server, protecting traffic from interception and masking the user's true IP address.

#### How a VPN Works
```
Your Device → [Encrypted Tunnel] → VPN Server → Internet
```
- Traffic appears to originate from the **VPN server's IP**
- All data is **encrypted** between you and the VPN server
- Useful on public Wi-Fi to prevent MitM attacks

#### VPN Types

| Type | Use Case |
|------|---------|
| **Remote Access VPN** | Employee connects to company network remotely |
| **Site-to-Site VPN** | Connects two office networks together |
| **SSL/TLS VPN** | Browser-based, no client software needed |

#### Common VPN Protocols

| Protocol | Description |
|----------|-------------|
| **OpenVPN** | Open-source, highly secure, widely used |
| **WireGuard** | Modern, fast, lightweight |
| **IPSec/IKEv2** | Strong security, common on mobile |
| **L2TP/IPSec** | Older but widely supported |
| **PPTP** | Outdated, insecure — avoid |

> [!warning] Security Note
> VPNs are commonly used in pen testing to connect to target lab networks. On TryHackMe, you connect via **OpenVPN** to access rooms.

---

### Network Devices Summary

| Device | Function | Layer |
|--------|----------|-------|
| **Hub** | Broadcasts to all ports (dumb) | L1 |
| **Switch** | Forwards to specific port by MAC | L2 |
| **Router** | Routes packets between networks by IP | L3 |
| **Firewall** | Filters traffic by rules | L3–L7 |
| **Proxy** | Intermediary for client requests | L7 |
| **Load Balancer** | Distributes traffic across servers | L4/L7 |

---

## 🛠️ Commands

```bash
# View routing table (Linux)
ip route
route -n

# View routing table (Windows)
route print

# Test connectivity through a firewall
traceroute 8.8.8.8      # Linux
tracert 8.8.8.8         # Windows

# Connect to TryHackMe via OpenVPN
sudo openvpn your-config.ovpn
```

---

## 🔑 Key Takeaways
- Port forwarding exposes internal services to the Internet — use with caution
- Firewalls filter traffic using rules; stateful firewalls are more intelligent than stateless
- VPNs encrypt traffic and mask your IP — critical for privacy and remote work
- Understanding these technologies is essential for both attacking and defending networks

---

## 🔗 Related Notes
- [[Packets and Frames]] — ports and protocols that firewalls filter
- [[Intro to LAN]] — the internal network these technologies extend
- [[Firewall]] · [[VPN]] · [[Port Forwarding]] · [[NAT]] · [[iptables]]
