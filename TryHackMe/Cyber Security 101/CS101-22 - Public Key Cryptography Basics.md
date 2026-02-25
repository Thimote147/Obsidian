---
tags: [THM, cyber-security-101, cryptography, RSA, PKI, room]
platform: TryHackMe
type: room
module: "06 - Cryptography"
module_number: 6
room_number: 22
status: "⬜"
url: https://tryhackme.com/room/publickeycryptographybasics
difficulty: Easy
---

# 🔑 Public Key Cryptography Basics

> [!abstract] Summary
> Asymmetric (public-key) cryptography — RSA, Diffie-Hellman, digital signatures, and PKI. How HTTPS, SSH, and code signing all depend on these principles.

**Path:** [[Cyber Security 101]] > Module 6 > Public Key Cryptography Basics

## 🎯 Learning Objectives
- Understand asymmetric encryption and key pairs
- Know how RSA and Diffie-Hellman work
- Understand digital signatures and certificates
- Configure SSH key authentication

## 📖 Key Concepts

### Asymmetric Key Pairs
- **Encrypt** with public key → only private key can decrypt
- **Sign** with private key → anyone with public key can verify

### RSA
Based on difficulty of factoring large primes. Minimum 2048-bit keys (4096 recommended). Used for key exchange, signatures, certificates.

### Diffie-Hellman Key Exchange
Two parties agree on a shared secret over a public channel without transmitting the secret. Basis of Forward Secrecy (PFS). **ECDH** = modern elliptic curve variant.

### Digital Signatures
1. Alice hashes message → signs with **private key**
2. Bob decrypts signature with Alice's **public key**
3. Bob hashes message independently → compare hashes
4. Match = authentic and unmodified

### PKI Chain of Trust
```
Root CA (offline, self-signed)
  └── Intermediate CA
        └── Server Certificate
```

```bash
openssl genrsa -out private.pem 4096
openssl rsa -in private.pem -pubout -out public.pem
openssl x509 -in cert.pem -text -noout  # View cert details
```

### SSH Key Auth
```bash
ssh-keygen -t ed25519                  # Generate key pair
ssh-copy-id user@server                # Copy public key
ssh -i ~/.ssh/id_ed25519 user@host     # Connect with key
```

> [!warning] **Never share your private key.** Use `chmod 600 ~/.ssh/id_ed25519`. The private key is equivalent to a master password.

## 🔑 Key Takeaways
- Asymmetric crypto solves the key distribution problem
- Encrypt with public, decrypt with private; Sign with private, verify with public
- PKI chain of trust makes HTTPS work
- SSH key auth is more secure than passwords — always prefer it

## 🔗 Related Notes
- [[CS101-21 - Cryptography Basics]] · [[CS101-23 - Hashing Basics]]
- [[CS101-17 - Networking Secure Protocols]] · [[RSA]] · [[PKI]] · [[Digital Signatures]]
