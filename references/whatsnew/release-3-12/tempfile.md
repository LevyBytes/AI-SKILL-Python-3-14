# What’s New In Python 3.12 / tempfile — tempfile

### tempfile

- A fresh optional argument *delete_on_close* has been added to the [`tempfile.NamedTemporaryFile`](https://docs.python.org/3.14/library/tempfile.html#tempfile.NamedTemporaryFile) function (Contributed by Evgeny Zorin in [gh-58451](https://github.com/python/cpython/issues/58451).)

- Whenever a relative path reaches the *dir* parameter, [`tempfile.mkdtemp()`](https://docs.python.org/3.14/library/tempfile.html#tempfile.mkdtemp) still hands back an absolute path.

[Subject index](INDEX.md) · [Previous source section](sys.md) · [Next source section](threading.md) · [Release/subject declaration](summary-release-highlights.md)
