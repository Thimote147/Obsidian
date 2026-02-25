---
tags: [THM, cyber-security-101, cryptography, hashing, room]
platform: TryHackMe
type: room
module: "06 - Cryptography"
module_number: 6
room_number: 23
status: "⬜"
url: https://tryhackme.com/room/hashingbasics
difficulty: Easy
---

# #️⃣ Hashing Basics

> [!abstract] Summary
> Hash functions — one-way mathematical transformations used for password storage, file integrity, and digital signatures. Understand weak vs strong algorithms, rainbow tables, and salting.

**Path:** [[Cyber Security 101]] > Module 6 > Hashing Basics

## 🎯 Learning Objectives
- Understand hash function properties
- Know algorithm security status (MD5, SHA-256, bcrypt)
- Understand password hashing with salts
- Identify and crack hash types

## 📖 Key Concepts

### Hash Properties
1. Deterministic — same input → same output
2. Fixed length — output size fixed regardless of input
3. One-way — computationally infeasible to reverse
4. Avalanche effect — tiny change → completely different hash
5. Collision resistant — infeasible to find two inputs with same hash

### Algorithm Status
| Algorithm | Output | Status |
|-----------|--------|--------|
| MD5 | 32 hex | Broken ❌ |
| SHA-1 | 40 hex | Deprecated ❌ |
| SHA-256 | 64 hex | Secure ✅ |
| SHA-512 | 128 hex | Secure ✅ |
| bcrypt | 60 chars | Best for passwords ✅ |
| Argon2 | Variable | Best for passwords ✅ |
| NTLM | 32 hex | Weak (fast to crack) ❌ |

### Password Hashing + Salting
A random salt added before hashing defeats rainbow tables:
```
salt = random_bytes()
hash = bcrypt(password + salt)  # Same password → different hash each time
```

### Hash Identification
```bash
hashid "5f4dcc3b5aa765d61d8327deb882cf99"

32 chars hex  → MD5 or NTLM
40 chars hex  → SHA-1
64 chars hex  → SHA-256
$2y$... → bcrypt
$6$...  → SHA-512crypt
```

### Cracking
```bash
hashcat -m 0 hash.txt rockyou.txt      # MD5
hashcat -m 1000 hash.txt rockyou.txt   # NTLM
hashcat -m 3200 hash.txt rockyou.txt   # bcrypt (very slow)
# Online: crackstation.net
```

> [!warning] **MD5 and NTLM are trivially crackable** — modern GPUs compute billions per second. If you find MD5 password hashes in a database, treat all passwords as compromised.

## 🔑 Key Takeaways
- Hashing is one-way; encryption is reversible — never confuse them
- Use bcrypt/Argon2 for passwords — intentionally slow
- Salting defeats rainbow tables
- MD5/SHA-1 are broken for security — use SHA-256+ or bcrypt

## 🔗 Related Notes
- [[CS101-24 - John the Ripper The Basics]] · [[CS101-21 - Cryptography Basics]]
- [[Hashing]] · [[Password Cracking]] · [[bcrypt]] · [[Rainbow Tables]] · [[Salt]]
