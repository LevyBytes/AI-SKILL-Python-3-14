# 3.3.3.1. Metaclasses

#### 3.3.3.1. Metaclasses

Classes are built with [`type()`](https://docs.python.org/3.14/library/functions.html#type) by default. The class body runs inside a fresh namespace, and the class name is bound locally to whatever `type(name, bases, namespace)` returns.

You can tailor the class creation process by supplying the `metaclass` keyword argument on the class definition line, or by inheriting from an existing class that already carried such an argument. In the example that follows, both `MyClass` and `MySubclass` are instances of `Meta`:

```python
class Meta(type):
    pass

class MyClass(metaclass=Meta):
    pass

class MySubclass(MyClass):
    pass

```

Whatever additional keyword arguments appear in the class definition get forwarded to every metaclass operation covered below.

Executing a class definition runs through these steps:

- MRO entries are resolved;

- the appropriate metaclass is determined;

- the class namespace is prepared;

- the class body is executed;

- the class object is created.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](customizing-class-creation.md) · [Previous source section](object-set-name.md) · [Following source section](object-mro-entries.md)
