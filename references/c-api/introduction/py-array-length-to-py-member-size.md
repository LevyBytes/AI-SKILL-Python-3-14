# Type size utilities

#### Type size utilities

 Py_ARRAY_LENGTH(array)

Works out, at compile time, how long a statically allocated C array is.

The *array* argument has to be a C array whose size is known when compiling. Hand it an array of unknown size, like a heap-allocated array, and you'll either trigger a compilation error on some compilers or otherwise get wrong results.

Roughly equivalent to:

```c
sizeof(array) / sizeof((array)[0])

```

 Py_MEMBER_SIZE(type, member)

Yields, in bytes, the size of a *member* of a structure (*type*).

Roughly equivalent to `sizeof(((*type* *)NULL)->*member*)`.

Added in version 3.6.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-unused-to-py-gcc-attribute.md) · [Previous source contract](py-unreachable-to-py-build-assert-expr.md) · [Following source contract](py-force-expansion-to-py-stringify.md)
