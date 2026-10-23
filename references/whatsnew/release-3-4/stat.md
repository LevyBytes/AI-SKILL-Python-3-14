# What's New In Python 3.4 / stat - stat

### stat

The [`stat`](https://docs.python.org/3.14/library/stat.html#module-stat) module is now driven by a C implementation living in `_stat`. A C implementation is necessary since the bulk of the values are platform-dependent rather than standardized. (Contributed by Christian Heimes in [bpo-11016](https://bugs.python.org/issue?@action=redirect&bpo=11016).)

This module now recognizes new [`ST_MODE`](https://docs.python.org/3.14/library/stat.html#stat.ST_MODE) flags — [`S_IFDOOR`](https://docs.python.org/3.14/library/stat.html#stat.S_IFDOOR), [`S_IFPORT`](https://docs.python.org/3.14/library/stat.html#stat.S_IFPORT), and [`S_IFWHT`](https://docs.python.org/3.14/library/stat.html#stat.S_IFWHT). (Contributed by Christian Hiemes in [bpo-11016](https://bugs.python.org/issue?@action=redirect&bpo=11016).)

[Subject index](INDEX.md) · [Previous source section](ssl.md) · [Next source section](struct.md) · [Release/subject declaration](release-highlights.md)
