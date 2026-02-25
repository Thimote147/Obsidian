---
tags: [THM, cyber-security-101, defensive-tooling, CyberChef, encoding, room]
platform: TryHackMe
type: room
module: "12 - Defensive Security Tooling"
module_number: 12
room_number: 47
status: "⬜"
url: https://tryhackme.com/room/cyberchefbasics
difficulty: Easy
---

# 🍳 CyberChef: The Basics

> [!abstract] Summary
> Learn CyberChef — the "Swiss Army Knife" for data transformation. Encode, decode, hash, and analyse data with a drag-and-drop recipe interface. Essential for CTFs and investigations.

**Path:** [[Cyber Security 101]] > Module 12 > CyberChef: The Basics

## 🎯 Learning Objectives
- Navigate the CyberChef interface
- Decode common encodings (Base64, hex, URL)
- Chain operations into recipes
- Use CyberChef in investigations

## 📖 Key Concepts

### Access
Browser-based — no install: **gchq.github.io/CyberChef**

### Common Operations
```
From Base64 / To Base64
From Hex / To Hex
URL Decode
HTML Entity Decode
ROT13
XOR (with key)
MD5 / SHA256
Gunzip / Raw Inflate
Extract URLs · Extract IP addresses
Regular expression
```

### Recipes — Chaining Operations
```
Input: aGVsbG8gd29ybGQ=   (Base64 of hex of "hello world")

Recipe:
1. From Base64
2. From Hex
→ Output: hello world
```

### Practical Use Cases

**CTF:** Decode challenge strings (Base64, XOR, ROT13, multi-layer)

**Malware Analysis:**
```
Input: powershell -EncodedCommand <BASE64>
Recipe: From Base64 → Decode text (UTF-16LE)
→ Output: Deobfuscated PowerShell command
```

**Forensics:** Decode cookie values · analyse email headers · decode PCAP payloads

**IOC Extraction:** Extract URLs / Extract IP addresses operations pull IOCs from log dumps or malware strings

> [!tip] Use the **Magic** operation — CyberChef auto-detects the encoding and suggests a recipe. Perfect starting point when you don't know the encoding.

## 🔑 Key Takeaways
- Bookmark gchq.github.io/CyberChef — use it constantly
- Magic auto-detects encoding
- Chained recipes handle multi-layer obfuscation
- Extract URLs/IPs is invaluable for IOC extraction from malware/logs

## 🔗 Related Notes
- [[CS101-48 - CAPA The Basics]] · [[CS101-40 - Digital Forensics Fundamentals]]
- [[CyberChef]] · [[Encoding]] · [[Malware Analysis]] · [[IOC]] · [[CTF Tools]]
