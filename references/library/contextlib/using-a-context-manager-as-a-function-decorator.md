# contextlib - Using a context manager as a function decorator

### Using a context manager as a function decorator

`ContextDecorator` lets a single context manager serve double duty: as a plain `with` statement and equally as a function decorator.

As an illustration, you might want to surround functions or blocks of statements with a logger noting when control enters and when it leaves. Instead of authoring a function decorator and a context manager separately for that, deriving from `ContextDecorator` hands you both abilities from one class:

```python
from contextlib import ContextDecorator
import logging

logging.basicConfig(level=logging.INFO)

class track_entry_and_exit(ContextDecorator):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        logging.info('Entering: %s', self.name)

    def __exit__(self, exc_type, exc, exc_tb):
        logging.info('Exiting: %s', self.name)

```

Instances of this class can be used as both a context manager:

```python
with track_entry_and_exit('widget loader'):
    print('Some time consuming activity goes here')
    load_widget()

```

And also as a function decorator:

```python
@track_entry_and_exit('widget loader')
def activity():
    print('Some time consuming activity goes here')
    load_widget()

```

Bear in mind one further restriction when context managers act as function decorators: the value that [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) returns stays out of reach. Whenever you actually require that value, an explicit `with` statement remains unavoidable.

See also

[**PEP 343**](https://peps.python.org/pep-0343/) - The “with” statement

Covers the formal definition, the motivation, and sample usage of Python's [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement.

[Subject index](INDEX.md) · [Previous](replacing-any-use-of-try-finally-and-flag-variables.md) · [Continue](single-use-reusable-and-reentrant-context-managers.md) · [Owning module, declaration or section: contextlib](contextlib-utilities-for-with-statement-contexts.md)
