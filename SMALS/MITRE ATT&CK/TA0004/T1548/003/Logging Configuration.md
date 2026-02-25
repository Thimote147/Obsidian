### Auditd Rules Configuration

**Create audit rules file:** `/etc/audit/rules.d/sudo-monitoring.rules`

```sh
# Monitor sudo command execution
-a always,exit -F arch=b64 -F path=/usr/bin/sudo -F perm=x -F auid>=1000 -F auid!=4294967295 -k sudo_execution
-a always,exit -F arch=b32 -F path=/usr/bin/sudo -F perm=x -F auid>=1000 -F auid!=4294967295 -k sudo_execution

# Monitor sudoers file access and modifications
-w /etc/sudoers -p wa -k sudoers_modification
-w /etc/sudoers.d/ -p wa -k sudoers_modification

# Monitor sudo timestamp directory (credential caching)
-w /var/db/sudo/ -p wa -k sudo_token_manipulation
-w /var/run/sudo/ -p wa -k sudo_token_manipulation
-w /var/lib/sudo/ -p wa -k sudo_token_manipulation

# Monitor common privilege escalation binaries when executed via sudo
-a always,exit -F arch=b64 -F path=/usr/bin/find -F perm=x -k priv_esc_binaries
-a always,exit -F arch=b64 -F path=/usr/bin/awk -F perm=x -k priv_esc_binaries
-a always,exit -F arch=b64 -F path=/usr/bin/python -F perm=x -k priv_esc_binaries
-a always,exit -F arch=b64 -F path=/usr/bin/python3 -F perm=x -k priv_esc_binaries
-a always,exit -F arch=b64 -F path=/usr/bin/vim -F perm=x -k priv_esc_binaries
-a always,exit -F arch=b64 -F path=/usr/bin/less -F perm=x -k priv_esc_binaries
-a always,exit -F arch=b64 -F path=/usr/bin/more -F perm=x -k priv_esc_binaries

# Monitor privilege escalation attempts (setuid system calls)
-a always,exit -F arch=b64 -S setuid -S setgid -S setreuid -S setregid -k privilege_escalation
-a always,exit -F arch=b32 -S setuid -S setgid -S setreuid -S setregid -k privilege_escalation
```

**Apply auditd rules:**
```sh
# Load the rules
sudo auditctl -R /etc/audit/rules.d/sudo-monitoring.rules

# Restart auditd service
sudo service auditd restart
# OR
sudo systemctl restart auditd

# Verify rules are loaded
sudo auditctl -l | grep sudo
```

---
### Syslog Configuration

**Configure sudo logging in:** `/etc/sudoers` or via `visudo`

```sh
# Add these directives to /etc/sudoers
Defaults    log_input
Defaults    log_output
Defaults    iolog_dir=/var/log/sudo-io
Defaults    logfile=/var/log/sudo.log
Defaults    syslog=auth
```

**Rsyslog configuration for sudo:** `/etc/rsyslog.d/10-sudo.conf`

```conf
# Separate sudo logs to dedicated file
:programname, isequal, "sudo" /var/log/sudo.log
:programname, isequal, "sudo" stop

# Enhanced sudo logging
auth,authpriv.*         /var/log/auth.log
auth.info               /var/log/auth.log
```

**Restart rsyslog:**
```sh
sudo systemctl restart rsyslog
```
