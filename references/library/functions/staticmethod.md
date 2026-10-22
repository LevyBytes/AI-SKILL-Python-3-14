# staticmethod

@staticmethod

Transform a method into a static method.

No implicit first argument reaches a static method. The way to declare one is with this idiom:

```python
class C:
    @staticmethod
    def f(arg1, arg2, argN): ...

```

The `@staticmethod` notation is a function [decorator](https://docs.python.org/3.14/glossary.html#term-decorator) – consult [Function definitions](https://docs.python.org/3.14/reference/compound_stmts.html#function) for the particulars.

You can invoke a static method through the class (for instance `C.f()`) or through an instance (for instance `C().f()`). On top of that, the static method [descriptor](https://docs.python.org/3.14/glossary.html#term-descriptor) is itself callable, which lets it be used inside the class body (for instance `f()`).

Python's static methods resemble the ones in Java or C++. Have a look at `classmethod()` too, a variant handy for building alternate class constructors.

As with every decorator, you can also invoke `staticmethod` like an ordinary function and do something with what it returns. You'd need this in certain situations where you want a reference to a function pulled from a class body without the automatic conversion into an instance method. Here's the idiom for those situations:

```python
def regular_function():
    ...

class C:
    method = staticmethod(regular_function)

```

For deeper coverage of static methods, look at [The standard type hierarchy](https://docs.python.org/3.14/reference/datamodel.html#types).

Changed in version 3.10: A static method picks up the method attributes from then on ([`__module__`](https://docs.python.org/3.14/reference/datamodel.html#function.__module__), [`__name__`](https://docs.python.org/3.14/reference/datamodel.html#function.__name__), [`__qualname__`](https://docs.python.org/3.14/reference/datamodel.html#function.__qualname__), [`__doc__`](https://docs.python.org/3.14/reference/datamodel.html#function.__doc__) and [`__annotations__`](https://docs.python.org/3.14/reference/datamodel.html#function.__annotations__)), gains a fresh `__wrapped__` attribute, and may from then on be invoked like ordinary functions.

[Builtin task index](INDEX.md).
