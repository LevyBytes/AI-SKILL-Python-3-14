# What’s New In Python 3.8 / Other Language Changes - pickle

A tuple returned by [`object.__reduce__()`](https://docs.python.org/3.14/library/pickle.html#object.__reduce__) may now hold anywhere from two up to six entries; previously the cap stood at five. That fresh, optional sixth slot holds a callable whose signature is `(obj, state)`. With it you gain direct say over how a given object has its state refreshed. When it is not *None*, this callable takes precedence over whatever the object's [`__setstate__()`](https://docs.python.org/3.14/library/pickle.html#object.__setstate__) method would do.

[Subject index](INDEX.md) · [Next source section](new-modules.md) · [Release/subject declaration](assignment-expressions.md) · [Release/subject declaration](other-language-changes.md) · [Preceding release/subject continuation](modular-inverses-and-language-changes.md)
