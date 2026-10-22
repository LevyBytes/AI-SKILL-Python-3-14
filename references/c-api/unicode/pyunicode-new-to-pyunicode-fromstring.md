# unicode C API: `PyUnicode_New()`, `PyUnicode_FromKindAndData()`, `PyUnicode_FromStringAndSize()`, `PyUnicode_FromString()`

### Creating and accessing Unicode strings

The following APIs let you build Unicode objects and reach their basic sequence properties:

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_New([Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size, Py_UCS4 maxchar)

*Return value: New reference.*

Builds a fresh Unicode object. The *maxchar* argument should be the genuine highest code point destined for the string. As an estimate, you may round it up to the next value among 127, 255, 65535, 1114111.

When something goes wrong, an exception is set and `NULL` is returned.

Once created, you may populate the string with `PyUnicode_WriteChar()`, `PyUnicode_CopyCharacters()`, `PyUnicode_Fill()`, `PyUnicode_WRITE()`, or the like. Because strings are meant to be immutable, be careful never to “use” the result while it is still under modification. Specifically, until it carries its final contents, a string:

- must not be hashed,

- must not be `converted to UTF-8`, or another non-“canonical” representation,

- must not have its reference count changed,

- must not be shared with any code that could perform an action listed above.

The list above is not complete. Steering clear of these uses falls to you; Python will not always enforce these requirements.

So you don't accidentally leak a half-written string object, lean on the `PyUnicodeWriter` API, or one of the `PyUnicode_From*` functions described below.

Added in version 3.3.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_FromKindAndData(int kind, const void *buffer, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size)

*Return value: New reference.*

Builds a fresh Unicode object carrying the given *kind* (the allowed values are `PyUnicode_1BYTE_KIND` and so on, as handed back by `PyUnicode_KIND()`). The *buffer* has to address an array holding *size* units of 1, 2, or 4 bytes per character, matching the kind.

When required, the supplied *buffer* gets copied and converted into the canonical representation. For instance, when the *buffer* holds a UCS4 string (`PyUnicode_4BYTE_KIND`) yet contains only codepoints inside the UCS1 range, it gets converted down to UCS1 (`PyUnicode_1BYTE_KIND`).

Added in version 3.3.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_FromStringAndSize(const char *str, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Builds a Unicode object out of the char buffer *str*. Those bytes are taken to be UTF-8 encoded. The buffer gets copied into the new object. The result may turn out to be a shared object, meaning you may not modify the data.

This function raises [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) when:

- *size* < 0,

- *str* is `NULL` and *size* > 0

Changed in version 3.12: passing *str* == `NULL` together with *size* > 0 is now disallowed.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_FromString(const char *str)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Builds a Unicode object out of a UTF-8 encoded null-terminated char buffer *str*.

[Subject index](INDEX.md) · [Previous source contract](py-unicode-is-low-surrogate-to-py-unicode-join-surrogates.md) · [Following source contract](pyunicode-fromformat.md)
