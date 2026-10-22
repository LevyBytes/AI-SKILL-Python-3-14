# sys.pycache_prefix

sys.pycache_prefix

When this is given a value (not `None`), Python writes its bytecode-cache `.pyc` files into — and reads them back from — a parallel directory tree anchored at this directory, instead of the `__pycache__` directories sitting in the source code tree. Any `__pycache__` directories within the source code tree are then disregarded, and fresh `.pyc` files are written under the pycache prefix. So if you employ [`compileall`](https://docs.python.org/3.14/library/compileall.html#module-compileall) as a pre-build step, take care to run it with whatever pycache prefix (if any) you intend to use at runtime.

A relative path is taken relative to the current working directory.

This value is set initially from the [`-X`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) `pycache_prefix=PATH` command-line option or the [`PYTHONPYCACHEPREFIX`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPYCACHEPREFIX) environment variable (with the command-line option winning). When neither is provided, it is `None`.

Added in version 3.8.

[API family](INDEX.md) · [sys context index](../INDEX.md).
