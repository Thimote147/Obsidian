---
tags: [THM, cyber-security-101, networking, tcpdump, room]
platform: TryHackMe
type: room
module: "05 - Networking"
module_number: 5
room_number: 19
status: "⬜"
url: https://tryhackme.com/room/tcpdump
difficulty: Easy
---

# 📡 Tcpdump: The Basics

> [!abstract] Summary
> Learn Tcpdump — the command-line packet capture tool. Essential for headless servers and scripted analysis. Capture, filter, and save packets without a GUI.

**Path:** [[Cyber Security 101]] > Module 5 > Tcpdump: The Basics

## 🎯 Learning Objectives
- Capture traffic with Tcpdump
- Apply BPF filters
- Save to PCAP for Wireshark analysis
- Read and interpret Tcpdump output

## 📖 Key Concepts

### Basic Usage
```bash
tcpdump -D                       # List interfaces
tcpdump -i eth0                  # Capture on eth0
tcpdump -i eth0 -c 100           # Capture 100 packets
tcpdump -i eth0 -w capture.pcap  # Save to file
tcpdump -r capture.pcap          # Read from file
tcpdump -nn -i eth0              # No hostname/port resolution
```

### BPF Filters
```bash
tcpdump -i eth0 host 192.168.1.1
tcpdump -i eth0 src 192.168.1.1
tcpdump -i eth0 port 80
tcpdump -i eth0 tcp
tcpdump -i eth0 not arp
tcpdump -i eth0 host 10.0.0.1 and port 443
tcpdump -i eth0 net 192.168.1.0/24
```

### Output Verbosity
```bash
tcpdump -v    # Verbose
tcpdump -A    # ASCII payload
tcpdump -X    # Hex + ASCII payload
```

### Practical Examples
```bash
# Find credentials in HTTP traffic
tcpdump -i eth0 -A port 80 | grep -i "password\|pass\|login"

# Capture DNS
tcpdump -i eth0 port 53 -n

# Detect SYN scans
tcpdump -i eth0 "tcp[tcpflags] & (tcp-syn) != 0"
```

> [!tip] Standard workflow on servers: `tcpdump -w /tmp/cap.pcap` → transfer to analyst machine → open in Wireshark.

## 🔑 Key Takeaways
- Tcpdump = Wireshark without GUI — essential for headless servers
- BPF syntax is same as Wireshark capture filters
- `-nn` prevents DNS resolution — use during investigations
- Save to PCAP with `-w` for later Wireshark analysis

## 🔗 Related Notes
- [[CS101-18 - Wireshark The Basics]] · [[CS101-20 - Nmap The Basics]]
- [[Tcpdump]] · [[PCAP]] · [[BPF Filters]] · [[Network Analysis]]
