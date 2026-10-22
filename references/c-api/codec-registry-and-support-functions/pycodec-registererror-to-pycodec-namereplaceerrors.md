# Registry API for Unicode encoding error handlers

### Registry API for Unicode encoding error handlers

 int PyCodec_RegisterError(const char *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *error)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Register the error handling callback function *error* beneath the given *name*. A codec invokes this callback whenever it runs into unencodable characters or undecodable bytes and *name* was the error parameter handed to the encode/decode call.

A lone argument reaches the callback: an instance of [`UnicodeEncodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeEncodeError), [`UnicodeDecodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeDecodeError), or [`UnicodeTranslateError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeTranslateError), carrying details of the troublesome run of characters or bytes together with its offset within the original string (see [Unicode Exception Objects](https://docs.python.org/3.14/c-api/exceptions.html#unicodeexceptions) for the functions that pull this information out). The callback has to either raise the exception it was handed or return a two-item tuple holding the substitute for the troublesome run plus an integer naming the offset in the original string where encoding/decoding ought to pick back up.

Hand back `0` when it works, `-1` on error.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyCodec_LookupError(const char *name)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Look up the error handling callback function that was registered beneath *name*. In one special case you may pass `NULL`, whereupon the error handling callback tied to “strict” is handed back.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyCodec_StrictErrors([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc)

*Return value: Always NULL.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Raise *exc*, treating it as an exception.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyCodec_IgnoreErrors([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Pass over the unicode error and skip the faulty input.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyCodec_ReplaceErrors([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Swap the unicode encode error for `?` or `U+FFFD`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyCodec_XMLCharRefReplaceErrors([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Swap the unicode encode error for XML character references.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyCodec_BackslashReplaceErrors([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Swap the unicode encode error for backslash escapes (`\x`, `\u` and `\U`).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyCodec_NameReplaceErrors([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exc)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Swap the unicode encode error for `\N{...}` escapes.

Added in version 3.5.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pycodec-register-to-pycodec-decode.md) · [Previous source contract](pycodec-encoder-to-pycodec-streamwriter.md) · [Following source contract](py-hexdigits.md)
