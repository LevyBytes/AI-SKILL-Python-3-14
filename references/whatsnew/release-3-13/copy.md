# What's New In Python 3.13 / copy - collections, copy, dataclasses, datetime, inspect, types

### copy

- The fresh [`replace()`](https://docs.python.org/3.14/library/copy.html#copy.replace) function together with the [`replace protocol`](https://docs.python.org/3.14/library/copy.html#object.__replace__) greatly ease producing altered copies of objects. That proves particularly handy with immutable objects. These types below provide the `replace()` function and carry out the replace protocol:

  - [`collections.namedtuple()`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple)

  - [`dataclasses.dataclass`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass)

  - [`datetime.datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime), [`datetime.date`](https://docs.python.org/3.14/library/datetime.html#datetime.date), [`datetime.time`](https://docs.python.org/3.14/library/datetime.html#datetime.time)

  - [`inspect.Signature`](https://docs.python.org/3.14/library/inspect.html#inspect.Signature), [`inspect.Parameter`](https://docs.python.org/3.14/library/inspect.html#inspect.Parameter)

  - [`types.SimpleNamespace`](https://docs.python.org/3.14/library/types.html#types.SimpleNamespace)

  - [code objects](https://docs.python.org/3.14/reference/datamodel.html#code-objects)

Whatever user-defined class you write can likewise back [`copy.replace()`](https://docs.python.org/3.14/library/copy.html#copy.replace) once it supplies the [`__replace__()`](https://docs.python.org/3.14/library/copy.html#object.__replace__) method. (Contributed by Serhiy Storchaka in [gh-108751](https://github.com/python/cpython/issues/108751).)

[Subject index](INDEX.md) · [Previous source section](configparser.md) · [Next source section](ctypes.md) · [Release/subject declaration](summary-release-highlights.md)
