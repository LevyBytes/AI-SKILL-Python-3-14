# Python 3.14.0 alpha 6 / library / pdb

[gh-131123](https://github.com/python/cpython/issues/131123): Brings completion support to attributes of convenience variables within [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb).

[gh-125377](https://github.com/python/cpython/issues/125377): Pressing `<tab>` at the line's start during [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) multi-line input now supplies a 4-space indentation rather than dropping in a `\t` character.

[gh-124703](https://github.com/python/cpython/issues/124703): Running the `quit` command inside [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) will throw [`bdb.BdbQuit`](https://docs.python.org/3.14/library/bdb.html#bdb.BdbQuit) whenever `pdb` got launched from an interactive console via [`breakpoint()`](https://docs.python.org/3.14/library/functions.html#breakpoint) or [`pdb.set_trace()`](https://docs.python.org/3.14/library/pdb.html#pdb.set_trace).

[gh-126944](https://github.com/python/cpython/issues/126944): Surfaces clear errors whenever required arguments to [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) commands are absent

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
