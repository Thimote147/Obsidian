---
tags: [THM, cyber-security-101, windows, security, room]
platform: TryHackMe
type: room
module: "03 - Windows and AD Fundamentals"
module_number: 3
room_number: 9
status: "⬜"
url: https://tryhackme.com/room/windowsfundamentals3xzx
difficulty: Easy
---

# 🪟 Windows Fundamentals 3

> [!abstract] Summary
> Part 3 — Built-in Microsoft security tools: Windows Updates, Windows Security (Defender), BitLocker encryption, and other hardening features.

**Path:** [[Cyber Security 101]] > Module 3 > Windows Fundamentals 3

## 🎯 Learning Objectives
- Understand and configure Windows Update
- Use Windows Security / Defender components
- Understand BitLocker disk encryption
- Know EFS and Volume Shadow Copy (VSS)

## 📖 Key Concepts

### Windows Update
Critical for patching CVEs. WannaCry exploited MS17-010 — the patch existed 2 months before the outbreak.

### Windows Security (Defender) Components
| Component | Purpose |
|-----------|---------|
| Virus & Threat Protection | AV + real-time protection |
| Firewall & Network Protection | Windows Defender Firewall |
| App & Browser Control | SmartScreen, exploit protection |
| Device Security | Secure Boot, TPM, Core isolation |

```powershell
Get-NetFirewallProfile | Select Name, Enabled
Set-NetFirewallProfile -All -Enabled True
```

### BitLocker
Full disk encryption using TPM. Recovery key should be stored in AD or Azure AD.

> [!warning] BitLocker recovery keys in AD are a high-value target — compromise allows decrypting all protected drives.

### Volume Shadow Copy (VSS)
Windows snapshots — used for backups. Ransomware deletes these:
`vssadmin delete shadows /all` — monitor for this command!

## 🔑 Key Takeaways
- Patch management is the single most impactful security control
- Windows Defender = solid baseline — never disable without replacement
- VSS deletion is a key ransomware indicator

## 🔗 Related Notes
- [[CS101-07 - Windows Fundamentals 1]] · [[CS101-08 - Windows Fundamentals 2]]
- [[CS101-10 - Active Directory Basics]] · [[BitLocker]] · [[Windows Defender]] · [[Ransomware]]
