# Python 3.6.0 alpha 1 / core and builtins / debug

[bpo-26516](https://bugs.python.org/issue?@action=redirect&bpo=26516): Introduce the [`PYTHONMALLOC`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONMALLOC) environment variable, which selects the Python memory allocators and can also install debug hooks.

[bpo-26516](https://bugs.python.org/issue?@action=redirect&bpo=26516): When Python has been configured without pymalloc, debug mode now still places debug hooks onto the Python memory allocators.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
