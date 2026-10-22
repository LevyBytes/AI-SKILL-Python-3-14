# 3.3.3.6. Creating the class object

#### 3.3.3.6. Creating the class object

After the class body has filled in the class namespace, the class object is produced by calling `metaclass(name, bases, namespace, **kwds)` (the extra keywords supplied here match those given to `__prepare__`).

This class object is exactly what the zero-argument form of [`super()`](https://docs.python.org/3.14/library/functions.html#super) refers to. `__class__` is an implicit closure reference that the compiler manufactures whenever any methods in a class body mention either `__class__` or `super`. It lets the zero-argument form of `super()` pin down the class under definition through lexical scoping, while the class or instance that drove the current call is identified from the first argument handed to the method.

**CPython implementation detail:** From CPython 3.6 onward, the `__class__` cell reaches the metaclass as a `__classcell__` entry within the class namespace. When present, it has to be passed up to the `type.__new__` call so the class initialises properly. Neglecting to do so yields a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) in Python 3.8.

With the default metaclass [`type`](https://docs.python.org/3.14/library/functions.html#type) in play, or any metaclass that eventually calls `type.__new__`, these further customization steps run once the class object exists:

1.

The `type.__new__` method gathers every attribute in the class namespace that defines a `__set_name__()` method;

2.

Each of those `__set_name__` methods is invoked with the class being defined plus the name assigned to that specific attribute;

3.

The `__init_subclass__()` hook fires on the immediate parent of the new class within its method resolution order.

Once the class object exists, it is handed to the class decorators listed in the class definition (when there are any), and the object that results is bound under the defined class's name in the local namespace.

Whenever `type.__new__` creates a new class, the object handed in as the namespace parameter is copied into a fresh ordered mapping and the original object is thrown away. That fresh copy is wrapped in a read-only proxy, which then serves as the class object's `__dict__` attribute.

See also

[**PEP 3135**](https://peps.python.org/pep-3135/) - New super

Describes the implicit `__class__` closure reference

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](customizing-class-creation.md) · [Previous source section](executing-the-class-body.md) · [Following source section](uses-for-metaclasses.md)
