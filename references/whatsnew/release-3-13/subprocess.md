# What's New In Python 3.13 / subprocess - os, subprocess

### subprocess

- There are now more scenarios where the [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module reaches for the [`posix_spawn()`](https://docs.python.org/3.14/library/os.html#os.posix_spawn) function.

In particular, with *close_fds* set to `True` (its default), [`posix_spawn()`](https://docs.python.org/3.14/library/os.html#os.posix_spawn) gets used whenever the C library supplies `posix_spawn_file_actions_addclosefrom_np()` ? covering recent Linux, FreeBSD, and Solaris releases. Under Linux the performance should roughly match the current Linux `vfork()` based path.

Should you ever need [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) to avoid [`posix_spawn()`](https://docs.python.org/3.14/library/os.html#os.posix_spawn) entirely, a private toggle `subprocess._USE_POSIX_SPAWN` can be flipped to `False`. If you do, kindly note your motivation and platform on the [issue tracker](https://docs.python.org/3.14/bugs.html#using-the-tracker) so the API selection logic can get better for everybody. (Contributed by Jakub Kulik in [gh-113117](https://github.com/python/cpython/issues/113117).)

[Subject index](INDEX.md) · [Previous source section](statistics.md) · [Next source section](sys.md) · [Release/subject declaration](summary-release-highlights.md)
