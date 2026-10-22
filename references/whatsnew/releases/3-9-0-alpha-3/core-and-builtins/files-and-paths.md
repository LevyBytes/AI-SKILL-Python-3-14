# Python 3.9.0 alpha 3 / core and builtins / files and paths

[bpo-13601](https://bugs.python.org/issue?@action=redirect&bpo=13601): The default behavior of `sys.stderr` is now line-buffered, including the case where `stderr` is redirected toward a file. To turn off buffering on `sys.stderr`, you can still supply the [`-u`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-u) command-line option or define the [`PYTHONUNBUFFERED`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONUNBUFFERED) environment variable.

Jendrik Seipp landed this work ([bpo-13601](https://bugs.python.org/issue?@action=redirect&bpo=13601)).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
