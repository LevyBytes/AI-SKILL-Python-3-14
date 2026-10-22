# What’s New in Python 2.4 / Why is Decimal needed?

### Why is Decimal needed?

These shortcomings stem from how floating-point numbers get represented. An FP number consists of three pieces:

- The sign, either positive or negative.

- The mantissa, a single-digit binary number trailed by a fractional portion. As an example, `1.01` written in base-2 stands for `1 + 0/2 + 1/4`, which is 1.25 in decimal.

- The exponent, which indicates where in the represented number the decimal point sits.

Consider the number 1.25: it carries a positive sign, a mantissa of 1.01 (in binary), and an exponent of 0 (no shifting of the decimal point is required). The number 5 shares that sign and mantissa, yet its exponent is 2 because the mantissa gets multiplied by 4 (2 raised to the exponent 2); 1.25 * 4 comes to 5.

These days, floating-point support on most systems follows a standard known as IEEE 754. Typically C’s double type is realized as a 64-bit IEEE 754 value, devoting 52 bits to the mantissa. That caps the precision of any number at 52 bits. When you attempt to represent numbers whose expansion never terminates, the expansion gets truncated past 52 bits. The trouble is, most software has to emit output in base 10, and ordinary base-10 fractions frequently turn into repeating decimals once expressed in binary. Consider 1.1 in decimal, which is `1.0001100110011 ...` in binary; .1 = 1/16 + 1/32 + 1/256 along with an endless run of further terms. After 52 digits IEEE 754 must lop off that endlessly repeating decimal, leaving the representation a touch off.

Now and then the inaccuracy becomes visible once you print the number:

```python
>>> 1.1
1.1000000000000001

```

That inaccuracy doesn’t always surface when you print the number, since the C library handles the FP-to-decimal-string conversion, and the majority of C libraries aim to emit reasonable output. Even when it stays hidden, though, the inaccuracy persists, and later operations can amplify the error.

Plenty of applications won’t care about this. Suppose I’m plotting points and showing them on my monitor: the gap between 1.1 and 1.1000000000000001 is far too tiny to see. Reports frequently trim output down to some fixed count of decimal places, and rounding to two places, or three, or even eight, keeps the error from ever showing. But where it truly does matter, building your own bespoke arithmetic routines takes a lot of effort.

That’s the reason the `Decimal` type came to be.

[Subject index](INDEX.md) · [Previous source section](pep-327-decimal-data-type.md) · [Next source section](the-decimal-type.md) · [Release/subject declaration](pep-218-built-in-set-objects.md)
