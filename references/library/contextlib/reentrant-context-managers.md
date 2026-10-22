# contextlib — Reentrant context managers

### Reentrant context managers

Fancier context managers can be “reentrant”. Beyond serving several [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statements, such ones may even appear *inside* a `with` statement that is currently driving the very same context manager.

[`threading.RLock`](https://docs.python.org/3.14/library/threading.html#threading.RLock) counts as a reentrant context manager, and so do `suppress()`, `redirect_stdout()`, and `chdir()`. A bare-bones demonstration of reentrant use follows:

```python
>>> from contextlib import redirect_stdout
>>> from io import StringIO
>>> stream = StringIO()
>>> write_to_stream = redirect_stdout(stream)
>>> with write_to_stream:
...     print("This is written to the stream rather than stdout")
...     with write_to_stream:
...         print("This is also written to the stream")
...
>>> print("This is written directly to stdout")
This is written directly to stdout
>>> print(stream.getvalue())
This is written to the stream rather than stdout
This is also written to the stream

```

Out in practice, reentrancy tends to show up across several functions invoking one another, making it considerably more involved than what you see here.

Keep in mind too that reentrancy is *not* equivalent to thread safety. Take `redirect_stdout()`: it is decidedly not thread safe, because it alters global system state by pointing [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout) at another stream.

[Subject index](INDEX.md) · [Previous](single-use-reusable-and-reentrant-context-managers.md) · [Continue](reusable-context-managers.md) · [Owning module, declaration or section: contextlib](contextlib-utilities-for-with-statement-contexts.md)
