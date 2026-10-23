# decimal - Constants

### Constants

This section's constants matter solely for the C module. For compatibility, they appear in the pure Python version as well.

|  | 32-bit | 64-bit |
| --- | --- | --- |
| decimal.MAX_PREC | `425000000` | `999999999999999999` |
| decimal.MAX_EMAX | `425000000` | `999999999999999999` |
| decimal.MIN_EMIN | `-425000000` | `-999999999999999999` |
| decimal.MIN_ETINY | `-849999999` | `-1999999999999999997` |
| decimal.IEEE_CONTEXT_MAX_BITS | `256` | `512` |

 decimal.HAVE_THREADS

Its value is `True`. Deprecated, since Python now ships with threads at all times.

Deprecated since version 3.9.

 decimal.HAVE_CONTEXTVAR

`True` is the default value. When Python is [`configured using the --without-decimal-contextvar option`](https://docs.python.org/3.14/using/configure.html#cmdoption-without-decimal-contextvar), the C version relies on a thread-local context in place of a coroutine-local one, and the value becomes `False`. Under certain nested context scenarios this runs marginally faster.

Added in version 3.8.3.

[Subject index](INDEX.md) · [Previous](decimal-context-to-sci-string.md) · [Continue](decimal-round-ceiling-to-decimal-round-05up.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md)
