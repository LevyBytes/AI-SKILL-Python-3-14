# Python 3.14.0 beta 1 / core and builtins / imports and modules

[gh-130907](https://github.com/python/cpython/issues/130907): When a module object's `__annotations__` is read while the module is still executing, the annotations defined up to that point are returned, and they are not cached.

[gh-69605](https://github.com/python/cpython/issues/69605): Module autocomplete is added to PyREPL.

[gh-102567](https://github.com/python/cpython/issues/102567): [`-X importtime`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) now takes the value `2`, signalling that an `importtime` entry should be printed even when an imported module is already loaded. Noah Kim and Adam Turner wrote this patch.

[gh-133346](https://github.com/python/cpython/issues/133346): The `_colorize` module gained experimental support for color theming.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
