# What's New In Python 3.13 / compileall — os

### compileall

- How many worker threads and processes get used by default is henceforth derived from [`os.process_cpu_count()`](https://docs.python.org/3.14/library/os.html#os.process_cpu_count) in place of [`os.cpu_count()`](https://docs.python.org/3.14/library/os.html#os.cpu_count). (Contributed by Victor Stinner in [gh-109649](https://github.com/python/cpython/issues/109649).)

[Subject index](INDEX.md) · [Previous source section](base64.md) · [Next source section](concurrent-futures.md) · [Release/subject declaration](summary-release-highlights.md)
