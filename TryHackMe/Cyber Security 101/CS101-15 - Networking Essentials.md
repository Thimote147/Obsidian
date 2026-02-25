---
tags: [THM, cyber-security-101, networking, DHCP, NAT, room]
platform: TryHackMe
type: room
module: "05 - Networking"
module_number: 5
room_number: 15
status: "⬜"
url: https://tryhackme.com/room/networkingessentials
difficulty: Easy
---

# 🌐 Networking Essentials

> [!abstract] Summary
> Practical networking — DHCP automatic configuration, NAT, routing, and how packets find their path. How home and enterprise networks function day-to-day.

**Path:** [[Cyber Security 101]] > Module 5 > Networking Essentials

## 🎯 Learning Objectives
- Understand DHCP and the DORA process
- Explain NAT and why it's used
- Understand routing tables
- Use traceroute to trace packet paths

## 📖 Key Concepts

### DHCP — DORA Process (UDP 67/68)
1. **D**iscover — client broadcasts "I need an IP"
2. **O**ffer — server offers an IP lease
3. **R**equest — client accepts
4. **A**cknowledge — server confirms

```bash
dhclient -r && dhclient              # Linux: renew DHCP
ipconfig /release && ipconfig /renew # Windows
```

> [!warning] **DHCP Starvation** — flood DHCP pool to exhaust IPs. **Rogue DHCP** — fake server poisons clients for MitM. Defence: DHCP snooping on switches.

### NAT (Network Address Translation)
Maps private IPs → public IP. Types:
- **SNAT** — outbound (most common)
- **DNAT** — port forwarding (inbound)

### Routing
```bash
ip route       # Linux routing table
route print    # Windows routing table
```

### Traceroute
```bash
traceroute google.com   # Linux
tracert google.com      # Windows
```

### Key Ports
| Port | Protocol |
|------|---------|
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |
| 3389 | RDP |

## 🔑 Key Takeaways
- DHCP automates network config — DORA is the 4-step process
- NAT hides internal structure — port forwarding enables external access to internal services
- Traceroute reveals network topology — useful for recon

## 🔗 Related Notes
- [[CS101-14 - Networking Concepts]] · [[CS101-16 - Networking Core Protocols]]
- [[DHCP]] · [[NAT]] · [[Routing]] · [[Port Numbers]]
