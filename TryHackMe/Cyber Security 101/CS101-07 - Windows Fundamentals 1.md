---
tags: [THM, cyber-security-101, windows, room]
platform: TryHackMe
type: room
module: "03 - Windows and AD Fundamentals"
module_number: 3
room_number: 7
status: "⬜"
url: https://tryhackme.com/room/windowsfundamentals1xbx
difficulty: Easy
---

# 🪟 Windows Fundamentals 1

> [!abstract] Summary
> Part 1 of Windows Fundamentals — the desktop, NTFS file system, UAC, and Control Panel. Hands-on access to a live Windows VM.

**Path:** [[Cyber Security 101]] > Module 3 > Windows Fundamentals 1

## 🎯 Learning Objectives
- Navigate the Windows desktop and filesystem
- Understand NTFS permissions and Alternate Data Streams (ADS)
- Configure UAC
- Use Control Panel and Settings

## 📖 Key Concepts

### NTFS Filesystem
NTFS replaced FAT32. Key features: files >4GB, permissions, encryption (EFS), **Alternate Data Streams (ADS)**.

```powershell
dir /R                              # View ADS (CMD)
Get-Item -Path file.txt -Stream *   # PowerShell ADS
```

### NTFS Permissions
| Permission | Description |
|-----------|-------------|
| Full Control | Read, write, modify, delete, change perms |
| Modify | Read, write, delete |
| Read & Execute | View and run |
| Read | View only |
| Write | Create/modify |

### UAC (User Account Control)
Prompts for elevation when admin rights are needed. Standard user → admin password prompt. Admin user → confirm prompt.

### Environment Variables
```cmd
echo %SYSTEMROOT%    # C:\Windows
echo %USERPROFILE%   # C:\Users\username
echo %TEMP%          # Temp folder
```

> [!warning] ADS can hide malware payloads. Check with `dir /R` or Sysinternals Streams during forensic analysis.

## 🔑 Key Takeaways
- NTFS permissions are the foundation of Windows access control
- ADS is a stealth hiding spot — check in investigations
- UAC is key defence but can be bypassed (UAC bypass techniques exist)

## 🔗 Related Notes
- [[CS101-08 - Windows Fundamentals 2]] · [[CS101-09 - Windows Fundamentals 3]]
- [[NTFS]] · [[UAC]] · [[Windows Registry]] · [[Privilege Escalation]]
