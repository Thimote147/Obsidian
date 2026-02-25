---
tags:
  - THM
  - pre-security
  - networking
  - TCP
  - UDP
  - room
platform: TryHackMe
type: room
module: "Network Fundamentals"
module_number: 2
room_number: 7
status: "⬜"
url: https://tryhackme.com/room/packetsframes
difficulty: Easy
---

# 📦 Packets and Frames

> [!abstract] Summary
> Deep dive into how data is divided and transmitted across networks. Covers the difference between packets and frames, the TCP three-way handshake, UDP, and how port numbers work.

**Path:** [[Pre Security (New)]] > [[Network Fundamentals]] > [[Packets and Frames]]

---

## 🎯 Learning Objectives
- Understand the difference between packets and frames
- Learn how TCP establishes connections (three-way handshake)
- Understand UDP and when it's used
- Know common port numbers and their protocols

---

## 📖 Key Concepts

### Packets vs Frames

| | **Frame** | **Packet** |
|---|---|---|
| **OSI Layer** | Layer 2 (Data Link) | Layer 3 (Network) |
| **Address** | MAC address | IP address |
| **Scope** | Local network only | Across networks |
| **Protocol** | Ethernet | IP |

> [!tip] Analogy
> Think of a **packet** as a letter inside an envelope (the **frame**). The frame handles delivery within the local network; the packet handles routing between networks.

---

### TCP (Transmission Control Protocol)

TCP is a **connection-oriented, reliable** protocol. Before sending data, it establishes a connection.

#### Three-Way Handshake (TCP Connection Setup)
```
Client                    Server
  |------- SYN ---------->|   "I want to connect"
  |<------ SYN-ACK -------|   "OK, I acknowledge"
  |------- ACK ---------->|   "Great, connection open"
  |                        |
  |===== DATA FLOWS ======|
```

| Flag | Meaning |
|------|---------|
| **SYN** | Synchronize — initiate connection |
| **ACK** | Acknowledge — confirm receipt |
| **FIN** | Finish — close connection gracefully |
| **RST** | Reset — abort connection immediately |

#### TCP Four-Way Handshake (Connection Teardown)
```
Client → FIN  →  Server    "I'm done sending"
Client ← ACK  ←  Server    "Got it"
Client ← FIN  ←  Server    "I'm done too"
Client → ACK  →  Server    "Confirmed, bye"
```

#### TCP Header Fields
| Field | Description |
|-------|-------------|
| Source Port | Sending port number |
| Destination Port | Receiving port number |
| Sequence Number | Tracks order of segments |
| Acknowledgement Number | Next expected byte |
| Flags | SYN, ACK, FIN, RST, PSH, URG |
| Window Size | Flow control — buffer capacity |
| Checksum | Error detection |

> [!warning] Security Note
> **SYN Flood Attack** — Attacker sends many SYN packets but never completes the handshake, exhausting server resources. Mitigated with SYN cookies.

---

### UDP (User Datagram Protocol)

UDP is **connectionless and unreliable** — no handshake, no guaranteed delivery.

**When to use UDP:**
- Speed is more important than reliability
- Small loss is acceptable
- Application handles its own error checking

| Use Case | Why UDP? |
|----------|---------|
| DNS queries | Fast, single request/response |
| Video streaming | Better to skip a frame than pause |
| Online gaming | Low latency is critical |
| VoIP | Real-time, small loss acceptable |
| DHCP | Broadcast-based discovery |

**UDP vs TCP Summary:**

| Feature | TCP | UDP |
|---------|-----|-----|
| Connection | Yes (handshake) | No |
| Reliability | Guaranteed | Not guaranteed |
| Order | In-order delivery | No ordering |
| Speed | Slower | Faster |
| Overhead | Higher | Lower |
| Error checking | Yes | Basic checksum only |

---

### Port Numbers

Ports identify **which service/application** receives data on a host.

- **Range:** 0–65535
- **Well-known ports:** 0–1023 (reserved for standard services)
- **Registered ports:** 1024–49151
- **Dynamic/ephemeral ports:** 49152–65535 (used by clients)

#### Common Port Numbers

| Port | Protocol | Service |
|------|----------|---------|
| 21 | TCP | FTP (File Transfer) |
| 22 | TCP | [[SSH]] (Secure Shell) |
| 23 | TCP | Telnet (unencrypted remote) |
| 25 | TCP | SMTP (email sending) |
| 53 | TCP/UDP | [[DNS]] |
| 80 | TCP | [[HTTP]] |
| 110 | TCP | POP3 (email retrieval) |
| 143 | TCP | IMAP (email retrieval) |
| 443 | TCP | [[HTTPS]] |
| 445 | TCP | SMB (Windows file sharing) |
| 3306 | TCP | MySQL |
| 3389 | TCP | RDP (Remote Desktop) |
| 8080 | TCP | HTTP (alternate) |

> [!tip] Security Note
> Port scanning (e.g., with [[Nmap]]) is a core reconnaissance technique. Knowing default ports helps identify running services.

---

## 🛠️ Commands

```bash
# View open ports (Linux)
ss -tulnp
netstat -tulnp

# View open ports (Windows)
netstat -ano

# Capture packets (requires Wireshark or tcpdump)
tcpdump -i eth0 port 80
tcpdump -i eth0 -w capture.pcap
```

---

## 🔑 Key Takeaways
- Frames operate at Layer 2 (MAC), Packets at Layer 3 (IP)
- TCP provides reliable delivery via the three-way handshake
- UDP is fast but unreliable — used for real-time applications
- Port numbers identify services; memorizing common ports is essential for security

---

## 🔗 Related Notes
- [[OSI Model]] — where TCP/UDP fit in the 7-layer model
- [[Extending Your Network]] — firewalls, VPNs using ports
- [[TCP]] · [[UDP]] · [[Three-Way Handshake]] · [[Port Numbers]] · [[Nmap]]
