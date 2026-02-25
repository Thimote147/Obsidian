---
tags: [THM, cyber-security-101, networking, Wireshark, packet-analysis, room]
platform: TryHackMe
type: room
module: "05 - Networking"
module_number: 5
room_number: 18
status: "⬜"
url: https://tryhackme.com/room/wiresharkthebasics
difficulty: Easy
---

# 🦈 Wireshark: The Basics

> [!abstract] Summary
> Learn Wireshark — the world's most popular network protocol analyser. Capture, filter, and analyse traffic to investigate protocols, detect anomalies, and extract evidence.

**Path:** [[Cyber Security 101]] > Module 5 > Wireshark: The Basics

## 🎯 Learning Objectives
- Navigate the Wireshark interface
- Apply display and capture filters
- Follow TCP/HTTP streams
- Use Statistics for traffic overview

## 📖 Key Concepts

### Interface
- **Packet List** — one row per packet
- **Packet Details** — expandable protocol layers
- **Packet Bytes** — raw hex/ASCII

### Display Filters
```
# Protocol
http · dns · tcp · udp · icmp · tls

# IP
ip.addr == 192.168.1.1
ip.src == 192.168.1.1

# Port
tcp.port == 80
udp.port == 53

# Combine
ip.addr == 10.0.0.1 && tcp.port == 80
http || dns
!(arp)

# HTTP
http.request.method == "POST"
http contains "password"

# TCP flags
tcp.flags.syn == 1
tcp.flags.reset == 1    ← connection resets (suspicious)
```

### Follow Streams
Right-click → Follow → TCP/HTTP Stream → shows full conversation in readable form. HTTP streams may reveal credentials.

### Statistics Menu
Protocol Hierarchy · Conversations · Endpoints · IO Graphs

### Capture Filters (BPF — set before capture)
```
host 192.168.1.1 · port 80 · tcp · not arp
```

> [!tip] **SOC use:** `http.request.method == "POST"` finds credential submissions. `dns` spots C2 beaconing. `tcp.flags.syn == 1` detects port scans.

## 🔑 Key Takeaways
- Wireshark is the gold standard for network analysis
- Display filters ≠ capture filters — different syntax
- "Follow TCP Stream" reconstructs full conversations
- HTTP (unencrypted) exposes credentials — hunt for POST requests

## 🔗 Related Notes
- [[CS101-19 - Tcpdump The Basics]] · [[CS101-14 - Networking Concepts]]
- [[Wireshark]] · [[PCAP]] · [[Network Forensics]] · [[Protocol Analysis]]
