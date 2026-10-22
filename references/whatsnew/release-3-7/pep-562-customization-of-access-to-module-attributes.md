# What's New In Python 3.7 / PEP 562: Customization of Access to Module Attributes

### PEP 562: Customization of Access to Module Attributes

Python 3.7 lets you define [`__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#module.__getattr__) at module level, and it gets invoked any time a module attribute is otherwise missing. Modules may now define [`__dir__()`](https://docs.python.org/3.14/reference/datamodel.html#module.__dir__) as well.

Deprecating module attributes and loading them lazily are common scenarios where this comes in handy.

See also

[**PEP 562**](https://peps.python.org/pep-0562/) — Module `__getattr__` and `__dir__`

PEP written and implemented by Ivan Levkivskyi

[Subject index](INDEX.md) · [Previous source section](pep-539-new-c-api-for-thread-local-storage.md) · [Next source section](pep-564-new-time-functions-with-nanosecond-resolution.md) · [Release/subject declaration](summary-release-highlights.md)
