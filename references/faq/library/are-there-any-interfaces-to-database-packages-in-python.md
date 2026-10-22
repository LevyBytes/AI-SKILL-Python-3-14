# Are there any interfaces to database packages in Python?

### Databases

### Are there any interfaces to database packages in Python?

Yes.

Standard Python ships with bindings for on-disk hashes like [`DBM`](https://docs.python.org/3.14/library/dbm.html#module-dbm.ndbm) and [`GDBM`](https://docs.python.org/3.14/library/dbm.html#module-dbm.gnu). On top of that, the [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) module gives you a small, file-backed relational database.

Most relational databases are catered for as well. Consult the [DatabaseProgramming wiki page](https://wiki.python.org/moin/DatabaseProgramming) if you want specifics.

[Subject index](INDEX.md)
