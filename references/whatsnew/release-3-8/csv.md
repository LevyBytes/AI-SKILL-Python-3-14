# What’s New In Python 3.8 / csv - collections, csv

> (Contributed by Scott Sanderson in [bpo-29235](https://bugs.python.org/issue?@action=redirect&bpo=29235).)

### csv

Rows from [`csv.DictReader`](https://docs.python.org/3.14/library/csv.html#csv.DictReader) now arrive as [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) objects rather than a [`collections.OrderedDict`](https://docs.python.org/3.14/library/collections.html#collections.OrderedDict). It runs quicker and consumes less memory, yet the field ordering still stays intact.

[Subject index](INDEX.md) · [Previous source section](cprofile.md) · [Next source section](curses.md) · [Release/subject declaration](assignment-expressions.md)
