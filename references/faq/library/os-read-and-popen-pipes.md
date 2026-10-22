# I can't seem to use os.read() on a pipe created with os.popen(); why?

### I can't seem to use os.read() on a pipe created with os.popen(); why?

A low-level function, [`os.read()`](https://docs.python.org/3.14/library/os.html#os.read) accepts a file descriptor — a small integer standing for the opened file. By contrast, [`os.popen()`](https://docs.python.org/3.14/library/os.html#os.popen) produces a high-level file object of the same kind the built-in [`open()`](https://docs.python.org/3.14/library/functions.html#open) function returns. So to pull *n* bytes from a pipe *p* made with `os.popen()`, you must call `p.read(n)`.

[Subject index](INDEX.md)
