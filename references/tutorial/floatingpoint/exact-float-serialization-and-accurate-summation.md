# Exact float serialization and accurate summation

For the uncommon moments when you genuinely *do* need a float's exact value, Python supplies some helpers. One is the [`float.as_integer_ratio()`](https://docs.python.org/3.14/library/stdtypes.html#float.as_integer_ratio) method, which renders a float's value as a fraction:

```pycon
>>> x = 3.14159
>>> x.as_integer_ratio()
(3537115888337719, 1125899906842624)

```

Because that ratio is exact, you can rebuild the original value from it with no loss:

```pycon
>>> x == 3537115888337719 / 1125899906842624
True

```

The [`float.hex()`](https://docs.python.org/3.14/library/stdtypes.html#float.hex) method writes a float in hexadecimal (base 16), once more yielding the precise value your computer keeps:

```pycon
>>> x.hex()
'0x1.921f9f01b866ep+1'

```

From that exact hexadecimal form, the float value can be rebuilt without any error:

```pycon
>>> x == float.fromhex('0x1.921f9f01b866ep+1')
True

```

As the representation carries no error, it serves well for dependably moving values between different Python releases (independent of platform) and for trading data with other languages that handle the same format (Java and C99 among them).

The [`sum()`](https://docs.python.org/3.14/library/functions.html#sum) function is another useful aid, since it curbs precision loss while summing. As each value joins the running total, it carries out the intermediate rounding at extended precision. That can shift the overall accuracy enough that errors never pile up far enough to taint the final total:

```pycon
>>> 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 == 1.0
False
>>> sum([0.1] * 10) == 1.0
True

```

Going a step beyond, [`math.fsum()`](https://docs.python.org/3.14/library/math.html#math.fsum) keeps account of every “lost digit” while values accumulate into a running total, so that just one rounding affects the outcome. It runs slower than [`sum()`](https://docs.python.org/3.14/library/functions.html#sum) yet proves more accurate in those rare situations where large-magnitude inputs largely cancel, leaving a final sum hovering near zero:

```pycon
>>> arr = [-0.10430216751806065, -266310978.67179024, 143401161448607.16,
...        -143401161400469.7, 266262841.31058735, -0.003244936839808227]
>>> float(sum(map(Fraction, arr)))   # Exact summation with single rounding
8.042173697819788e-13
>>> math.fsum(arr)                   # Single rounding
8.042173697819788e-13
>>> sum(arr)                         # Multiple roundings in extended precision
8.042178034628478e-13
>>> total = 0.0
>>> for x in arr:
...     total += x                   # Multiple roundings in standard precision
...
>>> total                            # Straight addition has no correct digits!
-0.0051575902860057365

```

[Subject index](INDEX.md) · [Previous source section](float-comparison-rounding-and-exact-alternatives.md) · [Following source section](deriving-the-nearest-binary64-representation-of-one-tenth.md) · [Related tutorial example and explanation](binary-approximation-decimal-display-and-representation.md) · [Related tutorial example and explanation](float-comparison-rounding-and-exact-alternatives.md)
