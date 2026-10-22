# Outdated macros

### Outdated macros

The macros below once served features that have since been standardized in C11.

 Py_ALIGNED(num)

Set alignment at *num* bytes on whichever compilers support it.

Think about preferring the C11 standard `_Alignas` specifier over this macro.

 Py_LL(number)

 Py_ULL(number)

Treat *number*, in order, as a `long long` or an `unsigned long long` integer literal.

Expands to *number* trailed by `LL` or `LLU` respectively, though on some older compilers it expands into certain compiler-specific suffixes.

Think about preferring the C99 standard suffixes `LL` and `LLU` directly.

 Py_MEMCPY(dest, src, n)

A [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated) alias for `memcpy()`. Reach for `memcpy()` directly in its place.

Deprecated since version 3.14: The macro is [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated).

 Py_VA_COPY

A [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated) alias for the C99-standard `va_copy` function.

In the past, this would reach for a compiler-specific way to copy a `va_list`.

Changed in version 3.6: This is now an alias to `va_copy`.

[Subject index](INDEX.md) · [Previous source contract](py-always-inline-to-pyapi-data.md) · [Following source contract](objects-types-and-reference-counts.md)
