# What's New In Python 3.3 / decimal / API changes - collections.abc, decimal

#### API changes

- Context ceilings in the C module differ by the machine's architecture, as follows:

>
|  | 32-bit | 64-bit |
| --- | --- | --- |
| `MAX_PREC` | `425000000` | `999999999999999999` |
| `MAX_EMAX` | `425000000` | `999999999999999999` |
| `MIN_EMIN` | `-425000000` | `-999999999999999999` |

- Across the context templates ([`DefaultContext`](https://docs.python.org/3.14/library/decimal.html#decimal.DefaultContext), [`BasicContext`](https://docs.python.org/3.14/library/decimal.html#decimal.BasicContext) and [`ExtendedContext`](https://docs.python.org/3.14/library/decimal.html#decimal.ExtendedContext)) the size of [`Emax`](https://docs.python.org/3.14/library/decimal.html#decimal.Context.Emax) together with [`Emin`](https://docs.python.org/3.14/library/decimal.html#decimal.Context.Emin) is now `999999`.

- Inside decimal.py the [`Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) constructor ignores any context ceilings and reproduces values bearing arbitrary exponents or precision with full fidelity. The C build, carrying internal ceilings, follows this rule instead: where it can, a value is reproduced exactly; if not, [`InvalidOperation`](https://docs.python.org/3.14/library/decimal.html#decimal.InvalidOperation) fires and NaN comes back. Whenever that happens, you can still reach for [`create_decimal()`](https://docs.python.org/3.14/library/decimal.html#decimal.Context.create_decimal) to get a rounded or inexact answer.

- decimal.py rounds its power function correctly every time. The C build expresses it through the correctly rounded [`exp()`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal.exp) plus [`ln()`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal.ln) routines, yet the closing result is merely “almost always correctly rounded”.

- Within the C build the context dictionary that holds the signals is a [`MutableMapping`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.MutableMapping). To stay fast, [`flags`](https://docs.python.org/3.14/library/decimal.html#decimal.Context.flags) plus [`traps`](https://docs.python.org/3.14/library/decimal.html#decimal.Context.traps) keep pointing at the very same `MutableMapping` supplied when the context was set up. Assign a fresh signal dictionary and `flags` and `traps` take on its values, though they never start referencing the RHS dictionary.

- When you pickle a [`Context`](https://docs.python.org/3.14/library/decimal.html#decimal.Context), the emitted form differs now so that the Python build and the C build share one interchange format.

- Arguments to the [`Context`](https://docs.python.org/3.14/library/decimal.html#decimal.Context) constructor were reordered to line up with how [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) lays them out.

- [`quantize()`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal.quantize) now treats its `watchexp` parameter as deprecated.

[Subject index](INDEX.md) · [Previous source section](decimal-features.md) · [Next source section](email-policy-framework.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](decimal.md)
