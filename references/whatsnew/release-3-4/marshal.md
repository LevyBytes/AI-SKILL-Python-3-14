# What's New In Python 3.4 / marshal — marshal

### marshal

The default [`marshal`](https://docs.python.org/3.14/library/marshal.html#module-marshal) version moved up to 3. Code behind the new version brings back the Python2 habit of keeping just a single copy of interned strings and holding the interning through deserialization, then widens that "one copy" trait to every object type (recursive references included). The result trims both the byte size of `.pyc` files and the memory a module takes up once it loads from a `.pyc` (or `.pyo`) file. (Contributed by Kristján Valur Jónsson in [bpo-16475](https://bugs.python.org/issue?@action=redirect&bpo=16475), with additional speedups by Antoine Pitrou in [bpo-19219](https://bugs.python.org/issue?@action=redirect&bpo=19219).)

[Subject index](INDEX.md) · [Previous source section](logging.md) · [Next source section](mmap.md) · [Release/subject declaration](release-highlights.md)
