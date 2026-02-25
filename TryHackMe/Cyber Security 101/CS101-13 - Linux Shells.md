---
tags: [THM, cyber-security-101, linux, bash, shells, room]
platform: TryHackMe
type: room
module: "04 - Command Line"
module_number: 4
room_number: 13
status: "⬜"
url: https://tryhackme.com/room/linuxshells
difficulty: Easy
---

# 🐚 Linux Shells

> [!abstract] Summary
> Learn the different Linux shell types, Bash scripting fundamentals, and environment customisation. Essential for automation and understanding shell-based attacks.

**Path:** [[Cyber Security 101]] > Module 4 > Linux Shells

## 🎯 Learning Objectives
- Know shell types (sh, bash, zsh, fish)
- Write Bash scripts for automation
- Understand environment variables and PATH
- Understand shells in a security context (reverse/bind shells)

## 📖 Key Concepts

### Shell Types
```bash
echo $SHELL        # Current shell
cat /etc/shells    # All installed shells
```
bash → most common · zsh → macOS default · sh → minimal · fish → user-friendly

### Bash Scripting
```bash
#!/bin/bash
name="Alice"
echo "Hello $name"

# Conditionals
if [ $name == "Alice" ]; then
    echo "Welcome"
fi

# Loops
for i in 1 2 3; do echo $i; done

# Functions
greet() { echo "Hello, $1!"; }
greet "Alice"

# Exit codes
echo $?    # 0=success
```

### Environment Variables
```bash
env                  # All variables
echo $PATH           # Command search path — PATH hijacking for privesc!
export MYVAR="value"
PATH=$PATH:/new/path  # Add to PATH
```

> [!warning] **PATH hijacking** — if a script runs commands without full paths and an attacker controls a directory in PATH, they can hijack execution. Monitor $PATH during privilege escalation checks.

### Security Context
- **Reverse shell** — target calls back to attacker listener (most common)
- **Bind shell** — target listens, attacker connects in

See [[CS101-36 - Shells Overview]] for full shell exploitation detail.

## 🔑 Key Takeaways
- Bash is the universal Linux shell — master it
- Scripting automates both admin tasks and attack automation
- PATH variable manipulation = privilege escalation technique
- "Getting a shell" = the goal of most exploitation

## 🔗 Related Notes
- [[CS101-06 - Linux Fundamentals Part 3]] · [[CS101-36 - Shells Overview]]
- [[Bash]] · [[Reverse Shell]] · [[Linux Privilege Escalation]] · [[Scripting]]
