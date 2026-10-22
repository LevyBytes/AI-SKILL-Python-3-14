# Deprecated API

### Deprecated API

The following macros are [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated). What they characterize are parameters of how `PyLongObject` instances are represented internally.

Turn to `PyLong_GetNativeLayout()` in their place, paired with `PyLong_Export()` for reading integer data or `PyLongWriter` for writing it. For the moment these share one layout, yet they are built to keep functioning correctly should CPython's internal integer representation ever change.

 PyLong_SHIFT

This matches `bits_per_digit` as it appears in what `PyLong_GetNativeLayout()` outputs.

 PyLong_BASE

For now this matches `1 << PyLong_SHIFT`.

 PyLong_MASK

For now this matches `(1 << PyLong_SHIFT) - 1`

[Subject index](INDEX.md) · [Previous source contract](pylongwriter-to-pylongwriter-discard.md)
