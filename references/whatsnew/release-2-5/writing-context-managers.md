# What's New in Python 2.5 / Writing Context Managers — sys

### Writing Context Managers

Internally, the "[`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)" statement carries quite a bit of machinery. Since most folks will simply pair "`with`" with objects that already exist and never need these specifics, feel free to skip ahead from here. Anyone building new objects, though, will have to grasp how the underlying implementation operates and ought to continue.

Stated at a high level, the context management protocol works like this:

- Evaluating the expression should produce something known as a "context manager". That context manager is required to define [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) and [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) methods.

- Next the context manager's [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) method runs. Whatever it returns gets assigned to *VAR*. When there is no `'as VAR'` clause, that returned value is just thrown away.

- The statements in *BLOCK* then run.

- Should *BLOCK* throw an exception, `__exit__(type, value, traceback)` is invoked with the details of that exception — the very same values you'd get from [`sys.exc_info()`](https://docs.python.org/3.14/library/sys.html#sys.exc_info). What the method returns determines whether the exception propagates again: returning any false value lets the exception re-raise, while `True` causes it to be swallowed. Suppressing an exception is something you'll want only on rare occasions, since doing so means whoever wrote the code wrapping the "[`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)" statement stays unaware that a problem occurred.

- When *BLOCK* finishes without throwing, [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) is invoked anyway, except that *type*, *value*, and *traceback* all arrive as `None`.

Consider a worked example. Rather than full code, I'll merely outline the methods you'd need for a transaction-capable database.

(If database vocabulary is new to you: a collection of modifications to the database gets bundled together as a transaction. A transaction may be committed — meaning every change lands permanently in the database — or rolled back — meaning all the changes are thrown away and the database stays untouched. Consult any database textbook to learn more.)

Suppose we have an object standing in for a database connection. What we're aiming for is to allow the user to write something along these lines:

```python
db_connection = DatabaseConnection()
with db_connection as cursor:
    cursor.execute('insert into ...')
    cursor.execute('delete from ...')
    # ... more operations ...

```

When the block's code completes without trouble the transaction ought to be committed, and rolled back whenever an exception arises. Below is the baseline `DatabaseConnection` interface I'm going to assume:

```python
class DatabaseConnection:
    # Database interface
    def cursor (self):
        "Returns a cursor object and starts a new transaction"
    def commit (self):
        "Commits current transaction"
    def rollback (self):
        "Rolls back current transaction"

```

There's not much to the [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) method — its only job is opening a fresh transaction. Because the cursor object it produces would be handy here, the method returns that cursor. The user is then free to tack `as cursor` onto their "[`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)" statement so the cursor binds to a name.

```python
class DatabaseConnection:
    ...
    def __enter__ (self):
        # Code to start a new transaction
        cursor = self.cursor()
        return cursor

```

Of the two, [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) is the trickier, since this is where the bulk of the work lands. It needs to determine whether an exception was raised. When none was, the transaction gets committed. When one was, the transaction is rolled back.

In the listing that follows, control simply runs off the end of the function, which returns the default `None`. Because `None` is falsy, the exception gets re-raised on its own. Should you prefer, it's possible to be explicit and place a [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return) statement at the indicated spot.

```python
class DatabaseConnection:
    ...
    def __exit__ (self, type, value, tb):
        if tb is None:
            # No exception, so commit
            self.commit()
        else:
            # Exception occurred, so rollback.
            self.rollback()
            # return False

```

[Subject index](INDEX.md) · [Previous source section](pep-343-the-with-statement.md) · [Release/subject declaration](pep-308-conditional-expressions.md) · [Next source section](the-contextlib-module.md)
