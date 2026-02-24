---
tags: [THM, pre-security, software-basics, binary, room]
platform: TryHackMe
type: room
module: "Software Basics"
module_number: 6
room_number: 23
status: "⬜"
url: https://tryhackme.com/room/datarepresentation
difficulty: Easy
---

# 🔢 Data Representation

> [!abstract] Summary
> How computers represent data — binary, decimal, hexadecimal, and the relationships between them. Foundational for understanding low-level security concepts.

**Path:** [[Pre Security (New)]] > [[Software Basics]] > Data Representation

---

## 📖 Key Concepts

### Number Systems

| Base | Name | Digits |
|------|------|--------|
| 2 | Binary | 0, 1 |
| 8 | Octal | 0–7 |
| 10 | Decimal | 0–9 |
| 16 | Hexadecimal | 0–9, A–F |

### Binary
Computers store everything as **bits** (0 or 1). Groups of 8 bits = 1 byte.

```
Binary:    1 0 1 0 1 1 0 1
Position:  128 64 32 16 8 4 2 1

= 128 + 32 + 8 + 4 + 1 = 173 (decimal)
```

### Hexadecimal
Hex is used extensively in security (memory addresses, color codes, hashes, shellcode).

| Decimal | Hex | Binary |
|---------|-----|--------|
| 0 | 0 | 0000 |
| 10 | A | 1010 |
| 15 | F | 1111 |
| 255 | FF | 11111111 |

Hex addresses look like: `0x7fff5fbff820`

### Conversion Commands
```bash
# Python (best tool for conversions)
python3 -c "print(bin(173))"       # Decimal → Binary: 0b10101101
python3 -c "print(hex(173))"       # Decimal → Hex: 0xad
python3 -c "print(int('10101101', 2))"  # Binary → Decimal: 173
python3 -c "print(int('ad', 16))"  # Hex → Decimal: 173
```

---

## 🔑 Key Takeaways
- All data in a computer is ultimately binary (0s and 1s)
- Hex is a compact representation of binary — 2 hex digits = 1 byte
- These number systems appear constantly in exploit development and forensics

## 🔗 Related Notes
- [[24 - Data Encoding]] · [[Binary]] · [[Hexadecimal]] · [[ASCII]]
