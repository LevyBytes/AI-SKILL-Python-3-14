# What’s New In Python 3.5 / shutil — shutil

### shutil

You may now hand the [`move()`](https://docs.python.org/3.14/library/shutil.html#shutil.move) function a *copy_function* argument; this lets you, say, swap in the [`copy()`](https://docs.python.org/3.14/library/shutil.html#shutil.copy) function in place of the default [`copy2()`](https://docs.python.org/3.14/library/shutil.html#shutil.copy2) whenever file metadata should be dropped during a move. Claudiu Popa contributed this (see [bpo-19840](https://bugs.python.org/issue?@action=redirect&bpo=19840)).

The *xztar* format is now among those that the [`make_archive()`](https://docs.python.org/3.14/library/shutil.html#shutil.make_archive) function can produce. Serhiy Storchaka added it (see [bpo-5411](https://bugs.python.org/issue?@action=redirect&bpo=5411)).

[Subject index](INDEX.md) · [Previous source section](selectors.md) · [Next source section](signal.md) · [Release/subject declaration](summary-release-highlights.md)
