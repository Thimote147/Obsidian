---
tags: [THM, cyber-security-101, linux, room]
platform: TryHackMe
type: room
module: "02 - Linux Fundamentals"
module_number: 2
room_number: 6
status: "⬜"
url: https://tryhackme.com/room/linuxfundamentalspart3
difficulty: Easy
---

# 🐧 Linux Fundamentals Part 3

> [!abstract] Summary
> Power-up your Linux skills with text editors, process management, cron jobs, package management, and system logs.

**Path:** [[Cyber Security 101]] > Module 2 > Linux Fundamentals Part 3

## 🎯 Learning Objectives
- Use nano and vim
- Manage processes with ps, kill, systemctl
- Schedule tasks with cron
- Install packages with apt
- Read system logs

## 📖 Key Concepts
### Text Editors
```bash
nano file.txt   # Ctrl+O save, Ctrl+X exit
vim file.txt    # i=insert, Esc=normal, :wq=save+quit
```

### Process Management
```bash
ps aux                    # All processes
top / htop                # Live monitor
kill -9 PID               # Force kill
systemctl start apache2   # Start service
systemctl enable apache2  # Enable at boot
systemctl status apache2  # Check status
```

### Cron Jobs
```bash
crontab -e    # Edit cron jobs
# Format: min hour day month weekday command
0 2 * * * /opt/backup.sh   # Daily at 2am
```

### Package Management
```bash
apt update && apt upgrade  # Update all
apt install nmap           # Install
apt remove nmap            # Remove
```

### Logs
```bash
/var/log/syslog        # General
/var/log/auth.log      # Authentication
journalctl -f          # Live follow
```

### Downloading
```bash
wget http://example.com/file.txt
curl -o file.txt http://example.com
```



> [!warning] Cron jobs run by root on world-writable scripts = privilege escalation vector. Always check cron job permissions during pen tests.



## 🔑 Key Takeaways
- Cron jobs automate tasks AND are a common privilege escalation vector
- systemctl manages services — running services = attack surface
- Package management keeps software patched

## 🔗 Related Notes
- [[CS101-04 - Linux Fundamentals Part 1]] · [[CS101-05 - Linux Fundamentals Part 2]]
- [[CS101-13 - Linux Shells]] · [[Cron Jobs]] · [[Privilege Escalation]] · [[Log Analysis]]
