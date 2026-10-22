# system interface C API: `PyOS_setsig()`, `PyOS_InterruptOccurred()`, `Py_EncodeLocale()`

PyOS_sighandler_t PyOS_setsig(int i, PyOS_sighandler_t h)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Bind the signal handler for signal *i* to *h*; yield the prior signal handler. It is a slim wrapper over either `sigaction()` or `signal()`. Never call those functions directly!

 int PyOS_InterruptOccurred(void)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Determine whether a `SIGINT` signal has arrived.

Yields `1` when a `SIGINT` has happened, clearing the signal flag, and otherwise yields `0`.

Most of the time, favor [`PyErr_CheckSignals()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_CheckSignals) rather than this routine. `PyErr_CheckSignals()` runs the right signal handlers for every pending signal, which lets Python code respond to the signal correctly. This routine merely notices `SIGINT` and runs no Python signal handlers at all.

The routine is async-signal-safe and is incapable of failing. Its caller is required to hold an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state).

 wchar_t *Py_DecodeLocale(const char *arg, size_t *size)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Warning

This routine ought not to be invoked directly: rely on the [`PyConfig`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig) API together with the [`PyConfig_SetBytesString()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_SetBytesString) function, which guarantees that [Python is preinitialized](https://docs.python.org/3.14/c-api/init_config.html#c-preinit).

The routine must not run before [Python is preinitialized](https://docs.python.org/3.14/c-api/init_config.html#c-preinit) so that the LC_CTYPE locale is set up correctly: consult the [`Py_PreInitialize()`](https://docs.python.org/3.14/c-api/init_config.html#c.Py_PreInitialize) function.

Decode a byte string using the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler). When the error handler is the [surrogateescape error handler](https://docs.python.org/3.14/library/codecs.html#surrogateescape), bytes that cannot be decoded turn into characters spanning U+DC80..U+DCFF; and whenever a byte sequence would decode into a surrogate character, those bytes get escaped through the surrogateescape error handler rather than being decoded.

Yield a pointer to a freshly allocated wide character string, and release that memory with [`PyMem_RawFree()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_RawFree). When size is not `NULL`, store the count of wide characters, excluding the null character, into `*size`

Yield `NULL` upon a decoding error or a memory allocation error. When *size* is not `NULL`, `*size` becomes `(size_t)-1` for a memory error or `(size_t)-2` for a decoding error.

The [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler) get chosen by [`PyConfig_Read()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Read): consult the [`filesystem_encoding`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.filesystem_encoding) and [`filesystem_errors`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.filesystem_errors) members of [`PyConfig`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig).

Decoding errors ought never to arise, save for a bug in the C library.

Apply the `Py_EncodeLocale()` function to encode the character string back into a byte string.

See also

The [`PyUnicode_DecodeFSDefaultAndSize()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_DecodeFSDefaultAndSize) and [`PyUnicode_DecodeLocaleAndSize()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_DecodeLocaleAndSize) functions.

Added in version 3.5.

Changed in version 3.7: Within the [Python UTF-8 Mode](https://docs.python.org/3.14/library/os.html#utf8-mode), the function henceforth relies on UTF-8 encoding.

Changed in version 3.8: On Windows the function henceforth relies on UTF-8 encoding whenever [`PyPreConfig.legacy_windows_fs_encoding`](https://docs.python.org/3.14/c-api/init_config.html#c.PyPreConfig.legacy_windows_fs_encoding) equals zero;

 char *Py_EncodeLocale(const wchar_t *text, size_t *error_pos)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Encode a wide character string with the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler). When the error handler is the [surrogateescape error handler](https://docs.python.org/3.14/library/codecs.html#surrogateescape), surrogate characters spanning U+DC80..U+DCFF become the bytes 0x80..0xFF.

Yield a pointer to a freshly allocated byte string, and release that memory with [`PyMem_Free()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Free). Yield `NULL` upon an encoding error or a memory allocation error.

When error_pos is not `NULL`, `*error_pos` becomes `(size_t)-1` on success, or it becomes the index of the offending character upon an encoding error.

The [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler) get chosen by [`PyConfig_Read()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Read): consult the [`filesystem_encoding`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.filesystem_encoding) and [`filesystem_errors`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.filesystem_errors) members of [`PyConfig`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig).

Apply the `Py_DecodeLocale()` function to decode the bytes string back into a wide character string.

Warning

You must not run this routine before [Python is preinitialized](https://docs.python.org/3.14/c-api/init_config.html#c-preinit), ensuring the LC_CTYPE locale ends up correctly set up: consult the [`Py_PreInitialize()`](https://docs.python.org/3.14/c-api/init_config.html#c.Py_PreInitialize) function.

See also

The [`PyUnicode_EncodeFSDefault()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_EncodeFSDefault) and [`PyUnicode_EncodeLocale()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_EncodeLocale) functions.

Added in version 3.5.

Changed in version 3.7: Within the [Python UTF-8 Mode](https://docs.python.org/3.14/library/os.html#utf8-mode), the function henceforth relies on UTF-8 encoding.

Changed in version 3.8: On Windows the function henceforth relies on UTF-8 encoding whenever [`PyPreConfig.legacy_windows_fs_encoding`](https://docs.python.org/3.14/c-api/init_config.html#c.PyPreConfig.legacy_windows_fs_encoding) equals zero.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyos-fspath-to-pyos-getsig.md) · [Following source contract](py-fopen-to-py-fclose.md)
