# inspect: Async generators, frames, routines and descriptor predicates

inspect.isasyncgenfunction(*object*)

Return `True` if the object is an [asynchronous generator](https://docs.python.org/3.14/glossary.html#term-asynchronous-generator) function, for example:

```pycon
>>> async def agen():
...     yield 1
...
>>> inspect.isasyncgenfunction(agen)
True

```

Added in version 3.6.

Changed in version 3.8: A [`functools.partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial) wrapper now yields `True` whenever its wrapped target is an [asynchronous generator](https://docs.python.org/3.14/glossary.html#term-asynchronous-generator) function.

Changed in version 3.13: A [`functools.partialmethod()`](https://docs.python.org/3.14/library/functools.html#functools.partialmethod) wrapper now yields `True` whenever its wrapped target is a [asynchronous generator](https://docs.python.org/3.14/glossary.html#term-asynchronous-generator) function.

 inspect.isasyncgen(*object*)

Return `True` if the object is an [asynchronous generator iterator](https://docs.python.org/3.14/glossary.html#term-asynchronous-generator-iterator) created by an [asynchronous generator](https://docs.python.org/3.14/glossary.html#term-asynchronous-generator) function.

Added in version 3.6.

 inspect.istraceback(*object*)

Return `True` if the object is a traceback.

 inspect.isframe(*object*)

Return `True` if the object is a frame.

 inspect.iscode(*object*)

Return `True` if the object is a code.

 inspect.isbuiltin(*object*)

Return `True` when the object is a built-in function, or alternatively a bound built-in method.

 inspect.ismethodwrapper(*object*)

Return `True` if the type of object is a [`MethodWrapperType`](https://docs.python.org/3.14/library/types.html#types.MethodWrapperType).

These count as instances of [`MethodWrapperType`](https://docs.python.org/3.14/library/types.html#types.MethodWrapperType), for instance [`__str__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__str__), [`__eq__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__eq__) and [`__repr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__repr__).

Added in version 3.11.

 inspect.isroutine(*object*)

Return `True` when the object is a function or method, whether user-defined or built-in.

 inspect.isabstract(*object*)

Return `True` if the object is an abstract base class.

 inspect.ismethoddescriptor(*object*)

Return `True` for a method descriptor — provided that none of `ismethod()`, `isclass()`, `isfunction()` or `isbuiltin()` hold true for it.

Take `int.__add__` as an example where this holds. Anything that clears this test carries a [`__get__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__get__) method, yet lacks both a [`__set__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__set__) method and a [`__delete__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__delete__) method. Past that point, which attributes exist differs from case to case. A [`__name__`](https://docs.python.org/3.14/library/stdtypes.html#definition.__name__) attribute is generally meaningful, and [`__doc__`](https://docs.python.org/3.14/library/stdtypes.html#definition.__doc__) frequently is too.

Methods built through descriptors that also clear one of the remaining tests come back `False` from the `ismethoddescriptor()` test, for the simple reason that those other tests offer stronger guarantees — you can, for instance, rely on the [`__func__`](https://docs.python.org/3.14/reference/datamodel.html#method.__func__) attribute (and so on) once an object clears `ismethod()`.

Changed in version 3.13: Objects that expose [`__get__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__get__) along with [`__delete__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__delete__) yet lack [`__set__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__set__) are no longer wrongly flagged by this function as method descriptors — they qualify instead as data descriptors.

 inspect.isdatadescriptor(*object*)

Return `True` if the object is a data descriptor.

A data descriptor owns either a [`__set__`](https://docs.python.org/3.14/reference/datamodel.html#object.__set__) or a [`__delete__`](https://docs.python.org/3.14/reference/datamodel.html#object.__delete__) method. Properties (written in Python), getsets, and members serve as examples. The last two are written in C, and more targeted tests exist for those types that hold up reliably across Python implementations. As a rule, data descriptors carry [`__name__`](https://docs.python.org/3.14/library/stdtypes.html#definition.__name__) and `__doc__` attributes as well (properties, getsets, and members each have both), though there is no guarantee of this.

 inspect.isgetsetdescriptor(*object*)

Return `True` if the object is a getset descriptor.

**CPython implementation detail:** getsets are attributes defined in extension modules via [`PyGetSetDef`](https://docs.python.org/3.14/c-api/structures.html#c.PyGetSetDef) structures. On Python implementations that lack such types, this method always comes back `False`.

[Subject index](INDEX.md) · [Previous](inspect-isfunction-to-inspect-isawaitable.md) · [Continue](inspect-ismemberdescriptor.md) · [Owning module, declaration or section: inspect](inspect-inspect-live-objects.md) · [Owning module, declaration or section: Types and members](types-and-members-section-introduction-and-initial-examples.md)
