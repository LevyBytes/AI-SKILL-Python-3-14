# classmethod

@classmethod

Convert a method into a class method.

Just as an instance method gets the instance as its implicit first argument, a class method gets the class. The idiom for declaring one is:

```python
class C:
    @classmethod
    def f(cls, arg1, arg2): ...

```

Written this way, `@classmethod` is a function [decorator](https://docs.python.org/3.14/glossary.html#term-decorator) – consult [Function definitions](https://docs.python.org/3.14/reference/compound_stmts.html#function) for the specifics.

You may invoke a class method by way of the class itself (for instance `C.f()`) or by way of an instance (for instance `C().f()`). Beyond supplying its class, the instance plays no role. Invoke a class method on a subclass and the subclass object becomes the implied first argument.

Class methods are not the same as the static methods of C++ or Java. Should you need those, consult `staticmethod()` later in this section. Further detail on class methods appears in [The standard type hierarchy](https://docs.python.org/3.14/reference/datamodel.html#types).

Changed in version 3.9: Wrapping further [descriptors](https://docs.python.org/3.14/glossary.html#term-descriptor) like `property()` around a class method became possible.

Changed in version 3.10: A class method now picks up the method attributes ([`__module__`](https://docs.python.org/3.14/reference/datamodel.html#function.__module__), [`__name__`](https://docs.python.org/3.14/reference/datamodel.html#function.__name__), [`__qualname__`](https://docs.python.org/3.14/reference/datamodel.html#function.__qualname__), [`__doc__`](https://docs.python.org/3.14/reference/datamodel.html#function.__doc__) and [`__annotations__`](https://docs.python.org/3.14/reference/datamodel.html#function.__annotations__)) and gains a fresh `__wrapped__` attribute.

Deprecated since version 3.11, removed in version 3.13: Wrapping further [descriptors](https://docs.python.org/3.14/glossary.html#term-descriptor) like `property()` around a class method is no longer supported.

[Builtin task index](INDEX.md).
