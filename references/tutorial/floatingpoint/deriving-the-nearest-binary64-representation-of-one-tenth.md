# Deriving the nearest binary64 representation of one tenth

### 15.1. Representation Error

Here the “0.1” example is laid out thoroughly, demonstrating how you can carry out an exact analysis of such cases on your own. The text takes for granted a basic acquaintance with binary floating-point representation.

*Representation error* names the reality that a portion — in truth, most — of decimal fractions have no exact binary (base 2) fractional form. That is the principal reason Python (along with Perl, C, C++, Java, Fortran, and plenty more) frequently fails to show the precise decimal figure you'd anticipate.

What lies behind it? 1/10 simply has no exact binary-fraction form. From around the year 2000 onward, nearly every machine relies on IEEE 754 binary floating-point arithmetic, and nearly every platform maps Python floats onto IEEE 754 binary64 “double precision” values. Such binary64 values carry 53 bits of precision, so when 0.1 arrives the computer works to turn it into the nearest fraction it can manage of the form `J/2**N`, with *J* being an integer that holds exactly 53 bits. Recasting

```python
1 / 10 ~= J / (2**N)

```

as

```python
J ~= 2**N / 10

```

and bearing in mind that *J* spans exactly 53 bits (it is `>= 2**52` yet `< 2**53`), the optimal *N* turns out to be 56:

```pycon
>>> 2**52 <=  2**56 // 10  < 2**53
True

```

Put differently, 56 stands alone as the *N* that keeps *J* at precisely 53 bits. The finest *J* available is then that quotient after rounding:

```pycon
>>> q, r = divmod(2**56, 10)
>>> r
6

```

Given that the leftover exceeds half of 10, rounding upward yields the closest approximation:

```pycon
>>> q+1
7205759403792794

```

Consequently, the closest approximation to 1/10 that IEEE 754 double precision allows is:

```python
7205759403792794 / 2 ** 56

```

Halving the numerator alongside the denominator brings the fraction down to:

```python
3602879701896397 / 2 ** 55

```

Observe that, because we rounded upward, the figure sits marginally above 1/10; had we skipped the rounding up, the quotient would have come in marginally below 1/10 instead. Either way, it can never equal *exactly* 1/10!

[Subject index](INDEX.md) · [Previous source section](exact-float-serialization-and-accurate-summation.md) · [Following source section](recovering-the-stored-decimal-value-and-exact-fractions.md) · [Related tutorial example and explanation](recovering-the-stored-decimal-value-and-exact-fractions.md)
