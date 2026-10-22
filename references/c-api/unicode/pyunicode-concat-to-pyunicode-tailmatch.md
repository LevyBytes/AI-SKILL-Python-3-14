# unicode C API: `PyUnicode_Concat()`, `PyUnicode_Split()`, `PyUnicode_RSplit()`, `PyUnicode_Splitlines()`, `PyUnicode_Partition()`, `PyUnicode_RPartition()`, `PyUnicode_Join()`, `PyUnicode_Tailmatch()`

### Methods and Slot Functions

The APIs below can accept Unicode objects and strings as input (the descriptions call them strings) and give back either Unicode objects or integers as suits the case.

Each one returns `NULL` or `-1` when an exception occurs.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_Concat([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *left, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *right)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Join two strings to yield a fresh Unicode string.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_Split([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *sep, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) maxsplit)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Split a string to yield a list of Unicode strings. When *sep* is `NULL`, the split happens at every whitespace substring. Otherwise the splits land at the supplied separator. No more than *maxsplit* splits are performed. A negative value imposes no limit. Separators are left out of the list that results.

On error, return `NULL` with an exception set.

Equivalent to [`str.split()`](https://docs.python.org/3.14/library/stdtypes.html#str.split).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_RSplit([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *sep, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) maxsplit)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Like `PyUnicode_Split()`, except the splitting proceeds starting from the string's end.

On error, return `NULL` with an exception set.

Equivalent to [`str.rsplit()`](https://docs.python.org/3.14/library/stdtypes.html#str.rsplit).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_Splitlines([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, int keepends)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Split a Unicode string at line breaks and return a list of Unicode strings. A CRLF counts as a single line break. When *keepends* is `0`, the line break characters are left out of the strings that result.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_Partition([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *sep)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Split a Unicode string at where *sep* first appears, and return a 3-tuple holding the portion ahead of the separator, the separator on its own, and the portion following the separator. When the separator is absent, return a 3-tuple holding the string itself trailed by two empty strings.

*sep* must not be empty.

On error, return `NULL` with an exception set.

Equivalent to [`str.partition()`](https://docs.python.org/3.14/library/stdtypes.html#str.partition).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_RPartition([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *sep)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Like `PyUnicode_Partition()`, except it splits a Unicode string at where *sep* last appears. When the separator is absent, return a 3-tuple holding two empty strings trailed by the string itself.

*sep* must not be empty.

On error, return `NULL` with an exception set.

Equivalent to [`str.rpartition()`](https://docs.python.org/3.14/library/stdtypes.html#str.rpartition).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_Join([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *separator, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *seq)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Join a sequence of strings by way of the supplied *separator* and return the Unicode string that results.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyUnicode_Tailmatch([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *substr, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) start, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) end, int direction)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Return `1` when *substr* matches `unicode[start:end]` at the indicated tail end (*direction* == `-1` requests a prefix match, *direction* == `1` a suffix match), and `0` otherwise. Return `-1` should an error occur.

[Subject index](INDEX.md) · [Previous source contract](pyunicode-decodembcs-to-pyunicode-encodecodepage.md) · [Following source contract](pyunicode-find.md)
