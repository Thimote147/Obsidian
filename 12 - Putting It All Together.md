---
tags:
  - THM
  - pre-security
  - web
  - room
platform: TryHackMe
type: room
module: "How The Web Works"
module_number: 3
room_number: 12
status: "⬜"
url: https://tryhackme.com/room/puttingitalltogether
difficulty: Easy
---

# 🧩 Putting It All Together

> [!abstract] Summary
> Consolidates all web knowledge — tracing the complete journey of a web request from typing a URL in a browser to receiving a rendered page. Covers Load Balancers, CDNs, Databases, and WAFs.

**Path:** [[Pre Security (New)]] > [[How The Web Works]] > Putting It All Together

---

## 🎯 Learning Objectives
- Trace the full lifecycle of a web request
- Understand Load Balancers, CDNs, Databases, and WAFs
- Understand static vs dynamic content
- Consolidate all Module 3 knowledge

---

## 📖 Full Web Request Journey

```
1. User types: https://tryhackme.com/room/example
2. Browser checks local DNS cache
3. DNS query → Recursive Resolver → Root → TLD → Authoritative NS → IP
4. Browser initiates TCP connection to server (3-way handshake)
5. TLS handshake (for HTTPS) → encrypted connection established
6. Browser sends HTTP GET request
7. Request may pass through: Load Balancer → Web Server → App Server → Database
8. Server generates HTTP response (HTML/JSON)
9. Browser receives response, renders HTML, loads CSS/JS
10. Page displayed to user
```

---

## 📖 Infrastructure Components

### Load Balancer
Distributes incoming traffic across multiple servers to prevent overload.

**Benefits:**
- **High availability** — if one server fails, others handle traffic
- **Scalability** — add more servers to handle more users
- **Health checks** — removes unhealthy servers automatically

**Algorithms:**
- **Round Robin** — requests cycle evenly across servers
- **Least Connections** — sends to server with fewest active connections
- **IP Hash** — same user always goes to same server (sticky sessions)

---

### CDN (Content Delivery Network)
A distributed network of servers globally that caches **static content** close to users.

**Benefits:**
- Faster load times (server is geographically close to user)
- Reduces origin server load
- DDoS protection

**What CDNs cache:** Images, CSS, JavaScript, videos, fonts

**Examples:** Cloudflare, Akamai, AWS CloudFront

---

### Databases
Stores and retrieves dynamic content (user data, posts, products, etc.)

| Type | Description | Examples |
|------|-------------|---------|
| **Relational (SQL)** | Tables with relationships | MySQL, PostgreSQL, SQLite |
| **NoSQL** | Flexible document/key-value storage | MongoDB, Redis, Cassandra |

**Web server → Database flow:**
```
User requests profile page
→ App server queries: SELECT * FROM users WHERE id=123
→ Database returns data
→ App server inserts data into HTML template
→ HTML response sent to browser
```

> [!warning] Security Note
> **SQL Injection** occurs when user input is unsanitized and inserted directly into SQL queries. It's one of the most critical web vulnerabilities (OWASP Top 10).

---

### WAF (Web Application Firewall)
Sits in front of web servers and filters malicious HTTP requests.

**Protects against:**
- [[SQL Injection]]
- [[XSS]] (Cross-Site Scripting)
- [[CSRF]]
- Directory traversal
- Known attack signatures

**Examples:** Cloudflare WAF, AWS WAF, ModSecurity

> [!tip] WAF Bypass
> WAFs can be bypassed with obfuscation, encoding, or unusual payloads. Pen testers often need to bypass WAFs when testing web applications.

---

### Static vs Dynamic Content

| | Static Content | Dynamic Content |
|---|---|---|
| **Generated** | Pre-made files on disk | Generated per request by app server |
| **Examples** | HTML files, images, CSS, JS | User profiles, search results, news feeds |
| **Server needed** | Web server only | Web + App server + Database |
| **Speed** | Very fast | Slower (processing needed) |
| **CDN-cacheable** | Yes | Generally no |

---

### Web Server Software
| Software | Description |
|----------|-------------|
| **Nginx** | High-performance, often used as reverse proxy/load balancer |
| **Apache** | Widely used, highly configurable |
| **IIS** | Microsoft's web server for Windows |
| **Node.js** | JavaScript runtime that can serve web apps |

---

## 🔑 Key Takeaways
- A web request involves DNS → TCP → TLS → HTTP → (Load Balancer → Server → DB) → Response
- Load balancers ensure availability; CDNs deliver content fast
- Databases store dynamic data; SQL injection attacks them directly
- WAFs add a security layer but can be bypassed
- Understanding the full stack is essential for both web dev and web pen testing

---

## 🔗 Related Notes
- [[09 - DNS in Detail]] — step 3 of the request journey
- [[10 - HTTP in Detail]] — step 6-8
- [[11 - How Websites Work]] — the HTML that gets returned
- [[Load Balancer]] · [[CDN]] · [[WAF]] · [[SQL Injection]] · [[Database]]
