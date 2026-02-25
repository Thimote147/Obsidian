---
tags:
  - THM
  - pre-security
  - computer-fundamentals
  - hardware
  - room
platform: TryHackMe
type: room
module: "Computer Fundamentals"
module_number: 4
room_number: 13
status: "⬜"
url: https://tryhackme.com/room/insideacomputersystem
difficulty: Easy
---

# 🧠 Inside a Computer System

> [!abstract] Summary
> Explores the hardware components that make up a computer — CPU, RAM, storage, motherboard — and how they work together to execute programs.

**Path:** [[Pre Security (New)]] > [[Computer Fundamentals]] > Inside a Computer System

---

## 🎯 Learning Objectives
- Identify and understand the main hardware components of a computer
- Understand how CPU, RAM, and storage interact
- Learn how data flows between components

---

## 📖 Key Concepts

### Core Components

#### CPU (Central Processing Unit)
- The "brain" of the computer — executes instructions
- **Clock speed:** measured in GHz (e.g., 3.5 GHz = 3.5 billion cycles/second)
- **Cores:** modern CPUs have multiple cores (4, 8, 16) for parallelism
- **Cache:** L1/L2/L3 fast memory built into the CPU
- **Architecture:** x86/x64 (Intel/AMD), ARM (mobile/Mac M-series)

> [!tip] Security Note
> CPU architecture affects what exploits work — shellcode must match the target architecture.

#### RAM (Random Access Memory)
- Temporary, fast storage for **currently running programs**
- Volatile — data lost when power is off
- Measured in GB (e.g., 8GB, 16GB, 32GB)
- **DDR4/DDR5** — current standards

> [!tip] Security Note
> **Memory forensics** (e.g., with Volatility) can extract running processes, encryption keys, and passwords from RAM dumps.

#### Storage (HDD / SSD)
- Permanent data storage (survives power off)
- **HDD** (Hard Disk Drive) — magnetic, slower, cheaper
- **SSD** (Solid State Drive) — flash-based, faster, more expensive
- **NVMe** — fastest SSD interface (PCIe)

> [!tip] Security Note
> Deleted files may still exist on disk until overwritten — recoverable with tools like Autopsy or PhotoRec.

#### Motherboard
- The main circuit board connecting all components
- Contains: CPU socket, RAM slots, PCIe slots, BIOS/UEFI chip
- **BIOS/UEFI** — firmware that initializes hardware at boot

#### GPU (Graphics Processing Unit)
- Specialized for parallel processing (graphics, AI, crypto mining)
- **VRAM** — dedicated graphics memory

#### PSU (Power Supply Unit)
- Converts AC wall power to DC power for components

---

### Data Flow Between Components

```
Storage (slow, permanent)
    ↕ loads programs into
RAM (fast, temporary)
    ↕ CPU fetches instructions from
CPU (executes)
    ↕ displays output via
GPU → Monitor
```

---

### Units of Measurement

| Unit | Value |
|------|-------|
| 1 Bit | 0 or 1 |
| 1 Byte | 8 bits |
| 1 KB | 1,024 bytes |
| 1 MB | 1,024 KB |
| 1 GB | 1,024 MB |
| 1 TB | 1,024 GB |

---

## 🔑 Key Takeaways
- CPU executes instructions; RAM holds active data; Storage holds persistent data
- CPU architecture (x86/ARM) matters for exploit development
- RAM is forensically valuable — contains live process data and keys
- Understanding hardware helps understand OS behavior and security implications

---

## 🔗 Related Notes
- [[Computer Types]] — different form factors of computers
- [[Operating Systems Introduction]] — the software that manages hardware
- [[CPU]] · [[RAM]] · [[Storage]] · [[Motherboard]] · [[Memory Forensics]]
