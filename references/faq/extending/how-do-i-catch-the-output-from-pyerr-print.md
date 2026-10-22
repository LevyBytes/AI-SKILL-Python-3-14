# How do I catch the output from PyErr_Print() (or anything that prints to stdout/stderr)?

### How do I catch the output from PyErr_Print() (or anything that prints to stdout/stderr)?

Within Python code, build an object that implements the `write()` method. Bind that object to [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout) along with [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr). Either invoke print_error or simply let the usual traceback machinery run its course. From then on, the output lands wherever your `write()` method directs it.

Leaning on the [`io.StringIO`](https://docs.python.org/3.14/library/io.html#io.StringIO) class is the simplest path:

```pycon
>>> import io, sys
>>> sys.stdout = io.StringIO()
>>> print('foo')
>>> print('hello world!')
>>> sys.stderr.write(sys.stdout.getvalue())
foo
hello world!

```

A bespoke object accomplishing the very same thing might read as follows:

```pycon
>>> import io, sys
>>> class StdoutCatcher(io.TextIOBase):
...     def __init__(self):
...         self.data = []
...     def write(self, stuff):
...         self.data.append(stuff)
...
>>> import sys
>>> sys.stdout = StdoutCatcher()
>>> print('foo')
>>> print('hello world!')
>>> sys.stderr.write(''.join(sys.stdout.data))
foo
hello world!

```

[Subject index](INDEX.md)
