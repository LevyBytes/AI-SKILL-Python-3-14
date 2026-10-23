# What's New in Python 2.5 / The contextlib module - contextlib

### The contextlib module

A handful of functions plus a decorator, all aimed at making it easier to build objects that work with the "[`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)" statement, are supplied by the new [`contextlib`](https://docs.python.org/3.14/library/contextlib.html#module-contextlib) module.

That decorator, named `contextmanager()`, allows you to author one generator function rather than declaring an entirely new class. Your generator ought to yield precisely one value. Everything leading up to the [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) runs as the [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) method, and the yielded value serves as that method's return value, which binds to the variable named in the "[`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)" statement's `as` clause when one exists. Code positioned after the `yield` runs within the [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) method. Whatever exception is thrown inside the block surfaces at the `yield` statement.

Rewriting the database example from the earlier section with this decorator gives:

```python
from contextlib import contextmanager

@contextmanager
def db_transaction (connection):
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

The [`contextlib`](https://docs.python.org/3.14/library/contextlib.html#module-contextlib) module additionally offers a `nested(mgr1, mgr2, ...)` function for merging several context managers together, sparing you from stacking nested "[`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)" statements. Here the lone "`with`" statement opens a database transaction while also taking a thread lock:

```python
lock = threading.Lock()
with nested (db_transaction(db), lock) as (cursor, locked):
    ...

```

Lastly, the `closing(object)` function gives back *object* so it can bind to a variable, and invokes `object.close` once the block ends.

```python
import urllib, sys
from contextlib import closing

with closing(urllib.urlopen('http://www.yahoo.com')) as f:
    for line in f:
        sys.stdout.write(line)

```

See also

[**PEP 343**](https://peps.python.org/pep-0343/) - The "with" statement

PEP authored by Guido van Rossum and Nick Coghlan; the implementation came from Mike Bland, Guido van Rossum, and Neal Norwitz. The PEP displays the code that gets generated for a "[`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)" statement, which is useful for understanding how the statement operates.

The documentation for the [`contextlib`](https://docs.python.org/3.14/library/contextlib.html#module-contextlib) module.

[Subject index](INDEX.md) · [Previous source section](writing-context-managers.md) · [Next source section](pep-352-exceptions-as-new-style-classes.md) · [Release/subject declaration](pep-308-conditional-expressions.md)
