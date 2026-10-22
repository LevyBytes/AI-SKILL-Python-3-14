# Python 3.7.0 alpha 3 / library / netrc

[bpo-28334](https://bugs.python.org/issue?@action=redirect&bpo=28334): Within [`netrc.netrc`](https://docs.python.org/3.14/library/netrc.html#netrc.netrc), the `~/.netrc` file is now located via [`os.path.expanduser()`](https://docs.python.org/3.14/library/os.path.html#os.path.expanduser). When that file is absent, [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError) gets raised. Dimitri Merejkowsky authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
