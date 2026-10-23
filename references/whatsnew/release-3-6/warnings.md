# What's New In Python 3.6 / warnings - tracemalloc, warnings

### warnings

A fresh optional *source* parameter joined the [`warnings.warn_explicit()`](https://docs.python.org/3.14/library/warnings.html#warnings.warn_explicit) function: the discarded object responsible for raising a [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning). A *source* attribute likewise joined `warnings.WarningMessage` (contributed by Victor Stinner in [bpo-26568](https://bugs.python.org/issue?@action=redirect&bpo=26568) and [bpo-26567](https://bugs.python.org/issue?@action=redirect&bpo=26567)).

Whenever a [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning) warning gets logged, the [`tracemalloc`](https://docs.python.org/3.14/library/tracemalloc.html#module-tracemalloc) module is now leveraged to attempt to recover the traceback marking where the discarded object had been allocated.

Example with the script `example.py`:

```python
import warnings

def func():
    return open(__file__)

f = func()
f = None

```

Output of the command `python3.6 -Wd -X tracemalloc=5 example.py`:

```python
example.py:7: ResourceWarning: unclosed file <_io.TextIOWrapper name='example.py' mode='r' encoding='UTF-8'>
  f = None
Object allocated at (most recent call first):
  File "example.py", lineno 4
    return open(__file__)
  File "example.py", lineno 6
    f = func()

```

That "Object allocated at" traceback is a new addition and surfaces only when [`tracemalloc`](https://docs.python.org/3.14/library/tracemalloc.html#module-tracemalloc) happens to be tracing Python memory allocations and when the [`warnings`](https://docs.python.org/3.14/library/warnings.html#module-warnings) module had already been imported.

[Subject index](INDEX.md) · [Previous source section](venv.md) · [Next source section](winreg.md) · [Release/subject declaration](summary-release-highlights.md)
