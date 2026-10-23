# sqlite3 - Transaction control

### Explanation

### Transaction control

`sqlite3` gives you several ways to govern if, when, and how database transactions get opened and closed. The advised mechanism is Transaction control via the autocommit attribute, whereas Transaction control via the isolation_level attribute preserves the way things worked prior to Python 3.12.

[Subject index](INDEX.md) · [Continue](transaction-control-via-the-autocommit-attribute.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md)
