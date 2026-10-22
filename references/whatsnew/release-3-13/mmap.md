# What's New In Python 3.13 / mmap — mmap

### mmap

- On Windows, [`mmap`](https://docs.python.org/3.14/library/mmap.html#mmap.mmap) is now guarded against crashes when the mapped region cannot be reached owing to file system faults or access violations. (Contributed by Jannis Weigend in [gh-118209](https://github.com/python/cpython/issues/118209).)

- A fresh [`seekable()`](https://docs.python.org/3.14/library/mmap.html#mmap.mmap.seekable) method on [`mmap`](https://docs.python.org/3.14/library/mmap.html#mmap.mmap) serves callers that expect a seekable file-like object. Its [`seek()`](https://docs.python.org/3.14/library/mmap.html#mmap.mmap.seek) method has been updated to hand back the resulting absolute position. (Contributed by Donghee Na and Sylvie Liberman in [gh-111835](https://github.com/python/cpython/issues/111835).)

- A UNIX-only *trackfd* parameter has been introduced for [`mmap`](https://docs.python.org/3.14/library/mmap.html#mmap.mmap) to govern file descriptor duplication; when false, the descriptor named by *fileno* is not duplicated. (Contributed by Zackery Spytz and Petr Viktorin in [gh-78502](https://github.com/python/cpython/issues/78502).)

[Subject index](INDEX.md) · [Previous source section](mimetypes.md) · [Next source section](multiprocessing.md) · [Release/subject declaration](summary-release-highlights.md)
