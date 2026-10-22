# Runtime Python configuration API

### Runtime Python configuration API

While Python runs, configuration options can be read and written via the `PyConfig_Get()` and `PyConfig_Set()` functions.

The configuration option *name* argument has to be a non-NULL, null-terminated string encoded in UTF-8. Refer to Configuration Options.

Certain options derive from the [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) attributes. The `"argv"` option, for instance, comes from [`sys.argv`](https://docs.python.org/3.14/library/sys.html#sys.argv).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyConfig_Get(const char *name)

Read the live runtime value of a configuration option, returned as a Python object.

- On success, hand back a new reference.

- On error, raise an exception and hand back `NULL`.

Which object type you get hinges on the configuration option. The possibilities are:

- `bool`

- `int`

- `str`

- `list[str]`

- `dict[str, str]`

An [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) is required of the caller. Invocation is impossible prior to Python initialization or following Python finalization.

Added in version 3.14.

 int PyConfig_GetInt(const char *name, int *value)

Like `PyConfig_Get()`, except the value comes back as a C int.

- On success, hand back `0`.

- On error, raise an exception and hand back `-1`.

Added in version 3.14.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyConfig_Names(void)

Read every configuration option name back as a `frozenset`.

- On success, hand back a new reference.

- On error, raise an exception and hand back `NULL`.

An [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) is required of the caller. Invocation is impossible prior to Python initialization or following Python finalization.

Added in version 3.14.

[Subject index](INDEX.md) · [Previous source contract](configuration-options.md) · [Following source contract](pyconfig-set.md)
