---
tags: [THM, pre-security, operating-systems, windows, room]
platform: TryHackMe
type: room
module: "Operating Systems Basics"
module_number: 5
room_number: 19
status: "⬜"
url: https://tryhackme.com/room/windowsbasics
difficulty: Easy
---

# 🪟 Windows Basics

> [!abstract] Summary
> Introduction to Windows OS — the filesystem (NTFS), user accounts, the Registry, Task Manager, Control Panel, and key security features like UAC and Windows Defender.

**Path:** [[Pre Security (New)]] > [[Operating Systems Basics]] > Windows Basics

---

## 📖 Key Concepts

### Windows Filesystem — NTFS
**NTFS** (New Technology File System) is the standard filesystem for Windows.

| Feature | Description |
|---------|-------------|
| **Permissions** | File/folder ACLs (Access Control Lists) |
| **Encryption** | EFS (Encrypting File System) |
| **Journaling** | Crash recovery |
| **Alternate Data Streams** | Hidden data within files (ADS) — used by malware |
| **Compression** | Built-in file compression |

**Key Windows directories:**
```
C:\Windows\          → OS files
C:\Windows\System32\ → Core system executables + DLLs
C:\Users\            → User profiles
C:\Program Files\    → 64-bit applications
C:\Program Files (x86)\ → 32-bit applications
C:\Temp\ or %TEMP%   → Temporary files
```

> [!warning] Security Note
> **Alternate Data Streams (ADS)** can hide malicious files inside legitimate files: `malware.exe` hidden in `document.txt:malware.exe`. Detection requires specialized tools.

---

### User Accounts & Permissions

| Account Type | Description |
|-------------|-------------|
| **Administrator** | Full control over the system |
| **Standard User** | Limited — can't install system-wide software |
| **Guest** | Very restricted, usually disabled |
| **System (SYSTEM)** | Highest privilege — used by OS and services |

**View users:**
```powershell
net user                    # List all users
net user <username>         # User details
whoami                      # Current user
whoami /priv                # Current user's privileges
```

---

### UAC (User Account Control)
UAC prompts for confirmation when an action requires admin privileges — prevents silent privilege escalation.

- Even Administrators run as standard users by default
- **UAC Bypass** — common privilege escalation technique in pen testing

---

### Windows Registry
A hierarchical database storing OS and application configuration.

**Key hives:**
| Hive | Contents |
|------|---------|
| `HKEY_LOCAL_MACHINE (HKLM)` | System-wide settings |
| `HKEY_CURRENT_USER (HKCU)` | Current user settings |
| `HKEY_CLASSES_ROOT` | File associations |
| `HKEY_USERS` | All user profiles |

```powershell
# Open Registry Editor
regedit

# Persistence in Registry (common malware technique)
HKCU\Software\Microsoft\Windows\CurrentVersion\Run
HKLM\Software\Microsoft\Windows\CurrentVersion\Run
```

> [!warning] Security Note
> Malware commonly achieves **persistence** by adding entries to `Run` keys in the Registry.

---

### Task Manager & Process Tools

```powershell
# Open Task Manager
Ctrl+Shift+Esc
taskmgr

# Command line process tools
tasklist                          # List running processes
taskkill /PID 1234 /F             # Kill process by PID
Get-Process                       # PowerShell
```

---

### Windows Defender & Security Center
- Built-in antivirus and security suite
- **Windows Defender Firewall** — built-in firewall
- **Windows Update** — patches are critical for security

---

### Key System Tools

| Tool | Purpose | Access |
|------|---------|--------|
| `msconfig` | System Configuration | Run dialog |
| `services.msc` | Windows Services | Run dialog |
| `eventvwr` | Event Viewer / logs | Run dialog |
| `lusrmgr.msc` | Local Users and Groups | Run dialog |
| `msinfo32` | System Information | Run dialog |
| `resmon` | Resource Monitor | Task Manager |

---

## 🔑 Key Takeaways
- NTFS permissions and ACLs control file access — misconfigurations are exploitable
- UAC provides a layer of protection against privilege escalation
- The Registry stores critical config — malware abuses Run keys for persistence
- Knowing Windows tools helps both using and defending the system

## 🔗 Related Notes
- [[Windows CLI Basics]] · [[Operating System Security]] · [[Operating Systems Introduction]]
- [[NTFS]] · [[UAC]] · [[Windows Registry]] · [[Privilege Escalation]] · [[Persistence]]
