# What’s New in Python 2.6 / The contextlib module - contextlib

### The contextlib module

The [`contextlib`](https://docs.python.org/3.14/library/contextlib.html#module-contextlib) module supplies a few functions plus a decorator that come in handy when you author objects intended for the ‘[`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)’ statement.

That decorator goes by [`contextmanager()`](https://docs.python.org/3.14/library/contextlib.html#contextlib.contextmanager), and it lets you author one generator function rather than declaring a whole new class. The generator is meant to yield precisely one value. Everything leading up to the [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) runs as the [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) method, and the yielded value becomes the method’s return value, which gets bound to the variable in the `as` clause of the ‘[`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)’ statement, should one be present. Whatever comes after the `yield` runs inside the [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) method. The `yield` statement re-raises any exception thrown within the block.

With this decorator in hand, the database example from the section above could be expressed like so:

```python
from contextlib import contextmanager

@contextmanager
def db_transaction(connection):
    cursor = connection.cursor()
    try:
        yield cursor
    except:
        connection.rollback()
        raise
    else:
        connection.commit()

db = DatabaseConnection()
with db_transaction(db) as cursor:
    ...

```

The [`contextlib`](https://docs.python.org/3.14/library/contextlib.html#module-contextlib) module additionally provides a `nested(mgr1, mgr2, ...)` function that bundles several context managers together so you’re spared from nesting ‘[`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)’ statements. Here, one ‘`with`’ statement opens a database transaction and grabs a thread lock at the same time:

```python
lock = threading.Lock()
with nested (db_transaction(db), lock) as (cursor, locked):
    ...

```

Lastly, the [`closing()`](https://docs.python.org/3.14/library/contextlib.html#contextlib.closing) function passes its argument back so you can bind it to a variable, then invokes that argument’s `.close()` method when the block wraps up.

```python
import urllib, sys
from contextlib import closing

with closing(urllib.urlopen('http://www.yahoo.com')) as f:
    for line in f:
        sys.stdout.write(line)

```

See also

[**PEP 343**](https://peps.python.org/pep-0343/) - The “with” statement

PEP authored by Guido van Rossum and Nick Coghlan; built by Mike Bland, Guido van Rossum, and Neal Norwitz. Within the PEP you’ll see the code that a ‘[`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)’ statement compiles to, a useful aid for understanding how the statement operates.

The documentation for the [`contextlib`](https://docs.python.org/3.14/library/contextlib.html#module-contextlib) module.

[Subject index](INDEX.md) · [Previous source section](writing-context-managers.md) · [Next source section](pep-366-explicit-relative-imports-from-a-main-module.md) · [Release/subject declaration](python-3-0.md)
