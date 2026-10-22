# typing: `typing.no_type_check`, `typing.no_type_check_decorator`, `typing.override`, `typing.type_check_only`

@typing.no_type_check

Decorator to indicate that annotations are not type hints.

It functions as either a class or a function [decorator](https://docs.python.org/3.14/glossary.html#term-decorator). Applied to a class, it reaches recursively into every method and class declared inside that class (though not into methods declared on its superclasses or subclasses). Type checkers will disregard every annotation within a function or class bearing this decorator.

`@no_type_check` mutates the decorated object in place.

 @typing.no_type_check_decorator

Decorator to give another decorator the `no_type_check()` effect.

It surrounds the decorator with logic that in turn surrounds the decorated function with `no_type_check()`.

Deprecated since version 3.13, will be removed in version 3.15: Support for `@no_type_check_decorator` was never implemented by any type checker. For that reason it is deprecated and slated for removal in Python 3.15.

 @typing.override

Decorator marking that a subclass method is meant to override some method or attribute belonging to a superclass.

A type checker ought to raise an error when a method carrying `@override` does not actually override anything. The mechanism guards against bugs arising when a base class gets altered while the matching change to a child class is left out.

For example:

```python
class Base:
    def log_status(self) -> None:
        ...

class Sub(Base):
    @override
    def log_status(self) -> None:  # Okay: overrides Base.log_status
        ...

    @override
    def done(self) -> None:  # Error reported by type checker
        ...

```

There is no runtime checking of this property.

The decorator tries to assign an `__override__` attribute of `True` onto the object it decorates. Consequently, a test such as `if getattr(obj, "__override__", False)` lets you find out at runtime whether some object `obj` was tagged as an override. Where the decorated object will not accept attribute assignment, the decorator simply gives the object back as-is and raises no exception.

See [**PEP 698**](https://peps.python.org/pep-0698/) for more details.

Added in version 3.12.

 @typing.type_check_only

Decorator to mark a class or function as unavailable at runtime.

The decorator itself cannot be reached at runtime. Its primary purpose is flagging classes declared in type stub files for cases where an implementation hands back an instance of a private class:

```python
@type_check_only
class Response:  # private or not available at runtime
    code: int
    def get_header(self, name: str) -> str: ...

def fetch_response() -> Response: ...

```

Bear in mind that handing back instances of private classes is discouraged. The better course is usually to expose such classes publicly.

[Subject index](INDEX.md) · [Previous](typing-get-overloads-to-typing-clear-overloads.md) · [Continue](typing-get-type-hints-to-typing-get-origin.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Functions and decorators](typing-cast-to-typing-assert-never.md)
