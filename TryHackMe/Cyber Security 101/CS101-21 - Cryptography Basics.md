---
tags: [THM, cyber-security-101, cryptography, AES, room]
platform: TryHackMe
type: room
module: "06 - Cryptography"
module_number: 6
room_number: 21
status: "⬜"
url: https://tryhackme.com/room/cryptographybasics
difficulty: Easy
---

# 🔐 Cryptography Basics

> [!abstract] Summary
> Foundations of cryptography — symmetric encryption, cipher types, AES, and cipher modes. The base for understanding all encrypted communications.

**Path:** [[Cyber Security 101]] > Module 6 > Cryptography Basics

## 🎯 Learning Objectives
- Differentiate encoding, encryption, and hashing
- Understand symmetric encryption algorithms
- Know block vs stream ciphers
- Understand cipher modes (ECB, CBC, GCM)

## 📖 Key Concepts

### Encoding vs Encryption vs Hashing
| | Encoding | Encryption | Hashing |
|-|---------|-----------|---------|
| Reversible | Yes (no key) | Yes (with key) | No |
| Purpose | Format change | Confidentiality | Integrity |
| Example | Base64 | AES | SHA-256 |

### Symmetric Algorithms
| Algorithm | Key Size | Status |
|-----------|---------|--------|
| DES | 56-bit | Broken ❌ |
| 3DES | 112/168-bit | Deprecated ❌ |
| AES-128 | 128-bit | Secure ✅ |
| AES-256 | 256-bit | Very secure ✅ |
| RC4 | Variable | Broken (WEP) ❌ |
| ChaCha20 | 256-bit | Modern ✅ |

### Block vs Stream Ciphers
| | Block | Stream |
|-|-------|--------|
| Processes | Fixed blocks | Bit by bit |
| Examples | AES, DES | RC4, ChaCha20 |

### Cipher Modes
| Mode | Security |
|------|---------|
| ECB | ❌ Broken — identical blocks → identical ciphertext |
| CBC | ✅ Secure — XOR with previous block |
| GCM | ✅ Best — CTR + authentication tag |

> [!warning] **ECB mode is broken** — reveals patterns in plaintext (the "ECB penguin" demonstrates this). Never use ECB. Use AES-256-GCM.

```bash
# OpenSSL AES encryption
openssl enc -aes-256-cbc -in file.txt -out file.enc -k password
openssl enc -d -aes-256-cbc -in file.enc -out file.txt -k password
```

## 🔑 Key Takeaways
- Encryption ≠ encoding ≠ hashing — know the difference
- AES-256-GCM is the modern standard for symmetric encryption
- ECB mode is insecure — never use it
- Symmetric crypto solves bulk data encryption; key exchange needs asymmetric

## 🔗 Related Notes
- [[CS101-22 - Public Key Cryptography Basics]] · [[CS101-23 - Hashing Basics]]
- [[AES]] · [[Encryption]] · [[Symmetric Cryptography]]
