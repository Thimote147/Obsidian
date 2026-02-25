---
tags: [THM, cyber-security-101, windows, CLI, room]
platform: TryHackMe
type: room
module: "04 - Command Line"
module_number: 4
room_number: 11
status: "⬜"
url: https://tryhackme.com/room/windowscommandline
difficulty: Easy
---

# 💻 Windows Command Line

> [!abstract] Summary
> Essential Windows CMD commands for navigation, file management, networking, and system info. Core skill for attack and defence on Windows.

**Path:** [[Cyber Security 101]] > Module 4 > Windows Command Line

## 🎯 Learning Objectives
- Navigate filesystem using CMD
- Manage files and directories
- Use network diagnostic commands
- Gather system information

## 📖 Key Concepts

### Navigation & Files
```cmd
dir /a                       # List including hidden files
dir /s /b *.txt              # Recursive search
cd C:\Users\Admin           # Change directory
copy src dest                # Copy file
move src dest                # Move/rename
del file.txt                 # Delete file
rmdir /s /q folder           # Delete folder
type file.txt                # Display file
find "password" file.txt     # Search in file
```

### System Info
```cmd
whoami                       # Current user
whoami /priv                 # Current privileges ← key for privesc
hostname                     # Machine name
systeminfo                   # Full system details
tasklist                     # Running processes
tasklist /svc                # Processes with services
net user                     # List local users
net localgroup administrators # Local admins
```

### Networking
```cmd
ipconfig /all                # Full network details
ping target                  # Connectivity test
tracert target               # Trace route
nslookup domain.com          # DNS lookup
netstat -ano                 # Active connections + PIDs ← key for investigation
arp -a                       # ARP cache
```

> [!tip] **Post-exploitation first commands:** `whoami /priv`, `net localgroup administrators`, `netstat -ano`, `systeminfo` — run these immediately after gaining access.

## 🔑 Key Takeaways
- `whoami /priv` reveals privileges — essential for privilege escalation
- `netstat -ano` reveals active connections and listening services
- `systeminfo` fingerprints OS version for exploit selection
- No install needed — CMD is on every Windows system

## 🔗 Related Notes
- [[CS101-12 - Windows PowerShell]] · [[CS101-07 - Windows Fundamentals 1]]
- [[Windows CLI]] · [[Post-Exploitation]] · [[Privilege Escalation]]
