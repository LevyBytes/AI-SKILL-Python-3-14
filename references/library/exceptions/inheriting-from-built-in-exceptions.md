# Inheriting from built-in exceptions

### Inheriting from built-in exceptions

User code is free to derive subclasses from an exception type. The advice is to subclass just a single exception type at any one time, both to sidestep potential clashes over how the bases treat the `args` attribute and because of possible incompatibilities in memory layout.

**CPython implementation detail:** For the sake of efficiency, the majority of built-in exceptions are written in C, see: [Objects/exceptions.c](https://github.com/python/cpython/tree/3.14/Objects/exceptions.c). A few carry custom memory layouts, which rules out building a subclass that derives from more than one exception type. Since a type's memory layout counts as an implementation detail that may shift across Python versions, fresh conflicts could arise down the road. For that reason, the guidance is to steer clear of subclassing several exception types together at all.

[Subject index](INDEX.md) · [Previous](baseexception-context-to-baseexception-suppress-context.md) · [Continue](baseexception-to-lookuperror.md)
