# Python 3.8.0 alpha 1 / core and builtins / stdtypes

[bpo-34974](https://bugs.python.org/issue?@action=redirect&bpo=34974): The [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) constructors will no longer turn unforeseen exceptions (for instance [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError) and [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt)) into [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

[bpo-34973](https://bugs.python.org/issue?@action=redirect&bpo=34973): Resolved a crash in [`bytes()`](https://docs.python.org/3.14/library/stdtypes.html#bytes) that happened when the [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) argument was mutated during its own iteration.

[bpo-33954](https://bugs.python.org/issue?@action=redirect&bpo=33954): For the [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format), `float.__format__()` and `complex.__format__()` methods covering a non-ASCII decimal point while using the "n" formatter.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
