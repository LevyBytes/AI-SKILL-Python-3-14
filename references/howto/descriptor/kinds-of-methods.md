# Kinds of methods

### Kinds of methods

Variations on the usual ways of binding functions into methods come easily thanks to non-data descriptors.

As a reminder, functions own a [`__get__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__get__) method that lets them become a method when reached as an attribute. The non-data descriptor turns a call of `obj.f(*args)` into `f(obj, *args)`. Likewise, `cls.f(*args)` turns into `f(*args)`.

The table below recaps the binding alongside its two handiest variants:

>
| Transformation | Called from an object | Called from a class |
| --- | --- | --- |
| function | f(obj, *args) | f(*args) |
| staticmethod | f(*args) | f(*args) |
| classmethod | f(type(obj), *args) | f(cls, *args) |

[Subject index](INDEX.md) · [Previous source context](function-descriptors-and-bound-method-inspection.md) · [Following source context](static-methods.md)
