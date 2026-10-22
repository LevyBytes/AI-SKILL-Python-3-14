# Closing thoughts

### Closing thoughts

We use the term [descriptor](https://docs.python.org/3.14/glossary.html#term-descriptor) for any object that supplies [`__get__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__get__), [`__set__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__set__), or [`__delete__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__delete__).

A descriptor may additionally include a [`__set_name__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__set_name__) method. It serves only the situations where a descriptor must discover either the class in which it was defined or the name of the class variable it was bound to. (When present, this method runs even if the surrounding class is not itself a descriptor.)

The dot operator triggers descriptors during attribute lookup. Should a descriptor instead be reached indirectly via `vars(some_class)[descriptor_name]`, you get back the descriptor instance itself, with no invocation.

Descriptors take effect solely as class variables. Placed within instances, they accomplish nothing.

The central reason descriptors exist is to supply a hook by which objects held in class variables can govern what occurs during attribute lookup.

Conventionally, the calling class governs what happens during lookup. Descriptors flip that arrangement, granting the data being retrieved a voice in the outcome.

The whole language relies on descriptors. They are the means by which functions become bound methods. Familiar utilities such as [`classmethod()`](https://docs.python.org/3.14/library/functions.html#classmethod), [`staticmethod()`](https://docs.python.org/3.14/library/functions.html#staticmethod), [`property()`](https://docs.python.org/3.14/library/functions.html#property), and [`functools.cached_property()`](https://docs.python.org/3.14/library/functools.html#functools.cached_property) are every one of them built as descriptors.

[Subject index](INDEX.md) · [Previous source context](customized-names.md) · [Following source context](complete-practical-example.md)
