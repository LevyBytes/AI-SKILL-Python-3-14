# What's new in Python 3.14 / Concurrent safe warnings control — sys, warnings

> (Contributed by Pablo Galindo, Łukasz Langa, Yury Selivanov, and Marta Gomez Macias in [gh-91048](https://github.com/python/cpython/issues/91048).)

### Concurrent safe warnings control

It is now possible for the [`warnings.catch_warnings`](https://docs.python.org/3.14/library/warnings.html#warnings.catch_warnings) context manager to optionally rely on a context variable to hold warning filters. You turn this on by setting the [`context_aware_warnings`](https://docs.python.org/3.14/library/sys.html#sys.flags.context_aware_warnings) flag, whether through the `-X` command-line option or an environment variable. The result is dependable warnings control whenever `catch_warnings` is paired with several threads or asynchronous tasks. For the free-threaded build the flag defaults to true, whereas the GIL-enabled build defaults it to false.

(Contributed by Neil Schemenauer and Kumar Aditya in [gh-130010](https://github.com/python/cpython/issues/130010).)

[Subject index](INDEX.md) · [Previous source section](asyncio-task-tree-output.md) · [Next source section](other-language-changes.md) · [Release/subject declaration](summary-release-highlights.md)
