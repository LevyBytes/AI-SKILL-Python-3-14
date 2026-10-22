# Python 3.14.0 beta 1 / library / cmd

[gh-133363](https://github.com/python/cpython/issues/133363): The [`cmd.Cmd`](https://docs.python.org/3.14/library/cmd.html#cmd.Cmd) class now dependably invokes the `completedefault` method in cases where `do_shell` is absent and tab completion runs for a line that starts with `!`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
