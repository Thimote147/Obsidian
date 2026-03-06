delete all sigma in prod and keep in common
Migrate through servicenow
Filter fields
Check logs to find sigma rules ideas
Check MITRE ATT&CK
create doc confluence

1. User creation/deletation (windows/linux)
2. Add/delete a user group (windows/linux)
3. Sudo abuse
4. Nmap scanning
5. Persistence
---
6. If a user gets five failed Login Attempts in 10 seconds, raise an alert for `Multiple Failed Login Attempts`
7. If login is successful after multiple failed login attempts, raise an alert for Successful Login After multiple Login Attempts
8. If outbound traffic is > 25 MB, raise an alert to potential data exfiltration Attempt (Usually, it depends on the company policy) **very interesting to implement**


Toujours aller voir les règles existantes auprès de la communauté (nextron system)