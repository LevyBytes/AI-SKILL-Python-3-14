# What's New In Python 3.4 / dbm - dbm

### dbm

[`dbm.open()`](https://docs.python.org/3.14/library/dbm.html#dbm.open) objects now honor the context management protocol. Inside a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement, the database object's `close` method fires automatically once the block finishes. (Contributed by Claudiu Popa and Nick Coghlan in [bpo-19282](https://bugs.python.org/issue?@action=redirect&bpo=19282).)

[Subject index](INDEX.md) · [Previous source section](contextlib.md) · [Next source section](dis.md) · [Release/subject declaration](release-highlights.md)
