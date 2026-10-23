# sqlite3`sqlite3` - DB-API 2.0 interface for SQLite databases

### `sqlite3` - DB-API 2.0 interface for SQLite databases

**Source code:** [Lib/sqlite3/](https://github.com/python/cpython/tree/3.14/Lib/sqlite3/)

SQLite ships as a C library offering a small, file-backed database engine that runs without any standalone server process, and it is queried through a slightly nonstandard dialect of SQL. Programs sometimes adopt SQLite to keep their own data on disk. You can equally build a quick prototype against SQLite and later move that code onto a heavier engine like PostgreSQL or Oracle.

Gerhard Häring authored the `sqlite3` module. The module exposes an SQL layer that conforms to the DB-API 2.0 specification laid out in [**PEP 249**](https://peps.python.org/pep-0249/), and it depends on the external [SQLite](https://sqlite.org/) library.

The module counts as an [optional module](https://docs.python.org/3.14/glossary.html#term-optional-module). Should your build of CPython lack it, consult whatever documentation came from your distributor — meaning whoever handed Python to you. Distributors themselves can refer to [Requirements for optional modules](https://docs.python.org/3.14/using/configure.html#optional-module-requirements).

Four major sections make up this document:

- The Tutorial walks you through using the `sqlite3` module.

- The Reference covers the classes and functions defined by this module.

- The How-to guides spell out the steps for particular tasks.

- The Explanation supplies deeper background covering transaction control.

See also

[https://www.sqlite.org](https://www.sqlite.org)

The SQLite website; its docs lay out the grammar plus the data types offered by the SQL dialect that is supported.

[https://www.w3schools.com/sql/](https://www.w3schools.com/sql/)

A tutorial, plus reference material and examples, aimed at picking up SQL syntax.

[**PEP 249**](https://peps.python.org/pep-0249/) - Database API Specification 2.0

PEP written by Marc-André Lemburg.

[Subject index](INDEX.md) · [Continue](tutorial-section-introduction-and-initial-examples.md)
