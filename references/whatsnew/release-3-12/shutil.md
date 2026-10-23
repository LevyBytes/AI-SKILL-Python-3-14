# What’s New In Python 3.12 / shutil - shutil

### shutil

- [`shutil.make_archive()`](https://docs.python.org/3.14/library/shutil.html#shutil.make_archive) now forwards the *root_dir* argument to custom archivers that can accept it. When that happens it stops momentarily switching the process’s current working directory to *root_dir* while archiving. (Contributed by Serhiy Storchaka in [gh-74696](https://github.com/python/cpython/issues/74696).)

- [`shutil.rmtree()`](https://docs.python.org/3.14/library/shutil.html#shutil.rmtree) now takes a fresh argument *onexc*, an error handler resembling *onerror* except that it expects an exception instance in place of a *(typ, val, tb)* triplet; the older *onerror* has been deprecated. (Contributed by Irit Katriel in [gh-102828](https://github.com/python/cpython/issues/102828).)

- [`shutil.which()`](https://docs.python.org/3.14/library/shutil.html#shutil.which) now reads the *PATHEXT* environment variable to locate matches inside *PATH* on Windows, even where the supplied *cmd* carries a directory component. (Contributed by Charles Machalow in [gh-103179](https://github.com/python/cpython/issues/103179).)

[`shutil.which()`](https://docs.python.org/3.14/library/shutil.html#shutil.which) will invoke `NeedCurrentDirectoryForExePathW` while looking up executables on Windows to work out whether the current working directory belongs at the front of the search path. (Contributed by Charles Machalow in [gh-103179](https://github.com/python/cpython/issues/103179).)

[`shutil.which()`](https://docs.python.org/3.14/library/shutil.html#shutil.which) will give back a path matching the *cmd* together with a component drawn from `PATHEXT` ahead of any direct match found elsewhere across the search path on Windows. (Contributed by Charles Machalow in [gh-103179](https://github.com/python/cpython/issues/103179).)

[Subject index](INDEX.md) · [Previous source section](random.md) · [Next source section](sqlite3.md) · [Release/subject declaration](summary-release-highlights.md)
