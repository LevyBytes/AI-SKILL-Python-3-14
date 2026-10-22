# id

id(*object*, */*)

Return the “identity” of an object. This takes the form of an integer that is guaranteed to stay unique and constant for this object throughout its lifetime. Two objects whose lifetimes do not overlap may end up sharing the same `id()` value.

**CPython implementation detail:** This is the address of the object in memory.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `builtins.id` with argument `id`.

[Builtin task index](INDEX.md).
