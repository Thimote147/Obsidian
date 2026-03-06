# MITRE ATT&CK Sigma Coverage Report

> Generated: 2026-03-06  |  Source: `/opt/cso/sigma-rules`

## Summary

| Metric | Value |
|--------|-------|
| Sigma Rules Scanned | **2620** |
| Techniques Covered  | **313 / 691** |
| Coverage Rate       | **45.3%** |
| CVEs Referenced     | **9** |

## Coverage by Tactic

### Reconnaissance (TA0043)
Coverage: **3/11** (27.3%)

| Status | ID | Name | Rules | Sub-techs |
|--------|----|------|-------|-----------|
| ✅ | `T1589` | Gather Victim Identity Information | 1 | 0/3 |
| ⬜ | `T1589.001` | ↳ Credentials | 0 | — |
| ⬜ | `T1589.002` | ↳ Email Addresses | 0 | — |
| ⬜ | `T1589.003` | ↳ Employee Names | 0 | — |
| ✅ | `T1590` | Gather Victim Network Information | 9 | 1/6 |
| ✅ | `T1590.001` | ↳ Domain Properties | 1 | — |
| ⬜ | `T1590.002` | ↳ DNS | 0 | — |
| ⬜ | `T1590.003` | ↳ Network Trust Dependencies | 0 | — |
| ⬜ | `T1590.004` | ↳ Network Topology | 0 | — |
| ⬜ | `T1590.005` | ↳ IP Addresses | 0 | — |
| ⬜ | `T1590.006` | ↳ Network Security Appliances | 0 | — |
| ⬜ | `T1591` | Gather Victim Org Information | 0 | 0/4 |
| ⬜ | `T1591.001` | ↳ Determine Physical Locations | 0 | — |
| ⬜ | `T1591.002` | ↳ Business Relationships | 0 | — |
| ⬜ | `T1591.003` | ↳ Identify Business Tempo | 0 | — |
| ⬜ | `T1591.004` | ↳ Identify Roles | 0 | — |
| 🟡 | `T1592` | Gather Victim Host Information | 0 | 1/4 |
| ⬜ | `T1592.001` | ↳ Hardware | 0 | — |
| ⬜ | `T1592.002` | ↳ Software | 0 | — |
| ⬜ | `T1592.003` | ↳ Firmware | 0 | — |
| ✅ | `T1592.004` | ↳ Client Configurations | 3 | — |
| 🟡 | `T1593` | Search Open Websites/Domains | 0 | 1/3 |
| ⬜ | `T1593.001` | ↳ Social Media | 0 | — |
| ⬜ | `T1593.002` | ↳ Search Engines | 0 | — |
| ✅ | `T1593.003` | ↳ Code Repositories | 2 | — |
| ⬜ | `T1594` | Search Victim-Owned Websites | 0 | — |
| ✅ | `T1595` | Active Scanning | 2 | 0/3 |
| ⬜ | `T1595.001` | ↳ Scanning IP Blocks | 0 | — |
| ⬜ | `T1595.002` | ↳ Vulnerability Scanning | 0 | — |
| ⬜ | `T1595.003` | ↳ Wordlist Scanning | 0 | — |
| ⬜ | `T1596` | Search Open Technical Databases | 0 | 0/5 |
| ⬜ | `T1596.001` | ↳ DNS/Passive DNS | 0 | — |
| ⬜ | `T1596.002` | ↳ WHOIS | 0 | — |
| ⬜ | `T1596.003` | ↳ Digital Certificates | 0 | — |
| ⬜ | `T1596.004` | ↳ CDNs | 0 | — |
| ⬜ | `T1596.005` | ↳ Scan Databases | 0 | — |
| ⬜ | `T1597` | Search Closed Sources | 0 | 0/2 |
| ⬜ | `T1597.001` | ↳ Threat Intel Vendors | 0 | — |
| ⬜ | `T1597.002` | ↳ Purchase Technical Data | 0 | — |
| ⬜ | `T1598` | Phishing for Information | 0 | 0/4 |
| ⬜ | `T1598.001` | ↳ Spearphishing Service | 0 | — |
| ⬜ | `T1598.002` | ↳ Spearphishing Attachment | 0 | — |
| ⬜ | `T1598.003` | ↳ Spearphishing Link | 0 | — |
| ⬜ | `T1598.004` | ↳ Spearphishing Voice | 0 | — |
| ⬜ | `T1681` | Search Threat Vendor Data | 0 | — |

### Resource Development (TA0042)
Coverage: **4/8** (50.0%)

| Status | ID | Name | Rules | Sub-techs |
|--------|----|------|-------|-----------|
| ⬜ | `T1583` | Acquire Infrastructure | 0 | 0/8 |
| ⬜ | `T1583.001` | ↳ Domains | 0 | — |
| ⬜ | `T1583.002` | ↳ DNS Server | 0 | — |
| ⬜ | `T1583.003` | ↳ Virtual Private Server | 0 | — |
| ⬜ | `T1583.004` | ↳ Server | 0 | — |
| ⬜ | `T1583.005` | ↳ Botnet | 0 | — |
| ⬜ | `T1583.006` | ↳ Web Services | 0 | — |
| ⬜ | `T1583.007` | ↳ Serverless | 0 | — |
| ⬜ | `T1583.008` | ↳ Malvertising | 0 | — |
| ✅ | `T1584` | Compromise Infrastructure | 12 | 0/8 |
| ⬜ | `T1584.001` | ↳ Domains | 0 | — |
| ⬜ | `T1584.002` | ↳ DNS Server | 0 | — |
| ⬜ | `T1584.003` | ↳ Virtual Private Server | 0 | — |
| ⬜ | `T1584.004` | ↳ Server | 0 | — |
| ⬜ | `T1584.005` | ↳ Botnet | 0 | — |
| ⬜ | `T1584.006` | ↳ Web Services | 0 | — |
| ⬜ | `T1584.007` | ↳ Serverless | 0 | — |
| ⬜ | `T1584.008` | ↳ Network Devices | 0 | — |
| ⬜ | `T1585` | Establish Accounts | 0 | 0/3 |
| ⬜ | `T1585.001` | ↳ Social Media Accounts | 0 | — |
| ⬜ | `T1585.002` | ↳ Email Accounts | 0 | — |
| ⬜ | `T1585.003` | ↳ Cloud Accounts | 0 | — |
| ⬜ | `T1586` | Compromise Accounts | 0 | 0/3 |
| ⬜ | `T1586.001` | ↳ Social Media Accounts | 0 | — |
| ⬜ | `T1586.002` | ↳ Email Accounts | 0 | — |
| ⬜ | `T1586.003` | ↳ Cloud Accounts | 0 | — |
| ✅ | `T1587` | Develop Capabilities | 8 | 1/4 |
| ✅ | `T1587.001` | ↳ Malware | 6 | — |
| ⬜ | `T1587.002` | ↳ Code Signing Certificates | 0 | — |
| ⬜ | `T1587.003` | ↳ Digital Certificates | 0 | — |
| ⬜ | `T1587.004` | ↳ Exploits | 0 | — |
| ✅ | `T1588` | Obtain Capabilities | 2 | 1/7 |
| ⬜ | `T1588.001` | ↳ Malware | 0 | — |
| ✅ | `T1588.002` | ↳ Tool | 4 | — |
| ⬜ | `T1588.003` | ↳ Code Signing Certificates | 0 | — |
| ⬜ | `T1588.004` | ↳ Digital Certificates | 0 | — |
| ⬜ | `T1588.005` | ↳ Exploits | 0 | — |
| ⬜ | `T1588.006` | ↳ Vulnerabilities | 0 | — |
| ⬜ | `T1588.007` | ↳ Artificial Intelligence | 0 | — |
| ✅ | `T1608` | Stage Capabilities | 1 | 0/6 |
| ⬜ | `T1608.001` | ↳ Upload Malware | 0 | — |
| ⬜ | `T1608.002` | ↳ Upload Tool | 0 | — |
| ⬜ | `T1608.003` | ↳ Install Digital Certificate | 0 | — |
| ⬜ | `T1608.004` | ↳ Drive-by Target | 0 | — |
| ⬜ | `T1608.005` | ↳ Link Target | 0 | — |
| ⬜ | `T1608.006` | ↳ SEO Poisoning | 0 | — |
| ⬜ | `T1650` | Acquire Access | 0 | — |

### Initial Access (TA0001)
Coverage: **8/11** (72.7%)

| Status | ID | Name | Rules | Sub-techs |
|--------|----|------|-------|-----------|
| ✅ | `T1078` | Valid Accounts | 23 | 4/4 |
| ✅ | `T1078.001` | ↳ Default Accounts | 1 | — |
| ✅ | `T1078.002` | ↳ Domain Accounts | 1 | — |
| ✅ | `T1078.003` | ↳ Local Accounts | 2 | — |
| ✅ | `T1078.004` | ↳ Cloud Accounts | 4 | — |
| ✅ | `T1091` | Replication Through Removable Media | 1 | — |
| ✅ | `T1133` | External Remote Services | 8 | — |
| ✅ | `T1189` | Drive-by Compromise | 9 | — |
| ✅ | `T1190` | Exploit Public-Facing Application | 61 | — |
| ⬜ | `T1195` | Supply Chain Compromise | 0 | 0/3 |
| ⬜ | `T1195.001` | ↳ Compromise Software Dependencies and Development Tools | 0 | — |
| ⬜ | `T1195.002` | ↳ Compromise Software Supply Chain | 0 | — |
| ⬜ | `T1195.003` | ↳ Compromise Hardware Supply Chain | 0 | — |
| ✅ | `T1199` | Trusted Relationship | 5 | — |
| ✅ | `T1200` | Hardware Additions | 2 | — |
| ✅ | `T1566` | Phishing | 31 | 1/4 |
| ✅ | `T1566.001` | ↳ Spearphishing Attachment | 18 | — |
| ⬜ | `T1566.002` | ↳ Spearphishing Link | 0 | — |
| ⬜ | `T1566.003` | ↳ Spearphishing via Service | 0 | — |
| ⬜ | `T1566.004` | ↳ Spearphishing Voice | 0 | — |
| ⬜ | `T1659` | Content Injection | 0 | — |
| ⬜ | `T1669` | Wi-Fi Networks | 0 | — |

### Execution (TA0002)
Coverage: **9/17** (52.9%)

| Status | ID | Name | Rules | Sub-techs |
|--------|----|------|-------|-----------|
| ✅ | `T1047` | Windows Management Instrumentation | 36 | — |
| ✅ | `T1053` | Scheduled Task/Job | 6 | 3/5 |
| ✅ | `T1053.002` | ↳ At | 4 | — |
| ✅ | `T1053.003` | ↳ Cron | 8 | — |
| ✅ | `T1053.005` | ↳ Scheduled Task | 30 | — |
| ⬜ | `T1053.006` | ↳ Systemd Timers | 0 | — |
| ⬜ | `T1053.007` | ↳ Container Orchestration Job | 0 | — |
| ✅ | `T1059` | Command and Scripting Interpreter | 69 | 7/13 |
| ✅ | `T1059.001` | ↳ PowerShell | 179 | — |
| ⬜ | `T1059.002` | ↳ AppleScript | 0 | — |
| ✅ | `T1059.003` | ↳ Windows Command Shell | 30 | — |
| ✅ | `T1059.004` | ↳ Unix Shell | 15 | — |
| ✅ | `T1059.005` | ↳ Visual Basic | 14 | — |
| ✅ | `T1059.006` | ↳ Python | 4 | — |
| ✅ | `T1059.007` | ↳ JavaScript | 10 | — |
| ⬜ | `T1059.008` | ↳ Network Device CLI | 0 | — |
| ✅ | `T1059.009` | ↳ Cloud API | 3 | — |
| ⬜ | `T1059.010` | ↳ AutoHotKey & AutoIT | 0 | — |
| ⬜ | `T1059.011` | ↳ Lua | 0 | — |
| ⬜ | `T1059.012` | ↳ Hypervisor CLI | 0 | — |
| ⬜ | `T1059.013` | ↳ Container CLI/API | 0 | — |
| ✅ | `T1072` | Software Deployment Tools | 3 | — |
| ✅ | `T1106` | Native API | 13 | — |
| ⬜ | `T1129` | Shared Modules | 0 | — |
| ✅ | `T1203` | Exploitation for Client Execution | 23 | — |
| ✅ | `T1204` | User Execution | 4 | 2/5 |
| ✅ | `T1204.001` | ↳ Malicious Link | 6 | — |
| ✅ | `T1204.002` | ↳ Malicious File | 55 | — |
| ⬜ | `T1204.003` | ↳ Malicious Image | 0 | — |
| ⬜ | `T1204.004` | ↳ Malicious Copy and Paste | 0 | — |
| ⬜ | `T1204.005` | ↳ Malicious Library | 0 | — |
| ✅ | `T1559` | Inter-Process Communication | 1 | 1/3 |
| ✅ | `T1559.001` | ↳ Component Object Model | 1 | — |
| ⬜ | `T1559.002` | ↳ Dynamic Data Exchange | 0 | — |
| ⬜ | `T1559.003` | ↳ XPC Services | 0 | — |
| ✅ | `T1569` | System Services | 4 | 1/3 |
| ⬜ | `T1569.001` | ↳ Launchctl | 0 | — |
| ✅ | `T1569.002` | ↳ Service Execution | 16 | — |
| ⬜ | `T1569.003` | ↳ Systemctl | 0 | — |
| ⬜ | `T1609` | Container Administration Command | 0 | — |
| ⬜ | `T1610` | Deploy Container | 0 | — |
| ⬜ | `T1648` | Serverless Execution | 0 | — |
| ⬜ | `T1651` | Cloud Administration Command | 0 | — |
| ⬜ | `T1674` | Input Injection | 0 | — |
| ⬜ | `T1675` | ESXi Administration Command | 0 | — |
| ⬜ | `T1677` | Poisoned Pipeline Execution | 0 | — |

### Persistence (TA0003)
Coverage: **15/23** (65.2%)

| Status | ID | Name | Rules | Sub-techs |
|--------|----|------|-------|-----------|
| 🟡 | `T1037` | Boot or Logon Initialization Scripts | 0 | 1/5 |
| ✅ | `T1037.001` | ↳ Logon Script (Windows) | 2 | — |
| ⬜ | `T1037.002` | ↳ Login Hook | 0 | — |
| ⬜ | `T1037.003` | ↳ Network Logon Script | 0 | — |
| ⬜ | `T1037.004` | ↳ RC Scripts | 0 | — |
| ⬜ | `T1037.005` | ↳ Startup Items | 0 | — |
| ✅ | `T1053` | Scheduled Task/Job | 6 | 3/5 |
| ✅ | `T1053.002` | ↳ At | 4 | — |
| ✅ | `T1053.003` | ↳ Cron | 8 | — |
| ✅ | `T1053.005` | ↳ Scheduled Task | 30 | — |
| ⬜ | `T1053.006` | ↳ Systemd Timers | 0 | — |
| ⬜ | `T1053.007` | ↳ Container Orchestration Job | 0 | — |
| ✅ | `T1078` | Valid Accounts | 23 | 4/4 |
| ✅ | `T1078.001` | ↳ Default Accounts | 1 | — |
| ✅ | `T1078.002` | ↳ Domain Accounts | 1 | — |
| ✅ | `T1078.003` | ↳ Local Accounts | 2 | — |
| ✅ | `T1078.004` | ↳ Cloud Accounts | 4 | — |
| ✅ | `T1098` | Account Manipulation | 20 | 0/7 |
| ⬜ | `T1098.001` | ↳ Additional Cloud Credentials | 0 | — |
| ⬜ | `T1098.002` | ↳ Additional Email Delegate Permissions | 0 | — |
| ⬜ | `T1098.003` | ↳ Additional Cloud Roles | 0 | — |
| ⬜ | `T1098.004` | ↳ SSH Authorized Keys | 0 | — |
| ⬜ | `T1098.005` | ↳ Device Registration | 0 | — |
| ⬜ | `T1098.006` | ↳ Additional Container Cluster Roles | 0 | — |
| ⬜ | `T1098.007` | ↳ Additional Local or Domain Groups | 0 | — |
| ✅ | `T1112` | Modify Registry | 21 | — |
| ✅ | `T1133` | External Remote Services | 8 | — |
| ✅ | `T1136` | Create Account | 2 | 3/3 |
| ✅ | `T1136.001` | ↳ Local Account | 18 | — |
| ✅ | `T1136.002` | ↳ Domain Account | 2 | — |
| ✅ | `T1136.003` | ↳ Cloud Account | 11 | — |
| 🟡 | `T1137` | Office Application Startup | 0 | 1/6 |
| ⬜ | `T1137.001` | ↳ Office Template Macros | 0 | — |
| ⬜ | `T1137.002` | ↳ Office Test | 0 | — |
| ⬜ | `T1137.003` | ↳ Outlook Forms | 0 | — |
| ⬜ | `T1137.004` | ↳ Outlook Home Page | 0 | — |
| ⬜ | `T1137.005` | ↳ Outlook Rules | 0 | — |
| ✅ | `T1137.006` | ↳ Add-ins | 1 | — |
| ✅ | `T1176` | Software Extensions | 2 | 0/2 |
| ⬜ | `T1176.001` | ↳ Browser Extensions | 0 | — |
| ⬜ | `T1176.002` | ↳ IDE Extensions | 0 | — |
| ✅ | `T1197` | BITS Jobs | 26 | — |
| ⬜ | `T1205` | Traffic Signaling | 0 | 0/2 |
| ⬜ | `T1205.001` | ↳ Port Knocking | 0 | — |
| ⬜ | `T1205.002` | ↳ Socket Filters | 0 | — |
| 🟡 | `T1505` | Server Software Component | 0 | 5/6 |
| ✅ | `T1505.001` | ↳ SQL Stored Procedures | 1 | — |
| ✅ | `T1505.002` | ↳ Transport Agent | 1 | — |
| ✅ | `T1505.003` | ↳ Web Shell | 11 | — |
| ✅ | `T1505.004` | ↳ IIS Components | 1 | — |
| ✅ | `T1505.005` | ↳ Terminal Services DLL | 1 | — |
| ⬜ | `T1505.006` | ↳ vSphere Installation Bundles | 0 | — |
| ✅ | `T1525` | Implant Internal Image | 1 | — |
| 🟡 | `T1542` | Pre-OS Boot | 0 | 2/5 |
| ✅ | `T1542.001` | ↳ System Firmware | 1 | — |
| ⬜ | `T1542.002` | ↳ Component Firmware | 0 | — |
| ✅ | `T1542.003` | ↳ Bootkit | 1 | — |
| ⬜ | `T1542.004` | ↳ ROMMONkit | 0 | — |
| ⬜ | `T1542.005` | ↳ TFTP Boot | 0 | — |
| ✅ | `T1543` | Create or Modify System Process | 3 | 2/5 |
| ⬜ | `T1543.001` | ↳ Launch Agent | 0 | — |
| ✅ | `T1543.002` | ↳ Systemd Service | 2 | — |
| ✅ | `T1543.003` | ↳ Windows Service | 19 | — |
| ⬜ | `T1543.004` | ↳ Launch Daemon | 0 | — |
| ⬜ | `T1543.005` | ↳ Container Service | 0 | — |
| ✅ | `T1546` | Event Triggered Execution | 5 | 9/18 |
| ✅ | `T1546.001` | ↳ Change Default File Association | 2 | — |
| ✅ | `T1546.002` | ↳ Screensaver | 1 | — |
| ✅ | `T1546.003` | ↳ Windows Management Instrumentation Event Subscription | 7 | — |
| ✅ | `T1546.004` | ↳ Unix Shell Configuration Modification | 1 | — |
| ⬜ | `T1546.005` | ↳ Trap | 0 | — |
| ⬜ | `T1546.006` | ↳ LC_LOAD_DYLIB Addition | 0 | — |
| ✅ | `T1546.007` | ↳ Netsh Helper DLL | 2 | — |
| ✅ | `T1546.008` | ↳ Accessibility Features | 7 | — |
| ⬜ | `T1546.009` | ↳ AppCert DLLs | 0 | — |
| ⬜ | `T1546.010` | ↳ AppInit DLLs | 0 | — |
| ✅ | `T1546.011` | ↳ Application Shimming | 2 | — |
| ⬜ | `T1546.012` | ↳ Image File Execution Options Injection | 0 | — |
| ✅ | `T1546.013` | ↳ PowerShell Profile | 1 | — |
| ⬜ | `T1546.014` | ↳ Emond | 0 | — |
| ✅ | `T1546.015` | ↳ Component Object Model Hijacking | 3 | — |
| ⬜ | `T1546.016` | ↳ Installer Packages | 0 | — |
| ⬜ | `T1546.017` | ↳ Udev Rules | 0 | — |
| ⬜ | `T1546.018` | ↳ Python Startup Hooks | 0 | — |
| ✅ | `T1547` | Boot or Logon Autostart Execution | 2 | 7/14 |
| ✅ | `T1547.001` | ↳ Registry Run Keys / Startup Folder | 7 | — |
| ✅ | `T1547.002` | ↳ Authentication Package | 1 | — |
| ⬜ | `T1547.003` | ↳ Time Providers | 0 | — |
| ✅ | `T1547.004` | ↳ Winlogon Helper DLL | 1 | — |
| ⬜ | `T1547.005` | ↳ Security Support Provider | 0 | — |
| ✅ | `T1547.006` | ↳ Kernel Modules and Extensions | 1 | — |
| ⬜ | `T1547.007` | ↳ Re-opened Applications | 0 | — |
| ⬜ | `T1547.008` | ↳ LSASS Driver | 0 | — |
| ✅ | `T1547.009` | ↳ Shortcut Modification | 1 | — |
| ✅ | `T1547.010` | ↳ Port Monitors | 1 | — |
| ⬜ | `T1547.012` | ↳ Print Processors | 0 | — |
| ⬜ | `T1547.013` | ↳ XDG Autostart Entries | 0 | — |
| ✅ | `T1547.014` | ↳ Active Setup | 1 | — |
| ⬜ | `T1547.015` | ↳ Login Items | 0 | — |
| ✅ | `T1554` | Compromise Host Software Binary | 1 | — |
| ✅ | `T1556` | Modify Authentication Process | 7 | 1/9 |
| ⬜ | `T1556.001` | ↳ Domain Controller Authentication | 0 | — |
| ✅ | `T1556.002` | ↳ Password Filter DLL | 3 | — |
| ⬜ | `T1556.003` | ↳ Pluggable Authentication Modules | 0 | — |
| ⬜ | `T1556.004` | ↳ Network Device Authentication | 0 | — |
| ⬜ | `T1556.005` | ↳ Reversible Encryption | 0 | — |
| ⬜ | `T1556.006` | ↳ Multi-Factor Authentication | 0 | — |
| ⬜ | `T1556.007` | ↳ Hybrid Identity | 0 | — |
| ⬜ | `T1556.008` | ↳ Network Provider DLL | 0 | — |
| ⬜ | `T1556.009` | ↳ Conditional Access Policies | 0 | — |
| ✅ | `T1574` | Hijack Execution Flow | 5 | 7/12 |
| ✅ | `T1574.001` | ↳ DLL | 4 | — |
| ⬜ | `T1574.004` | ↳ Dylib Hijacking | 0 | — |
| ✅ | `T1574.005` | ↳ Executable Installer File Permissions Weakness | 1 | — |
| ✅ | `T1574.006` | ↳ Dynamic Linker Hijacking | 3 | — |
| ✅ | `T1574.007` | ↳ Path Interception by PATH Environment Variable | 1 | — |
| ✅ | `T1574.008` | ↳ Path Interception by Search Order Hijacking | 1 | — |
| ⬜ | `T1574.009` | ↳ Path Interception by Unquoted Path | 0 | — |
| ⬜ | `T1574.010` | ↳ Services File Permissions Weakness | 0 | — |
| ✅ | `T1574.011` | ↳ Services Registry Permissions Weakness | 11 | — |
| ✅ | `T1574.012` | ↳ COR_PROFILER | 1 | — |
| ⬜ | `T1574.013` | ↳ KernelCallbackTable | 0 | — |
| ⬜ | `T1574.014` | ↳ AppDomainManager | 0 | — |
| ⬜ | `T1653` | Power Settings | 0 | — |
| ⬜ | `T1668` | Exclusive Control | 0 | — |
| ⬜ | `T1671` | Cloud Application Integration | 0 | — |

### Privilege Escalation (TA0004)
Coverage: **11/14** (78.6%)

| Status | ID | Name | Rules | Sub-techs |
|--------|----|------|-------|-----------|
| 🟡 | `T1037` | Boot or Logon Initialization Scripts | 0 | 1/5 |
| ✅ | `T1037.001` | ↳ Logon Script (Windows) | 2 | — |
| ⬜ | `T1037.002` | ↳ Login Hook | 0 | — |
| ⬜ | `T1037.003` | ↳ Network Logon Script | 0 | — |
| ⬜ | `T1037.004` | ↳ RC Scripts | 0 | — |
| ⬜ | `T1037.005` | ↳ Startup Items | 0 | — |
| ✅ | `T1053` | Scheduled Task/Job | 6 | 3/5 |
| ✅ | `T1053.002` | ↳ At | 4 | — |
| ✅ | `T1053.003` | ↳ Cron | 8 | — |
| ✅ | `T1053.005` | ↳ Scheduled Task | 30 | — |
| ⬜ | `T1053.006` | ↳ Systemd Timers | 0 | — |
| ⬜ | `T1053.007` | ↳ Container Orchestration Job | 0 | — |
| ✅ | `T1055` | Process Injection | 15 | 4/12 |
| ✅ | `T1055.001` | ↳ Dynamic-link Library Injection | 6 | — |
| ⬜ | `T1055.002` | ↳ Portable Executable Injection | 0 | — |
| ✅ | `T1055.003` | ↳ Thread Execution Hijacking | 1 | — |
| ⬜ | `T1055.004` | ↳ Asynchronous Procedure Call | 0 | — |
| ⬜ | `T1055.005` | ↳ Thread Local Storage | 0 | — |
| ⬜ | `T1055.008` | ↳ Ptrace System Calls | 0 | — |
| ✅ | `T1055.009` | ↳ Proc Memory | 1 | — |
| ⬜ | `T1055.011` | ↳ Extra Window Memory Injection | 0 | — |
| ✅ | `T1055.012` | ↳ Process Hollowing | 2 | — |
| ⬜ | `T1055.013` | ↳ Process Doppelgänging | 0 | — |
| ⬜ | `T1055.014` | ↳ VDSO Hijacking | 0 | — |
| ⬜ | `T1055.015` | ↳ ListPlanting | 0 | — |
| ✅ | `T1068` | Exploitation for Privilege Escalation | 19 | — |
| ✅ | `T1078` | Valid Accounts | 23 | 4/4 |
| ✅ | `T1078.001` | ↳ Default Accounts | 1 | — |
| ✅ | `T1078.002` | ↳ Domain Accounts | 1 | — |
| ✅ | `T1078.003` | ↳ Local Accounts | 2 | — |
| ✅ | `T1078.004` | ↳ Cloud Accounts | 4 | — |
| ✅ | `T1098` | Account Manipulation | 20 | 0/7 |
| ⬜ | `T1098.001` | ↳ Additional Cloud Credentials | 0 | — |
| ⬜ | `T1098.002` | ↳ Additional Email Delegate Permissions | 0 | — |
| ⬜ | `T1098.003` | ↳ Additional Cloud Roles | 0 | — |
| ⬜ | `T1098.004` | ↳ SSH Authorized Keys | 0 | — |
| ⬜ | `T1098.005` | ↳ Device Registration | 0 | — |
| ⬜ | `T1098.006` | ↳ Additional Container Cluster Roles | 0 | — |
| ⬜ | `T1098.007` | ↳ Additional Local or Domain Groups | 0 | — |
| ✅ | `T1134` | Access Token Manipulation | 2 | 5/5 |
| ✅ | `T1134.001` | ↳ Token Impersonation/Theft | 6 | — |
| ✅ | `T1134.002` | ↳ Create Process with Token | 5 | — |
| ✅ | `T1134.003` | ↳ Make and Impersonate Token | 2 | — |
| ✅ | `T1134.004` | ↳ Parent PID Spoofing | 1 | — |
| ✅ | `T1134.005` | ↳ SID-History Injection | 1 | — |
| 🟡 | `T1484` | Domain or Tenant Policy Modification | 0 | 1/2 |
| ✅ | `T1484.001` | ↳ Group Policy Modification | 2 | — |
| ⬜ | `T1484.002` | ↳ Trust Modification | 0 | — |
| ✅ | `T1543` | Create or Modify System Process | 3 | 2/5 |
| ⬜ | `T1543.001` | ↳ Launch Agent | 0 | — |
| ✅ | `T1543.002` | ↳ Systemd Service | 2 | — |
| ✅ | `T1543.003` | ↳ Windows Service | 19 | — |
| ⬜ | `T1543.004` | ↳ Launch Daemon | 0 | — |
| ⬜ | `T1543.005` | ↳ Container Service | 0 | — |
| ✅ | `T1546` | Event Triggered Execution | 5 | 9/18 |
| ✅ | `T1546.001` | ↳ Change Default File Association | 2 | — |
| ✅ | `T1546.002` | ↳ Screensaver | 1 | — |
| ✅ | `T1546.003` | ↳ Windows Management Instrumentation Event Subscription | 7 | — |
| ✅ | `T1546.004` | ↳ Unix Shell Configuration Modification | 1 | — |
| ⬜ | `T1546.005` | ↳ Trap | 0 | — |
| ⬜ | `T1546.006` | ↳ LC_LOAD_DYLIB Addition | 0 | — |
| ✅ | `T1546.007` | ↳ Netsh Helper DLL | 2 | — |
| ✅ | `T1546.008` | ↳ Accessibility Features | 7 | — |
| ⬜ | `T1546.009` | ↳ AppCert DLLs | 0 | — |
| ⬜ | `T1546.010` | ↳ AppInit DLLs | 0 | — |
| ✅ | `T1546.011` | ↳ Application Shimming | 2 | — |
| ⬜ | `T1546.012` | ↳ Image File Execution Options Injection | 0 | — |
| ✅ | `T1546.013` | ↳ PowerShell Profile | 1 | — |
| ⬜ | `T1546.014` | ↳ Emond | 0 | — |
| ✅ | `T1546.015` | ↳ Component Object Model Hijacking | 3 | — |
| ⬜ | `T1546.016` | ↳ Installer Packages | 0 | — |
| ⬜ | `T1546.017` | ↳ Udev Rules | 0 | — |
| ⬜ | `T1546.018` | ↳ Python Startup Hooks | 0 | — |
| ✅ | `T1547` | Boot or Logon Autostart Execution | 2 | 7/14 |
| ✅ | `T1547.001` | ↳ Registry Run Keys / Startup Folder | 7 | — |
| ✅ | `T1547.002` | ↳ Authentication Package | 1 | — |
| ⬜ | `T1547.003` | ↳ Time Providers | 0 | — |
| ✅ | `T1547.004` | ↳ Winlogon Helper DLL | 1 | — |
| ⬜ | `T1547.005` | ↳ Security Support Provider | 0 | — |
| ✅ | `T1547.006` | ↳ Kernel Modules and Extensions | 1 | — |
| ⬜ | `T1547.007` | ↳ Re-opened Applications | 0 | — |
| ⬜ | `T1547.008` | ↳ LSASS Driver | 0 | — |
| ✅ | `T1547.009` | ↳ Shortcut Modification | 1 | — |
| ✅ | `T1547.010` | ↳ Port Monitors | 1 | — |
| ⬜ | `T1547.012` | ↳ Print Processors | 0 | — |
| ⬜ | `T1547.013` | ↳ XDG Autostart Entries | 0 | — |
| ✅ | `T1547.014` | ↳ Active Setup | 1 | — |
| ⬜ | `T1547.015` | ↳ Login Items | 0 | — |
| ✅ | `T1548` | Abuse Elevation Control Mechanism | 11 | 3/6 |
| ✅ | `T1548.001` | ↳ Setuid and Setgid | 1 | — |
| ✅ | `T1548.002` | ↳ Bypass User Account Control | 33 | — |
| ✅ | `T1548.003` | ↳ Sudo and Sudo Caching | 3 | — |
| ⬜ | `T1548.004` | ↳ Elevated Execution with Prompt | 0 | — |
| ⬜ | `T1548.005` | ↳ Temporary Elevated Cloud Access | 0 | — |
| ⬜ | `T1548.006` | ↳ TCC Manipulation | 0 | — |
| ✅ | `T1574` | Hijack Execution Flow | 5 | 7/12 |
| ✅ | `T1574.001` | ↳ DLL | 4 | — |
| ⬜ | `T1574.004` | ↳ Dylib Hijacking | 0 | — |
| ✅ | `T1574.005` | ↳ Executable Installer File Permissions Weakness | 1 | — |
| ✅ | `T1574.006` | ↳ Dynamic Linker Hijacking | 3 | — |
| ✅ | `T1574.007` | ↳ Path Interception by PATH Environment Variable | 1 | — |
| ✅ | `T1574.008` | ↳ Path Interception by Search Order Hijacking | 1 | — |
| ⬜ | `T1574.009` | ↳ Path Interception by Unquoted Path | 0 | — |
| ⬜ | `T1574.010` | ↳ Services File Permissions Weakness | 0 | — |
| ✅ | `T1574.011` | ↳ Services Registry Permissions Weakness | 11 | — |
| ✅ | `T1574.012` | ↳ COR_PROFILER | 1 | — |
| ⬜ | `T1574.013` | ↳ KernelCallbackTable | 0 | — |
| ⬜ | `T1574.014` | ↳ AppDomainManager | 0 | — |
| ⬜ | `T1611` | Escape to Host | 0 | — |

### Defense Evasion (TA0005)
Coverage: **27/47** (57.4%)

| Status | ID | Name | Rules | Sub-techs |
|--------|----|------|-------|-----------|
| ⬜ | `T1006` | Direct Volume Access | 0 | — |
| ✅ | `T1014` | Rootkit | 1 | — |
| ✅ | `T1027` | Obfuscated Files or Information | 76 | 7/17 |
| ✅ | `T1027.001` | ↳ Binary Padding | 3 | — |
| ⬜ | `T1027.002` | ↳ Software Packing | 0 | — |
| ✅ | `T1027.003` | ↳ Steganography | 5 | — |
| ✅ | `T1027.004` | ↳ Compile After Delivery | 5 | — |
| ✅ | `T1027.005` | ↳ Indicator Removal from Tools | 4 | — |
| ⬜ | `T1027.006` | ↳ HTML Smuggling | 0 | — |
| ⬜ | `T1027.007` | ↳ Dynamic API Resolution | 0 | — |
| ⬜ | `T1027.008` | ↳ Stripped Payloads | 0 | — |
| ✅ | `T1027.009` | ↳ Embedded Payloads | 2 | — |
| ✅ | `T1027.010` | ↳ Command Obfuscation | 2 | — |
| ⬜ | `T1027.011` | ↳ Fileless Storage | 0 | — |
| ⬜ | `T1027.012` | ↳ LNK Icon Smuggling | 0 | — |
| ✅ | `T1027.013` | ↳ Encrypted/Encoded File | 1 | — |
| ⬜ | `T1027.014` | ↳ Polymorphic Code | 0 | — |
| ⬜ | `T1027.015` | ↳ Compression | 0 | — |
| ⬜ | `T1027.016` | ↳ Junk Code Insertion | 0 | — |
| ⬜ | `T1027.017` | ↳ SVG Smuggling | 0 | — |
| ✅ | `T1036` | Masquerading | 39 | 5/12 |
| ⬜ | `T1036.001` | ↳ Invalid Code Signature | 0 | — |
| ✅ | `T1036.002` | ↳ Right-to-Left Override | 2 | — |
| ✅ | `T1036.003` | ↳ Rename Legitimate Utilities | 21 | — |
| ⬜ | `T1036.004` | ↳ Masquerade Task or Service | 0 | — |
| ✅ | `T1036.005` | ↳ Match Legitimate Resource Name or Location | 16 | — |
| ⬜ | `T1036.006` | ↳ Space after Filename | 0 | — |
| ✅ | `T1036.007` | ↳ Double File Extension | 1 | — |
| ✅ | `T1036.008` | ↳ Masquerade File Type | 1 | — |
| ⬜ | `T1036.009` | ↳ Break Process Trees | 0 | — |
| ⬜ | `T1036.010` | ↳ Masquerade Account Name | 0 | — |
| ⬜ | `T1036.011` | ↳ Overwrite Process Arguments | 0 | — |
| ⬜ | `T1036.012` | ↳ Browser Fingerprint | 0 | — |
| ✅ | `T1055` | Process Injection | 15 | 4/12 |
| ✅ | `T1055.001` | ↳ Dynamic-link Library Injection | 6 | — |
| ⬜ | `T1055.002` | ↳ Portable Executable Injection | 0 | — |
| ✅ | `T1055.003` | ↳ Thread Execution Hijacking | 1 | — |
| ⬜ | `T1055.004` | ↳ Asynchronous Procedure Call | 0 | — |
| ⬜ | `T1055.005` | ↳ Thread Local Storage | 0 | — |
| ⬜ | `T1055.008` | ↳ Ptrace System Calls | 0 | — |
| ✅ | `T1055.009` | ↳ Proc Memory | 1 | — |
| ⬜ | `T1055.011` | ↳ Extra Window Memory Injection | 0 | — |
| ✅ | `T1055.012` | ↳ Process Hollowing | 2 | — |
| ⬜ | `T1055.013` | ↳ Process Doppelgänging | 0 | — |
| ⬜ | `T1055.014` | ↳ VDSO Hijacking | 0 | — |
| ⬜ | `T1055.015` | ↳ ListPlanting | 0 | — |
| ✅ | `T1070` | Indicator Removal | 14 | 7/10 |
| ✅ | `T1070.001` | ↳ Clear Windows Event Logs | 4 | — |
| ✅ | `T1070.002` | ↳ Clear Linux or Mac System Logs | 3 | — |
| ✅ | `T1070.003` | ↳ Clear Command History | 7 | — |
| ✅ | `T1070.004` | ↳ File Deletion | 10 | — |
| ✅ | `T1070.005` | ↳ Network Share Connection Removal | 2 | — |
| ✅ | `T1070.006` | ↳ Timestomp | 8 | — |
| ⬜ | `T1070.007` | ↳ Clear Network Connection History and Configurations | 0 | — |
| ✅ | `T1070.008` | ↳ Clear Mailbox Data | 1 | — |
| ⬜ | `T1070.009` | ↳ Clear Persistence | 0 | — |
| ⬜ | `T1070.010` | ↳ Relocate Malware | 0 | — |
| ✅ | `T1078` | Valid Accounts | 23 | 4/4 |
| ✅ | `T1078.001` | ↳ Default Accounts | 1 | — |
| ✅ | `T1078.002` | ↳ Domain Accounts | 1 | — |
| ✅ | `T1078.003` | ↳ Local Accounts | 2 | — |
| ✅ | `T1078.004` | ↳ Cloud Accounts | 4 | — |
| ✅ | `T1112` | Modify Registry | 21 | — |
| ✅ | `T1127` | Trusted Developer Utilities Proxy Execution | 18 | 0/3 |
| ⬜ | `T1127.001` | ↳ MSBuild | 0 | — |
| ⬜ | `T1127.002` | ↳ ClickOnce | 0 | — |
| ⬜ | `T1127.003` | ↳ JamPlus | 0 | — |
| ✅ | `T1134` | Access Token Manipulation | 2 | 5/5 |
| ✅ | `T1134.001` | ↳ Token Impersonation/Theft | 6 | — |
| ✅ | `T1134.002` | ↳ Create Process with Token | 5 | — |
| ✅ | `T1134.003` | ↳ Make and Impersonate Token | 2 | — |
| ✅ | `T1134.004` | ↳ Parent PID Spoofing | 1 | — |
| ✅ | `T1134.005` | ↳ SID-History Injection | 1 | — |
| ✅ | `T1140` | Deobfuscate/Decode Files or Information | 14 | — |
| ✅ | `T1197` | BITS Jobs | 26 | — |
| ✅ | `T1202` | Indirect Command Execution | 35 | — |
| ⬜ | `T1205` | Traffic Signaling | 0 | 0/2 |
| ⬜ | `T1205.001` | ↳ Port Knocking | 0 | — |
| ⬜ | `T1205.002` | ↳ Socket Filters | 0 | — |
| ✅ | `T1207` | Rogue Domain Controller | 2 | — |
| ✅ | `T1211` | Exploitation for Defense Evasion | 1 | — |
| ✅ | `T1216` | System Script Proxy Execution | 12 | 1/2 |
| ✅ | `T1216.001` | ↳ PubPrn | 2 | — |
| ⬜ | `T1216.002` | ↳ SyncAppvPublishingServer | 0 | — |
| ✅ | `T1218` | System Binary Proxy Execution | 121 | 10/14 |
| ✅ | `T1218.001` | ↳ Compiled HTML File | 4 | — |
| ✅ | `T1218.002` | ↳ Control Panel | 1 | — |
| ✅ | `T1218.003` | ↳ CMSTP | 4 | — |
| ⬜ | `T1218.004` | ↳ InstallUtil | 0 | — |
| ✅ | `T1218.005` | ↳ Mshta | 6 | — |
| ✅ | `T1218.007` | ↳ Msiexec | 7 | — |
| ✅ | `T1218.008` | ↳ Odbcconf | 8 | — |
| ✅ | `T1218.009` | ↳ Regsvcs/Regasm | 2 | — |
| ✅ | `T1218.010` | ↳ Regsvr32 | 14 | — |
| ✅ | `T1218.011` | ↳ Rundll32 | 26 | — |
| ⬜ | `T1218.012` | ↳ Verclsid | 0 | — |
| ✅ | `T1218.013` | ↳ Mavinject | 2 | — |
| ⬜ | `T1218.014` | ↳ MMC | 0 | — |
| ⬜ | `T1218.015` | ↳ Electron Applications | 0 | — |
| ✅ | `T1220` | XSL Script Processing | 4 | — |
| ⬜ | `T1221` | Template Injection | 0 | — |
| ✅ | `T1222` | File and Directory Permissions Modification | 2 | 2/2 |
| ✅ | `T1222.001` | ↳ Windows File and Directory Permissions Modification | 3 | — |
| ✅ | `T1222.002` | ↳ Linux and Mac File and Directory Permissions Modification | 6 | — |
| ⬜ | `T1480` | Execution Guardrails | 0 | 0/2 |
| ⬜ | `T1480.001` | ↳ Environmental Keying | 0 | — |
| ⬜ | `T1480.002` | ↳ Mutual Exclusion | 0 | — |
| 🟡 | `T1484` | Domain or Tenant Policy Modification | 0 | 1/2 |
| ✅ | `T1484.001` | ↳ Group Policy Modification | 2 | — |
| ⬜ | `T1484.002` | ↳ Trust Modification | 0 | — |
| 🟡 | `T1497` | Virtualization/Sandbox Evasion | 0 | 1/3 |
| ✅ | `T1497.001` | ↳ System Checks | 1 | — |
| ⬜ | `T1497.002` | ↳ User Activity Based Checks | 0 | — |
| ⬜ | `T1497.003` | ↳ Time Based Checks | 0 | — |
| ⬜ | `T1535` | Unused/Unsupported Cloud Regions | 0 | — |
| 🟡 | `T1542` | Pre-OS Boot | 0 | 2/5 |
| ✅ | `T1542.001` | ↳ System Firmware | 1 | — |
| ⬜ | `T1542.002` | ↳ Component Firmware | 0 | — |
| ✅ | `T1542.003` | ↳ Bootkit | 1 | — |
| ⬜ | `T1542.004` | ↳ ROMMONkit | 0 | — |
| ⬜ | `T1542.005` | ↳ TFTP Boot | 0 | — |
| ✅ | `T1548` | Abuse Elevation Control Mechanism | 11 | 3/6 |
| ✅ | `T1548.001` | ↳ Setuid and Setgid | 1 | — |
| ✅ | `T1548.002` | ↳ Bypass User Account Control | 33 | — |
| ✅ | `T1548.003` | ↳ Sudo and Sudo Caching | 3 | — |
| ⬜ | `T1548.004` | ↳ Elevated Execution with Prompt | 0 | — |
| ⬜ | `T1548.005` | ↳ Temporary Elevated Cloud Access | 0 | — |
| ⬜ | `T1548.006` | ↳ TCC Manipulation | 0 | — |
| ✅ | `T1550` | Use Alternate Authentication Material | 4 | 3/4 |
| ✅ | `T1550.001` | ↳ Application Access Token | 4 | — |
| ✅ | `T1550.002` | ↳ Pass the Hash | 7 | — |
| ✅ | `T1550.003` | ↳ Pass the Ticket | 3 | — |
| ⬜ | `T1550.004` | ↳ Web Session Cookie | 0 | — |
| ✅ | `T1553` | Subvert Trust Controls | 1 | 3/6 |
| ⬜ | `T1553.001` | ↳ Gatekeeper Bypass | 0 | — |
| ✅ | `T1553.002` | ↳ Code Signing | 1 | — |
| ⬜ | `T1553.003` | ↳ SIP and Trust Provider Hijacking | 0 | — |
| ✅ | `T1553.004` | ↳ Install Root Certificate | 10 | — |
| ✅ | `T1553.005` | ↳ Mark-of-the-Web Bypass | 3 | — |
| ⬜ | `T1553.006` | ↳ Code Signing Policy Modification | 0 | — |
| ✅ | `T1556` | Modify Authentication Process | 7 | 1/9 |
| ⬜ | `T1556.001` | ↳ Domain Controller Authentication | 0 | — |
| ✅ | `T1556.002` | ↳ Password Filter DLL | 3 | — |
| ⬜ | `T1556.003` | ↳ Pluggable Authentication Modules | 0 | — |
| ⬜ | `T1556.004` | ↳ Network Device Authentication | 0 | — |
| ⬜ | `T1556.005` | ↳ Reversible Encryption | 0 | — |
| ⬜ | `T1556.006` | ↳ Multi-Factor Authentication | 0 | — |
| ⬜ | `T1556.007` | ↳ Hybrid Identity | 0 | — |
| ⬜ | `T1556.008` | ↳ Network Provider DLL | 0 | — |
| ⬜ | `T1556.009` | ↳ Conditional Access Policies | 0 | — |
| ✅ | `T1562` | Impair Defenses | 14 | 6/12 |
| ✅ | `T1562.001` | ↳ Disable or Modify Tools | 56 | — |
| ✅ | `T1562.002` | ↳ Disable Windows Event Logging | 16 | — |
| ✅ | `T1562.003` | ↳ Impair Command History Logging | 1 | — |
| ✅ | `T1562.004` | ↳ Disable or Modify System Firewall | 22 | — |
| ✅ | `T1562.006` | ↳ Indicator Blocking | 9 | — |
| ⬜ | `T1562.007` | ↳ Disable or Modify Cloud Firewall | 0 | — |
| ⬜ | `T1562.008` | ↳ Disable or Modify Cloud Logs | 0 | — |
| ⬜ | `T1562.009` | ↳ Safe Mode Boot | 0 | — |
| ✅ | `T1562.010` | ↳ Downgrade Attack | 1 | — |
| ⬜ | `T1562.011` | ↳ Spoof Security Alerting | 0 | — |
| ⬜ | `T1562.012` | ↳ Disable or Modify Linux Audit System | 0 | — |
| ⬜ | `T1562.013` | ↳ Disable or Modify Network Device Firewall | 0 | — |
| ✅ | `T1564` | Hide Artifacts | 7 | 5/14 |
| ✅ | `T1564.001` | ↳ Hidden Files and Directories | 7 | — |
| ✅ | `T1564.002` | ↳ Hidden Users | 2 | — |
| ✅ | `T1564.003` | ↳ Hidden Window | 3 | — |
| ✅ | `T1564.004` | ↳ NTFS File Attributes | 16 | — |
| ⬜ | `T1564.005` | ↳ Hidden File System | 0 | — |
| ✅ | `T1564.006` | ↳ Run Virtual Instance | 2 | — |
| ⬜ | `T1564.007` | ↳ VBA Stomping | 0 | — |
| ⬜ | `T1564.008` | ↳ Email Hiding Rules | 0 | — |
| ⬜ | `T1564.009` | ↳ Resource Forking | 0 | — |
| ⬜ | `T1564.010` | ↳ Process Argument Spoofing | 0 | — |
| ⬜ | `T1564.011` | ↳ Ignore Process Interrupts | 0 | — |
| ⬜ | `T1564.012` | ↳ File/Path Exclusions | 0 | — |
| ⬜ | `T1564.013` | ↳ Bind Mounts | 0 | — |
| ⬜ | `T1564.014` | ↳ Extended Attributes | 0 | — |
| ✅ | `T1574` | Hijack Execution Flow | 5 | 7/12 |
| ✅ | `T1574.001` | ↳ DLL | 4 | — |
| ⬜ | `T1574.004` | ↳ Dylib Hijacking | 0 | — |
| ✅ | `T1574.005` | ↳ Executable Installer File Permissions Weakness | 1 | — |
| ✅ | `T1574.006` | ↳ Dynamic Linker Hijacking | 3 | — |
| ✅ | `T1574.007` | ↳ Path Interception by PATH Environment Variable | 1 | — |
| ✅ | `T1574.008` | ↳ Path Interception by Search Order Hijacking | 1 | — |
| ⬜ | `T1574.009` | ↳ Path Interception by Unquoted Path | 0 | — |
| ⬜ | `T1574.010` | ↳ Services File Permissions Weakness | 0 | — |
| ✅ | `T1574.011` | ↳ Services Registry Permissions Weakness | 11 | — |
| ✅ | `T1574.012` | ↳ COR_PROFILER | 1 | — |
| ⬜ | `T1574.013` | ↳ KernelCallbackTable | 0 | — |
| ⬜ | `T1574.014` | ↳ AppDomainManager | 0 | — |
| ⬜ | `T1578` | Modify Cloud Compute Infrastructure | 0 | 0/5 |
| ⬜ | `T1578.001` | ↳ Create Snapshot | 0 | — |
| ⬜ | `T1578.002` | ↳ Create Cloud Instance | 0 | — |
| ⬜ | `T1578.003` | ↳ Delete Cloud Instance | 0 | — |
| ⬜ | `T1578.004` | ↳ Revert Cloud Instance | 0 | — |
| ⬜ | `T1578.005` | ↳ Modify Cloud Compute Configurations | 0 | — |
| ⬜ | `T1599` | Network Boundary Bridging | 0 | 0/1 |
| ⬜ | `T1599.001` | ↳ Network Address Translation Traversal | 0 | — |
| ⬜ | `T1600` | Weaken Encryption | 0 | 0/2 |
| ⬜ | `T1600.001` | ↳ Reduce Key Space | 0 | — |
| ⬜ | `T1600.002` | ↳ Disable Crypto Hardware | 0 | — |
| ⬜ | `T1601` | Modify System Image | 0 | 0/2 |
| ⬜ | `T1601.001` | ↳ Patch System Image | 0 | — |
| ⬜ | `T1601.002` | ↳ Downgrade System Image | 0 | — |
| ⬜ | `T1610` | Deploy Container | 0 | — |
| ⬜ | `T1612` | Build Image on Host | 0 | — |
| ✅ | `T1620` | Reflective Code Loading | 2 | — |
| ✅ | `T1622` | Debugger Evasion | 1 | — |
| ⬜ | `T1647` | Plist File Modification | 0 | — |
| ⬜ | `T1656` | Impersonation | 0 | — |
| ⬜ | `T1666` | Modify Cloud Resource Hierarchy | 0 | — |
| ⬜ | `T1672` | Email Spoofing | 0 | — |
| ⬜ | `T1678` | Delay Execution | 0 | — |
| ⬜ | `T1679` | Selective Exclusion | 0 | — |

### Credential Access (TA0006)
Coverage: **15/17** (88.2%)

| Status | ID | Name | Rules | Sub-techs |
|--------|----|------|-------|-----------|
| ✅ | `T1003` | OS Credential Dumping | 31 | 6/8 |
| ✅ | `T1003.001` | ↳ LSASS Memory | 47 | — |
| ✅ | `T1003.002` | ↳ Security Account Manager | 12 | — |
| ✅ | `T1003.003` | ↳ NTDS | 14 | — |
| ✅ | `T1003.004` | ↳ LSA Secrets | 6 | — |
| ✅ | `T1003.005` | ↳ Cached Domain Credentials | 6 | — |
| ✅ | `T1003.006` | ↳ DCSync | 8 | — |
| ⬜ | `T1003.007` | ↳ Proc Filesystem | 0 | — |
| ⬜ | `T1003.008` | ↳ /etc/passwd and /etc/shadow | 0 | — |
| ✅ | `T1040` | Network Sniffing | 7 | — |
| ✅ | `T1056` | Input Capture | 4 | 2/4 |
| ✅ | `T1056.001` | ↳ Keylogging | 4 | — |
| ✅ | `T1056.002` | ↳ GUI Input Capture | 1 | — |
| ⬜ | `T1056.003` | ↳ Web Portal Capture | 0 | — |
| ⬜ | `T1056.004` | ↳ Credential API Hooking | 0 | — |
| ✅ | `T1110` | Brute Force | 14 | 3/4 |
| ✅ | `T1110.001` | ↳ Password Guessing | 2 | — |
| ✅ | `T1110.002` | ↳ Password Cracking | 1 | — |
| ✅ | `T1110.003` | ↳ Password Spraying | 1 | — |
| ⬜ | `T1110.004` | ↳ Credential Stuffing | 0 | — |
| ⬜ | `T1111` | Multi-Factor Authentication Interception | 0 | — |
| ✅ | `T1187` | Forced Authentication | 2 | — |
| ✅ | `T1212` | Exploitation for Credential Access | 3 | — |
| ✅ | `T1528` | Steal Application Access Token | 4 | — |
| ✅ | `T1539` | Steal Web Session Cookie | 2 | — |
| ✅ | `T1552` | Unsecured Credentials | 2 | 5/8 |
| ✅ | `T1552.001` | ↳ Credentials In Files | 13 | — |
| ✅ | `T1552.002` | ↳ Credentials in Registry | 3 | — |
| ✅ | `T1552.003` | ↳ Shell History | 2 | — |
| ✅ | `T1552.004` | ↳ Private Keys | 10 | — |
| ⬜ | `T1552.005` | ↳ Cloud Instance Metadata API | 0 | — |
| ✅ | `T1552.006` | ↳ Group Policy Preferences | 5 | — |
| ⬜ | `T1552.007` | ↳ Container API | 0 | — |
| ⬜ | `T1552.008` | ↳ Chat Messages | 0 | — |
| ✅ | `T1555` | Credentials from Password Stores | 6 | 2/6 |
| ⬜ | `T1555.001` | ↳ Keychain | 0 | — |
| ⬜ | `T1555.002` | ↳ Securityd Memory | 0 | — |
| ✅ | `T1555.003` | ↳ Credentials from Web Browsers | 6 | — |
| ✅ | `T1555.004` | ↳ Windows Credential Manager | 2 | — |
| ⬜ | `T1555.005` | ↳ Password Managers | 0 | — |
| ⬜ | `T1555.006` | ↳ Cloud Secrets Management Stores | 0 | — |
| ✅ | `T1556` | Modify Authentication Process | 7 | 1/9 |
| ⬜ | `T1556.001` | ↳ Domain Controller Authentication | 0 | — |
| ✅ | `T1556.002` | ↳ Password Filter DLL | 3 | — |
| ⬜ | `T1556.003` | ↳ Pluggable Authentication Modules | 0 | — |
| ⬜ | `T1556.004` | ↳ Network Device Authentication | 0 | — |
| ⬜ | `T1556.005` | ↳ Reversible Encryption | 0 | — |
| ⬜ | `T1556.006` | ↳ Multi-Factor Authentication | 0 | — |
| ⬜ | `T1556.007` | ↳ Hybrid Identity | 0 | — |
| ⬜ | `T1556.008` | ↳ Network Provider DLL | 0 | — |
| ⬜ | `T1556.009` | ↳ Conditional Access Policies | 0 | — |
| ✅ | `T1557` | Adversary-in-the-Middle | 1 | 1/4 |
| ✅ | `T1557.001` | ↳ LLMNR/NBT-NS Poisoning and SMB Relay | 4 | — |
| ⬜ | `T1557.002` | ↳ ARP Cache Poisoning | 0 | — |
| ⬜ | `T1557.003` | ↳ DHCP Spoofing | 0 | — |
| ⬜ | `T1557.004` | ↳ Evil Twin | 0 | — |
| ✅ | `T1558` | Steal or Forge Kerberos Tickets | 1 | 1/5 |
| ⬜ | `T1558.001` | ↳ Golden Ticket | 0 | — |
| ⬜ | `T1558.002` | ↳ Silver Ticket | 0 | — |
| ✅ | `T1558.003` | ↳ Kerberoasting | 11 | — |
| ⬜ | `T1558.004` | ↳ AS-REP Roasting | 0 | — |
| ⬜ | `T1558.005` | ↳ Ccache Files | 0 | — |
| ⬜ | `T1606` | Forge Web Credentials | 0 | 0/2 |
| ⬜ | `T1606.001` | ↳ Web Cookies | 0 | — |
| ⬜ | `T1606.002` | ↳ SAML Tokens | 0 | — |
| ✅ | `T1621` | Multi-Factor Authentication Request Generation | 3 | — |
| ✅ | `T1649` | Steal or Forge Authentication Certificates | 2 | — |

### Discovery (TA0007)
Coverage: **25/34** (73.5%)

| Status | ID | Name | Rules | Sub-techs |
|--------|----|------|-------|-----------|
| ✅ | `T1007` | System Service Discovery | 12 | — |
| ✅ | `T1010` | Application Window Discovery | 1 | — |
| ✅ | `T1012` | Query Registry | 11 | — |
| ✅ | `T1016` | System Network Configuration Discovery | 7 | 0/2 |
| ⬜ | `T1016.001` | ↳ Internet Connection Discovery | 0 | — |
| ⬜ | `T1016.002` | ↳ Wi-Fi Discovery | 0 | — |
| ✅ | `T1018` | Remote System Discovery | 13 | — |
| ✅ | `T1033` | System Owner/User Discovery | 29 | — |
| ✅ | `T1040` | Network Sniffing | 7 | — |
| ✅ | `T1046` | Network Service Discovery | 8 | — |
| ✅ | `T1049` | System Network Connections Discovery | 7 | — |
| ✅ | `T1057` | Process Discovery | 6 | — |
| ✅ | `T1069` | Permission Groups Discovery | 3 | 2/3 |
| ✅ | `T1069.001` | ↳ Local Groups | 14 | — |
| ✅ | `T1069.002` | ↳ Domain Groups | 11 | — |
| ⬜ | `T1069.003` | ↳ Cloud Groups | 0 | — |
| ✅ | `T1082` | System Information Discovery | 25 | — |
| ✅ | `T1083` | File and Directory Discovery | 20 | — |
| ✅ | `T1087` | Account Discovery | 13 | 2/4 |
| ✅ | `T1087.001` | ↳ Local Account | 10 | — |
| ✅ | `T1087.002` | ↳ Domain Account | 15 | — |
| ⬜ | `T1087.003` | ↳ Email Account | 0 | — |
| ⬜ | `T1087.004` | ↳ Cloud Account | 0 | — |
| ✅ | `T1120` | Peripheral Device Discovery | 2 | — |
| ✅ | `T1124` | System Time Discovery | 2 | — |
| ✅ | `T1135` | Network Share Discovery | 4 | — |
| ✅ | `T1201` | Password Policy Discovery | 5 | — |
| ✅ | `T1217` | Browser Information Discovery | 3 | — |
| ✅ | `T1482` | Domain Trust Discovery | 12 | — |
| 🟡 | `T1497` | Virtualization/Sandbox Evasion | 0 | 1/3 |
| ✅ | `T1497.001` | ↳ System Checks | 1 | — |
| ⬜ | `T1497.002` | ↳ User Activity Based Checks | 0 | — |
| ⬜ | `T1497.003` | ↳ Time Based Checks | 0 | — |
| ✅ | `T1518` | Software Discovery | 5 | 1/2 |
| ✅ | `T1518.001` | ↳ Security Software Discovery | 5 | — |
| ⬜ | `T1518.002` | ↳ Backup Software Discovery | 0 | — |
| ✅ | `T1526` | Cloud Service Discovery | 1 | — |
| ⬜ | `T1538` | Cloud Service Dashboard | 0 | — |
| ✅ | `T1580` | Cloud Infrastructure Discovery | 1 | — |
| ⬜ | `T1613` | Container and Resource Discovery | 0 | — |
| 🟡 | `T1614` | System Location Discovery | 0 | 1/1 |
| ✅ | `T1614.001` | ↳ System Language Discovery | 2 | — |
| ✅ | `T1615` | Group Policy Discovery | 6 | — |
| ⬜ | `T1619` | Cloud Storage Object Discovery | 0 | — |
| ✅ | `T1622` | Debugger Evasion | 1 | — |
| ⬜ | `T1652` | Device Driver Discovery | 0 | — |
| ⬜ | `T1654` | Log Enumeration | 0 | — |
| ⬜ | `T1673` | Virtual Machine Discovery | 0 | — |
| ⬜ | `T1680` | Local Storage Discovery | 0 | — |

### Lateral Movement (TA0008)
Coverage: **6/9** (66.7%)

| Status | ID | Name | Rules | Sub-techs |
|--------|----|------|-------|-----------|
| ✅ | `T1021` | Remote Services | 3 | 7/8 |
| ✅ | `T1021.001` | ↳ Remote Desktop Protocol | 11 | — |
| ✅ | `T1021.002` | ↳ SMB/Windows Admin Shares | 23 | — |
| ✅ | `T1021.003` | ↳ Distributed Component Object Model | 6 | — |
| ✅ | `T1021.004` | ↳ SSH | 1 | — |
| ✅ | `T1021.005` | ↳ VNC | 1 | — |
| ✅ | `T1021.006` | ↳ Windows Remote Management | 7 | — |
| ✅ | `T1021.007` | ↳ Cloud Services | 1 | — |
| ⬜ | `T1021.008` | ↳ Direct Cloud VM Connections | 0 | — |
| ✅ | `T1072` | Software Deployment Tools | 3 | — |
| ⬜ | `T1080` | Taint Shared Content | 0 | — |
| ✅ | `T1091` | Replication Through Removable Media | 1 | — |
| ✅ | `T1210` | Exploitation of Remote Services | 3 | — |
| ⬜ | `T1534` | Internal Spearphishing | 0 | — |
| ✅ | `T1550` | Use Alternate Authentication Material | 4 | 3/4 |
| ✅ | `T1550.001` | ↳ Application Access Token | 4 | — |
| ✅ | `T1550.002` | ↳ Pass the Hash | 7 | — |
| ✅ | `T1550.003` | ↳ Pass the Ticket | 3 | — |
| ⬜ | `T1550.004` | ↳ Web Session Cookie | 0 | — |
| 🟡 | `T1563` | Remote Service Session Hijacking | 0 | 1/2 |
| ⬜ | `T1563.001` | ↳ SSH Hijacking | 0 | — |
| ✅ | `T1563.002` | ↳ RDP Hijacking | 3 | — |
| ✅ | `T1570` | Lateral Tool Transfer | 4 | — |

### Collection (TA0009)
Coverage: **11/17** (64.7%)

| Status | ID | Name | Rules | Sub-techs |
|--------|----|------|-------|-----------|
| ✅ | `T1005` | Data from Local System | 8 | — |
| ⬜ | `T1025` | Data from Removable Media | 0 | — |
| ✅ | `T1039` | Data from Network Shared Drive | 2 | — |
| ✅ | `T1056` | Input Capture | 4 | 2/4 |
| ✅ | `T1056.001` | ↳ Keylogging | 4 | — |
| ✅ | `T1056.002` | ↳ GUI Input Capture | 1 | — |
| ⬜ | `T1056.003` | ↳ Web Portal Capture | 0 | — |
| ⬜ | `T1056.004` | ↳ Credential API Hooking | 0 | — |
| 🟡 | `T1074` | Data Staged | 0 | 1/2 |
| ✅ | `T1074.001` | ↳ Local Data Staging | 4 | — |
| ⬜ | `T1074.002` | ↳ Remote Data Staging | 0 | — |
| ✅ | `T1113` | Screen Capture | 5 | — |
| ✅ | `T1114` | Email Collection | 8 | 1/3 |
| ✅ | `T1114.001` | ↳ Local Email Collection | 1 | — |
| ⬜ | `T1114.002` | ↳ Remote Email Collection | 0 | — |
| ⬜ | `T1114.003` | ↳ Email Forwarding Rule | 0 | — |
| ✅ | `T1115` | Clipboard Data | 6 | — |
| ✅ | `T1119` | Automated Collection | 4 | — |
| ✅ | `T1123` | Audio Capture | 4 | — |
| ⬜ | `T1125` | Video Capture | 0 | — |
| ✅ | `T1185` | Browser Session Hijacking | 2 | — |
| ⬜ | `T1213` | Data from Information Repositories | 0 | 0/6 |
| ⬜ | `T1213.001` | ↳ Confluence | 0 | — |
| ⬜ | `T1213.002` | ↳ Sharepoint | 0 | — |
| ⬜ | `T1213.003` | ↳ Code Repositories | 0 | — |
| ⬜ | `T1213.004` | ↳ Customer Relationship Management Software | 0 | — |
| ⬜ | `T1213.005` | ↳ Messaging Applications | 0 | — |
| ⬜ | `T1213.006` | ↳ Databases | 0 | — |
| ⬜ | `T1530` | Data from Cloud Storage | 0 | — |
| ✅ | `T1557` | Adversary-in-the-Middle | 1 | 1/4 |
| ✅ | `T1557.001` | ↳ LLMNR/NBT-NS Poisoning and SMB Relay | 4 | — |
| ⬜ | `T1557.002` | ↳ ARP Cache Poisoning | 0 | — |
| ⬜ | `T1557.003` | ↳ DHCP Spoofing | 0 | — |
| ⬜ | `T1557.004` | ↳ Evil Twin | 0 | — |
| ✅ | `T1560` | Archive Collected Data | 4 | 1/3 |
| ✅ | `T1560.001` | ↳ Archive via Utility | 14 | — |
| ⬜ | `T1560.002` | ↳ Archive via Library | 0 | — |
| ⬜ | `T1560.003` | ↳ Archive via Custom Method | 0 | — |
| ⬜ | `T1602` | Data from Configuration Repository | 0 | 0/2 |
| ⬜ | `T1602.001` | ↳ SNMP (MIB Dump) | 0 | — |
| ⬜ | `T1602.002` | ↳ Network Device Configuration Dump | 0 | — |

### Command and Control (TA0011)
Coverage: **11/18** (61.1%)

| Status | ID | Name | Rules | Sub-techs |
|--------|----|------|-------|-----------|
| 🟡 | `T1001` | Data Obfuscation | 0 | 1/3 |
| ⬜ | `T1001.001` | ↳ Junk Data | 0 | — |
| ⬜ | `T1001.002` | ↳ Steganography | 0 | — |
| ✅ | `T1001.003` | ↳ Protocol or Service Impersonation | 1 | — |
| ⬜ | `T1008` | Fallback Channels | 0 | — |
| ✅ | `T1071` | Application Layer Protocol | 2 | 2/5 |
| ✅ | `T1071.001` | ↳ Web Protocols | 268 | — |
| ⬜ | `T1071.002` | ↳ File Transfer Protocols | 0 | — |
| ⬜ | `T1071.003` | ↳ Mail Protocols | 0 | — |
| ✅ | `T1071.004` | ↳ DNS | 3 | — |
| ⬜ | `T1071.005` | ↳ Publish/Subscribe Protocols | 0 | — |
| ✅ | `T1090` | Proxy | 11 | 3/4 |
| ✅ | `T1090.001` | ↳ Internal Proxy | 6 | — |
| ✅ | `T1090.002` | ↳ External Proxy | 1 | — |
| ✅ | `T1090.003` | ↳ Multi-hop Proxy | 1 | — |
| ⬜ | `T1090.004` | ↳ Domain Fronting | 0 | — |
| ⬜ | `T1092` | Communication Through Removable Media | 0 | — |
| ✅ | `T1095` | Non-Application Layer Protocol | 2 | — |
| ✅ | `T1102` | Web Service | 3 | 3/3 |
| ✅ | `T1102.001` | ↳ Dead Drop Resolver | 18 | — |
| ✅ | `T1102.002` | ↳ Bidirectional Communication | 4 | — |
| ✅ | `T1102.003` | ↳ One-Way Communication | 18 | — |
| ✅ | `T1104` | Multi-Stage Channels | 1 | — |
| ✅ | `T1105` | Ingress Tool Transfer | 58 | — |
| 🟡 | `T1132` | Data Encoding | 0 | 1/2 |
| ✅ | `T1132.001` | ↳ Standard Encoding | 6 | — |
| ⬜ | `T1132.002` | ↳ Non-Standard Encoding | 0 | — |
| ⬜ | `T1205` | Traffic Signaling | 0 | 0/2 |
| ⬜ | `T1205.001` | ↳ Port Knocking | 0 | — |
| ⬜ | `T1205.002` | ↳ Socket Filters | 0 | — |
| ✅ | `T1219` | Remote Access Tools | 19 | 0/3 |
| ⬜ | `T1219.001` | ↳ IDE Tunneling | 0 | — |
| ⬜ | `T1219.002` | ↳ Remote Desktop Software | 0 | — |
| ⬜ | `T1219.003` | ↳ Remote Access Hardware | 0 | — |
| ✅ | `T1568` | Dynamic Resolution | 9 | 0/3 |
| ⬜ | `T1568.001` | ↳ Fast Flux DNS | 0 | — |
| ⬜ | `T1568.002` | ↳ Domain Generation Algorithms | 0 | — |
| ⬜ | `T1568.003` | ↳ DNS Calculation | 0 | — |
| ✅ | `T1571` | Non-Standard Port | 1 | — |
| ✅ | `T1572` | Protocol Tunneling | 12 | — |
| ✅ | `T1573` | Encrypted Channel | 17 | 1/2 |
| ⬜ | `T1573.001` | ↳ Symmetric Cryptography | 0 | — |
| ✅ | `T1573.002` | ↳ Asymmetric Cryptography | 3 | — |
| ⬜ | `T1659` | Content Injection | 0 | — |
| ⬜ | `T1665` | Hide Infrastructure | 0 | — |

### Exfiltration (TA0010)
Coverage: **6/9** (66.7%)

| Status | ID | Name | Rules | Sub-techs |
|--------|----|------|-------|-----------|
| ⬜ | `T1011` | Exfiltration Over Other Network Medium | 0 | 0/1 |
| ⬜ | `T1011.001` | ↳ Exfiltration Over Bluetooth | 0 | — |
| ✅ | `T1020` | Automated Exfiltration | 18 | 0/1 |
| ⬜ | `T1020.001` | ↳ Traffic Duplication | 0 | — |
| ⬜ | `T1029` | Scheduled Transfer | 0 | — |
| ✅ | `T1030` | Data Transfer Size Limits | 1 | — |
| ✅ | `T1041` | Exfiltration Over C2 Channel | 1 | — |
| ✅ | `T1048` | Exfiltration Over Alternative Protocol | 5 | 2/3 |
| ✅ | `T1048.001` | ↳ Exfiltration Over Symmetric Encrypted Non-C2 Protocol | 2 | — |
| ⬜ | `T1048.002` | ↳ Exfiltration Over Asymmetric Encrypted Non-C2 Protocol | 0 | — |
| ✅ | `T1048.003` | ↳ Exfiltration Over Unencrypted Non-C2 Protocol | 6 | — |
| ⬜ | `T1052` | Exfiltration Over Physical Medium | 0 | 0/1 |
| ⬜ | `T1052.001` | ↳ Exfiltration over USB | 0 | — |
| ✅ | `T1537` | Transfer Data to Cloud Account | 8 | — |
| ✅ | `T1567` | Exfiltration Over Web Service | 4 | 1/4 |
| ⬜ | `T1567.001` | ↳ Exfiltration to Code Repository | 0 | — |
| ✅ | `T1567.002` | ↳ Exfiltration to Cloud Storage | 19 | — |
| ⬜ | `T1567.003` | ↳ Exfiltration to Text Storage Sites | 0 | — |
| ⬜ | `T1567.004` | ↳ Exfiltration Over Webhook | 0 | — |

### Impact (TA0040)
Coverage: **10/15** (66.7%)

| Status | ID | Name | Rules | Sub-techs |
|--------|----|------|-------|-----------|
| ✅ | `T1485` | Data Destruction | 20 | 0/1 |
| ⬜ | `T1485.001` | ↳ Lifecycle-Triggered Deletion | 0 | — |
| ✅ | `T1486` | Data Encrypted for Impact | 29 | — |
| ✅ | `T1489` | Service Stop | 10 | — |
| ✅ | `T1490` | Inhibit System Recovery | 18 | — |
| 🟡 | `T1491` | Defacement | 0 | 1/2 |
| ✅ | `T1491.001` | ↳ Internal Defacement | 2 | — |
| ⬜ | `T1491.002` | ↳ External Defacement | 0 | — |
| ⬜ | `T1495` | Firmware Corruption | 0 | — |
| ✅ | `T1496` | Resource Hijacking | 2 | 0/4 |
| ⬜ | `T1496.001` | ↳ Compute Hijacking | 0 | — |
| ⬜ | `T1496.002` | ↳ Bandwidth Hijacking | 0 | — |
| ⬜ | `T1496.003` | ↳ SMS Pumping | 0 | — |
| ⬜ | `T1496.004` | ↳ Cloud Service Hijacking | 0 | — |
| ✅ | `T1498` | Network Denial of Service | 1 | 0/2 |
| ⬜ | `T1498.001` | ↳ Direct Network Flood | 0 | — |
| ⬜ | `T1498.002` | ↳ Reflection Amplification | 0 | — |
| ✅ | `T1499` | Endpoint Denial of Service | 1 | 0/4 |
| ⬜ | `T1499.001` | ↳ OS Exhaustion Flood | 0 | — |
| ⬜ | `T1499.002` | ↳ Service Exhaustion Flood | 0 | — |
| ⬜ | `T1499.003` | ↳ Application Exhaustion Flood | 0 | — |
| ⬜ | `T1499.004` | ↳ Application or System Exploitation | 0 | — |
| ✅ | `T1529` | System Shutdown/Reboot | 4 | — |
| ✅ | `T1531` | Account Access Removal | 9 | — |
| ⬜ | `T1561` | Disk Wipe | 0 | 0/2 |
| ⬜ | `T1561.001` | ↳ Disk Content Wipe | 0 | — |
| ⬜ | `T1561.002` | ↳ Disk Structure Wipe | 0 | — |
| ✅ | `T1565` | Data Manipulation | 5 | 1/3 |
| ✅ | `T1565.001` | ↳ Stored Data Manipulation | 3 | — |
| ⬜ | `T1565.002` | ↳ Transmitted Data Manipulation | 0 | — |
| ⬜ | `T1565.003` | ↳ Runtime Data Manipulation | 0 | — |
| ⬜ | `T1657` | Financial Theft | 0 | — |
| ⬜ | `T1667` | Email Bombing | 0 | — |

## CVE Coverage

| CVE | Rules | Rule Titles |
|-----|-------|-------------|
| CVE-2019-14287 | 1 | `Sudo Privilege Escalation CVE-2019-14287 - Builtin` |
| CVE-2021-1675 | 1 | `CVE-2021-1675 Print Spooler Exploitation Filename Pattern` |
| CVE-2022-41120 | 1 | `Suspicious Sysmon as Execution Parent` |
| CVE-2023-1389 | 7 | `CVE-2023-1389 Potential Exploitation Attempt - Unauthenticated Command Injection In TP-Link Archer AX21`, `CVE-2023-1389 Potential Exploitation Attempt - Unauthenticated Command Injection In TP-Link Archer AX21`, `CVE-2023-1389 Potential Exploitation Attempt - Unauthenticated Command Injection In TP-Link Archer AX21` +4 more |
| CVE-2023-36884 | 31 | `Potential CVE-2023-36884 Exploitation - URL Marker`, `Potential CVE-2303-36884 URL Request Pattern Traffic`, `Potential CVE-2023-36884 Exploitation - File Downloads` +28 more |
| CVE-2024-3094 | 1 | `Potential Exploitation of CVE-2024-3094 - Suspicious SSH Child Process` |
| CVE-2024-37085 | 2 | `Potential Exploitation of CVE-2024-37085 - Suspicious ESX Admins Group Activity`, `Potential Exploitation of CVE-2024-37085 - Suspicious Creation Of ESX Admins Group` |
| CVE-2024-49113 | 1 | `CVE-2024-49113 Exploitation Attempt - LDAP Nightmare` |
| CVE-2025-22457 | 3 | `CVE-2025-22457 - Ivanti Buffer Overflow for X-Forwarded-For`, `CVE-2025-22457 - Ivanti Buffer Overflow for X-Forwarded-For`, `CVE-2025-22457 - Ivanti Buffer Overflow for X-Forwarded-For` |
