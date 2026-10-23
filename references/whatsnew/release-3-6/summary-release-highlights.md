# What's New In Python 3.6 / Summary - Release highlights - asyncio, secrets

### What's New In Python 3.6

Editors:

Elvis Pranskevichus <[elvis@magic.io](mailto:elvis%40magic.io)>, Yury Selivanov <[yury@magic.io](mailto:yury%40magic.io)>

This document walks through what changed in Python 3.6 relative to the 3.5 line. The 3.6 release shipped on December 23, 2016. Consult the [changelog](https://docs.python.org/3.6/whatsnew/changelog.html) for the complete record of revisions.

See also

[**PEP 494**](https://peps.python.org/pep-0494/) - Python 3.6 Release Schedule

### Summary - Release highlights

New syntax features:

- PEP 498, formatted string literals.

- PEP 515, underscores in numeric literals.

- PEP 526, syntax for variable annotations.

- PEP 525, asynchronous generators.

- PEP 530: asynchronous comprehensions.

New library modules:

- [`secrets`](https://docs.python.org/3.14/library/secrets.html#module-secrets): PEP 506 — Adding A Secrets Module To The Standard Library.

CPython implementation improvements:

- The [dict](https://docs.python.org/3.14/library/stdtypes.html#typesmapping) type was rebuilt around a denser layout, drawing on [a proposal by Raymond Hettinger](https://mail.python.org/pipermail/python-dev/2012-December/123028.html) and echoing the [PyPy dict implementation](https://morepypy.blogspot.com/2015/01/faster-more-memory-efficient-and-more.html). The payoff is dictionaries consuming 20% to 25% less memory than they did under Python 3.5.

- Tailoring how classes get created is now easier thanks to the new protocol.

- How class attributes were defined is now retained in order.

- For `**kwargs`, the sequence of entries now mirrors the order in which keyword arguments reached the call.

- Probing via DTrace and SystemTap is now supported.

- A fresh PYTHONMALLOC environment variable is available for diagnosing the interpreter's memory allocation and access faults.

Significant improvements in the standard library:

- The [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) module picked up fresh capabilities, sizeable gains in usability and speed, plus a healthy round of fixes. As of Python 3.6 the `asyncio` module sheds its provisional label and its API counts as stable.

- A fresh file system path protocol now backs [path-like objects](https://docs.python.org/3.14/glossary.html#term-path-like-object). Every standard library routine that handles paths was revised to honor the new protocol.

-

The [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime) module picked up Local Time Disambiguation handling.

- The [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module saw several refinements.

- The [`tracemalloc`](https://docs.python.org/3.14/library/tracemalloc.html#module-tracemalloc) module underwent a major overhaul and now powers richer reporting for [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning) along with sharper diagnostics when memory allocation goes wrong. Consult the PYTHONMALLOC section for further detail.

Security improvements:

- A new [`secrets`](https://docs.python.org/3.14/library/secrets.html#module-secrets) module joins the library to ease producing cryptographically strong pseudo-random values fit for handling secrets like account authentication, tokens, and the like.

- Under Linux, [`os.urandom()`](https://docs.python.org/3.14/library/os.html#os.urandom) now waits until the system urandom entropy pool has been seeded, improving security. Consult the [**PEP 524**](https://peps.python.org/pep-0524/) for the reasoning.

- OpenSSL 1.1.0 is now handled by the [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) and [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) modules.

- For the [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) module, the default configuration and capabilities were upgraded.

- The [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib) module gained the BLAKE2, SHA-3 and SHAKE hash algorithms together with the [`scrypt()`](https://docs.python.org/3.14/library/hashlib.html#hashlib.scrypt) key derivation function.

Windows improvements:

- PEP 528 along with PEP 529, switching the Windows filesystem plus console encoding over to UTF-8.

- When run interactively, the `py.exe` launcher no longer favors Python 2 ahead of Python 3 if no version is named by the user (whether through command line arguments or a config file). The treatment of shebang lines is the same as before - "python" still points to Python 2 in that scenario.

- Both `python.exe` and `pythonw.exe` now carry the long-path aware flag, so the 260 character path limit may cease to bind. Consult [removing the MAX_PATH limitation](https://docs.python.org/3.14/using/windows.html#max-path) for the specifics.

- Dropping in a `._pth` file lets you require isolated mode and pin down every search path so registry and environment lookups are skipped. Consult [the documentation](https://docs.python.org/3.14/using/windows.html#windows-finding-modules) for further detail.

- A `python36.zip` file now serves as a marker for deriving [`PYTHONHOME`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONHOME). Consult [the documentation](https://docs.python.org/3.14/using/windows.html#windows-finding-modules) for further detail.

[Subject index](INDEX.md) · [Next source section](pep-498-formatted-string-literals.md)
