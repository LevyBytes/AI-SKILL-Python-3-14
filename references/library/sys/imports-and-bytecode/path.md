# sys.path

sys.path

A list of strings that lays out the search path for modules. It is initialized from the environment variable [`PYTHONPATH`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPATH), together with an installation-dependent default.

By default, when it is initialized at program startup, a potentially unsafe path gets prepended to `sys.path` (*before* the entries added because of [`PYTHONPATH`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPATH)):

- `python -m module` command line: the current working directory is prepended.

- `python script.py` command line: the directory holding the script is prepended; should that directory be a symbolic link, the links get resolved.

- `python -c code` together with the plain `python` (REPL) command lines: an empty string is prepended, signifying the current working directory.

To stop this potentially unsafe path from being prepended, apply the [`-P`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-P) command line option or the [`PYTHONSAFEPATH`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONSAFEPATH) environment variable.

A program may freely change this list to suit its own needs. Append only strings to `sys.path`; any other data type is disregarded while importing.

See also

- Module [`site`](https://docs.python.org/3.14/library/site.html#module-site) This explains how to employ .pth files to extend `sys.path`.

[API family](INDEX.md) · [sys context index](../INDEX.md).
