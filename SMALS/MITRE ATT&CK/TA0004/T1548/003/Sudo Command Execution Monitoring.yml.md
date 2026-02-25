```yml
title: Sudo Command Execution Monitoring
id: 9e9b9e92-8c5d-4d9f-af5b-2g4d5e6f8b8c
status: experimental
description: Monitors sudo command executions from system logs
references:
    - https://attack.mitre.org/techniques/T1548/003/
author: Thimoté Fétu
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