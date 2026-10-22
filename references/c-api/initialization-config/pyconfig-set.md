# int PyConfig_Set(const char *name, PyObject *value)

int PyConfig_Set(const char *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *value)

Write the live runtime value of a configuration option.

- Raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when no option *name* exists.

- Raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when *value* is not a valid value.

- Raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when the option is read-only (it cannot be written).

- Raise a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) when *value* is not of the proper type.

An [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) is required of the caller. Invocation is impossible prior to Python initialization or following Python finalization.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `cpython.PyConfig_Set` with arguments `name`, `value`.

Added in version 3.14.

Changed in version 3.14.6 (unreleased): Rather than editing `sys.flags` in place, the function now swaps in a brand-new [`sys.flags`](https://docs.python.org/3.14/library/sys.html#sys.flags) object.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyconfig-get-to-pyconfig-names.md) · [Following source contract](pyconfig-c-api.md)
