````yml
title: System Owner/User Discovery
id: N/A
Status: experimental
description: Detects when user attempts to execute `whoami` commande
References:
	- https://attack.mitre.org/techniques/T1033/
	- https://tryhackme.com/room/introtosiem
Author: Thimoté Fétu
Date: 2026/02/26
modified: 2026/02/26
Tags:
	- attack.discovery
	- Attack.t1033
logsource:
	Product: windows
	Service: WinEventLog
detection:
	Selection:
		EventCode: 4688
		NewProcessName|contains: ‘whoami’
	condition: selection
False positives:
	- unknown
Level: N/A
```