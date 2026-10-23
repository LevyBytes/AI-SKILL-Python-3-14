# What's New In Python 3.2 / contextlib - contextlib

### contextlib

A somewhat astonishing new utility, [`ContextDecorator`](https://docs.python.org/3.14/library/contextlib.html#contextlib.ContextDecorator), assists in building a [context manager](https://docs.python.org/3.14/glossary.html#term-context-manager) that simultaneously serves as a function decorator.

For convenience, [`contextmanager()`](https://docs.python.org/3.14/library/contextlib.html#contextlib.contextmanager) already takes advantage of this addition, meaning both roles work with no further effort on your part.

The underlying notion is that pre-action and post-action wrappers can be expressed either way, through context managers or through function decorators. A context manager wraps a block of statements via a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement, while a function decorator wraps statements bundled inside a function. Now and then, therefore, you want a single pre-action or post-action wrapper usable in both capacities.

Consider, say, wrapping functions or statement groups in a logger that records when execution begins and ends. Instead of authoring a separate function decorator alongside a separate context manager, [`contextmanager()`](https://docs.python.org/3.14/library/contextlib.html#contextlib.contextmanager) delivers both abilities from one definition:

```python
from contextlib import contextmanager
import logging

logging.basicConfig(level=logging.INFO)

@contextmanager
def track_entry_and_exit(name):
    logging.info('Entering: %s', name)
    yield
    logging.info('Exiting: %s', name)

```

Earlier on, only the context-manager usage would have been possible:

```python
with track_entry_and_exit('widget loader'):
    print('Some time consuming activity goes here')
    load_widget()

```

These days it serves equally well as a decorator:

```python
@track_entry_and_exit('widget loader')
def activity():
    print('Some time consuming activity goes here')
    load_widget()

```

Asking one object to cover two duties does impose certain constraints. Where a context manager would ordinarily be free to hand back a value usable by a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement, no equivalent path exists for function decorators.

So, in the snippet above, the *track_entry_and_exit* context manager has no tidy means of yielding a logging instance for the enclosed body to use.

(Contributed by Michael Foord in [bpo-9110](https://bugs.python.org/issue?@action=redirect&bpo=9110).)

[Subject index](INDEX.md) · [Previous source section](csv.md) · [Next source section](decimal-and-fractions.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
