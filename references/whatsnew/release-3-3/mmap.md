# What's New In Python 3.3 / mmap - mmap

### mmap

The [`read()`](https://docs.python.org/3.14/library/mmap.html#mmap.mmap.read) method now lines up better with other file-like objects: leave the argument out or pass `None` and it hands back the bytes spanning the current file position through the end of the mapping. Petri Lehtinen landed this ([bpo-12021](https://bugs.python.org/issue?@action=redirect&bpo=12021)).

[Subject index](INDEX.md) · [Previous source section](math.md) · [Next source section](multiprocessing.md) · [Release/subject declaration](summary-release-highlights.md)
