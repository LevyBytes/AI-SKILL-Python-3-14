# Binary approximation, decimal display and representation

# Floatingpoint

### 15. Floating-Point Arithmetic: Issues and Limitations

Inside a computer's hardware, floating-point numbers take the form of base 2 (binary) fractions. To illustrate, the **decimal** fraction `0.625` works out to 6/10 + 2/100 + 5/1000, and likewise the **binary** fraction `0.101` amounts to 1/2 + 0/4 + 1/8. Both fractions come out to the very same value; what truly separates them is that one appears in base 10 fractional notation and the other in base 2.

Regrettably, the bulk of decimal fractions have no exact binary-fraction equivalent. The upshot is that, as a rule, whatever decimal floating-point numbers you type in are merely approximated by the binary floating-point values the machine truly holds.

Grasping the issue is simpler if you begin in base 10. Take the fraction 1/3, which you might approximate as a base 10 fraction this way:

```python
0.3

```

or, better,

```python
0.33

```

or, better,

```python
0.333

```

and onward. However many digits you are prepared to jot down, you will never land on exactly 1/3 — though each step gets you a closer and closer approximation to 1/3.

By the same token, however many base 2 digits you care to employ, the decimal quantity 0.1 has no exact base 2 fractional form. Written in base 2, 1/10 becomes a fraction that repeats forever

```python
0.0001100110011001100110011001100110011001100110011...

```

Cut it off at any finite count of bits and what remains is an approximation. Across most of today's machines, a float is approximated by a binary fraction whose numerator takes the leading 53 bits beginning at the most significant bit, paired with a denominator that is some power of two. For 1/10 specifically, that binary fraction comes out to `3602879701896397 / 2 ** 55`, a figure that sits near the genuine value of 1/10 without ever matching it precisely.

Plenty of people never notice this approximation, thanks to how the values get shown. What Python prints is only a decimal approximation of the actual decimal value behind the binary approximation the machine keeps. On the majority of machines, were Python to spell out the full decimal value of the binary approximation it stores for 0.1, it would end up showing:

```python
>>> 0.1
0.1000000000000000055511151231257827021181583404541015625

```

Since that runs to more digits than anyone really needs, Python trims things to a sensible length and shows a rounded figure in its place:

```pycon
>>> 1 / 10
0.1

```

Bear in mind that although the displayed figure resembles the precise value of 1/10, what is actually kept is the closest binary fraction that can be represented.

Curiously, a whole range of distinct decimal numbers map onto one and the same closest binary fraction. Take `0.1`, `0.10000000000000001`, and `0.1000000000000000055511151231257827021181583404541015625` — every one of them is approximated by `3602879701896397 / 2 ** 55`. Because these decimal values all collapse to that single approximation, displaying any of them keeps the invariant `eval(repr(x)) == x` intact.

In earlier days, both the Python prompt and the built-in [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) function settled on the 17-significant-digit form, `0.10000000000000001`. From Python 3.1 onward, Python — on the bulk of systems — can pick the shortest candidate and just print `0.1`.

Understand that this stems from the fundamental character of binary floating point — it is neither a defect in Python nor a defect in what you wrote. Every language that taps your hardware's floating-point arithmetic exhibits the same behavior (though certain languages might not *display* the discrepancy by default, or across all output modes).

If you prefer tidier output, string formatting lets you cap how many significant digits appear:

```pycon
>>> format(math.pi, '.12g')  # give 12 significant digits
'3.14159265359'

>>> format(math.pi, '.2f')   # give 2 digits after the point
'3.14'

>>> repr(math.pi)
'3.141592653589793'

```

Keep in mind that this amounts, quite literally, to an illusion: all you are doing is rounding the *display* of the genuine machine value.

[Subject index](INDEX.md) · [Following source section](float-comparison-rounding-and-exact-alternatives.md) · [Related tutorial example and explanation](float-comparison-rounding-and-exact-alternatives.md) · [Related tutorial example and explanation](exact-float-serialization-and-accurate-summation.md)
