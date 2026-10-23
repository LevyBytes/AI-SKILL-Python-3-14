# What's New In Python 3.3 / zlib - zlib

### zlib

A new [`zlib.Decompress.eof`](https://docs.python.org/3.14/library/zlib.html#zlib.Decompress.eof) attribute lets you tell a well-formed compressed stream apart from one that is truncated or incomplete. Nadeem Vawda contributed this ? see [bpo-12646](https://bugs.python.org/issue?@action=redirect&bpo=12646).

A new [`zlib.ZLIB_RUNTIME_VERSION`](https://docs.python.org/3.14/library/zlib.html#zlib.ZLIB_RUNTIME_VERSION) attribute gives back the version string for whichever `zlib` library is loaded at runtime. Torsten Landschoff added it; refer to [bpo-12306](https://bugs.python.org/issue?@action=redirect&bpo=12306).

[Subject index](INDEX.md) · [Previous source section](xml-etree-elementtree.md) · [Next source section](optimizations.md) · [Release/subject declaration](summary-release-highlights.md)
