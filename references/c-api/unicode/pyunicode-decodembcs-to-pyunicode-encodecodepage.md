# MBCS codecs for Windows

### MBCS codecs for Windows

The MBCS codec APIs are listed below. At present they exist on Windows alone and call the Win32 MBCS converters to carry out the conversions. Keep in mind that MBCS (or DBCS) names a family of encodings rather than a single one. Which target encoding applies is determined by the user settings on the machine where the codec runs.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_DecodeMBCS(const char *str, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size, const char *errors)

*Return value: New reference.** Belongs to the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) on Windows as of version 3.7.*

Build a Unicode object by decoding *size* bytes from the MBCS encoded string *str*. Return `NULL` if the codec raised an exception.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_DecodeMBCSStateful(const char *str, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size, const char *errors, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *consumed)

*Return value: New reference.** Included in the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) on Windows starting with version 3.7.*

When *consumed* is `NULL`, the behavior matches `PyUnicode_DecodeMBCS()`. When *consumed* is not `NULL`, `PyUnicode_DecodeMBCSStateful()` leaves a trailing lead byte undecoded, and the count of bytes that were decoded gets recorded in *consumed*.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_DecodeCodePageStateful(int code_page, const char *str, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) size, const char *errors, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) *consumed)

*Return value: New reference.** Counts toward the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) on Windows beginning at version 3.7.*

Like `PyUnicode_DecodeMBCSStateful()`, save that it relies on the code page named by *code_page*.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_AsMBCSString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode)

*Return value: New reference.** A member of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) on Windows from version 3.7 onward.*

Apply MBCS to encode a Unicode object and hand back the outcome as a Python bytes object. Error handling is “strict”. Return `NULL` if the codec raised an exception.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyUnicode_EncodeCodePage(int code_page, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *unicode, const char *errors)

*Return value: New reference.** Listed in the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) on Windows since release 3.7.*

Use the named code page to encode the Unicode object and hand back a Python bytes object. Return `NULL` if the codec raised an exception. Pass the `CP_ACP` code page to obtain the MBCS encoder.

Added in version 3.3.

[Subject index](INDEX.md) · [Previous source contract](pyunicode-decodecharmap-to-pyunicode-translate.md) · [Following source contract](pyunicode-concat-to-pyunicode-tailmatch.md)
