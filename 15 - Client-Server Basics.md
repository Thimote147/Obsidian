---
tags: [THM, pre-security, computer-fundamentals, networking, room]
platform: TryHackMe
type: room
module: "Computer Fundamentals"
module_number: 4
room_number: 15
status: "⬜"
url: https://tryhackme.com/room/clientserverbasics
difficulty: Easy
---

# 🔄 Client-Server Basics

> [!abstract] Summary
> The client-server model is the foundation of networked computing. Clients request services; servers provide them. This model underpins the web, email, file sharing, and almost every network service.

**Path:** [[Pre Security (New)]] > [[Computer Fundamentals]] > Client-Server Basics

---

## 📖 Key Concepts

### The Client-Server Model
```
Client (requests)  ←→  Network  ←→  Server (responds)

Browser → HTTP Request → Web Server
Browser ← HTTP Response ← Web Server
```

**Client:** Any device/software that **requests** a service (browser, email client, game)
**Server:** Software/hardware that **provides** a service (web server, database, file server)

---

### Common Services & Protocols

| Service | Protocol | Default Port |
|---------|----------|-------------|
| Web browsing | HTTP/HTTPS | 80 / 443 |
| Email sending | SMTP | 25 / 587 |
| Email receiving | IMAP / POP3 | 143 / 110 |
| File transfer | FTP / SFTP | 21 / 22 |
| Remote shell | SSH | 22 |
| Remote desktop | RDP | 3389 |
| File sharing | SMB | 445 |
| Database | MySQL/PostgreSQL | 3306 / 5432 |
| DNS resolution | DNS | 53 |

---

### Request-Response Cycle
```
1. Client sends REQUEST (e.g., GET /index.html HTTP/1.1)
2. Server PROCESSES the request
3. Server sends RESPONSE (e.g., 200 OK + HTML)
4. Client RENDERS/USES the response
```

---

### Peer-to-Peer (P2P) vs Client-Server

| | Client-Server | Peer-to-Peer |
|---|---|---|
| **Structure** | Centralized server | Decentralized |
| **Reliability** | Single point of failure | More resilient |
| **Security** | Easier to control | Harder to monitor |
| **Examples** | Web, email | BitTorrent, blockchain |

> [!warning] Security Note
> **C2 (Command & Control)** — Malware uses client-server communication to receive commands from an attacker's server. Understanding this model helps in detecting malicious traffic.

---

### APIs (Application Programming Interfaces)
APIs are how modern client-server communication works — clients request data in structured formats (JSON/XML).

```json
GET /api/user/123
→ {"id": 123, "name": "Alice", "email": "alice@example.com"}
```

> [!tip] Security Note
> APIs are a major attack surface — broken authentication, missing authorization, data exposure are all common API vulnerabilities (OWASP API Top 10).

---

## 🔑 Key Takeaways
- The client-server model underpins all network services
- Clients request, servers respond — knowing the protocol tells you the attack surface
- Malware uses C2 infrastructure following the same client-server pattern
- APIs are the modern client-server interface and a key pen testing target

## 🔗 Related Notes
- [[Packets and Frames]] · [[10 - HTTP in Detail]] · [[12 - Putting It All Together]]
- [[HTTP]] · [[SSH]] · [[FTP]] · [[API Security]]
