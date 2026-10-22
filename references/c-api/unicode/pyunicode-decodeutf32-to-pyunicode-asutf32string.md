# UTF-32 Codecs

### UTF-32 Codecs

The UTF-32 codec APIs are listed below:

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_DecodeUTF32(const char *str, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size, const char *errors, int *byteorder)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Take *size* bytes out of a UTF-32 encoded buffer string, decode them, and hand back the matching Unicode object. When *errors* is non-`NULL` it specifies how errors are handled. The default value is “strict”.

When *byteorder* is non-`NULL`, the decoder begins decoding under the byte order it is handed:

```c
*byteorder == -1: little endian
*byteorder == 0:  native order
*byteorder == 1:  big endian

```

When `*byteorder` holds zero and the opening four bytes of the supplied data form a byte order mark (BOM), the decoder adopts that byte order, and the BOM does not get copied into the Unicode string that results. Should `*byteorder` equal `-1` or `1`, any byte order mark is copied to the output.

Once decoding finishes, **byteorder* holds the byte order in effect at the close of the input data.

When *byteorder* is `NULL`, native order mode is where the codec begins.

Return `NULL` if the codec raised an exception.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_DecodeUTF32Stateful(const char *str, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size, const char *errors, int *byteorder, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *consumed)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

When *consumed* is `NULL`, the behavior matches `PyUnicode_DecodeUTF32()`. When *consumed* is not `NULL`, `PyUnicode_DecodeUTF32Stateful()` refrains from flagging trailing incomplete UTF-32 byte sequences (for instance, a byte count that does not divide evenly by four) as an error. Such bytes go undecoded, and the count of bytes that were decoded gets recorded in *consumed*.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_AsUTF32String([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back a Python byte string encoded with UTF-32 in native byte order. A BOM mark always leads the string. Error handling is “strict”. Return `NULL` if the codec raised an exception.

[Subject index](INDEX.md) · [Previous source contract](pyunicode-asutf8.md) · [Following source contract](pyunicode-decodeutf16-to-pyunicode-asutf16string.md)
