# 3.2.5.2. Mutable sequences

#### 3.2.5.2. Mutable sequences

After being built, mutable sequences can be altered. You can place the subscription and slicing notations on the left of assignments and of [`del`](https://docs.python.org/3.14/reference/simple_stmts.html#del) (delete) statements.

Note

Further illustrations of mutable sequence types come from the [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) module and the [`array`](https://docs.python.org/3.14/library/array.html#module-array) module.

Two intrinsic mutable sequence types exist at present:

Lists

Whatever Python objects you like may serve as the items of a list. You form a list by wrapping a comma-separated run of expressions in square brackets. (Note that forming lists of length 0 or 1 calls for no special handling.)

Byte Arrays

What a bytearray object amounts to is a mutable array. The built-in [`bytearray()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) constructor produces them. Setting aside that they are mutable (and hence unhashable), byte arrays present otherwise the identical interface and capabilities found on immutable [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) objects.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](sequences.md) · [Previous source section](immutable-sequences.md) · [Following source section](set-types.md)
