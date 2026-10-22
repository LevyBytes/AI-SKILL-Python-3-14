# object.__len__(*self*)

object.__len__(*self*)

Invoked to implement the built-in function [`len()`](https://docs.python.org/3.14/library/functions.html#len). It should return the object's length as an integer `>=` 0. On top of that, an object that defines no `__bool__()` method and whose `__len__()` method returns zero is taken to be false in a Boolean context.
**CPython implementation detail:** Within CPython, the length may not exceed [`sys.maxsize`](https://docs.python.org/3.14/library/sys.html#sys.maxsize). Should the length surpass `sys.maxsize`, certain features (for example [`len()`](https://docs.python.org/3.14/library/functions.html#len)) might raise [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError). An object should provide a `__bool__()` method so that truth value testing avoids raising `OverflowError`.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](emulating-container-types.md) · [Previous source section](emulating-container-types.md) · [Previous source section](object-length-hint.md) · [Following source section](object-length-hint.md)
