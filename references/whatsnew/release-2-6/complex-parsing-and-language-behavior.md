# Python 2.6 changes: Complex parsing and string translation changes

Strings carrying parenthesized complex numbers are now accepted by the [`complex()`](https://docs.python.org/3.14/library/functions.html#complex) constructor, so `complex(repr(cplx))` will now round-trip values. As an example, `complex('(3+4j)')` now produces the value (3+4j). ([bpo-1491866](https://bugs.python.org/issue?@action=redirect&bpo=1491866))

- The string `translate()` method now takes `None` for the translation table parameter, which it reads as the identity transformation. That simplifies tasks whose only goal is to delete characters. (Contributed by Bengt Richter and implemented by Raymond Hettinger; [bpo-1193128](https://bugs.python.org/issue?@action=redirect&bpo=1193128).)

- When given an object, the built-in [`dir()`](https://docs.python.org/3.14/library/functions.html#dir) function now looks for a `__dir__()` method on it. That method has to return a list of strings naming the object’s valid attributes, granting the object a say in what `dir()` reports. Objects equipped with `__getattr__()` or `__getattribute__()` methods can lean on this to surface pseudo-attributes they intend to support. ([bpo-1591665](https://bugs.python.org/issue?@action=redirect&bpo=1591665))

- Instance method objects gain new attributes for the object and the function that make up the method; [`__self__`](https://docs.python.org/3.14/reference/datamodel.html#method.__self__) is the new synonym for `im_self`, and `im_func` is now reachable as [`__func__`](https://docs.python.org/3.14/reference/datamodel.html#method.__func__) too. Python 2.6 retains the older names, though 3.0 drops them.

- A subtle shift: calling the [`locals()`](https://docs.python.org/3.14/library/functions.html#locals) function within a [`class`](https://docs.python.org/3.14/reference/compound_stmts.html#class) statement now yields a dictionary that omits free variables. (Here free variables denote variables that the `class` statement references but that are not attributes of the class.)

[Subject index](INDEX.md) · [Previous source section](other-language-changes-c-and-d.md) · [Next source section](optimizations.md) · [Release/subject declaration](python-3-0.md) · [Release/subject declaration](core-language-changes.md)
