# What's New In Python 3.9 / Deprecated — ast, math

### Deprecated

- The distutils `bdist_msi` command has been deprecated; reach for `bdist_wheel` (wheel packages) in its place. (Contributed by Hugo van Kemenade in [bpo-39586](https://bugs.python.org/issue?@action=redirect&bpo=39586).)

- At present [`math.factorial()`](https://docs.python.org/3.14/library/math.html#math.factorial) tolerates [`float`](https://docs.python.org/3.14/library/functions.html#float) instances whose value is a non-negative integer (such as `5.0`). For non-integral and negative floats it raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError). That behavior is now deprecated. Later Python releases will instead raise a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) for every float. (Contributed by Serhiy Storchaka in [bpo-37315](https://bugs.python.org/issue?@action=redirect&bpo=37315).)

- The `parser` together with the `symbol` modules have been deprecated and are slated for removal in later Python releases. In most situations, users can instead rely on the Abstract Syntax Tree (AST) generation and compilation step by way of the [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) module.

- The Public C API functions `PyParser_SimpleParseStringFlags()`, `PyParser_SimpleParseStringFlagsFilename()`, `PyParser_SimpleParseFileFlags()` and `PyNode_Compile()` have been deprecated and are scheduled for removal in Python 3.10 alongside the old parser.

- Treating [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented) as a boolean has been deprecated, since it nearly always stems from a faulty rich comparator implementation. A later Python version will turn it into a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). (Contributed by Josh Rosenberg in [bpo-35712](https://bugs.python.org/issue?@action=redirect&bpo=35712).)

-

Right now the [`random`](https://docs.python.org/3.14/library/random.html#module-random) module will take any hashable type as a seed. The trouble is that several of those types do not promise a stable hash value. Beginning after Python 3.9, the seeds accepted by the module are narrowed to [`None`](https://docs.python.org/3.14/library/constants.html#None), [`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float), [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray).

- It is now deprecated to open a [`GzipFile`](https://docs.python.org/3.14/library/gzip.html#gzip.GzipFile) for writing while leaving out the *mode* argument. Later Python releases will, by default, always open it for reading. Supply the *mode* argument when you want write access and to suppress the warning. (Contributed by Serhiy Storchaka in [bpo-28286](https://bugs.python.org/issue?@action=redirect&bpo=28286).)

- The `split()` method on `_tkinter.TkappType` is now deprecated; prefer the `splitlist()` method, whose behavior is more consistent and easier to predict. (Contributed by Serhiy Storchaka in [bpo-38371](https://bugs.python.org/issue?@action=redirect&bpo=38371).)

- Handing coroutine objects directly to [`asyncio.wait()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.wait) is now deprecated, with removal slated for release 3.11. (Contributed by Yury Selivanov and Kyle Stanley in [bpo-34790](https://bugs.python.org/issue?@action=redirect&bpo=34790).)

- The binhex4 and hexbin4 standards are deprecated as of this release. The `binhex` module, along with these [`binascii`](https://docs.python.org/3.14/library/binascii.html#module-binascii) functions, are deprecated as well:

  - `b2a_hqx()`, `a2b_hqx()`

  - `rlecode_hqx()`, `rledecode_hqx()`

(Contributed by Victor Stinner in [bpo-39353](https://bugs.python.org/issue?@action=redirect&bpo=39353).)

- The [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) classes `slice`, `Index` and `ExtSlice` are treated as deprecated and are slated for removal in later Python releases. In their place, use `value` directly rather than `Index(value)`. Likewise, `Tuple(slices, Load())` replaces `ExtSlice(slices)`. (Contributed by Serhiy Storchaka in [bpo-34822](https://bugs.python.org/issue?@action=redirect&bpo=34822).)

- The [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) classes `Suite`, `Param`, `AugLoad` and `AugStore` are treated as deprecated and are slated for removal in later Python releases. The parser never produced them, and the code generator in Python 3 never accepted them. (Contributed by Batuhan Taskaya in [bpo-39639](https://bugs.python.org/issue?@action=redirect&bpo=39639) and [bpo-39969](https://bugs.python.org/issue?@action=redirect&bpo=39969) and Serhiy Storchaka in [bpo-39988](https://bugs.python.org/issue?@action=redirect&bpo=39988).)

- The `PyEval_InitThreads()` and `PyEval_ThreadsInitialized()` functions are now deprecated, with removal planned for Python 3.11. A call to `PyEval_InitThreads()` is now a no-op. Since Python 3.7 the [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) has been initialized by [`Py_Initialize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Initialize). (Contributed by Victor Stinner in [bpo-39877](https://bugs.python.org/issue?@action=redirect&bpo=39877).)

- Supplying `None` as the very first argument to the [`shlex.split()`](https://docs.python.org/3.14/library/shlex.html#shlex.split) function is now deprecated. (Contributed by Zackery Spytz in [bpo-33262](https://bugs.python.org/issue?@action=redirect&bpo=33262).)

- `smtpd.MailmanProxy()` is now deprecated because it cannot work without a separate module, `mailman`. (Contributed by Samuel Colvin in [bpo-35800](https://bugs.python.org/issue?@action=redirect&bpo=35800).)

- The `lib2to3` module now raises a [`PendingDeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#PendingDeprecationWarning). With Python 3.9 having moved to a PEG parser (refer to [**PEP 617**](https://peps.python.org/pep-0617/)), Python 3.10 might add new language syntax that the LL(1) parser in lib2to3 cannot handle. A later Python release could drop the `lib2to3` module from the standard library entirely. Look at third-party options like [LibCST](https://libcst.readthedocs.io/) or [parso](https://parso.readthedocs.io/). (Contributed by Carl Meyer in [bpo-40360](https://bugs.python.org/issue?@action=redirect&bpo=40360).)

- The *random* parameter belonging to [`random.shuffle()`](https://docs.python.org/3.14/library/random.html#random.shuffle) is now deprecated. (Contributed by Raymond Hettinger in [bpo-40465](https://bugs.python.org/issue?@action=redirect&bpo=40465))

[Subject index](INDEX.md) · [Previous source section](optimizations.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](removed.md)
