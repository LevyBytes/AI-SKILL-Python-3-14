# object.__repr__(*self*)

object.__repr__(*self*)
Invoked by the [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) built-in function to derive the “official” string form of an object. Wherever feasible, the result ought to resemble a valid Python expression capable of reconstructing an object holding the same value (assuming a suitable environment). When that cannot be achieved, return a string shaped like `<...some useful description...>`. A string object must be the return value. Should a class supply `__repr__()` while lacking `__str__()`, then `__repr__()` serves as well whenever an “informal” string form of that class’s instances is needed.

Because this typically serves debugging, the representation should be rich in information and free of ambiguity. The [`object`](https://docs.python.org/3.14/library/functions.html#object) class itself supplies a default implementation.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](object-new.md) · [Complete protocol declaration and contract](object-del.md) · [Previous source contract continuation](object-del.md) · [Previous source section](object-del.md) · [Previous source section](object-str.md) · [Following source section](object-str.md)
