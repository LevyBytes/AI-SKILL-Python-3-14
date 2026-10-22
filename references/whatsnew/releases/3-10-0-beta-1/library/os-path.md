# Python 3.10.0 beta 1 / library / os path

[bpo-25264](https://bugs.python.org/issue?@action=redirect&bpo=25264): [`os.path.realpath()`](https://docs.python.org/3.14/library/os.path.html#os.path.realpath) now takes a *strict* keyword-only argument. With it set to `True`, an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) gets raised should a path be missing or a symlink loop turn up.

[bpo-39899](https://bugs.python.org/issue?@action=redirect&bpo=39899): When the basename of the current user's home directory differs from their username, [`os.path.expanduser()`](https://docs.python.org/3.14/library/os.path.html#os.path.expanduser) will no longer try to infer Windows home directories.

For a home directory that cannot be resolved, [`pathlib.Path.expanduser()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.expanduser) and [`home()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.home) now uniformly raise a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) exception. Formerly, an unset `"USERNAME"` environment variable on Windows could trigger a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) exception instead.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
