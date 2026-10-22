# Python 3.14.0 alpha 1 / library / pdb

[gh-123756](https://github.com/python/cpython/issues/123756): A new `mode` argument joins [`pdb.Pdb`](https://docs.python.org/3.14/library/pdb.html#pdb.Pdb). The `restart` command is only permitted for [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) when invoked from the command line.

[gh-119824](https://github.com/python/cpython/issues/119824): Have [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) print the stack entry exactly at the moment user input is required, and only then.

[gh-118714](https://github.com/python/cpython/issues/118714): During post-mortem debugging with [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb), `restart` is now permitted. The restart notice that appeared when a user quit pdb from post-mortem mode has been taken out.

[gh-120254](https://github.com/python/cpython/issues/120254): Give [`pdb.set_trace()`](https://docs.python.org/3.14/library/pdb.html#pdb.set_trace) a `commands` argument that lets callers issue debugger commands straight from the source file.

[gh-58933](https://github.com/python/cpython/issues/58933): Make [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) come back to the caller frame correctly even when that caller frame's `f_trace` has not been set

[gh-125422](https://github.com/python/cpython/issues/125422): Corrected the defect letting [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) and [`bdb`](https://docs.python.org/3.14/library/bdb.html#module-bdb) descend into the bottom caller frame.

[gh-100141](https://github.com/python/cpython/issues/100141): Corrected the defect whereby [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) entered an endless loop while debugging an empty file.

[gh-120769](https://github.com/python/cpython/issues/120769): Arrange for a blank line in [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) to repeat the previous command, including the situation where that command originates from `cmdqueue`.

[gh-120606](https://github.com/python/cpython/issues/120606): Permit EOF as a way to leave a `commands` definition inside [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb)

[gh-124400](https://github.com/python/cpython/issues/124400): Repaired a [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) defect in which `until` did nothing once it showed up within a `commands` sequence. It also stops the frame info from being printed at a breakpoint whose command list holds a command that continues execution.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
