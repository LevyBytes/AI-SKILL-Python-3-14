# What's New In Python 3.6 / decimal — decimal

### decimal

A new [`Decimal.as_integer_ratio()`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal.as_integer_ratio) method hands back a pair `(n, d)` of integers expressing the supplied [`Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) instance as a fraction, reduced to lowest terms and carrying a positive denominator:

```python
>>> Decimal('-3.14').as_integer_ratio()
(-157, 50)

```

(Contributed by Stefan Krah amd Mark Dickinson in [bpo-25928](https://bugs.python.org/issue?@action=redirect&bpo=25928).)

[Subject index](INDEX.md) · [Previous source section](datetime.md) · [Next source section](distutils.md) · [Release/subject declaration](summary-release-highlights.md)
