---
tags: [THM, cyber-security-101, cryptography, password-cracking, room]
platform: TryHackMe
type: room
module: "06 - Cryptography"
module_number: 6
room_number: 24
status: "⬜"
url: https://tryhackme.com/room/johntheripperbasics
difficulty: Easy
---

# ⚔️ John the Ripper: The Basics

> [!abstract] Summary
> Learn John the Ripper — versatile hash-cracking tool. Crack passwords from /etc/shadow, ZIP files, PDFs, SSH keys, and more using wordlists and rules.

**Path:** [[Cyber Security 101]] > Module 6 > John the Ripper: The Basics

## 🎯 Learning Objectives
- Crack hashes with John using wordlists
- Apply rules to improve cracking
- Crack protected files (ZIP, PDF, SSH keys)
- Understand cracking modes

## 📖 Key Concepts

### Basic Usage
```bash
john hash.txt                                          # Auto-detect + default wordlist
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
john --format=NT hash.txt                              # NTLM
john --format=raw-md5 hash.txt                         # MD5
john --show hash.txt                                   # Show cracked passwords
john --list=formats                                    # List supported formats
```

### Linux /etc/shadow
```bash
unshadow /etc/passwd /etc/shadow > combined.txt
john combined.txt --wordlist=rockyou.txt
```

### Protected Files
```bash
zip2john protected.zip > zip.hash
pdf2john protected.pdf > pdf.hash
ssh2john id_rsa > ssh.hash
john <hash_file> --wordlist=rockyou.txt
```

### Rules (Word Mangling)
```bash
john --wordlist=rockyou.txt --rules=Single hash.txt   # Basic mutations
john --wordlist=rockyou.txt --rules=Jumbo hash.txt    # Extended mutations
```

### Cracking Modes
| Mode | Speed | Use |
|------|-------|-----|
| Wordlist | Fast | First attempt |
| Wordlist + Rules | Medium | If wordlist fails |
| Incremental | Slow | Last resort brute force |

> [!tip] **CTF strategy:** Always try `john --wordlist=rockyou.txt hash.txt` first. Add `--rules` if it fails. Incremental only as last resort.

## 🔑 Key Takeaways
- John is for offline hash cracking (vs Hydra for online attacks)
- `*2john` tools convert file formats to crackable hashes
- Unshadow combines passwd+shadow for Linux password cracking
- rockyou.txt at `/usr/share/wordlists/rockyou.txt` on Kali

## 🔗 Related Notes
- [[CS101-23 - Hashing Basics]] · [[CS101-34 - Hydra]]
- [[John the Ripper]] · [[Password Cracking]] · [[Hashcat]] · [[rockyou.txt]]
