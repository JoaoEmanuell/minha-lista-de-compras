- [Index](#index)
- [Relacional](#relacional)
  - [User](#user)
- [No Relacional](#no-relacional)
  - [List](#list)

# Index

This part of the documentation addresses questions about database modeling.

# Relacional

## User

Id: Primary key, auto-increment, single.

Username: single, text. **[hashed]**

Password: text. **[hashed]**

Table:

| Id | Username | Password |
| -- | -------- | -------- |
| 01 | username | password |

# No Relacional

Id: Primary key, auto-increment, single.

Id user: Foreign key, related to [user](#user). **[encrypted]**

Data: List of strings, containing content, item will be one line. **[encrypted]**

## List

Json:

    {
        id: 0000001
        id_user: 1
        data: [
            'line_1',
            'line_2'
        ]
    }