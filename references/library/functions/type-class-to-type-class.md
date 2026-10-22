# Built-in Functions

*class *type(*object*, */*)

 *class *type(*name*, *bases*, *dict*, */*, ***kwargs*)

Pass a single argument and you get back the type of that *object*. What comes back is a type object, normally the very object that [`object.__class__`](https://docs.python.org/3.14/reference/datamodel.html#object.__class__) returns.

For checking an object's type, the recommended choice is the `isinstance()` built-in function, since it accounts for subclasses.

Pass three arguments and you get back a new type object. That amounts to a runtime variant of the [`class`](https://docs.python.org/3.14/reference/compound_stmts.html#class) statement. The *name* string supplies the class name and becomes its [`__name__`](https://docs.python.org/3.14/reference/datamodel.html#type.__name__) attribute. The *bases* tuple holds the base classes and becomes the [`__bases__`](https://docs.python.org/3.14/reference/datamodel.html#type.__bases__) attribute; when it's empty, `object`, the ultimate base of all classes, gets appended. The *dict* dictionary holds the attribute and method definitions for the class body; it might be copied or wrapped on its way to becoming the [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#type.__dict__) attribute. These two statements below build equivalent `type` objects:

```python
>>> class X:
...     a = 1
...
>>> X = type('X', (), dict(a=1))

```

See also:

- [Documentation on attributes and methods on classes](https://docs.python.org/3.14/reference/datamodel.html#class-attrs-and-methods).

- [Type Objects](https://docs.python.org/3.14/library/stdtypes.html#bltin-type-objects)

Any keyword arguments handed to the three argument form get forwarded to the relevant metaclass machinery (typically [`__init_subclass__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init_subclass__)), just as keywords in a class definition (other than *metaclass*) would be.

See also [Customizing class creation](https://docs.python.org/3.14/reference/datamodel.html#class-customization).

Changed in version 3.6: A subclass of `type` that leaves `type.__new__` unoverridden can no longer rely on the one-argument form to obtain an object's type.

[Subject index](INDEX.md) · [Previous](tuple-class.md) · [Continue](INDEX.md) · [Owning module, declaration or section: Built-in Functions](INDEX.md)
