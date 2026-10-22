# What's New In Python 3.7 / Other Language Changes — types

### Other Language Changes

- Owing to an implementation issue, an [`await`](https://docs.python.org/3.14/reference/expressions.html#await) expression together with comprehensions holding an [`async for`](https://docs.python.org/3.14/reference/compound_stmts.html#async-for) clause used to be forbidden inside the expressions of [formatted string literals](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings). Python 3.7 removed that restriction.

- A function may now receive over 255 arguments, and a function may now declare over 255 parameters. (Contributed by Serhiy Storchaka in [bpo-12844](https://bugs.python.org/issue?@action=redirect&bpo=12844) and [bpo-18896](https://bugs.python.org/issue?@action=redirect&bpo=18896).)

- [`bytes.fromhex()`](https://docs.python.org/3.14/library/stdtypes.html#bytes.fromhex) and [`bytearray.fromhex()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.fromhex) now skip every ASCII whitespace character, not merely spaces. (Contributed by Robert Xiao in [bpo-28927](https://bugs.python.org/issue?@action=redirect&bpo=28927).)

- [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) picked up the new [`isascii()`](https://docs.python.org/3.14/library/stdtypes.html#str.isascii) method, handy for checking whether a string or bytes hold nothing but ASCII characters. (Contributed by INADA Naoki in [bpo-32677](https://bugs.python.org/issue?@action=redirect&bpo=32677).)

- [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) now reports the module name plus the module `__file__` path whenever `from ... import ...` does not succeed. (Contributed by Matthias Bussonnier in [bpo-29546](https://bugs.python.org/issue?@action=redirect&bpo=29546).)

- Circular imports that use absolute imports and bind a submodule to a name now work. (Contributed by Serhiy Storchaka in [bpo-30024](https://bugs.python.org/issue?@action=redirect&bpo=30024).)

- `object.__format__(x, '')` now matches `str(x)` instead of `format(str(self), '')`. (Contributed by Serhiy Storchaka in [bpo-28974](https://bugs.python.org/issue?@action=redirect&bpo=28974).)

- To better enable building stack traces on the fly, [`types.TracebackType`](https://docs.python.org/3.14/library/types.html#types.TracebackType) can now be created from Python code, and on [tracebacks](https://docs.python.org/3.14/reference/datamodel.html#traceback-objects) the [`tb_next`](https://docs.python.org/3.14/reference/datamodel.html#traceback.tb_next) attribute is now writable. (Contributed by Nathaniel J. Smith in [bpo-30579](https://bugs.python.org/issue?@action=redirect&bpo=30579).)

- With the [`-m`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m) switch, `sys.path[0]` now expands eagerly to the complete starting directory path rather than remaining the empty directory (which permits imports from the *current* working directory at the moment an import happens) (Contributed by Nick Coghlan in [bpo-33053](https://bugs.python.org/issue?@action=redirect&bpo=33053).)

- The new [`-X`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) `importtime` option, or else the [`PYTHONPROFILEIMPORTTIME`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPROFILEIMPORTTIME) environment variable, reports how long each module import takes. (Contributed by Inada Naoki in [bpo-31415](https://bugs.python.org/issue?@action=redirect&bpo=31415).)

### New Modules

### contextvars

[Subject index](INDEX.md) · [Previous source section](python-development-mode.md) · [Release/subject declaration](summary-release-highlights.md) · [Following release/subject continuation](contextvars.md)
