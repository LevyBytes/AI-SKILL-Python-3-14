# 6.1.3. "Compiled" Python files

### 6.1.3. "Compiled" Python files

So that modules load faster, Python keeps a cached compiled form of each module inside the `__pycache__` directory under the name `module.*version*.pyc`, where the version captures the compiled file's format; this usually carries the Python version number. As an example, under CPython release 3.3 the compiled form of spam.py would be stored as `__pycache__/spam.cpython-33.pyc`. Thanks to this naming scheme, compiled modules from differing releases and differing Python versions can sit side by side.

Python compares the source's modification date against the compiled form to determine whether it has gone stale and must be rebuilt. That check happens entirely on its own. On top of that, compiled modules don't depend on the platform, so a single library can be shared across systems with differing architectures.

Two situations cause Python to skip the cache. The first: it always recompiles, and never saves the outcome, for a module loaded straight from the command line. The second: it skips the cache check whenever no source module exists. If you want to ship a source-free (compiled-only) distribution, the compiled module has to sit in the source directory, and no source module may be present.

A few pointers for the experts:

- The [`-O`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-O) and [`-OO`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-OO) switches on the Python command can trim the size of a compiled module. The `-O` switch strips out assert statements, while `-OO` strips both assert statements and __doc__ strings. Because certain programs may depend on these being present, reach for this option only when you understand the consequences. "Optimized" modules carry an `opt-` tag and tend to be smaller. Later releases might alter what optimization does.

- Reading a program from a `.pyc` file gives no speed boost over reading it from a `.py` file; the sole advantage `.pyc` files have is how quickly they load.

- The [`compileall`](https://docs.python.org/3.14/library/compileall.html#module-compileall) module can produce .pyc files for every module in a directory.

- You'll find fuller coverage of this process, complete with a flow chart of the decisions, in [**PEP 3147**](https://peps.python.org/pep-3147/).

[Subject index](INDEX.md) · [Previous source section](the-module-search-path.md) · [Following source section](standard-modules.md)
