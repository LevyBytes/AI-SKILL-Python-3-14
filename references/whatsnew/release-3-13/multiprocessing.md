# What's New In Python 3.13 / multiprocessing — os

### multiprocessing

- Choosing the default count of worker threads and processes now relies on [`os.process_cpu_count()`](https://docs.python.org/3.14/library/os.html#os.process_cpu_count) rather than [`os.cpu_count()`](https://docs.python.org/3.14/library/os.html#os.cpu_count). (Contributed by Victor Stinner in [gh-109649](https://github.com/python/cpython/issues/109649).)

[Subject index](INDEX.md) · [Previous source section](mmap.md) · [Next source section](os.md) · [Release/subject declaration](summary-release-highlights.md)
