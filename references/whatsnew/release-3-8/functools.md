# What’s New In Python 3.8 / functools - functools

> (Contributed by Paul Ganssle in [bpo-36004](https://bugs.python.org/issue?@action=redirect&bpo=36004).)

### functools

You may now apply [`functools.lru_cache()`](https://docs.python.org/3.14/library/functools.html#functools.lru_cache) directly as a decorator rather than calling it to obtain one. Both spellings below therefore work today:

```python
@lru_cache
def f(x):
    ...

@lru_cache(maxsize=256)
def f(x):
    ...

```

> (Contributed by Raymond Hettinger in [bpo-36772](https://bugs.python.org/issue?@action=redirect&bpo=36772).)

A fresh [`functools.cached_property()`](https://docs.python.org/3.14/library/functools.html#functools.cached_property) decorator has arrived, meant for derived properties that stay cached across an instance's lifetime.

```python
import functools
import statistics

class Dataset:
   def __init__(self, sequence_of_numbers):
      self.data = sequence_of_numbers

   @functools.cached_property
   def variance(self):
      return statistics.variance(self.data)

```

> (Contributed by Carl Meyer in [bpo-21145](https://bugs.python.org/issue?@action=redirect&bpo=21145))

A fresh [`functools.singledispatchmethod()`](https://docs.python.org/3.14/library/functools.html#functools.singledispatchmethod) decorator has also arrived; it turns methods into [generic functions](https://docs.python.org/3.14/glossary.html#term-generic-function) driven by [single dispatch](https://docs.python.org/3.14/glossary.html#term-single-dispatch):

```python
from functools import singledispatchmethod
from contextlib import suppress

class TaskManager:

    def __init__(self, tasks):
        self.tasks = list(tasks)

    @singledispatchmethod
    def discard(self, value):
        with suppress(ValueError):
            self.tasks.remove(value)

    @discard.register(list)
    def _(self, tasks):
        targets = set(tasks)
        self.tasks = [x for x in self.tasks if x not in targets]

```

[Subject index](INDEX.md) · [Previous source section](datetime.md) · [Next source section](gc.md) · [Release/subject declaration](assignment-expressions.md)
