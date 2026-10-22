# integers C API: `PyUnstable_Long_IsCompact()`, `PyUnstable_Long_CompactValue()`

int PyUnstable_Long_IsCompact(const PyLongObject *op)

 *Counts as [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api). Minor releases may alter it with no advance notice.*

Hand back 1 when *op* is compact and 0 when it is not.

By means of this function, performance-critical code can roll out a “fast path” aimed at small integers. When values are compact, reach for `PyUnstable_Long_CompactValue()`; otherwise drop back to a `PyLong_As*` function or `PyLong_AsNativeBytes()`.

For the majority of users, the speedup ought to be negligible.

Precisely which values rank as compact is an implementation detail that may well change.

Added in version 3.12.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyUnstable_Long_CompactValue(const PyLongObject *op)

 *Falls under [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api), so a minor release could change it without any warning.*

When *op* is compact, as `PyUnstable_Long_IsCompact()` ascertains, give back its value.

Failing that, the value returned is undefined.

Added in version 3.12.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](integer-objects.md) · [Owning structure and shared ABI conditions](pylongobject-to-pylong-fromdouble.md) · [Previous source contract](pylong-aspid-to-pylong-getinfo.md) · [Following source contract](pylonglayout-to-pylong-getnativelayout.md)
