---
tags: [THM, cyber-security-101, security-solutions, IDS, IPS, Snort, room]
platform: TryHackMe
type: room
module: "11 - Security Solutions"
module_number: 11
room_number: 45
status: "⬜"
url: https://tryhackme.com/room/idsfundamentals
difficulty: Easy
---

# 🚦 IDS Fundamentals

> [!abstract] Summary
> Learn Intrusion Detection Systems and hands-on Snort — the most widely deployed open-source IDS/IPS. Understand detection methods, rule writing, and alert analysis.

**Path:** [[Cyber Security 101]] > Module 11 > IDS Fundamentals

## 🎯 Learning Objectives
- Understand IDS vs IPS and detection methods
- Use Snort for network intrusion detection
- Write Snort rules
- Analyse Snort alerts

## 📖 Key Concepts

### IDS vs IPS
| | IDS | IPS |
|-|-----|-----|
| Action | Detect & alert | Detect & **block** |
| Placement | Out-of-band | Inline |
| Risk of false positive | Alert only | Blocks legit traffic |

### Detection Methods
| Method | Pros | Cons |
|--------|------|------|
| **Signature** | Fast, precise | Misses 0-days |
| **Anomaly** | Catches new attacks | High false positive rate |

### Snort Usage
```bash
snort -v -i eth0                                 # Sniffer mode
snort -c /etc/snort/snort.conf -i eth0 -A console  # NIDS mode
snort -c /etc/snort/snort.conf -r capture.pcap -A console  # Read PCAP
```

### Snort Rule Structure
```
action protocol src_ip src_port direction dst_ip dst_port (options)

# Brute force detection
alert tcp any any -> $HOME_NET 22 (msg:"SSH Brute Force"; threshold:type threshold, track by_src, count 5, seconds 60; sid:1000001; rev:1;)

# SQL injection
alert tcp any any -> $HTTP_SERVERS 80 (msg:"SQL Injection"; content:"UNION SELECT"; nocase; sid:1000002; rev:1;)
```

### Key Rule Options
| Option | Description |
|--------|-------------|
| `msg` | Alert message |
| `content` | Payload match |
| `nocase` | Case-insensitive |
| `flags:S` | TCP SYN flag |
| `sid` | Unique rule ID |
| `threshold` | Rate-based detection |

> [!tip] Snort rules are extensively used in THM SOC Level 1 path and real-world SOC roles. Understanding rule syntax is a key analyst competency.

## 🔑 Key Takeaways
- IDS detects; IPS blocks — IPS requires careful tuning
- Signature detection misses 0-days; anomaly detection is noisy
- Every Snort rule needs a unique `sid` — increment `rev` on updates
- Snort is free and industry-standard — learn it thoroughly

## 🔗 Related Notes
- [[CS101-44 - Firewall Fundamentals]] · [[CS101-43 - Introduction to SIEM]]
- [[IDS]] · [[Snort]] · [[Network Security]] · [[Intrusion Detection]]
