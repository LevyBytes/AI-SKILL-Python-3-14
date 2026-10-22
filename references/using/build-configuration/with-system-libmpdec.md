# --with-system-libmpdec

--with-system-libmpdec

Compile the `_decimal` extension module against an already-installed `mpdecimal` library; refer to the [`decimal`](https://docs.python.org/3.14/library/decimal.html#module-decimal) module (on by default).

Added in version 3.3.

Changed in version 3.13: Default to using the installed `mpdecimal` library.

Changed in version 3.15: When no installed `mpdecimal` library turns up, a bundled copy of it will no longer be picked automatically. For Python 3.15 alone, you can still choose it deliberately via `--with-system-libmpdec=no` or `--without-system-libmpdec`.

Deprecated since version 3.13, will be removed in version 3.16: Python 3.16 will stop shipping a copy of the `mpdecimal` library sources.

See also

`LIBMPDEC_CFLAGS` and `LIBMPDEC_LIBS`.

[Subject index](INDEX.md) · [Previous source section](with-system-expat.md) · [Following source section](with-readline-readline-editline.md)
