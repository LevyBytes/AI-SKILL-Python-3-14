# warnings: `warnings.deprecated()`

@warnings.deprecated(*msg*, ***, *category=DeprecationWarning*, *stacklevel=1*)

Decorator to mark a class, function or overload as deprecated.

Once this decorator is on an object, using that object may produce deprecation warnings at runtime. [static type checkers](https://docs.python.org/3.14/glossary.html#term-static-type-checker) will likewise raise a diagnostic whenever the deprecated object is used.

Usage:

```python
from warnings import deprecated
from typing import overload

@deprecated("Use B instead")
class A:
    pass

@deprecated("Use g instead")
def f():
    pass

@overload
@deprecated("int support is deprecated")
def g(x: int) -> int: ...
@overload
def g(x: str) -> int: ...

```

At runtime, the warning named by *category* fires whenever a deprecated object is used. With functions that occurs on calls; with classes it occurs on instantiation and on the creation of subclasses. When *category* is `None`, nothing is emitted at runtime. Where the warning fires is set by *stacklevel*. At `1` (the default), the warning fires at the deprecated object's direct caller; at a higher value, it fires further up the stack. The *category* and *stacklevel* arguments have no bearing on how static type checkers behave.

[Subject index](INDEX.md) · [Previous](warnings-warn-to-warnings-resetwarnings.md) · [Owning module, declaration or section: warnings](warnings-warning-control.md) · [Owning module, declaration or section: Available Functions](warnings-warn-to-warnings-resetwarnings.md)
