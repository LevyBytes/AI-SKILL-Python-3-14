# What’s New in Python 2.6 / Interpreter Changes

### Interpreter Changes

A pair of command-line switches are now set aside for the benefit of alternative Python implementations. Jython claims the `-J` switch for Jython-specific options, for instance flags forwarded to the JVM underneath. [`-X`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) is set aside for choices peculiar to a given Python implementation, whether CPython, Jython, or IronPython. Pass either one to Python 2.6 and the interpreter announces that the switch is not in use at the moment.

You can stop Python from emitting `.pyc` or `.pyo` files either by handing the [`-B`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-B) switch to the interpreter or by defining the [`PYTHONDONTWRITEBYTECODE`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE) environment variable ahead of launching it. Programs can read this state through the `sys.dont_write_bytecode` variable, and code is free to overwrite that value to alter how the interpreter behaves. (Contributed by Neal Norwitz and Georg Brandl.)

You can pick the encoding for standard input, standard output, and standard error by defining the [`PYTHONIOENCODING`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONIOENCODING) environment variable before the interpreter starts. Its value is expected as a string shaped like `<encoding>` or `<encoding>:<errorhandler>`. The *encoding* portion names the encoding, for example `utf-8` or `latin-1`; the optional *errorhandler* portion describes how to treat characters the encoding cannot represent and must be one of “error”, “ignore”, or “replace”. (Contributed by Martin von Löwis.)

[Subject index](INDEX.md) · [Previous source section](optimizations.md) · [Next source section](standard-library-module-changes.md) · [Release/subject declaration](python-3-0.md)
