- [Inicio](#inicio)
- [Relacional](#relacional)
  - [User](#user)
- [No Relacional](#no-relacional)
  - [List](#list)

# Inicio

Essa parte da documentação trata questões acerca da modelagem do banco de dados

# Relacional

## User

Id: Primary key, auto-increment, single.

Username: single, text. **[hashed]**

Password: text. **[hashed]**

Tabela:

| Id | Username | Password |
| -- | -------- | -------- |
| 01 | username | password |

# No Relacional

## List

Id: Primary key, auto-increment, single.

Id user: Foreign key, relacionada ao [user](#user). **[encrypted]**

Data: List de strings, contendo o conteúdo, item irá ser uma linha. **[encrypted]**

Json:

    {
        id: 0000001
        id_user: 1
        data: [
            'line_1',
            'line_2'
        ]
    }