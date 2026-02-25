---
tags: [THM, cyber-security-101, linux, room]
platform: TryHackMe
type: room
module: "02 - Linux Fundamentals"
module_number: 2
room_number: 4
status: "⬜"
url: https://tryhackme.com/room/linuxfundamentalspart1
difficulty: Easy
---

# 🐧 Linux Fundamentals Part 1

> [!abstract] Summary
> First steps in Linux — the filesystem structure, essential commands, and interactive terminal practice. Learn to navigate and interact with a Linux system from scratch.

**Path:** [[Cyber Security 101]] > Module 2 > Linux Fundamentals Part 1

## 🎯 Learning Objectives
- Understand why Linux matters in cybersecurity
- Navigate the Linux filesystem
- Run essential first commands on an interactive terminal

## 📖 Key Concepts

### Why Linux?
- Powers ~67% of web servers
- All major security tools run natively (Kali, Parrot)
- Required for pen testing, SOC work, forensics

### Linux Filesystem
```
/           ← Root
├── /home   ← User home directories
├── /etc    ← Configuration files
├── /var    ← Variable data (logs)
├── /tmp    ← Temporary files (world-writable!)
├── /bin    ← Essential binaries
└── /root   ← Root user home
```

## 🛠️ Essential Commands
```bash
echo "Hello World"          # Print text
whoami                       # Current user
ls / ls -la                  # List files (including hidden)
cd /home/user                # Change directory
cat /etc/passwd              # Read file
pwd                          # Print working directory
find / -name "flag.txt" 2>/dev/null  # Find files
```

### Operators
| Operator | Description |
|----------|-------------|
| `&&` | Run second only if first succeeds |
| `\|\|` | Run second only if first fails |
| `>` | Redirect output (overwrite) |
| `>>` | Redirect output (append) |

## 🔑 Key Takeaways
- Linux is mandatory knowledge for cybersecurity
- Everything is a file in Linux
- `find` is essential for locating files (and CTF flags!)

## 🔗 Related Notes
- [[CS101-05 - Linux Fundamentals Part 2]] · [[CS101-06 - Linux Fundamentals Part 3]]
- [[Linux CLI]] · [[Linux Filesystem]] · [[Bash]]
