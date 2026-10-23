# What’s New In Python 3.8 / Parallel filesystem cache for compiled bytecode files - sys

### Parallel filesystem cache for compiled bytecode files

A freshly added [`PYTHONPYCACHEPREFIX`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPYCACHEPREFIX) setting — also reachable through [`-X`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) `pycache_prefix` — tells the implicit bytecode cache to write into its own parallel filesystem tree instead of the usual `__pycache__` subdirectories sitting beside each source directory.

Wherever the cache ends up gets surfaced in [`sys.pycache_prefix`](https://docs.python.org/3.14/library/sys.html#sys.pycache_prefix); a value of [`None`](https://docs.python.org/3.14/library/constants.html#None) means the standard spot inside `__pycache__` subdirectories.

(Carl Meyer contributed this in [bpo-33499](https://bugs.python.org/issue?@action=redirect&bpo=33499).)

[Subject index](INDEX.md) · [Previous source section](positional-only-parameters.md) · [Next source section](debug-build-uses-the-same-abi-as-release-build.md) · [Release/subject declaration](assignment-expressions.md)
