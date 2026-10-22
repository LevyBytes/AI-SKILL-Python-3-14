# argument parsing C API: `Py_BuildValue()`

### Building values

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *Py_BuildValue(const char *format, ...)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Builds a fresh value out of a format string resembling those the `PyArg_Parse*` family of functions accepts, together with a run of values. It hands back the value, or `NULL` when something goes wrong; a returned `NULL` is accompanied by a raised exception.

`Py_BuildValue()` won't always produce a tuple. A tuple results only when its format string carries two or more format units. An empty format string gives back `None`; a format string with just one format unit gives back whatever object that single unit describes. Wrap the format string in parentheses to compel a tuple of size 0 or one.

Whenever memory buffers come in as parameters that feed data into the objects being built — as happens with the `s` and `s#` formats — the needed data gets copied. The objects that `Py_BuildValue()` creates never hold onto buffers the caller supplied. Put differently, if your code calls `malloc()` and forwards that allocated memory to `Py_BuildValue()`, it falls to your code to call `free()` on it once `Py_BuildValue()` has returned.

Throughout the description below, the quoted item is the format unit; the item in (round) parentheses names the Python object type the format unit yields; and the item in [square] brackets names the type of the C value(s) you have to pass.

Within format strings, the space, tab, colon, and comma characters get disregarded (though not inside a format unit such as `s#`). You can exploit this to render a lengthy format string a little easier to read.

`s` ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or `None`) [const char *]

Turns a null-terminated C string into a Python [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) object via `'utf-8'` encoding. Where the C string pointer is `NULL`, `None` takes its place.

`s#` ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or `None`) [const char *, [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t)]

Turns a C string paired with its length into a Python [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) object via `'utf-8'` encoding. Where the C string pointer is `NULL`, the length goes unused and `None` comes back.

`y` ([`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes)) [const char *]

Turns a C string into a Python [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object. Where the C string pointer is `NULL`, `None` comes back.

`y#` ([`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes)) [const char *, [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t)]

Turns a C string along with its lengths into a Python object. Where the C string pointer is `NULL`, `None` comes back.

`z` ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or `None`) [const char *]

Same as `s`.

`z#` ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or `None`) [const char *, [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t)]

Same as `s#`.

`u` ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str)) [const wchar_t *]

Turns a null-terminated `wchar_t` buffer carrying Unicode (UTF-16 or UCS-4) data into a Python Unicode object. Where the Unicode buffer pointer is `NULL`, `None` comes back.

`u#` ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str)) [const wchar_t *, [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t)]

Turns a Unicode (UTF-16 or UCS-4) data buffer together with its length into a Python Unicode object. Where the Unicode buffer pointer is `NULL`, the length goes unused and `None` comes back.

`U` ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or `None`) [const char *]

Same as `s`.

`U#` ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or `None`) [const char *, [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t)]

Same as `s#`.

`i` ([`int`](https://docs.python.org/3.14/library/functions.html#int)) [int]

Turns a plain C int into a Python integer object.

`b` ([`int`](https://docs.python.org/3.14/library/functions.html#int)) [char]

Turns a plain C char into a Python integer object.

`h` ([`int`](https://docs.python.org/3.14/library/functions.html#int)) [short int]

Turns a plain C short int into a Python integer object.

`l` ([`int`](https://docs.python.org/3.14/library/functions.html#int)) [long int]

Turns a C long int into a Python integer object.

`B` ([`int`](https://docs.python.org/3.14/library/functions.html#int)) [unsigned char]

Turns a C unsigned char into a Python integer object.

`H` ([`int`](https://docs.python.org/3.14/library/functions.html#int)) [unsigned short int]

Turns a C unsigned short int into a Python integer object.

`I` ([`int`](https://docs.python.org/3.14/library/functions.html#int)) [unsigned int]

Turns a C unsigned int into a Python integer object.

[Subject index](INDEX.md) · [Previous source contract](py-cxx-const.md) · [Following source contract](py-vabuildvalue.md)
