# Python 3.8.0 alpha 1 / security / multiprocessing

[bpo-34812](https://bugs.python.org/issue?@action=redirect&bpo=34812): The [`-I`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-I) command line option (run Python in isolated mode) now gets copied too by the [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) and `distutils` modules while they spawn child processes. Formerly, only the [`-E`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-E) and [`-s`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-s) options (turned on by `-I`) were copied.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
