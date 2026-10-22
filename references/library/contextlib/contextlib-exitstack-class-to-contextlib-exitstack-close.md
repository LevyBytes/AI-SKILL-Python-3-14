# contextlib / Utilities: `contextlib.ExitStack`, `enter_context()`, `push()`, `callback()`, `pop_all()`, `close()`

*class *contextlib.ExitStack

A context manager crafted to simplify combining other context managers and cleanup functions programmatically, particularly when they are optional or otherwise dictated by input data.

To illustrate, a collection of files can be dealt with comfortably inside a single with statement in this fashion:

```python
with ExitStack() as stack:
    files = [stack.enter_context(open(fname)) for fname in filenames]
    # All opened files will automatically be closed at the end of
    # the with statement, even if attempts to open files later
    # in the list raise an exception

```

Its [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) method returns the `ExitStack` instance itself and carries out nothing further.

Every instance keeps a stack of enrolled callbacks, which fire in reverse sequence the moment the instance closes (whether explicitly or implicitly once a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement ends). Be aware that these callbacks are *not* triggered implicitly when the context stack instance is garbage collected.

Adopting this stack model means context managers that grab their resources within their `__init__` method (file objects among them) get handled properly.

Given that enrolled callbacks run in the opposite order to how they were registered, the net effect mirrors stacking several nested [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statements around the registered callbacks. The behavior even reaches exception handling — should an inner callback swallow or substitute an exception, the outer callbacks receive arguments reflecting that revised state.

This counts as a fairly low level API that handles the intricacies of unwinding the exit callback stack correctly. It supplies a solid base on which higher level context managers can manipulate the exit stack in ways specific to an application.

Added in version 3.3.

 enter_context(*cm*)

Enters a new context manager and appends its [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) method onto the callback stack. What gets returned is the outcome of that context manager's own [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) method.

Such context managers are free to swallow exceptions exactly as they would were they wired directly into a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement.

Changed in version 3.11: when *cm* is not a context manager, [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is now raised rather than [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError).

 push(*exit*)

Appends a context manager's [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) method onto the callback stack.

Because `__enter__` is *not* called, this method serves to guard part of an [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) implementation using a context manager's own [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) method.

When handed an object that isn't a context manager, this method takes it to be a callback bearing the same signature as a context manager's [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) method and places it straight onto the callback stack.

By handing back true values, these callbacks can swallow exceptions in the same manner that context manager [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__) methods do.

The object that was passed in is returned from the function, which lets this method double as a function decorator.

 callback(*callback*, */*, **args*, ***kwds*)

Takes any callback function plus arguments and pushes it onto the callback stack.

In contrast with the other methods, callbacks registered through this route cannot swallow exceptions (since the exception details are never handed to them).

The callback that was passed in is returned from the function, which lets this method double as a function decorator.

 pop_all()

Moves the callback stack over to a brand-new `ExitStack` instance and returns it. This operation fires no callbacks — rather, they will now run once the new stack closes (whether explicitly or implicitly at the close of a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement).

To illustrate, a batch of files can be opened as an "all or nothing" operation in this manner:

```python
with ExitStack() as stack:
    files = [stack.enter_context(open(fname)) for fname in filenames]
    # Hold onto the close method, but don't call it yet.
    close_files = stack.pop_all().close
    # If opening any file fails, all previously opened files will be
    # closed automatically. If all files are opened successfully,
    # they will remain open even after the with statement ends.
    # close_files() can then be invoked explicitly to close them all.

```

 close()

Unwinds the callback stack right away, firing callbacks in the reverse order to their registration. For whatever context managers and exit callbacks were registered, the arguments handed in will signal that no exception arose.

[Subject index](INDEX.md) · [Previous](contextlib-asynccontextdecorator-class.md) · [Continue](async-exit-stack-contexts-and-callbacks.md) · [Owning module, declaration or section: contextlib](contextlib-utilities-for-with-statement-contexts.md) · [Owning module, declaration or section: Utilities](contextlib-abstractcontextmanager-class.md)
