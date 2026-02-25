---
tags: [THM, cyber-security-101, defensive-security, forensics, DFIR, room]
platform: TryHackMe
type: room
module: "10 - Defensive Security"
module_number: 10
room_number: 40
status: "⬜"
url: https://tryhackme.com/room/digitalforensicsfundamentals
difficulty: Easy
---

# 🔬 Digital Forensics Fundamentals

> [!abstract] Summary
> Learn digital forensics — systematic investigation of digital evidence after a security incident. Covers the forensics process, evidence types, acquisition, and analysis.

**Path:** [[Cyber Security 101]] > Module 10 > Digital Forensics Fundamentals

## 🎯 Learning Objectives
- Understand the forensics process (PICEFRL)
- Know evidence types and order of volatility
- Perform basic disk and memory forensics
- Maintain chain of custody

## 📖 Key Concepts

### Forensics Process
1. **Identification** — identify evidence sources
2. **Preservation** — protect integrity (write blockers, hashes)
3. **Collection** — acquire forensic images
4. **Examination** — extract relevant data
5. **Analysis** — draw conclusions
6. **Reporting** — document for legal/management

### Order of Volatility (collect most volatile first)
RAM → Running processes → Network connections → Disk → Remote logs

### Disk Forensics
```bash
dd if=/dev/sda of=/mnt/evidence.img bs=512 status=progress
md5sum /dev/sda > hash.md5                 # Hash before imaging
mount -o ro,loop evidence.img /mnt/analysis  # Mount read-only
```

### Memory Forensics (Volatility)
```bash
volatility -f memory.dmp imageinfo
volatility -f memory.dmp --profile=Win7SP1x64 pslist
volatility -f memory.dmp --profile=Win7SP1x64 netscan
volatility -f memory.dmp --profile=Win7SP1x64 malfind
```

### Key Windows Artefacts
| Artefact | Location | Value |
|---------|----------|-------|
| Event Logs | `C:\Windows\System32\winevt\` | Auth/execution events |
| Prefetch | `C:\Windows\Prefetch\` | Programs that ran |
| Registry | `HKCU\...\Run` | Persistence |
| LNK files | `%AppData%\...\Recent\` | Recently opened files |

> [!warning] Always hash evidence immediately on collection and verify at each transfer. Admissibility in court requires unbroken chain of custody.

## 🔑 Key Takeaways
- Collect volatile evidence first — it's gone after reboot
- Memory forensics reveals running malware with no disk trace
- Chain of custody is non-negotiable for legal proceedings

## 🔗 Related Notes
- [[CS101-41 - Incident Response Fundamentals]] · [[CS101-42 - Logs Fundamentals]]
- [[Digital Forensics]] · [[Volatility]] · [[Chain of Custody]]
