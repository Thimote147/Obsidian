```yml
title: Clear Windows Event Logs
id: N/A
status: experimental
description: Detects when a user attempts to clear event logs
references:
	- https://attack.mitre.org/techniques/T1070/001/
	- https://tryhackme.com/room/introtosiem
author: Thimoté Fétu
date: 2026/02/26
modified: 2026/02/26
tags:
	- attack.defense_evasion
	- attack.t1070.001
logsource:
	product: windows
	service: WinEventLog
detection:
	selection:
		- EventID: 104
	condition: selection
falsepositives:
	- unknown
level: N/A
```