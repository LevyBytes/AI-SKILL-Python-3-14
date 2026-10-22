# What's new in Python 3.14 / Other language changes

### Other language changes

- Every Windows code page is now reachable as a ‘cpXXX’ codec on Windows. (Contributed by Serhiy Storchaka in [gh-123803](https://github.com/python/cpython/issues/123803).)

- The mixed-mode arithmetic rules that combine real and complex numbers, as laid out by the C standard from C99 onward, are now implemented. (Contributed by Sergey B Kirpichev in [gh-69639](https://github.com/python/cpython/issues/69639).)

- Additional syntax errors now surface no matter the optimisation level or the [`-O`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-O) command-line option. Covered cases include writes to `__debug__`, misuse of [`await`](https://docs.python.org/3.14/reference/expressions.html#await), and asynchronous comprehensions placed outside asynchronous functions. To illustrate, `python -O -c 'assert (__debug__ := 1)'` or `python -O -c 'assert await 1'` will now raise [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError)s. (Contributed by Irit Katriel and Jelle Zijlstra in [gh-122245](https://github.com/python/cpython/issues/122245) & [gh-121637](https://github.com/python/cpython/issues/121637).)

- While subclassing a pure C type, the C slots belonging to the new type are no longer swapped for a wrapped version at class creation when the subclass leaves them unoverridden. (Contributed by Tomasz Pytel in [gh-132284](https://github.com/python/cpython/issues/132284).)

[Subject index](INDEX.md) · [Previous source section](concurrent-safe-warnings-control.md) · [Next source section](built-ins.md) · [Release/subject declaration](summary-release-highlights.md)
