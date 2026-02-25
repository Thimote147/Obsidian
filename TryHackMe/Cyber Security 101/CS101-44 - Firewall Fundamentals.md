---
tags: [THM, cyber-security-101, security-solutions, firewall, iptables, room]
platform: TryHackMe
type: room
module: "11 - Security Solutions"
module_number: 11
room_number: 44
status: "⬜"
url: https://tryhackme.com/room/firewallfundamentals
difficulty: Easy
---

# 🔥 Firewall Fundamentals

> [!abstract] Summary
> Learn firewall types and hands-on configuration with Windows Defender Firewall and Linux iptables/ufw. Core network security control for both hardening and bypass.

**Path:** [[Cyber Security 101]] > Module 11 > Firewall Fundamentals

## 🎯 Learning Objectives
- Understand firewall types (stateless, stateful, NGFW)
- Configure Windows Defender Firewall
- Use Linux iptables and ufw
- Understand firewall evasion

## 📖 Key Concepts

### Firewall Types
| Type | Inspection Level |
|------|----------------|
| Packet Filter (stateless) | Layer 3-4 headers only |
| Stateful | Tracks connection state |
| Application/NGFW | Layer 7 deep packet inspection |
| WAF | HTTP/HTTPS only |

### Linux — ufw (simpler)
```bash
ufw enable
ufw default deny incoming
ufw default allow outgoing
ufw allow ssh && ufw allow 80/tcp && ufw allow 443/tcp
ufw deny 23/tcp
ufw status verbose
```

### Linux — iptables (powerful)
```bash
iptables -L -n -v                              # View rules
iptables -A INPUT -p tcp --dport 22 -j ACCEPT  # Allow SSH
iptables -A INPUT -s 10.10.10.10 -j DROP       # Block IP
iptables -A INPUT -j DROP                      # Drop all other inbound
iptables-save > /etc/iptables/rules.v4
```

### Windows (PowerShell)
```powershell
New-NetFirewallRule -DisplayName "Allow SSH" -Direction Inbound -Protocol TCP -LocalPort 22 -Action Allow
New-NetFirewallRule -DisplayName "Block IP" -Direction Outbound -RemoteAddress 10.10.10.10 -Action Block
```

### Firewall Evasion
- **Tunnelling** — HTTP/DNS tunnelling to bypass port restrictions
- **Reverse shell** — outbound connection bypasses inbound rules
- **Allowed protocols** — use HTTPS (443) for C2

> [!warning] Blocking inbound traffic doesn't stop reverse shells — attackers call **out** on allowed ports (80, 443). **Egress filtering** is equally critical. Monitor outbound connections.

## 🔑 Key Takeaways
- NGFW provides the deepest inspection — preferred over stateless
- Block inbound AND filter outbound (egress)
- ufw simplifies iptables for common use cases
- Reverse shells bypass inbound-only firewalls

## 🔗 Related Notes
- [[CS101-45 - IDS Fundamentals]] · [[CS101-43 - Introduction to SIEM]]
- [[Firewall]] · [[iptables]] · [[ufw]] · [[Network Security]] · [[Egress Filtering]]
