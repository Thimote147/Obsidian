---
tags: [THM, pre-security, software-basics, encoding, room]
platform: TryHackMe
type: room
module: "Software Basics"
module_number: 6
room_number: 24
status: "⬜"
url: https://tryhackme.com/room/dataencoding
difficulty: Easy
---

# 🔡 Data Encoding

> [!abstract] Summary
> How data is encoded for storage and transmission — ASCII, Unicode, Base64, and URL encoding. Understanding encoding is critical for web exploitation and data analysis.

**Path:** [[Pre Security (New)]] > [[Software Basics]] > Data Encoding

---

## 📖 Key Concepts

### ASCII
Maps characters to numbers (0–127).

| Char | Decimal | Hex |
|------|---------|-----|
| A | 65 | 0x41 |
| a | 97 | 0x61 |
| 0 | 48 | 0x30 |
| Space | 32 | 0x20 |

### Unicode (UTF-8)
Extends ASCII to support all world languages. UTF-8 is backward-compatible with ASCII.

### Base64
Encodes binary data as printable ASCII text. Used to transmit binary over text channels (email attachments, JWT tokens, embedded images).

**Characters:** A–Z, a–z, 0–9, +, / (64 chars) + `=` padding

```bash
# Encode
echo -n "TryHackMe" | base64
# VHJ5SGFja01l

# Decode
echo "VHJ5SGFja01l" | base64 -d
# TryHackMe
```

> [!warning] Security Note
> Base64 is **NOT encryption** — it's trivially reversible. Data encoded in Base64 is not protected. Attackers use Base64 to obfuscate payloads and bypass basic filters.

### URL Encoding (Percent Encoding)
Encodes special characters in URLs using `%` + hex value.

| Character | URL Encoded |
|-----------|-------------|
| Space | `%20` or `+` |
| `&` | `%26` |
| `=` | `%3D` |
| `/` | `%2F` |
| `<` | `%3C` |
| `>` | `%3E` |
| `'` | `%27` |

> [!warning] Security Note
> URL encoding is used to **bypass WAF filters** and inject payloads. Double encoding (`%252F` → `%2F` → `/`) can bypass input validation.

### HTML Encoding
Encodes characters to prevent HTML injection.

| Character | HTML Entity |
|-----------|------------|
| `<` | `&lt;` |
| `>` | `&gt;` |
| `&` | `&amp;` |
| `"` | `&quot;` |
| `'` | `&#39;` |

---

## 🛠️ Commands

```bash
# Base64
echo -n "text" | base64           # Encode
echo "dGV4dA==" | base64 -d      # Decode

# Python for encoding/decoding
python3 -c "import base64; print(base64.b64decode('VHJ5SGFja01l').decode())"
python3 -c "from urllib.parse import unquote; print(unquote('%3Cscript%3E'))"

# CyberChef (browser tool) — excellent for chained encoding/decoding
# https://gchq.github.io/CyberChef/
```

---

## 🔑 Key Takeaways
- ASCII/Unicode encode text as numbers; Base64 encodes binary as text
- Base64 is NOT encryption — it provides zero security
- URL encoding is used legitimately AND maliciously to bypass filters
- CyberChef is the best tool for encoding/decoding chains in CTFs

## 🔗 Related Notes
- [[Data Representation]] · [[Cryptography Concepts]]
- [[Base64]] · [[URL Encoding]] · [[ASCII]] · [[CyberChef]]
