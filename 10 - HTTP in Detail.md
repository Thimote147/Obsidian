---
tags:
  - THM
  - pre-security
  - web
  - HTTP
  - room
platform: TryHackMe
type: room
module: "How The Web Works"
module_number: 3
room_number: 10
status: "⬜"
url: https://tryhackme.com/room/httpindetail
difficulty: Easy
---

# 🌐 HTTP in Detail

> [!abstract] Summary
> Deep dive into the HyperText Transfer Protocol — the foundation of all web communication. Covers HTTP methods, status codes, headers, cookies, and the structure of requests/responses.

**Path:** [[Pre Security (New)]] > [[How The Web Works]] > HTTP in Detail

---

## 🎯 Learning Objectives
- Understand how HTTP and HTTPS work
- Know HTTP request and response structure
- Learn HTTP methods (GET, POST, PUT, DELETE)
- Understand HTTP status codes
- Know what headers and cookies are and their security relevance

---

## 📖 Key Concepts

### HTTP vs HTTPS
| | HTTP | HTTPS |
|---|---|---|
| **Port** | 80 | 443 |
| **Encryption** | None | TLS/SSL |
| **Security** | Traffic visible to anyone | Encrypted |
| **Certificate** | Not required | Required (CA-signed) |

> [!warning] Always use HTTPS! HTTP traffic can be intercepted by anyone on the network (MitM attacks).

---

### HTTP Request Structure

```
GET /page HTTP/1.1
Host: tryhackme.com
User-Agent: Mozilla/5.0
Accept: text/html
Cookie: session=abc123

[Body — only for POST/PUT]
```

| Part | Description |
|------|-------------|
| **Method** | What action to perform (GET, POST, etc.) |
| **Path** | The resource being requested (`/page`) |
| **HTTP Version** | Protocol version (HTTP/1.1 or HTTP/2) |
| **Headers** | Additional metadata |
| **Body** | Optional data (for POST/PUT) |

---

### HTTP Methods

| Method | Description | Has Body? |
|--------|-------------|-----------|
| **GET** | Retrieve a resource | No |
| **POST** | Send data to create/update a resource | Yes |
| **PUT** | Replace a resource entirely | Yes |
| **PATCH** | Partially update a resource | Yes |
| **DELETE** | Delete a resource | No |
| **HEAD** | GET without response body | No |
| **OPTIONS** | Ask what methods are supported | No |

> [!tip] Security Note
> **GET** parameters are visible in the URL — never put passwords or sensitive data in GET requests. **POST** parameters go in the body (still visible in plain HTTP, but not in URL history/logs).

---

### HTTP Response Structure

```
HTTP/1.1 200 OK
Server: nginx
Content-Type: text/html
Set-Cookie: session=xyz; HttpOnly; Secure

<!DOCTYPE html>...
```

---

### HTTP Status Codes

| Code | Category | Meaning |
|------|----------|---------|
| **1xx** | Informational | Request received, processing |
| **2xx** | Success | Request successful |
| **3xx** | Redirection | Further action needed |
| **4xx** | Client Error | Problem with the request |
| **5xx** | Server Error | Problem on the server |

**Common codes:**
| Code | Meaning |
|------|---------|
| `200 OK` | Success |
| `201 Created` | Resource created |
| `301 Moved Permanently` | Permanent redirect |
| `302 Found` | Temporary redirect |
| `400 Bad Request` | Malformed request |
| `401 Unauthorized` | Authentication required |
| `403 Forbidden` | Authenticated but no permission |
| `404 Not Found` | Resource doesn't exist |
| `405 Method Not Allowed` | HTTP method not permitted |
| `500 Internal Server Error` | Server-side error |
| `503 Service Unavailable` | Server overloaded/down |

---

### HTTP Headers

#### Common Request Headers
| Header | Description |
|--------|-------------|
| `Host` | Target server (required in HTTP/1.1) |
| `User-Agent` | Browser/client identifier |
| `Accept` | Accepted content types |
| `Accept-Encoding` | Accepted compression (gzip, br) |
| `Authorization` | Authentication credentials |
| `Cookie` | Session cookies |
| `Referer` | Page that made the request |
| `Content-Type` | Body format (application/json, etc.) |

#### Common Response Headers
| Header | Description |
|--------|-------------|
| `Server` | Web server software |
| `Content-Type` | Response body format |
| `Set-Cookie` | Issue a cookie to the client |
| `Cache-Control` | Caching directives |
| `X-Frame-Options` | Clickjacking protection |
| `Content-Security-Policy` | XSS/injection protection |
| `Strict-Transport-Security` | Force HTTPS |

---

### Cookies
Cookies are small pieces of data stored in the browser, sent with every request to the same domain.

**Main uses:** Session management, user preferences, tracking

**Cookie Flags (Security):**

| Flag | Effect |
|------|--------|
| `HttpOnly` | JS cannot access — prevents XSS cookie theft |
| `Secure` | Only sent over HTTPS |
| `SameSite=Strict` | Not sent on cross-site requests — prevents CSRF |
| `SameSite=Lax` | Sent on same-site + top-level navigation |

```
Set-Cookie: session=abc123; HttpOnly; Secure; SameSite=Strict; Path=/
```

> [!warning] Security Note
> Missing `HttpOnly` → cookie theft via XSS. Missing `Secure` → cookie sent over HTTP. Missing `SameSite` → CSRF vulnerability.

---

## 🛠️ Tools & Commands

```bash
# Make HTTP requests with curl
curl http://tryhackme.com
curl -v http://tryhackme.com           # verbose (see headers)
curl -X POST -d "user=admin&pass=1234" http://target.com/login
curl -H "Authorization: Bearer TOKEN" http://api.example.com
curl -I http://tryhackme.com           # HEAD request (headers only)
curl -L http://tryhackme.com           # follow redirects

# Intercept and modify requests: Burp Suite
# Open proxy on 127.0.0.1:8080 and route browser traffic through it
```

---

## 🔑 Key Takeaways
- HTTPS encrypts HTTP traffic with TLS — always prefer it over HTTP
- HTTP methods define the action: GET (read), POST (write), DELETE (remove)
- Status codes tell you what happened: 2xx=success, 4xx=client error, 5xx=server error
- Cookies maintain session state — security flags (HttpOnly, Secure, SameSite) are critical

---

## 🔗 Related Notes
- [[09 - DNS in Detail]] — how the domain gets resolved before HTTP
- [[11 - How Websites Work]] — how web servers generate HTTP responses
- [[12 - Putting It All Together]] — full web request flow
- [[HTTP]] · [[HTTPS]] · [[Cookies]] · [[Burp Suite]] · [[TLS]] · [[CSRF]] · [[XSS]]
