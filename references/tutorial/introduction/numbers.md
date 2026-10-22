# 3.1.1. Numbers

### 3.1.1. Numbers

Think of the interpreter as a basic calculator: feed it an expression and it returns the result. The syntax for expressions is plain — the operators `+`, `-`, `*` and `/` carry out arithmetic, while parentheses (`()`) handle grouping. Here is an illustration:

```python
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5  # division always returns a floating-point number
1.6

```

Whole numbers (for instance `2`, `4`, `20`) carry the type [`int`](https://docs.python.org/3.14/library/functions.html#int), whereas those carrying a fractional component (for instance `5.0`, `1.6`) carry the type [`float`](https://docs.python.org/3.14/library/functions.html#float). More on the numeric types comes up further along in the tutorial.

The `/` operator always hands back a float. When you instead want [floor division](https://docs.python.org/3.14/glossary.html#term-floor-division) yielding a whole number, reach for the `//` operator; for the leftover remainder, reach for `%`:

```python
>>> 17 / 3  # classic division returns a float
5.666666666666667
>>>
>>> 17 // 3  # floor division discards the fractional part
5
>>> 17 % 3  # the % operator returns the remainder of the division
2
>>> 5 * 3 + 2  # floored quotient * divisor + remainder
17

```

In Python you can raise a value to a power with the `**` operator [1]:

```python
>>> 5 ** 2  # 5 squared
25
>>> 2 ** 7  # 2 to the power of 7
128

```

A variable receives a value by way of the equal sign (`=`). Once that happens, nothing prints back before the next interactive prompt shows up:

```python
>>> width = 20
>>> height = 5 * 9
>>> width * height
900

```

Should a variable never have been "defined" (given a value), an attempt to reference it raises an error:

```python
>>> n  # try to access an undefined variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined

```

Floating point is fully supported; when an operator's operands mix types, the integer operand is promoted to floating point:

```python
>>> 4 * 3.75 - 1
14.0

```

While in interactive mode, the variable `_` holds whatever expression was printed last. As a result, treating Python like a pocket calculator becomes a little smoother for chaining one calculation onto the next, as shown here:

```python
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06

```

Regard this variable as read-only on your end. Avoid binding a value to it directly — doing that spins up a separate local variable of the same name that shadows the built-in one along with its special behavior.

Beyond [`int`](https://docs.python.org/3.14/library/functions.html#int) and [`float`](https://docs.python.org/3.14/library/functions.html#float), Python offers further kinds of numbers, among them [`Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) and [`Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction). The language likewise ships native handling for [complex numbers](https://docs.python.org/3.14/library/stdtypes.html#typesnumeric), marking the imaginary component with a `j` or `J` suffix (for instance `3+5j`).

[Subject index](INDEX.md) · [Previous source section](using-python-as-a-calculator.md) · [Following source section](string-quotation-escapes-raw-strings-and-multiline-literals.md)
