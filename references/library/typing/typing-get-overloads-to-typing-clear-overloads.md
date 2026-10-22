# typing: `typing.overload`, `typing.get_overloads()`, `typing.clear_overloads()`, `typing.final`

@typing.overload

Decorator for creating overloaded functions and methods.

By means of the `@overload` decorator you can spell out functions and methods that accept several distinct mixes of argument types. A run of `@overload`-decorated definitions has to be capped by precisely one definition for the same function/method that is not `@overload`-decorated.

The `@overload`-decorated definitions exist purely to serve the type checker, given that the non-`@overload`-decorated definition will replace them. That non-`@overload`-decorated definition, in turn, is what runs at runtime yet ought to be disregarded by a type checker. Should you call an `@overload`-decorated function directly at runtime, it raises [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

An overload example yielding a tighter type than a union or a type variable could capture:

```python
@overload
def process(response: None) -> None:
    ...
@overload
def process(response: int) -> tuple[int, str]:
    ...
@overload
def process(response: bytes) -> str:
    ...
def process(response):
    ...  # actual implementation goes here

```

See [**PEP 484**](https://peps.python.org/pep-0484/) for more details and comparison with other typing semantics.

Changed in version 3.11: Runtime introspection of overloaded functions is now possible via `get_overloads()`.

 typing.get_overloads(*func*)

Return a sequence of `@overload`-decorated definitions for *func*.

Here *func* names the function object implementing the overloaded function. Take the definition of `process` from the `@overload` documentation as an example: `get_overloads(process)` yields a sequence holding the three function objects for the three declared overloads. When run against a function that has no overloads, `get_overloads()` produces an empty sequence.

`get_overloads()` can be used for introspecting an overloaded function at runtime.

Added in version 3.11.

 typing.clear_overloads()

Clear all registered overloads in the internal registry.

This can be used to reclaim the memory used by the registry.

Added in version 3.11.

 @typing.final

Decorator to indicate final methods and final classes.

Putting `@final` on a method signals to a type checker that no subclass may override it. Putting `@final` on a class signals that it admits no subclasses.

For example:

```python
class Base:
    @final
    def done(self) -> None:
        ...
class Sub(Base):
    def done(self) -> None:  # Error reported by type checker
        ...

@final
class Leaf:
    ...
class Other(Leaf):  # Error reported by type checker
    ...

```

These properties are never enforced at runtime. See [**PEP 591**](https://peps.python.org/pep-0591/) for more details.

Added in version 3.8.

Changed in version 3.11: The decorator now tries to assign a `__final__` attribute of `True` onto the object it decorates. Consequently, a test such as `if getattr(obj, "__final__", False)` lets you find out at runtime whether some object `obj` was tagged as final. Where the decorated object will not accept attribute assignment, the decorator simply gives the object back as-is and raises no exception.

[Subject index](INDEX.md) · [Previous](dataclass-field-specifier-options.md) · [Continue](functions-and-decorators.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Functions and decorators](typing-cast-to-typing-assert-never.md)
