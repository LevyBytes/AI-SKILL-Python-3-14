# typing: `typing.runtime_checkable`

@typing.runtime_checkable

Mark a protocol class as a runtime protocol.

You can then use such a protocol with [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) and [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass). This enables a simple-minded structural check much like the “one-trick ponies” found in [`collections.abc`](https://docs.python.org/3.14/library/collections.abc.html#module-collections.abc), for instance [`Iterable`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Iterable). For example:

```python
@runtime_checkable
class Closable(Protocol):
    def close(self): ...

assert isinstance(open('/some/file'), Closable)

@runtime_checkable
class Named(Protocol):
    name: str

import threading
assert isinstance(threading.Thread(name='Bob'), Named)

```

Applying this decorator to a class that is not a protocol raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

Note

What `runtime_checkable()` verifies is merely that the required methods or attributes exist, not their types or type signatures. As an illustration, [`ssl.SSLObject`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLObject) is a class, so it satisfies an [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass) check against Callable. The `ssl.SSLObject.__init__` method, however, is present purely to raise a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) carrying a clearer message, which makes calling (instantiating) `ssl.SSLObject` impossible.

Note

Compared with an `isinstance()` check against a non-protocol class, an [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) check against a runtime-checkable protocol can run surprisingly slowly. In performance-sensitive code, weigh alternative idioms such as [`hasattr()`](https://docs.python.org/3.14/library/functions.html#hasattr) calls for structural checks.

Added in version 3.8.

Changed in version 3.12: When checking [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) against runtime-checkable protocols, the internal machinery now looks up attributes with [`inspect.getattr_static()`](https://docs.python.org/3.14/library/inspect.html#inspect.getattr_static) (formerly [`hasattr()`](https://docs.python.org/3.14/library/functions.html#hasattr) handled this). Consequently, certain objects formerly treated as instances of a runtime-checkable protocol may, on Python 3.12+, no longer be treated as such, and the reverse can happen as well. The change is unlikely to affect most users.

Changed in version 3.12: A runtime-checkable protocol's members are now treated as “frozen” at runtime the moment the class is created. You can still monkey-patch attributes onto a runtime-checkable protocol, yet doing so has no bearing on [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) checks that compare objects against the protocol. Refer to [What’s new in Python 3.12](https://docs.python.org/3.14/whatsnew/3.12.html#whatsnew-typing-py312) for additional detail.

[Subject index](INDEX.md) · [Previous](typing-protocol-class.md) · [Continue](typing-typeddict-class.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Other special directives](type-construction-directives.md)
