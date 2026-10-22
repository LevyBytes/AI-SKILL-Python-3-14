# Distinguishing Python integers/strings from GDB native values

One spot that trips people up is that the custom printer for certain types resembles GDB's built-in printer for standard types quite closely. Take the pretty-printer for a Python `int` ([PyLongObject](https://docs.python.org/3.14/c-api/long.html#c.PyLongObject)*): it yields a representation you cannot tell apart from that of an ordinary machine-level integer:

```none
(gdb) p some_machine_integer
$3 = 42

(gdb) p some_python_integer
$4 = 42

```

Casting to [PyLongObject](https://docs.python.org/3.14/c-api/long.html#c.PyLongObject)* exposes the internal structure:

```none
(gdb) p *(PyLongObject*)some_python_integer
$5 = {ob_base = {ob_base = {ob_refcnt = 8, ob_type = 0x3dad39f5e0}, ob_size = 1},
ob_digit = {42}}

```

Comparable confusion can crop up with the `str` type, whose output closely resembles gdb's built-in printer for `char *`:

```none
(gdb) p ptr_to_python_str
$6 = '__builtins__'

```

For `str` instances the pretty-printer defaults to single-quotes (just as Python's `repr` does for strings), whereas the standard printer for `char *` values opts for double-quotes and carries a hexadecimal address:

```none
(gdb) p ptr_to_char_star
$7 = 0x6d72c0 "hello world"

```

Once more, casting to [PyUnicodeObject](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeObject)* exposes the implementation details:

```none
(gdb) p *(PyUnicodeObject*)$6
$8 = {ob_base = {ob_refcnt = 33, ob_type = 0x3dad3a95a0}, length = 12,
str = 0x7ffff2128500, hash = 7065186196740147912, state = 1, defenc = 0x0}

```

[Subject index](INDEX.md) · [GDB PyObject pretty printing and underlying layouts](gdb-pyobject-pretty-printing-and-underlying-layouts.md) · [Previous source context](gdb-pyobject-pretty-printing-and-underlying-layouts.md) · [Following source context](py-list.md)
