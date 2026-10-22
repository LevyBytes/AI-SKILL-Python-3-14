# 3.3.5. Emulating generic types

### 3.3.5. Emulating generic types

When you work with [type annotations](https://docs.python.org/3.14/glossary.html#term-annotation), it is frequently handy to *parameterize* a [generic type](https://docs.python.org/3.14/glossary.html#term-generic-type) by means of Python's square-brackets syntax. For instance, the annotation `list[int]` could indicate a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) whose elements are every one of type [`int`](https://docs.python.org/3.14/library/functions.html#int).

See also

[**PEP 484**](https://peps.python.org/pep-0484/) - Type Hints

Introducing Python's framework for type annotations

[Generic Alias Types](https://docs.python.org/3.14/library/stdtypes.html#types-genericalias)

Documentation for objects representing parameterized generic classes

[Generics](https://docs.python.org/3.14/library/typing.html#generics), [user-defined generics](https://docs.python.org/3.14/library/typing.html#user-defined-generics) and [`typing.Generic`](https://docs.python.org/3.14/library/typing.html#typing.Generic)

A guide to writing generic classes whose runtime parameterization is also recognised by static type-checkers.

In general a class can be parameterized only when it defines the special class method `__class_getitem__()`.

 *classmethod *object.__class_getitem__(*cls*, *key*)

Return an object that represents the specialization of a generic class by the type arguments contained in *key*.

Once it is defined on a class, `__class_getitem__()` becomes a class method automatically. For that reason there is no requirement to decorate it with [`@classmethod`](https://docs.python.org/3.14/library/functions.html#classmethod) at its definition.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Previous source section](type-subclasscheck.md) · [Following source section](the-purpose-of-class-getitem.md)
