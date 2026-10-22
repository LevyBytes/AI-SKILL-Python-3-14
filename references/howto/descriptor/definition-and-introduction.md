# Definition and introduction

### Definition and introduction

Broadly speaking, a descriptor is an attribute value carrying one of the methods belonging to the descriptor protocol. Those methods are [`__get__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__get__), [`__set__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__set__), and [`__delete__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__delete__). Whenever any of them is present on an attribute, that attribute qualifies as a [descriptor](https://docs.python.org/3.14/glossary.html#term-descriptor).

By default, attribute access works by getting, setting, or deleting the attribute out of an object’s dictionary. Take `a.x`: its lookup chain begins at `a.__dict__['x']`, proceeds to `type(a).__dict__['x']`, and carries on through the method resolution order of `type(a)`. When the retrieved value is an object that implements one of the descriptor methods, Python can supersede the default behavior and call the descriptor method in its place. The point in the precedence chain at which this happens is governed by which descriptor methods are present.

Descriptors form a potent, general-purpose protocol. They underpin properties, methods, static methods, class methods, and [`super()`](https://docs.python.org/3.14/library/functions.html#super). Python itself relies on them everywhere. Descriptors keep the underlying C code simpler and provide a versatile collection of new facilities for ordinary Python code.

[Subject index](INDEX.md) · [Previous source context](abstract.md) · [Following source context](descriptor-protocol.md)
