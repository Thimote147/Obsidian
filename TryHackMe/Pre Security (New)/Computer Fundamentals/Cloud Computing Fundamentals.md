---
tags: [THM, pre-security, computer-fundamentals, cloud, room]
platform: TryHackMe
type: room
module: "Computer Fundamentals"
module_number: 4
room_number: 17
status: "⬜"
url: https://tryhackme.com/room/cloudcomputingfundamentals
difficulty: Easy
---

# ☁️ Cloud Computing Fundamentals

> [!abstract] Summary
> Introduction to cloud computing — what it is, service models (IaaS, PaaS, SaaS), deployment models, and the shared responsibility model that defines cloud security.

**Path:** [[Pre Security (New)]] > [[Computer Fundamentals]] > Cloud Computing Fundamentals

---

## 📖 Key Concepts

### What is Cloud Computing?
Delivering computing resources (servers, storage, databases, networking, software) **over the Internet** on a pay-as-you-go basis — instead of owning physical infrastructure.

**Key benefits:** Scalability, cost efficiency, global availability, no hardware management

**Major providers:** AWS (Amazon), Azure (Microsoft), GCP (Google)

---

### Service Models

| Model | You manage | Provider manages | Example |
|-------|-----------|-----------------|---------|
| **IaaS** (Infrastructure as a Service) | OS, apps, data | Hardware, network, virtualisation | AWS EC2, Azure VMs |
| **PaaS** (Platform as a Service) | Apps, data | Everything below | Heroku, Google App Engine |
| **SaaS** (Software as a Service) | Just your data/config | Everything | Gmail, Office 365, Salesforce |

> [!tip] Memory Aid
> Pizza analogy: IaaS = bring your own toppings, PaaS = choose from menu, SaaS = order delivery.

---

### Deployment Models

| Model | Description | Use Case |
|-------|-------------|---------|
| **Public Cloud** | Shared infrastructure, managed by provider | Startups, general workloads |
| **Private Cloud** | Dedicated infrastructure, on-prem or hosted | High-security, compliance |
| **Hybrid Cloud** | Mix of public + private | Most enterprises |
| **Multi-Cloud** | Using multiple cloud providers | Avoid vendor lock-in |

---

### Shared Responsibility Model

Security responsibilities are **split** between the cloud provider and the customer:

```
PROVIDER responsible for:        CUSTOMER responsible for:
- Physical security               - Data
- Hypervisor/infrastructure       - Identity & Access Management (IAM)
- Networking                      - Application security
- Storage hardware                - OS patching (IaaS)
                                  - Encryption configuration
```

> [!warning] Cloud Misconfigurations
> The #1 cause of cloud breaches is **customer misconfiguration**, not provider vulnerabilities:
> - S3 buckets set to public
> - Over-permissive IAM roles
> - Exposed admin interfaces
> - Missing encryption

---

### Key Cloud Security Concepts

| Concept | Description |
|---------|-------------|
| **IAM** | Identity and Access Management — who can do what |
| **Least Privilege** | Grant only the minimum permissions needed |
| **S3 Bucket** | AWS object storage — can be misconfigured to expose data publicly |
| **Security Groups** | Virtual firewalls for cloud instances |
| **CloudTrail** | AWS logging service — records all API calls |
| **CSPM** | Cloud Security Posture Management — detects misconfigs |

---

## 🔑 Key Takeaways
- Cloud = renting computing resources over the Internet instead of owning hardware
- IaaS/PaaS/SaaS define how much you manage vs the provider
- The **shared responsibility model** means customers must secure their data and apps
- Misconfiguration is the #1 cloud security risk

## 🔗 Related Notes
- [[Virtualisation Basics]] · [[Client-Server Basics]]
- [[Cloud Computing]] · [[AWS]] · [[IAM]] · [[S3 Bucket]] · [[Shared Responsibility Model]]
