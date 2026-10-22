# What's new in Python 3.14 / Porting to Python 3.14 / Changes in the C API

### Changes in the C API

- Calling [`Py_Finalize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Finalize) now wipes out every interned string. That breaks compatibility for a C extension that keeps a reference to an interned string past a `Py_Finalize()` call and then tries to use it once [`Py_Initialize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Initialize) has run again. Trouble of this sort usually shows up as a crash while the following `Py_Initialize()` call executes, because freed memory is being read. The remedy is to run an address sanitizer, pinpoint the use-after-free tied to an interned string, and release that string while your module is tearing down. (Contributed by Eddie Elizondo in [gh-113601](https://github.com/python/cpython/issues/113601).)

- When the exception you hand to the [Unicode Exception Objects](https://docs.python.org/3.14/c-api/exceptions.html#unicodeexceptions) C API is not a [`UnicodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeError) instance, that API will now throw a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). (Contributed by Bénédikt Tran in [gh-127691](https://github.com/python/cpython/issues/127691).)

- Where it can, the interpreter skips certain refcount updates as it pushes objects onto the operands stack, opting to [borrow](https://docs.python.org/3.14/glossary.html#term-borrowed-reference) the reference instead. As a result, you may observe lower reference-count figures than earlier Python releases produced. Any C API extension that inspected [`Py_REFCNT()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_REFCNT) for a value of `1` to judge whether nothing else holds a given function argument ought to swap in [`PyUnstable_Object_IsUniqueReferencedTemporary()`](https://docs.python.org/3.14/c-api/object.html#c.PyUnstable_Object_IsUniqueReferencedTemporary), which is the safer choice.

- Formerly private routines that have graduated into the public C API surface:

  - `_PyBytes_Join()`: [`PyBytes_Join()`](https://docs.python.org/3.14/c-api/bytes.html#c.PyBytes_Join)

  - `_PyLong_IsNegative()`: [`PyLong_IsNegative()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_IsNegative)

  - `_PyLong_IsPositive()`: [`PyLong_IsPositive()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_IsPositive)

  - `_PyLong_IsZero()`: [`PyLong_IsZero()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_IsZero)

  - `_PyLong_Sign()`: [`PyLong_GetSign()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_GetSign)

  - `_PyUnicodeWriter_Dealloc()`: [`PyUnicodeWriter_Discard()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_Discard)

  - `_PyUnicodeWriter_Finish()`: [`PyUnicodeWriter_Finish()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_Finish)

  - `_PyUnicodeWriter_Init()`: use [`PyUnicodeWriter_Create()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_Create)

  - `_PyUnicodeWriter_Prepare()`: (no replacement)

  - `_PyUnicodeWriter_PrepareKind()`: (no replacement)

  - `_PyUnicodeWriter_WriteChar()`: [`PyUnicodeWriter_WriteChar()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteChar)

  - `_PyUnicodeWriter_WriteStr()`: [`PyUnicodeWriter_WriteStr()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteStr)

  - `_PyUnicodeWriter_WriteSubstring()`: [`PyUnicodeWriter_WriteSubstring()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicodeWriter_WriteSubstring)

  - `_PyUnicode_EQ()`: [`PyUnicode_Equal()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_Equal)

  - `_PyUnicode_Equal()`: [`PyUnicode_Equal()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_Equal)

  - `_Py_GetConfig()`: [`PyConfig_Get()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_Get) and [`PyConfig_GetInt()`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig_GetInt)

  -

`_Py_HashBytes()`: [`Py_HashBuffer()`](https://docs.python.org/3.14/c-api/hash.html#c.Py_HashBuffer)

  - `_Py_fopen_obj()`: [`Py_fopen()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_fopen)

  - `PyMutex_IsLocked()` : [`PyMutex_IsLocked()`](https://docs.python.org/3.14/c-api/synchronization.html#c.PyMutex_IsLocked)

If you need the bulk of these freshly exposed functions while running on Python 3.13 or earlier, the [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/) provides them.

[Subject index](INDEX.md) · [Previous source section](changes-in-annotations-from-future-import-annotations.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](porting-to-python-3-14.md) · [Next source section](notable-changes-in-3-14-1.md)
