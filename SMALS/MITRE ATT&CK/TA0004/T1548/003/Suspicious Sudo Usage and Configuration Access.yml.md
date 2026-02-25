```yml
title: Suspicious Sudo Usage and Configuration Access
id: 8d8a8d91-7b4c-4c8f-9e4a-1f3c4d5e6f7a
status: experimental
description: Detects suspicious sudo command usage, sudoers file access, and potential privilege escalation attempts
references:
    - https://attack.mitre.org/techniques/T1548/003/
    - https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.003/T1548.003.md
author: Thimoté Fétu
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
