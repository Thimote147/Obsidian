---
tags: [THM, cyber-security-101, defensive-tooling, FlareVM, malware-analysis, room]
platform: TryHackMe
type: room
module: "12 - Defensive Security Tooling"
module_number: 12
room_number: 50
status: "⬜"
url: https://tryhackme.com/room/flarevmarsenaloftools
difficulty: Easy
---

# 🪟 FlareVM: Arsenal of Tools

> [!abstract] Summary
> Learn FlareVM — Mandiant's Windows malware analysis distribution. The Windows counterpart to REMnux, packed with PE analysis, debugging, and reverse engineering tools.

**Path:** [[Cyber Security 101]] > Module 12 > FlareVM: Arsenal of Tools

## 🎯 Learning Objectives
- Navigate the FlareVM environment
- Triage PE files with pestudio
- Debug with x64dbg
- Disassemble/decompile with Ghidra

## 📖 Key Concepts

### Key Tool Categories
| Category | Tools |
|----------|-------|
| **PE Analysis** | pestudio, PE-bear, CFF Explorer, DIE |
| **Disassemblers** | Ghidra (free), IDA Pro (paid), Binary Ninja |
| **Debuggers** | x64dbg/x32dbg, WinDbg |
| **Network** | Wireshark, FakeNet-NG |

### pestudio — Quick Triage
First tool to use — highlights suspicious indicators:
- High entropy sections (packed/encrypted)
- Suspicious API imports (VirtualAllocEx, WriteProcessMemory → process injection)
- Blacklisted strings (known malicious IOCs)

### x64dbg Key Shortcuts
```
F2 → Set breakpoint    F7 → Step into
F8 → Step over         F9 → Run to breakpoint
F4 → Run to cursor     Ctrl+G → Go to address
```

### Suspicious PE Indicators
```
UPX/MPRESS sections        → packed binary (unpack first)
Very few imports           → packed/obfuscated
VirtualAllocEx + WriteProcessMemory + CreateRemoteThread → process injection
RegCreateKey + RegSetValue → registry persistence
High entropy .text section → encrypted code
```

### Ghidra
1. File → New Project → Import PE
2. Run auto-analysis
3. Navigate functions list → decompiler shows C-like pseudocode

> [!warning] Always run malware in an **isolated VM** — no network (or INetSim/FakeNet only), no shared folders, no clipboard sharing. Take a snapshot before analysis. **Revert after** every sample.

## 🔑 Key Takeaways
- FlareVM = Windows malware lab — REMnux for Windows
- pestudio is the fastest first-look triage tool
- x64dbg is the go-to open-source Windows debugger
- Ghidra is free and excellent — no excuse not to learn it

## 🔗 Related Notes
- [[CS101-49 - REMnux Getting Started]] · [[CS101-48 - CAPA The Basics]]
- [[FlareVM]] · [[Malware Analysis]] · [[Reverse Engineering]] · [[x64dbg]] · [[Ghidra]]
