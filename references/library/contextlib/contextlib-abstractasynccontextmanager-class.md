# contextlib: `contextlib.AbstractAsyncContextManager`

*class *contextlib.AbstractAsyncContextManager

Serves as an [abstract base class](https://docs.python.org/3.14/glossary.html#term-abstract-base-class) for any class supplying [`__aenter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__aenter__) plus [`__aexit__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__aexit__). The `__aenter__()` method ships with a default body that hands back `self`, whereas `__aexit__()` stays abstract and, by default, yields `None`. Consult as well the description of [Asynchronous Context Managers](https://docs.python.org/3.14/reference/datamodel.html#async-context-managers).

Added in version 3.7.

[Subject index](INDEX.md) · [Previous](contextlib-abstractcontextmanager-class.md) · [Continue](utilities-managed-resource.md) · [Owning module, declaration or section: contextlib](contextlib-utilities-for-with-statement-contexts.md) · [Owning module, declaration or section: Utilities](contextlib-abstractcontextmanager-class.md)
