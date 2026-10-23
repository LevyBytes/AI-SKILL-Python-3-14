# contextlib - Replacing any use of `try-finally` and flag variables

### Replacing any use of `try-finally` and flag variables

One construct that crops up occasionally is a `try-finally` statement paired with a flag variable that records whether the `finally` clause's body ought to run. At its most basic (the kind that an `except` clause alone couldn't already cover), it resembles the following:

```python
cleanup_needed = True
try:
    result = perform_operation()
    if result:
        cleanup_needed = False
finally:
    if cleanup_needed:
        cleanup_resources()

```

Like all code built around a `try` statement, this hampers both writing and reviewing, since the setup portion and the teardown portion may wind up split apart by stretches of code of any length.

With `ExitStack` you can instead enqueue a callback to fire as a `with` statement closes, then afterward choose to bypass running that callback:

```python
from contextlib import ExitStack

with ExitStack() as stack:
    stack.callback(cleanup_resources)
    result = perform_operation()
    if result:
        stack.pop_all()

```

That way the cleanup you have in mind is stated plainly at the outset, with no extra flag variable needed.

When some program leans on this construct repeatedly, a tiny helper class can streamline it further still:

```python
from contextlib import ExitStack

class Callback(ExitStack):
    def __init__(self, callback, /, *args, **kwds):
        super().__init__()
        self.callback(callback, *args, **kwds)

    def cancel(self):
        self.pop_all()

with Callback(cleanup_resources) as cb:
    result = perform_operation()
    if result:
        cb.cancel()

```

Should the resource cleanup not already sit packaged inside its own function, you can still reach for the decorator flavor of `ExitStack.callback()` to spell out that cleanup ahead of time:

```python
from contextlib import ExitStack

with ExitStack() as stack:
    @stack.callback
    def cleanup_resources():
        ...
    result = perform_operation()
    if result:
        stack.pop_all()

```

Because of how the decorator protocol operates, a callback function written like this accepts no parameters whatsoever. Anything you intend to release therefore has to be reached as a closure variable.

[Subject index](INDEX.md) · [Previous](cleaning-up-in-an-enter-implementation.md) · [Continue](using-a-context-manager-as-a-function-decorator.md) · [Owning module, declaration or section: contextlib](contextlib-utilities-for-with-statement-contexts.md)
