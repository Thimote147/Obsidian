---
tags: [THM, cyber-security-101, web-hacking, HTTP, room]
platform: TryHackMe
type: room
module: "08 - Web Hacking"
module_number: 8
room_number: 30
status: "⬜"
url: https://tryhackme.com/room/webapplicationbasics
difficulty: Easy
---

# 🌐 Web Application Basics

> [!abstract] Summary
> Foundation of web application security — HTTP request/response cycle, cookies, sessions, same-origin policy, and common web architecture. Prerequisite for all web hacking rooms.

**Path:** [[Cyber Security 101]] > Module 8 > Web Application Basics

## 🎯 Learning Objectives
- Understand the HTTP request/response cycle
- Know HTTP methods, headers, and status codes
- Understand cookies and sessions
- Know same-origin policy and CORS

## 📖 Key Concepts

### HTTP Request Structure
```
GET /login?user=admin HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Cookie: session=abc123
```

### HTTP Methods
| Method | Purpose |
|--------|---------|
| GET | Retrieve resource |
| POST | Submit data |
| PUT | Replace resource |
| PATCH | Partial update |
| DELETE | Delete resource |
| OPTIONS | Check allowed methods |
| HEAD | Headers only |

### HTTP Response Structure
```
HTTP/1.1 200 OK
Content-Type: text/html
Set-Cookie: session=xyz

<html>...</html>
```

### Status Codes
| Range | Meaning | Examples |
|-------|---------|---------|
| 2xx | Success | 200 OK, 201 Created |
| 3xx | Redirect | 301 Permanent, 302 Temporary |
| 4xx | Client Error | 401 Unauth, 403 Forbidden, 404 Not Found |
| 5xx | Server Error | 500 Internal, 503 Unavailable |

### Cookies
Set via `Set-Cookie` header, sent on every request.
```
Set-Cookie: session=abc123; HttpOnly; Secure; SameSite=Strict; Path=/; Expires=...
```

**Security flags:**
| Flag | Effect |
|------|--------|
| `HttpOnly` | JS can't read → blocks XSS cookie theft |
| `Secure` | HTTPS only |
| `SameSite=Strict` | Blocks CSRF |

### Same-Origin Policy (SOP)
Browser blocks cross-origin requests unless server allows via CORS headers.
Origin = scheme + domain + port.

> [!tip] **DevTools (F12)** is your best friend — Network tab shows all requests/responses including headers, cookies, and payloads in real-time.

## 🔑 Key Takeaways
- HTTP is stateless — cookies maintain state
- HttpOnly + Secure + SameSite cookies are the baseline
- Status codes reveal application behaviour — 403 vs 404 tells you something exists
- Understanding HTTP is the foundation for all web attacks

## 🔗 Related Notes
- [[CS101-31 - JavaScript Essentials]] · [[CS101-33 - Burp Suite The Basics]]
- [[HTTP]] · [[Cookies]] · [[Same-Origin Policy]] · [[Web Application Security]]
