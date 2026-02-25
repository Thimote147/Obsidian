---
tags: [THM, cyber-security-101, linux, SSH, room]
platform: TryHackMe
type: room
module: "02 - Linux Fundamentals"
module_number: 2
room_number: 5
status: "⬜"
url: https://tryhackme.com/room/linuxfundamentalspart2
difficulty: Easy
---

# 🐧 Linux Fundamentals Part 2

> [!abstract] Summary
> Continue your Linux journey — log in via SSH, use advanced commands with flags, interact with the filesystem, and understand file permissions.

**Path:** [[Cyber Security 101]] > Module 2 > Linux Fundamentals Part 2

## 🎯 Learning Objectives
- Log into a Linux machine via SSH
- Use commands with flags and switches
- Copy, move, delete files
- Understand file permissions (rwx)

## 📖 Key Concepts
### SSH
```bash
ssh user@10.10.x.x           # Connect
ssh -i key.pem user@host     # With key
```

### File Operations
```bash
touch file.txt   # Create
mkdir -p a/b/c   # Create nested dirs
cp src dst       # Copy
mv src dst       # Move/rename
rm -rf dir/      # Delete dir (careful!)
file document    # Detect file type
```

### Permissions
```
ls -la → -rwxr-xr-- 1 alice staff 1234 file.txt
         uuu|ggg|ooo  (r=4, w=2, x=1)
```
```bash
chmod 755 script.sh   # rwxr-xr-x
chmod +x script.sh    # Add execute
chown alice:staff file
```

### Key Directories
```
/etc/passwd   # User accounts (world-readable)
/etc/shadow   # Password hashes (root only!)
~/.ssh/       # SSH keys
~/.bash_history  # Command history (check for passwords!)
```

```bash
ls -la       # Long format + hidden
ls -lh       # Human-readable sizes
man ls       # Manual pages
```

> [!warning] `~/.bash_history` often contains accidentally typed passwords. Always check during post-exploitation.



## 🔑 Key Takeaways
- SSH key auth is more secure than passwords
- File permissions (rwx) control access for user/group/others
- `rm -rf` is irreversible — always double-check

## 🔗 Related Notes
- [[CS101-04 - Linux Fundamentals Part 1]] · [[CS101-06 - Linux Fundamentals Part 3]]
- [[SSH]] · [[Linux Permissions]] · [[Linux Filesystem]]
