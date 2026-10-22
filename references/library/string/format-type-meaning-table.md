# string — Format specification mini-language — Complete Type , Meaning table

| Type | Meaning |
| --- | --- |
| `'s'` | String format. This is the default type for strings and may be omitted. |
| None | The same as `'s'`. |

These are the available integer presentation types:

>
| Type | Meaning |
| --- | --- |
| `'b'` | Binary format. Outputs the number in base 2. |
| `'c'` | Character. Converts the integer to the corresponding unicode character before printing. |
| `'d'` | Decimal Integer. Outputs the number in base 10. |
| `'o'` | Octal format. Outputs the number in base 8. |
| `'x'` | Hex format. Outputs the number in base 16, using lower-case letters for the digits above 9. |
| `'X'` | Hex format. Outputs the number in base 16, using upper-case letters for the digits above 9. In case `'#'` is specified, the prefix `'0x'` will be upper-cased to `'0X'` as well. |
| `'n'` | Number. This is the same as `'d'`, except that it uses the current locale setting to insert the appropriate digit group separators. Note that the default locale is not the system locale. Depending on your use case, you may wish to set `LC_NUMERIC` with `locale.setlocale()` before using `'n'`. |
| None | The same as `'d'`. |

Beyond the presentation types above, integers may also be formatted using the floating-point presentation types given below (apart from `'n'` and `None`). When you do so, [`float()`](https://docs.python.org/3.14/library/functions.html#float) serves to turn the integer into a floating-point number ahead of formatting.

The available presentation types for [`float`](https://docs.python.org/3.14/library/functions.html#float) and [`Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) values are:

[Subject index](INDEX.md) · [Previous](format-specification-overview.md) · [Owning module, declaration or section: string](string-common-string-operations.md) · [Owning module, declaration or section: Format specification mini-language](format-specification-overview.md) · [Required continuation of the source contract](format-specification-mini-language.md)
