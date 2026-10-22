# What's New In Python 3.6 / Build and C API Changes

### Build and C API Changes

- Building Python now demands a measure of C99 support from the toolchain. Most prominently, Python now relies on standard integer types and macros where it once had custom macros such as `PY_LONG_LONG`. Further details appear in [**PEP 7**](https://peps.python.org/pep-0007/) and [bpo-17884](https://bugs.python.org/issue?@action=redirect&bpo=17884).

- Cross-compiling CPython against the Android NDK with the Android API level fixed at 21 (Android 5.0 Lollipop) or higher completes successfully. Even though Android is not a supported platform yet, the Python test suite executes on the Android emulator with merely about 16 tests failures. Consult the Android meta-issue [bpo-26865](https://bugs.python.org/issue?@action=redirect&bpo=26865).

- The `--enable-optimizations` configure flag was added. Switching it on enables costly optimizations such as PGO. (Original patch by Alecsandru Patrascu of Intel in [bpo-26359](https://bugs.python.org/issue?@action=redirect&bpo=26359).)

- The [GIL](https://docs.python.org/3.14/glossary.html#term-global-interpreter-lock) is now required to be held at the time allocator functions of the [`PYMEM_DOMAIN_OBJ`](https://docs.python.org/3.14/c-api/memory.html#c.PYMEM_DOMAIN_OBJ) (ex: [`PyObject_Malloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyObject_Malloc)) and [`PYMEM_DOMAIN_MEM`](https://docs.python.org/3.14/c-api/memory.html#c.PYMEM_DOMAIN_MEM) (ex: [`PyMem_Malloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Malloc)) domains get called.

- A new [`Py_FinalizeEx()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_FinalizeEx) API reports whether flushing buffered data failed. (Contributed by Martin Panter in [bpo-5319](https://bugs.python.org/issue?@action=redirect&bpo=5319).)

- [`PyArg_ParseTupleAndKeywords()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTupleAndKeywords) has gained handling for [positional-only parameters](https://docs.python.org/3.14/glossary.html#positional-only-parameter). You define positional-only parameters via empty names. (Contributed by Serhiy Storchaka in [bpo-26282](https://bugs.python.org/issue?@action=redirect&bpo=26282)).

- `PyTraceback_Print` method now shortens lengthy runs of identical lines into `"[Previous line repeated {count} more times]"`. (Contributed by Emanuel Barry in [bpo-26823](https://bugs.python.org/issue?@action=redirect&bpo=26823).)

- A new [`PyErr_SetImportErrorSubclass()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_SetImportErrorSubclass) function lets you name a subclass of [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) to raise. (Contributed by Eric Snow in [bpo-15767](https://bugs.python.org/issue?@action=redirect&bpo=15767).)

- A new [`PyErr_ResourceWarning()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_ResourceWarning) function serves to emit a [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning) that names where the resource was allocated. (Contributed by Victor Stinner in [bpo-26567](https://bugs.python.org/issue?@action=redirect&bpo=26567).)

- A new [`PyOS_FSPath()`](https://docs.python.org/3.14/c-api/sys.html#c.PyOS_FSPath) function hands back the file system representation belonging to a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object). (Contributed by Brett Cannon in [bpo-27186](https://bugs.python.org/issue?@action=redirect&bpo=27186).)

- The [`PyUnicode_FSConverter()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FSConverter) and [`PyUnicode_FSDecoder()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FSDecoder) functions are now willing to accept [path-like objects](https://docs.python.org/3.14/glossary.html#term-path-like-object).

[Subject index](INDEX.md) · [Previous source section](optimizations.md) · [Next source section](other-improvements.md) · [Release/subject declaration](summary-release-highlights.md)
