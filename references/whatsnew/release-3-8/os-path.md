# What’s New In Python 3.8 / os.path - os.path

### os.path

The boolean-returning [`os.path`](https://docs.python.org/3.14/library/os.path.html#module-os.path) helpers, such as [`exists()`](https://docs.python.org/3.14/library/os.path.html#os.path.exists), [`lexists()`](https://docs.python.org/3.14/library/os.path.html#os.path.lexists), [`isdir()`](https://docs.python.org/3.14/library/os.path.html#os.path.isdir), [`isfile()`](https://docs.python.org/3.14/library/os.path.html#os.path.isfile), [`islink()`](https://docs.python.org/3.14/library/os.path.html#os.path.islink), and [`ismount()`](https://docs.python.org/3.14/library/os.path.html#os.path.ismount), henceforth yield `False` rather than throwing [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) (or the [`UnicodeEncodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeEncodeError) and [`UnicodeDecodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeDecodeError) subclasses) when a path holds characters or bytes that the OS layer cannot represent. (Contributed by Serhiy Storchaka in [bpo-33721](https://bugs.python.org/issue?@action=redirect&bpo=33721).)

Under Windows, [`expanduser()`](https://docs.python.org/3.14/library/os.path.html#os.path.expanduser) now favors the `USERPROFILE` environment variable and skips `HOME`, a value that ordinary user accounts do not usually have set. (Contributed by Anthony Sottile in [bpo-36264](https://bugs.python.org/issue?@action=redirect&bpo=36264).)

Under Windows, [`isdir()`](https://docs.python.org/3.14/library/os.path.html#os.path.isdir) no longer reports `True` when given a link aimed at a directory that does not exist.

Under Windows, [`realpath()`](https://docs.python.org/3.14/library/os.path.html#os.path.realpath) henceforth resolves reparse points, symlinks and directory junctions included.

(Contributed by Steve Dower in [bpo-37834](https://bugs.python.org/issue?@action=redirect&bpo=37834).)

[Subject index](INDEX.md) · [Previous source section](os.md) · [Next source section](pathlib.md) · [Release/subject declaration](assignment-expressions.md)
