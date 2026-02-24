---
tags: [THM, pre-security, computer-fundamentals, virtualisation, room]
platform: TryHackMe
type: room
module: "Computer Fundamentals"
module_number: 4
room_number: 16
status: "⬜"
url: https://tryhackme.com/room/virtualisationbasics
difficulty: Easy
---

# 🖥️ Virtualisation Basics

> [!abstract] Summary
> Virtualisation allows multiple operating systems to run simultaneously on a single physical machine using a hypervisor. Essential for lab environments, cloud computing, and malware analysis.

**Path:** [[Pre Security (New)]] > [[Computer Fundamentals]] > Virtualisation Basics

---

## 📖 Key Concepts

### What is Virtualisation?
Virtualisation creates a **software-based (virtual) version** of hardware, allowing multiple OS instances (**VMs**) to run on one physical machine.

```
Physical Host Machine
├── Hypervisor
│   ├── VM 1: Windows 10
│   ├── VM 2: Kali Linux
│   └── VM 3: Ubuntu Server
```

---

### Hypervisors

**Type 1 — Bare Metal (runs directly on hardware)**
- More efficient, used in enterprise/cloud
- Examples: VMware ESXi, Microsoft Hyper-V, Xen

**Type 2 — Hosted (runs on top of an OS)**
- Easier to use, common for personal labs
- Examples: VirtualBox, VMware Workstation, Parallels

---

### Virtual Machine (VM) Features

| Feature | Description |
|---------|-------------|
| **Snapshot** | Save VM state at a point in time — restore if something breaks |
| **Isolation** | VM is sandboxed — malware can't easily escape |
| **Cloning** | Duplicate a VM quickly |
| **Shared folders** | Transfer files between host and VM |
| **NAT / Bridged networking** | Control how VM accesses the network |

---

### Containers vs VMs

| | Virtual Machine | Container (Docker) |
|---|---|---|
| **Isolation** | Full OS isolation | Process-level isolation |
| **Size** | GBs | MBs |
| **Boot time** | Minutes | Seconds |
| **Overhead** | High | Low |
| **Use case** | Full OS environments | Microservices, app deployment |

---

### Security Relevance

**For Defenders:**
- **Malware sandboxes** run samples in isolated VMs (Cuckoo Sandbox, Any.run)
- **Snapshots** allow safe rollback after testing

**For Pen Testers:**
- Build personal labs with VMs (Kali Linux attacking a vulnerable VM)
- TryHackMe itself deploys VMs per room

**Risks:**
- **VM Escape** — rare but critical vulnerability where malware breaks out of a VM
- Misconfigured shared folders can expose host files

---

## 🛠️ Common Tools
| Tool | Type | Use |
|------|------|-----|
| VirtualBox | Type 2 Hypervisor | Free, personal labs |
| VMware Workstation | Type 2 Hypervisor | Professional labs |
| Kali Linux | Security distro | Pen testing VM |
| Docker | Container runtime | App deployment |

---

## 🔑 Key Takeaways
- Virtualisation runs multiple OSes on one physical machine via a hypervisor
- Type 1 = bare metal (enterprise); Type 2 = hosted (personal lab)
- VMs are essential for security labs, malware analysis, and safe experimentation
- Containers are lighter than VMs but provide less isolation

## 🔗 Related Notes
- [[17 - Cloud Computing Fundamentals]] · [[13 - Inside a Computer System]]
- [[Virtualisation]] · [[Docker]] · [[Kali Linux]] · [[Malware Analysis]]
