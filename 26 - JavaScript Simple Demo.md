---
tags: [THM, pre-security, software-basics, javascript, room]
platform: TryHackMe
type: room
module: "Software Basics"
module_number: 6
room_number: 26
status: "⬜"
url: https://tryhackme.com/room/javascriptsimpledemo
difficulty: Easy
---

# 🟡 JavaScript: Simple Demo

> [!abstract] Summary
> Introduction to JavaScript — the language of the web browser. Understanding JS is essential for web security: XSS attacks, client-side logic analysis, and recognizing vulnerable code patterns.

**Path:** [[Pre Security (New)]] > [[Software Basics]] > JavaScript: Simple Demo

---

## 📖 Key Concepts

### What is JavaScript?
JS is the **only language that runs natively in browsers**. It makes websites interactive and dynamic.

- **Client-side JS** — runs in the browser (visible to users!)
- **Server-side JS** — Node.js (runs on the server)

---

### JS Basics

```javascript
// Variables
let name = "Alice";          // mutable
const MAX = 100;             // immutable
var old = "legacy";          // avoid — function scoped

// Data types
let str = "hello";
let num = 42;
let bool = true;
let arr = [1, 2, 3];
let obj = {name: "Alice", role: "admin"};
let nothing = null;

// Functions
function greet(name) {
    return `Hello, ${name}!`;
}

// Arrow function
const add = (a, b) => a + b;

// Conditionals
if (user === "admin") {
    grantAccess();
} else {
    denyAccess();
}

// Loops
for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]);
}

arr.forEach(item => console.log(item));
```

### DOM Manipulation (Browser)
```javascript
// Get element
document.getElementById("username").value;
document.querySelector(".password").innerHTML;

// Modify content
document.getElementById("result").innerHTML = "Hacked!";

// XSS example — if user input is inserted like this:
document.getElementById("name").innerHTML = userInput;
// And userInput = "<script>alert(1)</script>"
// → XSS vulnerability!
```

### Fetch API (HTTP Requests from Browser)
```javascript
// GET request
fetch("/api/users")
    .then(res => res.json())
    .then(data => console.log(data));

// POST request
fetch("/api/login", {
    method: "POST",
    body: JSON.stringify({username: "admin", password: "test"}),
    headers: {"Content-Type": "application/json"}
});
```

---

### Security Relevance

> [!warning] JS is always visible to the user — never put secrets in client-side JS!

**What attackers look for in JS files:**
```javascript
// Hardcoded credentials (very common!)
const API_KEY = "sk-abc123secret";
const adminPassword = "SuperSecret123";

// Insecure direct object reference
fetch(`/api/user/${userId}/data`);  // Can user change userId?

// Client-side auth bypass
if (isAdmin == true) { showAdminPanel(); }
// → What if attacker sets isAdmin=true in browser console?

// DOM XSS
element.innerHTML = location.hash;  // XSS via URL fragment
```

**Tools to analyze JS:**
- Browser DevTools → Sources tab
- `curl` to download and search JS files
- Beautify minified JS: `js-beautify`

---

## 🔑 Key Takeaways
- JS is always visible — never trust client-side validation or store secrets in it
- DOM manipulation with unsanitized user input = XSS vulnerability
- API keys and credentials in JS files are a very common finding in pen tests
- Browser DevTools → Console lets you run JS in the context of any page

## 🔗 Related Notes
- [[11 - How Websites Work]] · [[10 - HTTP in Detail]] · [[25 - Python Simple Demo]]
- [[JavaScript]] · [[XSS]] · [[DOM]] · [[Client-Side Security]]
