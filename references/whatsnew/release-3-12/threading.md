# What’s New In Python 3.12 / threading — threading

### threading

- Two helpers, [`threading.settrace_all_threads()`](https://docs.python.org/3.14/library/threading.html#threading.settrace_all_threads) and [`threading.setprofile_all_threads()`](https://docs.python.org/3.14/library/threading.html#threading.setprofile_all_threads), have been added; beyond the calling thread, they let you install trace and profile hooks across every thread that is currently running. (Contributed by Pablo Galindo in [gh-93503](https://github.com/python/cpython/issues/93503).)

[Subject index](INDEX.md) · [Previous source section](tempfile.md) · [Next source section](tkinter.md) · [Release/subject declaration](summary-release-highlights.md)
