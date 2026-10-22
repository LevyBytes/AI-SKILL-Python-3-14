# Python 3.13.0 alpha 1 / core and builtins / grp

[gh-104432](https://github.com/python/cpython/issues/104432): Resolves a possible misaligned memory read in C APIs that hand back sequences of `char *` pointers inside the [`grp`](https://docs.python.org/3.14/library/grp.html#module-grp) and [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) modules. A `-fsaniziter=alignment` build on ARM macOS surfaced these. Christopher Chavez supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
