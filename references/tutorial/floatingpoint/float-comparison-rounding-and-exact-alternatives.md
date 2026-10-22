# Floating-point comparisons, rounding and exact-arithmetic alternatives

A single illusion can spawn the next. Because 0.1 is not precisely 1/10, for instance, adding three copies of 0.1 together need not come out to exactly 0.3:

```pycon
>>> 0.1 + 0.1 + 0.1 == 0.3
False

```

What's more, given that 0.1 can draw no nearer to the true 1/10 and 0.3 can draw no nearer to the true 3/10, rounding ahead of time with the [`round()`](https://docs.python.org/3.14/library/functions.html#round) function brings no relief:

```pycon
>>> round(0.1, 1) + round(0.1, 1) + round(0.1, 1) == round(0.3, 1)
False

```

Even though the numbers can't be nudged any nearer to the exact values they stand for, the [`math.isclose()`](https://docs.python.org/3.14/library/math.html#math.isclose) function proves handy when you need to compare inexact values:

```pycon
>>> math.isclose(0.1 + 0.1 + 0.1, 0.3)
True

```

As another option, you can lean on the [`round()`](https://docs.python.org/3.14/library/functions.html#round) function to weigh rough approximations against each other:

```pycon
>>> round(math.pi, ndigits=2) == round(22 / 7, ndigits=2)
True

```

Surprises of this sort abound in binary floating-point arithmetic. The “0.1” puzzle gets a thorough, exact treatment further down, under the “Representation Error” heading. For an approachable rundown of how binary floating point operates and the troubles people routinely hit, look at [Examples of Floating Point Problems](https://jvns.ca/blog/2023/01/13/examples-of-floating-point-problems/). For a fuller catalog of further common gotchas, see [The Perils of Floating Point](http://www.indowsway.com/floatingpoint.htm).

To borrow its closing line, “there are no easy answers.” All the same, there's no cause to fear floating point unduly! Python's float operations inherit their errors straight from the floating-point hardware, and on the typical machine those errors stay within roughly 1 part in `2**53` for each operation. For the vast majority of jobs that precision is plenty, yet you should remember it is not decimal arithmetic and that any float operation may introduce a fresh rounding error.

Pathological cases certainly turn up, but for everyday, casual floating-point work you'll get the answer you anticipate as long as you round the displayed final results to however many decimal digits you're after. Generally [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) does the job, and when you want tighter control, consult the format specifiers of the [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) method described in [Format string syntax](https://docs.python.org/3.14/library/string.html#formatstrings).

When your scenario demands an exact decimal representation, reach for the [`decimal`](https://docs.python.org/3.14/library/decimal.html#module-decimal) module, whose decimal arithmetic fits accounting work and other high-precision needs.

A different flavor of exact arithmetic comes by way of the [`fractions`](https://docs.python.org/3.14/library/fractions.html#module-fractions) module, which builds its arithmetic on rational numbers (letting values such as 1/3 be held exactly).

Should floating-point operations be a big part of your work, it's worth examining the NumPy package along with the many other mathematical and statistical packages that the SciPy project provides. Visit <[https://scipy.org](https://scipy.org)>.

[Subject index](INDEX.md) · [Previous source section](binary-approximation-decimal-display-and-representation.md) · [Following source section](exact-float-serialization-and-accurate-summation.md) · [Related tutorial example and explanation](binary-approximation-decimal-display-and-representation.md) · [Related tutorial example and explanation](exact-float-serialization-and-accurate-summation.md)
