# What's new in Python 3.14 / os - os

### os

- Add the [`reload_environ()`](https://docs.python.org/3.14/library/os.html#os.reload_environ) function so that [`os.environ`](https://docs.python.org/3.14/library/os.html#os.environ) and [`os.environb`](https://docs.python.org/3.14/library/os.html#os.environb) pick up environment edits performed through [`os.putenv()`](https://docs.python.org/3.14/library/os.html#os.putenv), through [`os.unsetenv()`](https://docs.python.org/3.14/library/os.html#os.unsetenv), or applied outside of Python within the same process. (Contributed by Victor Stinner in [gh-120057](https://github.com/python/cpython/issues/120057).)

- Add the [`SCHED_DEADLINE`](https://docs.python.org/3.14/library/os.html#os.SCHED_DEADLINE) and [`SCHED_NORMAL`](https://docs.python.org/3.14/library/os.html#os.SCHED_NORMAL) constants to the `os` module. (Contributed by James Roy in [gh-127688](https://github.com/python/cpython/issues/127688).)

- Add the [`readinto()`](https://docs.python.org/3.14/library/os.html#os.readinto) function for reading out of a file descriptor straight into a [buffer object](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects). (Contributed by Cody Maloney in [gh-129205](https://github.com/python/cpython/issues/129205).)

[Subject index](INDEX.md) · [Previous source section](operator.md) · [Next source section](os-path.md) · [Release/subject declaration](summary-release-highlights.md)
