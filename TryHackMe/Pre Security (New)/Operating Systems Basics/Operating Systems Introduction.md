---
tags: [THM, pre-security, operating-systems, room]
platform: TryHackMe
type: room
module: "Operating Systems Basics"
module_number: 5
room_number: 18
status: "⬜"
url: https://tryhackme.com/room/osintro
difficulty: Easy
---

# ⚙️ Operating Systems: Introduction

> [!abstract] Summary
> What an OS is, its role in managing hardware and software, key OS concepts (kernel, processes, file systems), and an overview of Windows vs Linux.

**Path:** [[Pre Security (New)]] > [[Operating Systems Basics]] > OS Introduction

---

## 📖 Key Concepts

### What is an Operating System?
The OS is software that **manages hardware resources** and provides services to applications. It is the intermediary between user programs and hardware.

**Core functions:**
- Process management (scheduling CPU time)
- Memory management (allocating RAM)
- File system management (organizing storage)
- Device management (drivers)
- Security & access control

---

### The Kernel
The **kernel** is the core of the OS — it runs in privileged mode and directly manages hardware.

```
User Applications
      ↕
  System Calls
      ↕
    Kernel  ←→ Hardware (CPU, RAM, Storage, Network)
```

**Kernel space vs User space:**
- **Kernel space** — privileged, direct hardware access (OS core)
- **User space** — restricted, where normal apps run

> [!tip] Security Note
> **Privilege Escalation** attacks attempt to move from user space to kernel space (ring 0) or from a low-privilege user to root/Administrator.

---

### Process Management

| Concept | Description |
|---------|-------------|
| **Process** | A running instance of a program |
| **Thread** | A unit of execution within a process |
| **PID** | Process ID — unique number per process |
| **Scheduling** | OS decides which process gets CPU time |

```bash
# List processes
ps aux              # Linux
Get-Process         # Windows PowerShell
tasklist            # Windows CMD
```

---

### Common Operating Systems

| OS | Use Case | Kernel |
|----|----------|--------|
| **Windows 10/11** | Desktop/enterprise | NT Kernel |
| **Windows Server** | Servers | NT Kernel |
| **macOS** | Apple desktop | XNU (Darwin) |
| **Linux** | Servers, security, embedded | Linux Kernel |
| **Android** | Mobile | Linux Kernel |
| **iOS** | Apple mobile | XNU |

---

### Windows vs Linux (Security Perspective)

| | Windows | Linux |
|---|---|---|
| **Market share (desktop)** | ~72% | ~4% |
| **Market share (server)** | ~33% | ~67% |
| **Default shell** | CMD / PowerShell | Bash |
| **File system** | NTFS | ext4, XFS |
| **Admin account** | Administrator | root |
| **Pen testing tools** | Limited native | Kali Linux — industry standard |
| **Attack surface** | Higher (more targets) | More secure by default |

---

## 🔑 Key Takeaways
- The OS manages hardware and provides services to applications
- The kernel is the core — kernel-level access = full control
- Understanding processes, file systems, and permissions is core to security
- Linux dominates servers; Windows dominates desktops — both are key targets

## 🔗 Related Notes
- [[Windows Basics]] · [[Linux CLI Basics]] · [[Operating System Security]]
- [[Kernel]] · [[Privilege Escalation]] · [[System Owner-User Discovery - Linux]] · [[System Owner-User Discovery - Windows]]
