---
tags: [THM, pre-security, operating-systems, linux, CLI, room]
platform: TryHackMe
type: room
module: "Operating Systems Basics"
module_number: 5
room_number: 20
status: "⬜"
url: https://tryhackme.com/room/linuxclibasics
difficulty: Easy
---

# 🐧 Linux CLI Basics

> [!abstract] Summary
> Master the Linux command line — filesystem navigation, file operations, permissions, process management, searching, and shell operators. Linux is the dominant OS in cybersecurity tooling and servers.

**Path:** [[Pre Security (New)]] > [[Operating Systems Basics]] > Linux CLI Basics

---

## 📖 Key Concepts

### Linux Filesystem Structure

```
/                   ← Root (top of hierarchy)
├── /bin            ← Essential user binaries (ls, cat, cp)
├── /sbin           ← System binaries (root)
├── /etc            ← Configuration files
├── /home           ← User home directories (/home/alice)
├── /root           ← Root user home
├── /var            ← Variable data (logs, databases)
├── /tmp            ← Temporary files (world-writable!)
├── /usr            ← User programs and libraries
├── /opt            ← Optional/third-party software
├── /dev            ← Device files
├── /proc           ← Virtual filesystem (kernel/process info)
└── /mnt, /media    ← Mount points
```

> [!tip] Security Note
> `/tmp` is world-writable — attackers often drop payloads here. `/etc/passwd` and `/etc/shadow` store user credentials.

---

## 🛠️ Essential Commands

### Navigation
```bash
pwd                 # Print Working Directory
ls                  # List files
ls -la              # Long format + hidden files
cd /path/to/dir     # Change directory
cd ..               # Go up one level
cd ~                # Go to home directory
```

### File Operations
```bash
cat file.txt        # Display file content
less file.txt       # Paginated view
head -n 20 file.txt # First 20 lines
tail -n 20 file.txt # Last 20 lines
tail -f /var/log/syslog  # Follow live log output

cp source dest      # Copy file
mv source dest      # Move/rename
rm file.txt         # Delete file
rm -rf directory/   # Delete directory recursively
mkdir newdir        # Create directory
touch newfile.txt   # Create empty file

nano file.txt       # Text editor (beginner-friendly)
vim file.txt        # Advanced text editor
```

### Finding Files
```bash
find / -name "flag.txt"           # Find by name
find / -name "*.conf" 2>/dev/null # Find all .conf files
find /home -user alice            # Files owned by alice
find / -perm -4000 2>/dev/null    # Find SUID files (priv esc!)
locate flag.txt                   # Fast search (uses index)
which python3                     # Find binary location
```

> [!warning] Security Note
> `find / -perm -4000` finds **SUID binaries** — files that run as root regardless of who executes them. A misconfigured SUID binary is a classic privilege escalation vector.

### Searching Content
```bash
grep "password" file.txt          # Search in file
grep -r "password" /etc/          # Recursive search
grep -i "error" log.txt           # Case-insensitive
grep -v "^#" config.conf          # Exclude comment lines
cat file.txt | grep "admin"       # Pipe output to grep
```

### Permissions
```bash
ls -la
# -rwxr-xr-- 1 alice staff 1234 Jan 1 file.txt
#  ↑↑↑↑↑↑↑↑↑
#  |uuu|ggg|ooo
#  u=user, g=group, o=others
#  r=read(4), w=write(2), x=execute(1)

chmod 755 file.sh      # rwxr-xr-x
chmod +x script.sh     # Add execute permission
chmod u+w file.txt     # Add write for user
chown alice:staff file  # Change owner:group
```

**Permission Table:**
| Value | Permission |
|-------|-----------|
| 4 | Read (r) |
| 2 | Write (w) |
| 1 | Execute (x) |
| 7 | rwx |
| 6 | rw- |
| 5 | r-x |

### Process Management
```bash
ps aux              # All running processes
ps aux | grep nginx # Find specific process
top                 # Real-time process monitor
htop                # Better top (if installed)
kill PID            # Send SIGTERM (graceful)
kill -9 PID         # Send SIGKILL (force)
jobs                # List background jobs
bg                  # Resume in background
fg                  # Bring to foreground
command &           # Run in background
```

### Shell Operators
```bash
command1 && command2    # Run 2 only if 1 succeeds
command1 || command2    # Run 2 only if 1 fails
command1 ; command2     # Run both regardless
command1 | command2     # Pipe output of 1 into 2
command > file.txt      # Redirect output (overwrite)
command >> file.txt     # Redirect output (append)
command < file.txt      # Use file as input
command 2>/dev/null     # Redirect errors to null
```

### Networking Commands
```bash
ip a                    # Show interfaces and IPs
ip route                # Show routing table
ping 8.8.8.8            # Test connectivity
curl http://target.com  # HTTP request
wget http://target.com/file  # Download file
netstat -tulnp          # Open ports
ss -tulnp               # Modern netstat
```

### User & Privilege Management
```bash
whoami              # Current user
id                  # User ID and group memberships
sudo command        # Run as root
sudo -l             # What can I run as sudo?
su alice            # Switch to user alice
su -                # Switch to root (if known pw)
passwd              # Change password
```

---

## 🔑 Key Takeaways
- Linux CLI is essential for cybersecurity — most tools and servers run on Linux
- `find` with SUID flag is a critical privilege escalation recon command
- Permissions (rwx + owner/group/others) control access to every file
- `sudo -l` is one of the first commands to run after getting a shell

## 🔗 Related Notes
- [[Windows CLI Basics]] · [[Operating System Security]] · [[Operating Systems Introduction]]
- [[System Owner-User Discovery - Linux]] · [[Linux Permissions]] · [[Privilege Escalation]] · [[SUID]] · [[Bash]]
