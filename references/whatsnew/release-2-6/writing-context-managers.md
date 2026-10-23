# What’s New in Python 2.6 / Writing Context Managers - sys

### Writing Context Managers

Beneath the surface, the ‘[`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)’ statement is rather involved. Since the majority of people will simply pair ‘`with`’ with objects that already exist and have no need for these particulars, you’re welcome to skip the remainder of this section. Anyone authoring new objects, though, will have to grasp how the underlying mechanism works and ought to read on.

Here is the context management protocol described at a high level:

- The expression gets evaluated and ought to produce an object termed a “context manager”. That context manager is required to provide [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) and [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) methods.

- A call is made to the context manager’s [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) method. Whatever it returns gets assigned to *VAR*. Lacking an `as VAR` clause, that returned value is just thrown away.

- The code in *BLOCK* is executed.

- Should *BLOCK* throw an exception, the context manager’s [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) method is invoked with three arguments — the details of the exception (`type, value, traceback`, the identical values that [`sys.exc_info()`](https://docs.python.org/3.14/library/sys.html#sys.exc_info) hands back, which may instead be `None` when no exception arose). Whether the exception is raised once more hinges on the method’s return value: a false result re-raises it, whereas `True` causes the exception to be suppressed. Suppressing the exception is something you’ll want only on rare occasions, since doing so means the author of the code wrapping the ‘[`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)’ statement will have no clue that anything failed.

- Should *BLOCK* finish without throwing an exception, the [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) method still runs, but *type*, *value*, and *traceback* are all `None`.

Consider an example to work through. Instead of full code, I’ll merely outline the methods you’d need for a database that handles transactions.

(If you’re not acquainted with database vocabulary: a collection of modifications to the database is bundled together into a transaction. A transaction may be committed, which writes every change into the database, or rolled back, which throws away all the changes and leaves the database as it was. Any database textbook will tell you more.)

Suppose we have an object that stands for a database connection. What we’re after is to let the user write code along these lines:

```python
db_connection = DatabaseConnection()
with db_connection as cursor:
    cursor.execute('insert into ...')
    cursor.execute('delete from ...')
    # ... more operations ...

```

If the code in the block executes without a hitch the transaction ought to be committed, and rolled back when an exception turns up. Below is the bare-bones interface I’ll take for granted for `DatabaseConnection`:

```python
class DatabaseConnection:
    # Database interface
    def cursor(self):
        "Returns a cursor object and starts a new transaction"
    def commit(self):
        "Commits current transaction"
    def rollback(self):
        "Rolls back current transaction"

```

The [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) method is quite simple, since all it must do is open a new transaction. Because the cursor object it yields would be handy here, the method returns it. From there the user can tack `as cursor` onto their ‘[`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with)’ statement to attach the cursor to a variable name.

```python
class DatabaseConnection:
    ...
    def __enter__(self):
        # Code to start a new transaction
        cursor = self.cursor()
        return cursor

```

Of the two, the [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) method carries the most complexity, since it’s the place where the bulk of the work lands. It needs to determine whether an exception came up. When none did, the transaction gets committed. Should an exception have happened, the transaction is rolled back.

In the code that follows, control will simply run off the end of the function, handing back the default value of `None`. Since `None` counts as false, the exception gets re-raised on its own. If you prefer, you could spell it out more plainly by inserting a [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return) statement at the spot that’s marked.

```python
class DatabaseConnection:
    ...
    def __exit__(self, type, value, tb):
        if tb is None:
            # No exception, so commit
            self.commit()
        else:
            # Exception occurred, so rollback.
            self.rollback()
            # return False

```

[Subject index](INDEX.md) · [Previous source section](pep-343-the-with-statement.md) · [Release/subject declaration](python-3-0.md) · [Next source section](the-contextlib-module.md)
