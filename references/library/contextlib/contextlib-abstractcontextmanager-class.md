# contextlib: `contextlib.AbstractContextManager`

### Utilities

The classes and functions exposed here:

 *class *contextlib.AbstractContextManager

Serves as an [abstract base class](https://docs.python.org/3.14/glossary.html#term-abstract-base-class) for any class supplying [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) plus [`__exit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__exit__). The `__enter__()` method ships with a default body that hands back `self`, whereas `__exit__()` stays abstract and, by default, yields `None`. Consult as well the description of [Context Manager Types](https://docs.python.org/3.14/library/stdtypes.html#typecontextmanager).

Added in version 3.6.

[Subject index](INDEX.md) · [Previous](contextlib-utilities-for-with-statement-contexts.md) · [Continue](contextlib-abstractasynccontextmanager-class.md) · [Owning module, declaration or section: contextlib](contextlib-utilities-for-with-statement-contexts.md)
