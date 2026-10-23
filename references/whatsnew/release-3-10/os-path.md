# What's New In Python 3.10 / os.path - os.path

### os.path

[`os.path.realpath()`](https://docs.python.org/3.14/library/os.path.html#os.path.realpath) now takes a *strict* keyword-only argument. Passing `True` makes [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) get raised should a path be missing or a symlink loop turn up. (Contributed by Barney Gale in [bpo-43757](https://bugs.python.org/issue?@action=redirect&bpo=43757).)

[Subject index](INDEX.md) · [Previous source section](os.md) · [Next source section](pathlib.md) · [Release/subject declaration](summary-release-highlights.md)
