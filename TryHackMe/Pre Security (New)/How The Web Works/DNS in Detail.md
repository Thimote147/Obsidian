---
tags:
  - THM
  - pre-security
  - web
  - DNS
  - room
platform: TryHackMe
type: room
module: "How The Web Works"
module_number: 3
room_number: 9
status: "⬜"
url: https://tryhackme.com/room/dnsindetail
difficulty: Easy
---

# 🌍 DNS in Detail

> [!abstract] Summary
> How the Domain Name System (DNS) works — translating human-readable domain names into IP addresses. Covers domain hierarchy, DNS record types, and the full DNS resolution process.

**Path:** [[Pre Security (New)]] > [[How The Web Works]] > DNS in Detail

---

## 🎯 Learning Objectives
- Understand what DNS is and why it exists
- Learn the DNS hierarchy (TLD, SLD, subdomain)
- Know the main DNS record types
- Trace a full DNS resolution from browser to IP

---

## 📖 Key Concepts

### What is DNS?
DNS (**Domain Name System**) translates **human-readable names** (e.g., `tryhackme.com`) into **IP addresses** (e.g., `104.26.11.229`) that computers use to communicate.

> [!tip] Analogy
> DNS is the Internet's phone book — you look up a name to get the number (IP).

---

### Domain Hierarchy

```
.                          ← Root
└── .com                   ← Top-Level Domain (TLD)
    └── tryhackme.com      ← Second-Level Domain (SLD)
        └── www.tryhackme.com  ← Subdomain
```

| Level | Example | Description |
|-------|---------|-------------|
| **Root** | `.` | Implicit, managed by IANA |
| **TLD** | `.com`, `.org`, `.uk` | Top-Level Domain |
| **SLD** | `tryhackme` | The domain you register |
| **Subdomain** | `www`, `mail`, `blog` | Optional prefix |

**TLD Types:**
- **gTLD** (Generic) — `.com`, `.net`, `.org`, `.io`
- **ccTLD** (Country Code) — `.uk`, `.de`, `.fr`, `.be`

---

### DNS Record Types

| Record | Purpose | Example |
|--------|---------|---------|
| **A** | Maps domain → IPv4 address | `tryhackme.com → 104.26.11.229` |
| **AAAA** | Maps domain → IPv6 address | `tryhackme.com → 2606:4700::...` |
| **CNAME** | Alias — points to another domain | `www.tryhackme.com → tryhackme.com` |
| **MX** | Mail server for the domain | `tryhackme.com → mail.tryhackme.com` |
| **TXT** | Arbitrary text (SPF, DKIM, verification) | `"v=spf1 include:..."` |
| **NS** | Name servers for the domain | `tryhackme.com → ns1.cloudflare.com` |
| **PTR** | Reverse DNS — IP → domain | `104.26.11.229 → tryhackme.com` |
| **SOA** | Start of Authority — zone admin info | |

---

### DNS Resolution Process

```
1. Browser checks its local cache
2. OS checks /etc/hosts (Linux) or hosts file (Windows)
3. Query sent to Recursive DNS Resolver (usually your ISP or 8.8.8.8)
4. Resolver checks its cache
5. Resolver queries Root Name Server → points to TLD server
6. Resolver queries TLD Name Server (.com) → points to Authoritative NS
7. Resolver queries Authoritative Name Server → returns IP
8. Resolver caches the answer and returns IP to client
```

**TTL (Time to Live):** How long a DNS record is cached (in seconds). Lower TTL = faster propagation of changes.

---

## 🛠️ DNS Tools & Commands

```bash
# Basic DNS lookup
nslookup tryhackme.com
nslookup -type=MX tryhackme.com    # query specific record type

# Detailed DNS lookup
dig tryhackme.com
dig tryhackme.com MX
dig tryhackme.com ANY              # all records
dig @8.8.8.8 tryhackme.com        # query specific DNS server

# Reverse DNS lookup
dig -x 104.26.11.229

# Linux hosts file
cat /etc/hosts
# Windows hosts file
# C:\Windows\System32\drivers\etc\hosts
```

> [!warning] Security Note
> **DNS attacks include:** DNS Spoofing/Cache Poisoning (injecting false records), DNS Hijacking (redirecting to malicious resolvers), DNS Tunneling (exfiltrating data via DNS queries), Subdomain Takeover.

---

## 🔑 Key Takeaways
- DNS translates domain names to IPs via a hierarchical system
- The resolution process involves multiple servers: recursive resolver, root, TLD, authoritative
- Key record types: A, AAAA, CNAME, MX, TXT, NS
- `dig` and `nslookup` are essential DNS reconnaissance tools

---

## 🔗 Related Notes
- [[HTTP in Detail]] — HTTP relies on DNS to resolve server addresses
- [[What is Networking?]] — IP address fundamentals
- [[DNS]] · [[nslookup]] · [[dig]] · [[DNS Records]] · [[DNS Spoofing]]
