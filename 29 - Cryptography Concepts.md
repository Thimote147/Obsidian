---
tags: [THM, pre-security, attacks-defenses, cryptography, room]
platform: TryHackMe
type: room
module: "Attacks and Defenses"
module_number: 7
room_number: 29
status: "⬜"
url: https://tryhackme.com/room/cryptographyconcepts
difficulty: Easy
---

# 🔑 Cryptography Concepts

> [!abstract] Summary
> Foundational cryptography — encryption (symmetric & asymmetric), hashing, digital signatures, and TLS/HTTPS. Cryptography underpins all secure communication and data protection.

**Path:** [[Pre Security (New)]] > [[Attacks and Defenses]] > Cryptography Concepts

---

## 📖 Key Concepts

### Types of Encryption

#### Symmetric Encryption
- **Same key** used to encrypt AND decrypt
- Fast, efficient — good for bulk data
- Problem: how do you securely share the key?

| Algorithm | Key Size | Notes |
|-----------|----------|-------|
| AES-128 | 128-bit | Secure, widely used |
| AES-256 | 256-bit | Standard for high security |
| DES | 56-bit | **Broken** — do not use |
| 3DES | 168-bit | Deprecated — too slow |

```
Plaintext → [AES + Key] → Ciphertext
Ciphertext → [AES + Same Key] → Plaintext
```

#### Asymmetric Encryption
- **Two mathematically linked keys:** Public key (share freely) + Private key (keep secret)
- Slower than symmetric — used for key exchange and signatures
- Solves the key distribution problem

| Algorithm | Use Case |
|-----------|---------|
| RSA | Encryption, digital signatures |
| ECC | Modern alternative to RSA, smaller keys |
| Diffie-Hellman | Key exchange |

```
Alice's Public Key → encrypt → Ciphertext
Alice's Private Key → decrypt → Plaintext
```

#### Hybrid Encryption (How HTTPS Works)
Uses asymmetric to securely exchange a symmetric session key, then switches to fast symmetric encryption:
```
1. TLS Handshake: asymmetric crypto exchanges a symmetric session key
2. All data encrypted with fast symmetric (AES) session key
```

---

### Hashing
A **one-way function** — converts data of any size into a fixed-size digest. Cannot be reversed.

| Algorithm | Output | Status |
|-----------|--------|--------|
| MD5 | 128-bit (32 hex) | **Broken** — collision attacks |
| SHA-1 | 160-bit (40 hex) | **Weak** — avoid |
| SHA-256 | 256-bit (64 hex) | Secure, widely used |
| SHA-512 | 512-bit | Very secure |
| bcrypt | Variable | Best for passwords (has salt) |

```bash
# Generate hashes
echo -n "password" | md5sum
echo -n "password" | sha256sum
# Linux password hashing
python3 -c "import hashlib; print(hashlib.sha256(b'password').hexdigest())"
```

**Uses of hashing:**
- Password storage (never store plaintext!)
- File integrity verification
- Digital signatures
- Proof of work (blockchain)

#### Password Cracking
```bash
# Hashcat — GPU-accelerated
hashcat -m 0 hashes.txt wordlist.txt              # MD5
hashcat -m 1800 shadow.txt rockyou.txt            # SHA-512crypt (Linux shadow)
hashcat -m 1000 hashes.txt rockyou.txt            # NTLM (Windows)

# John the Ripper
john --wordlist=/usr/share/wordlists/rockyou.txt shadow.txt
```

---

### Digital Signatures
Prove **authenticity and integrity** of data using asymmetric cryptography.

```
1. Sender hashes the message → digest
2. Sender encrypts digest with PRIVATE key → signature
3. Receiver decrypts signature with SENDER'S PUBLIC key → digest
4. Receiver hashes the received message → their own digest
5. If digests match → authentic and unmodified
```

---

### TLS/HTTPS
TLS (Transport Layer Security) secures communications over the network.

**TLS Handshake (simplified):**
```
1. Client Hello (supported cipher suites)
2. Server Hello + Certificate (public key)
3. Client verifies certificate (via CA chain)
4. Key exchange (generate session key)
5. Both switch to symmetric encryption
6. Encrypted data flows
```

**Certificate Authorities (CAs):**
- CAs sign certificates to prove a server's identity
- Browser trusts CAs → trusts sites they've signed
- **Self-signed cert** = not trusted by browsers by default

---

### Common Cryptographic Attacks

| Attack | Target | Description |
|--------|--------|-------------|
| **Brute Force** | Passwords | Try all combinations |
| **Dictionary Attack** | Passwords | Try wordlist |
| **Rainbow Table** | Hashes | Precomputed hash→plaintext table |
| **Salt** | Defense | Random data added before hashing — defeats rainbow tables |
| **Padding Oracle** | Symmetric | Exploits padding error messages |
| **Downgrade Attack** | TLS | Forces use of older, weaker protocols |

---

## 🔑 Key Takeaways
- Symmetric = fast, same key; Asymmetric = key pair, solves distribution
- Hashing is one-way; never store plaintext passwords
- HTTPS = HTTP + TLS; asymmetric for handshake, symmetric for data
- Salting passwords defeats rainbow table attacks

## 🔗 Related Notes
- [[28 - The CIA Triad]] · [[10 - HTTP in Detail]] · [[24 - Data Encoding]]
- [[Encryption]] · [[Hashing]] · [[TLS]] · [[Hashcat]] · [[Digital Signature]]
