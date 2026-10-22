# sys.dont_write_bytecode

sys.dont_write_bytecode

When this holds true, Python skips writing `.pyc` files as source modules are imported. The value starts out as `True` or `False` according to the [`-B`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-B) command line option and the [`PYTHONDONTWRITEBYTECODE`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE) environment variable, yet you are free to assign it yourself to govern whether bytecode files are produced.

[API family](INDEX.md) · [sys context index](../INDEX.md).
