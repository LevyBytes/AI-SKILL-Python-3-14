# Why are floating-point calculations so inaccurate?

### Why are floating-point calculations so inaccurate?

Outcomes such as the following frequently catch users off guard:

```python
>>> 1.2 - 1.0
0.19999999999999996

```

and lead them to suppose Python has a bug. It doesn't. The cause has scarcely anything to do with Python, and far more to do with the way the underlying platform treats floating-point numbers.

In CPython, the [`float`](https://docs.python.org/3.14/library/functions.html#float) type relies on a C `double` for its storage. The value held by a `float` object lives in binary floating-point at a fixed precision (usually 53 bits), and Python leans on C operations, which themselves defer to the processor's hardware implementation, to carry out floating-point arithmetic. So where floating-point operations are concerned, Python acts like a number of widely used languages, C and Java among them.

A great many numbers that are simple to write in decimal form have no exact representation in binary floating point. As an illustration, following:

```python
>>> x = 1.2

```

the value kept for `x` is a (very good) approximation to the decimal value `1.2`, though it isn't precisely equal to it. On a typical machine, the value actually stored is:

```python
1.0011001100110011001100110011001100110011001100110011 (binary)

```

which is exactly:

```python
1.1999999999999999555910790149937383830547332763671875 (decimal)

```

The customary 53-bit precision grants Python floats roughly 15–16 decimal digits of accuracy.

For a more complete treatment, please consult the [floating-point arithmetic](https://docs.python.org/3.14/tutorial/floatingpoint.html#tut-fp-issues) chapter within the Python tutorial.

[Subject index](INDEX.md)
