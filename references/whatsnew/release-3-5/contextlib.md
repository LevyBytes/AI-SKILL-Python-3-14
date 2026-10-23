# What’s New In Python 3.5 / contextlib - contextlib, sys

### contextlib

The fresh [`redirect_stderr()`](https://docs.python.org/3.14/library/contextlib.html#contextlib.redirect_stderr) [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) (a sibling of [`redirect_stdout()`](https://docs.python.org/3.14/library/contextlib.html#contextlib.redirect_stdout)) eases the job for utility scripts that must cope with rigid APIs sending their output to [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr) while offering no way to redirect it:

```python
>>> import contextlib, io, logging
>>> f = io.StringIO()
>>> with contextlib.redirect_stderr(f):
...     logging.warning('warning')
...
>>> f.getvalue()
'WARNING:root:warning\n'

```

(Contributed by Berker Peksag in [bpo-22389](https://bugs.python.org/issue?@action=redirect&bpo=22389).)

[Subject index](INDEX.md) · [Previous source section](configparser.md) · [Next source section](csv.md) · [Release/subject declaration](summary-release-highlights.md)
