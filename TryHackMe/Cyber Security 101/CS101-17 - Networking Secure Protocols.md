---
tags: [THM, cyber-security-101, networking, TLS, SSH, VPN, room]
platform: TryHackMe
type: room
module: "05 - Networking"
module_number: 5
room_number: 17
status: "⬜"
url: https://tryhackme.com/room/networkingsecureprotocols
difficulty: Easy
---

# 🔒 Networking Secure Protocols

> [!abstract] Summary
> How TLS, SSH, and VPN secure network traffic. Foundations of encrypted communications — critical for implementing security and identifying weaknesses.

**Path:** [[Cyber Security 101]] > Module 5 > Networking Secure Protocols

## 🎯 Learning Objectives
- Understand TLS and the HTTPS handshake
- Use SSH for secure remote access and tunnelling
- Understand VPN types
- Identify secure vs insecure protocol equivalents

## 📖 Key Concepts

### TLS Handshake
1. Client Hello (cipher suites, TLS version)
2. Server Hello + Certificate
3. Client verifies certificate
4. Key exchange → session key
5. Encrypted session (symmetric)

**Insecure → Secure replacements:**
| Insecure | Secure | Port |
|----------|--------|------|
| HTTP (80) | HTTPS (443) | TLS |
| FTP (21) | SFTP (22) | SSH |
| Telnet (23) | SSH (22) | — |
| SMTP (25) | SMTPS (465/587) | TLS |

### SSH (Port 22)
```bash
ssh user@10.10.x.x                        # Password auth
ssh-keygen -t ed25519                     # Generate key pair
ssh -i ~/.ssh/id_ed25519 user@host        # Key auth

# Tunnelling
ssh -L 8080:127.0.0.1:80 user@host       # Local forward
ssh -R 9090:127.0.0.1:22 user@host       # Remote forward
ssh -D 1080 user@host                     # SOCKS proxy
```

> [!tip] SSH local port forwarding is essential for pivoting in pen tests — expose internal services through the compromised host.

### VPN Types
| Protocol | Description |
|----------|-------------|
| **OpenVPN** | Open-source, configurable |
| **WireGuard** | Modern, fast, minimal |
| **IPsec** | Enterprise standard |
| **PPTP** | Legacy — insecure, avoid |

> [!warning] **Never share your SSH private key.** Use `chmod 600 ~/.ssh/id_ed25519` to protect it. Key compromise = all systems using that key are compromised.

## 🔑 Key Takeaways
- TLS = asymmetric for key exchange, symmetric for bulk data
- SSH key auth > password auth — disable password auth on servers
- SSH tunnelling enables port forwarding and network pivoting
- VPN encrypts traffic between networks

## 🔗 Related Notes
- [[CS101-16 - Networking Core Protocols]] · [[CS101-21 - Cryptography Basics]]
- [[TLS]] · [[SSH]] · [[VPN]] · [[PKI]] · [[Port Forwarding]]
