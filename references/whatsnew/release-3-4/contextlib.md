# What's New In Python 3.4 / contextlib - contextlib, io, sys

### contextlib

The fresh [`contextlib.suppress`](https://docs.python.org/3.14/library/contextlib.html#contextlib.suppress) context manager makes plain the intent behind code that purposely swallows exceptions raised by a single statement. (Contributed by Raymond Hettinger in [bpo-15806](https://bugs.python.org/issue?@action=redirect&bpo=15806) and Zero Piraeus in [bpo-19266](https://bugs.python.org/issue?@action=redirect&bpo=19266).)

The fresh [`contextlib.redirect_stdout()`](https://docs.python.org/3.14/library/contextlib.html#contextlib.redirect_stdout) context manager eases the job of utility scripts that must cope with rigid APIs writing their results to [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout) while offering no knob to redirect it. With this context manager, the `sys.stdout` output can flow to any other stream, or ? together with [`io.StringIO`](https://docs.python.org/3.14/library/io.html#io.StringIO) ? into a string. That second route shines, say, when you want to grab output from a function written to power a command line interface. Reserve it for utility scripts, since it mutates the global state of `sys.stdout`. (Contributed by Raymond Hettinger in [bpo-15805](https://bugs.python.org/issue?@action=redirect&bpo=15805).)

The [`contextlib`](https://docs.python.org/3.14/library/contextlib.html#module-contextlib) documentation has likewise been revised to add a [discussion](https://docs.python.org/3.14/library/contextlib.html#single-use-reusable-and-reentrant-cms) covering how single use, reusable and reentrant context managers differ.

[Subject index](INDEX.md) · [Previous source section](colorsys.md) · [Next source section](dbm.md) · [Release/subject declaration](release-highlights.md)
