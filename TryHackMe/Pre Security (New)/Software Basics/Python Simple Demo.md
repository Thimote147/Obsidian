---
tags: [THM, pre-security, software-basics, python, room]
platform: TryHackMe
type: room
module: "Software Basics"
module_number: 6
room_number: 25
status: "⬜"
url: https://tryhackme.com/room/pythonsimpledemo
difficulty: Easy
---

# 🐍 Python: Simple Demo

> [!abstract] Summary
> Introduction to Python programming — variables, data types, control flow, functions, and file operations. Python is the primary language for security scripting, exploit development, and automation.

**Path:** [[Pre Security (New)]] > [[Software Basics]] > Python: Simple Demo

---

## 📖 Key Concepts

### Why Python for Security?
- Most security tools are written in Python (Impacket, Scapy, Volatility, pwntools)
- Quick to write scripts for automation
- Excellent libraries for networking, web scraping, cryptography
- Interpreter available on almost every Linux system

---

### Python Basics

```python
# Variables and data types
name = "Alice"              # str
age = 25                    # int
height = 1.75               # float
is_admin = True             # bool
ports = [80, 443, 8080]     # list
user = {"name": "Alice", "role": "admin"}  # dict

# Print
print(f"Hello, {name}! You are {age} years old.")

# Input
username = input("Enter username: ")

# Conditionals
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# Loops
for port in ports:
    print(f"Scanning port {port}")

for i in range(1, 11):
    print(i)

while True:
    data = input()
    if data == "quit":
        break

# Functions
def scan_port(host, port):
    # ... connect and check ...
    return True

result = scan_port("192.168.1.1", 80)
```

### File Operations
```python
# Read file
with open("passwords.txt", "r") as f:
    for line in f:
        print(line.strip())

# Write file
with open("results.txt", "w") as f:
    f.write("Scan complete\n")

# Append
with open("log.txt", "a") as f:
    f.write("Found: admin\n")
```

### Networking with Python
```python
import socket

# Basic port scanner
def check_port(host, port):
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((host, port))
        return True
    except:
        return False
    finally:
        s.close()

# HTTP request
import requests
response = requests.get("http://target.com")
print(response.status_code)
print(response.text)
```

### Useful Security Libraries
| Library | Use |
|---------|-----|
| `requests` | HTTP requests |
| `socket` | Low-level networking |
| `scapy` | Packet crafting/sniffing |
| `pwntools` | CTF/exploit development |
| `impacket` | Windows/AD protocols |
| `hashlib` | Hashing (MD5, SHA256) |
| `base64` | Encoding/decoding |
| `subprocess` | Run system commands |

---

## 🔑 Key Takeaways
- Python is the #1 language for security scripting
- Basics (variables, loops, functions, file I/O) are enough to write useful tools
- The `requests` and `socket` libraries unlock networking capabilities
- Practice by automating common CTF tasks (port scanning, brute forcing)

## 🔗 Related Notes
- [[JavaScript Simple Demo]] · [[Database SQL Basics]]
- [[Python]] · [[Scripting]] · [[Automation]]
