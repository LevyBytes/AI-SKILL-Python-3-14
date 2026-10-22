# fractions / Rational numbers: `__round__()`, `__format__()`

__round__()

 __round__(*ndigits*)

The opening version yields the [`int`](https://docs.python.org/3.14/library/functions.html#int) closest to `self`, breaking ties toward even. The second version snaps `self` to the closest multiple of `Fraction(1, 10**ndigits)` (or its logical sense when `ndigits` is negative), once more breaking ties toward even. You can also get at this method by way of the [`round()`](https://docs.python.org/3.14/library/functions.html#round) function.

 __format__(*format_spec*, */*)

Backs the formatting of `Fraction` instances through the [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) method, the [`format()`](https://docs.python.org/3.14/library/functions.html#format) built-in function, or [Formatted string literals](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings).

When the `format_spec` format specification string closes with none of the presentation types `'e'`, `'E'`, `'f'`, `'F'`, `'g'`, `'G'` or `'%'`, formatting obeys the general handling of fill, alignment, sign, minimum width, and grouping laid out in the [format specification mini-language](https://docs.python.org/3.14/library/string.html#formatspec). It honors the “alternate form” flag `'#'`: when that's present, the output string is always made to spell out an explicit denominator, even where the formatted value is an exact integer. There's no support for the zero-fill flag `'0'`.

When the `format_spec` format specification string does close with one of the presentation types `'e'`, `'E'`, `'f'`, `'F'`, `'g'`, `'G'` or `'%'`, formatting instead obeys the rules given for the [`float`](https://docs.python.org/3.14/library/functions.html#float) type over in the [Format specification mini-language](https://docs.python.org/3.14/library/string.html#formatspec) section.

Here are some examples:

```python
>>> from fractions import Fraction
>>> format(Fraction(103993, 33102), '_')
'103_993/33_102'
>>> format(Fraction(1, 7), '.^+10')
'...+1/7...'
>>> format(Fraction(3, 1), '')
'3'
>>> format(Fraction(3, 1), '#')
'3/1'
>>> format(Fraction(1, 7), '.40g')
'0.1428571428571428571428571428571428571429'
>>> format(Fraction('1234567.855'), '_.2f')
'1_234_567.86'
>>> f"{Fraction(355, 113):*>20.6e}"
'********3.141593e+00'
>>> old_price, new_price = 499, 672
>>> "{:.2%} price increase".format(Fraction(new_price, old_price) - 1)
'34.67% price increase'

```

See also

Module [`numbers`](https://docs.python.org/3.14/library/numbers.html#module-numbers)

The abstract base classes that constitute the numeric tower.

[Subject index](INDEX.md) · [Previous](fraction-construction-and-conversion.md) · [Continue](../frameworks/program-frameworks.md) · [Owning module, declaration or section: fractions](fractions-fraction-class-to-fractions-fraction-class.md) · [Owning module, declaration or section: fractions.Fraction; fractions.Fraction; fractions.Fraction](fractions-fraction-class-to-fractions-fraction-class.md)
