# What's New In Python 3.6 / os - os, os.path

### os

For specifics on how [path-like objects](https://docs.python.org/3.14/glossary.html#term-path-like-object) are now handled by the [`os`](https://docs.python.org/3.14/library/os.html#module-os) and [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path) modules, consult the summary of PEP 519.

On Windows, [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) paths are now accepted by [`scandir()`](https://docs.python.org/3.14/library/os.html#os.scandir).

You can now shut a [`scandir()`](https://docs.python.org/3.14/library/os.html#os.scandir) iterator explicitly via the fresh [`close()`](https://docs.python.org/3.14/library/os.html#os.scandir.close) method. That `scandir()` iterator additionally honors the [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) protocol now. Should a `scandir()` iterator be left neither drained nor deliberately closed, its destructor raises a [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning). (Contributed by Serhiy Storchaka in [bpo-25994](https://bugs.python.org/issue?@action=redirect&bpo=25994).)

For improved security on Linux, [`os.urandom()`](https://docs.python.org/3.14/library/os.html#os.urandom) now waits, blocking, until the system urandom entropy pool has been seeded. The [**PEP 524**](https://peps.python.org/pep-0524/) explains why.

Linux's `getrandom()` syscall, which fetches random bytes, is now reachable through the fresh [`os.getrandom()`](https://docs.python.org/3.14/library/os.html#os.getrandom) function. (Contributed by Victor Stinner, part of the [**PEP 524**](https://peps.python.org/pep-0524/))

[Subject index](INDEX.md) · [Previous source section](multiprocessing.md) · [Next source section](pathlib.md) · [Release/subject declaration](summary-release-highlights.md)
