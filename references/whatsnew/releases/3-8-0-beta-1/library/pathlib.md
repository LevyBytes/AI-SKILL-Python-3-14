# Python 3.8.0 beta 1 / library / pathlib

[bpo-36832](https://bugs.python.org/issue?@action=redirect&bpo=36832): Adds `zipfile.Path`, a wrapper compatible with pathlib for walking through zip archives.

[bpo-33123](https://bugs.python.org/issue?@action=redirect&bpo=33123): [`pathlib.Path.unlink`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.unlink) now takes a *missing_ok* parameter that keeps a [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError) from surfacing. Robert Buchholz supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
