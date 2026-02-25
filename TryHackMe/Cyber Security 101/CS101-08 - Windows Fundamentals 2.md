---
tags: [THM, cyber-security-101, windows, room]
platform: TryHackMe
type: room
module: "03 - Windows and AD Fundamentals"
module_number: 3
room_number: 8
status: "⬜"
url: https://tryhackme.com/room/windowsfundamentals2x0x
difficulty: Easy
---

# 🪟 Windows Fundamentals 2

> [!abstract] Summary
> Part 2 — System Configuration, UAC settings, Resource Monitoring, the Windows Registry, and built-in admin tools.

**Path:** [[Cyber Security 101]] > Module 3 > Windows Fundamentals 2

## 🎯 Learning Objectives
- Use msconfig and Task Manager
- Navigate the Windows Registry
- Monitor system resources
- Use Computer Management and System Information

## 📖 Key Concepts

### System Configuration (msconfig)
`Win+R → msconfig` — Tabs: General · Boot · Services · Startup · Tools

### Windows Registry
Hierarchical database storing OS and application configuration.

| Hive | Description |
|------|-------------|
| `HKLM` | System-wide settings |
| `HKCU` | Current user settings |
| `HKCR` | File associations |
| `HKU` | All user profiles |

```cmd
regedit    # Open Registry Editor
```

> [!warning] **Persistence keys** — malware commonly hides here:
> `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`
> `HKLM\Software\Microsoft\Windows\CurrentVersion\Run`

### Task Manager & Resource Monitor
- `Ctrl+Shift+Esc` → Task Manager
- `resmon` → Resource Monitor (per-process CPU/memory/disk/network)

### Computer Management (compmgmt.msc)
All-in-one admin console: Event Viewer · Device Manager · Disk Management · Services · Local Users and Groups

### Event Viewer
Critical for investigations — check **Security** log for auth events (4624/4625/4688).

## 🔑 Key Takeaways
- Registry Run keys = top persistence locations — check during forensics
- Event Viewer Security log is the primary incident investigation source
- msconfig is the first stop for startup/boot troubleshooting

## 🔗 Related Notes
- [[CS101-07 - Windows Fundamentals 1]] · [[CS101-09 - Windows Fundamentals 3]]
- [[Windows Registry]] · [[Persistence]] · [[CS101-42 - Logs Fundamentals]]
