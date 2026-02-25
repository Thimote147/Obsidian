## Test auditd logging

```sh
# Generate test event
sudo whoami

# Check auditd logs
sudo ausearch -k sudo_execution -i
sudo ausearch -k sudoers_modification -i

# View raw audit logs
sudo tail -f /var/log/audit/audit.log | grep sudo
```

## Test syslog logging

```sh
# Check sudo logs
sudo tail -f /var/log/sudo.log
sudo tail -f /var/log/auth.log | grep sudo

# Check for sudo commands
sudo grep "COMMAND=" /var/log/auth.log
```
