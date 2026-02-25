---
tags: [THM, cyber-security-101, defensive-tooling, REMnux, malware-analysis, room]
platform: TryHackMe
type: room
module: "12 - Defensive Security Tooling"
module_number: 12
room_number: 49
status: "⬜"
url: https://tryhackme.com/room/remnuxgettingstarted
difficulty: Easy
---

# 🐧 REMnux: Getting Started

> [!abstract] Summary
> Learn REMnux — a Linux distribution purpose-built for malware analysis. Pre-loaded with tools for static analysis, dynamic analysis, network simulation, and document analysis.

**Path:** [[Cyber Security 101]] > Module 12 > REMnux: Getting Started

## 🎯 Learning Objectives
- Navigate the REMnux environment
- Perform static analysis (strings, DIE)
- Analyse Office macros (oledump, olevba)
- Use network simulation (INetSim)

## 📖 Key Concepts

### Static Analysis Tools
```bash
strings malware.exe                   # Extract readable text
strings -n 8 malware.exe | grep http  # Find URLs
die malware.exe                       # Detect packer/compiler
exiftool malicious.doc                # Metadata
```

### Office Document Analysis
```bash
oledump.py malicious.doc              # List OLE streams
oledump.py malicious.doc -s 7 -v     # Decompressed VBA macro
olevba malicious.doc --reveal         # Deobfuscated VBA

pdf-parser.py suspicious.pdf --stats  # PDF structure
```

### Network Simulation
```bash
sudo inetsim    # Simulates DNS, HTTP, SMTP, FTP...
# All malware C2 traffic → INetSim (safe, no real internet)
```

### Dynamic Analysis
```bash
strace ./malware    # Trace system calls
ltrace ./malware    # Trace library calls
inotifywait -r -m /tmp/   # Watch filesystem changes
tcpdump -i lo -w cap.pcap  # Capture traffic during execution
```

> [!tip] Always start with `strings` — it reveals URLs, IPs, registry keys, and function names in seconds. Then use `die` to check for packers before deeper analysis.

## 🔑 Key Takeaways
- REMnux = pre-built Linux malware lab — everything ready to use
- `strings` is always step one — quick indicator extraction
- oledump/olevba target Office macros — the most common malware vector
- INetSim simulates internet for safe dynamic analysis

## 🔗 Related Notes
- [[CS101-48 - CAPA The Basics]] · [[CS101-50 - FlareVM Arsenal of Tools]]
- [[REMnux]] · [[Malware Analysis]] · [[INetSim]] · [[oledump]] · [[Dynamic Analysis]]
