# Python 3.11.0 alpha 1 / library / shutil

[bpo-41928](https://bugs.python.org/issue?@action=redirect&bpo=41928): [`shutil.copyfile()`](https://docs.python.org/3.14/library/shutil.html#shutil.copyfile) was updated to raise [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError) rather than the puzzling [`IsADirectoryError`](https://docs.python.org/3.14/library/exceptions.html#IsADirectoryError) when a path that ends in a `os.path.sep` is missing; [`shutil.copy()`](https://docs.python.org/3.14/library/shutil.html#shutil.copy) plus [`shutil.copy2()`](https://docs.python.org/3.14/library/shutil.html#shutil.copy2) share the change.

[bpo-45234](https://bugs.python.org/issue?@action=redirect&bpo=45234): Addressed a regression whereby [`copyfile()`](https://docs.python.org/3.14/library/shutil.html#shutil.copyfile), [`copy()`](https://docs.python.org/3.14/library/shutil.html#shutil.copy), and [`copy2()`](https://docs.python.org/3.14/library/shutil.html#shutil.copy2) emitted [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError) for a directory source, when the correct exception is [`IsADirectoryError`](https://docs.python.org/3.14/library/exceptions.html#IsADirectoryError)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
