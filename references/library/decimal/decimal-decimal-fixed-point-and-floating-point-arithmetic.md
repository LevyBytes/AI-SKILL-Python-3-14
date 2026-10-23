# decimal`decimal` - Decimal fixed-point and floating-point arithmetic

### `decimal` - Decimal fixed-point and floating-point arithmetic

**Source code:** [Lib/decimal.py](https://github.com/python/cpython/tree/3.14/Lib/decimal.py)

---

Fast, correctly rounded decimal floating-point arithmetic is what the `decimal` module supplies. Compared with the [`float`](https://docs.python.org/3.14/library/functions.html#float) datatype, it brings a number of benefits:

- As the decimal arithmetic specification puts it, Decimal rests on a [floating-point model](https://speleotrove.com/decimal/damodel.html#refnumber) built around human needs, governed by one overriding rule: a computer's arithmetic has to behave the same way as the arithmetic taught to people in school.

- Exact representation is possible for decimal numbers. By contrast, values such as `1.1` and `2.2` lack precise binary floating-point equivalents. A typical user would not anticipate that `1.1 + 2.2` shows up as `3.3000000000000003`, which is what happens under binary floating point.

- That exactness extends to arithmetic. Working in decimal floating point, `0.1 + 0.1 + 0.1 - 0.3` comes out precisely equal to zero. Under binary floating point, you instead get `5.5511151231257827e-017`. Although close to zero, such gaps undermine dependable equality checks and can build up over time. That is why decimal suits accounting work, where strict equality invariants matter.

- A concept of significant places lives inside the decimal module, which is why `1.30 + 1.20` yields `2.50`. Retaining the trailing zero signals significance — the standard convention for money handling. With multiplication, the “schoolbook” method keeps every digit of the multiplicands. As an illustration, `1.3 * 1.2` produces `1.56`, whereas `1.30 * 1.20` produces `1.5600`.

- In contrast to hardware-driven binary floating point, the decimal module offers a precision the user can change (28 places by default), scalable to whatever size a particular problem demands:

```python
>>> from decimal import *
>>> getcontext().prec = 6
>>> Decimal(1) / Decimal(7)
Decimal('0.142857')
>>> getcontext().prec = 28
>>> Decimal(1) / Decimal(7)
Decimal('0.1428571428571428571428571429')

```

- Published standards underpin both binary and decimal floating point. Whereas the built-in float type surfaces only a small slice of its functionality, the decimal module surfaces every mandated piece of the standard. Where it matters, the programmer retains complete authority over rounding and signal handling. That extends to a mode that forces exact arithmetic by raising exceptions to halt any inexact operation.

- Per the decimal arithmetic specification, the module aims to back, even-handedly, both exact unrounded decimal arithmetic — fixed-point arithmetic, as it is sometimes called — and rounded floating-point arithmetic.

Three ideas anchor the module's design: the decimal number, the arithmetic context, and signals.

Decimal numbers are immutable. Each carries a sign, coefficient digits, and an exponent. So that significance is retained, trailing zeros in the coefficient digits are left intact. Special values such as `Infinity`, `-Infinity`, and `NaN` are part of Decimals as well. The standard likewise treats `-0` as distinct from `+0`.

An arithmetic context is a setting that fixes precision, rounding behavior, exponent bounds, flags that report operation outcomes, and trap enablers that decide whether signals become exceptions. The rounding choices are `ROUND_CEILING`, `ROUND_DOWN`, `ROUND_FLOOR`, `ROUND_HALF_DOWN`, `ROUND_HALF_EVEN`, `ROUND_HALF_UP`, `ROUND_UP`, and `ROUND_05UP`.

Signals collect the exceptional conditions that can surface while a computation runs. Per the application's requirements, a signal might be disregarded, taken as informational, or raised as an exception. Within the decimal module the signals are: `Clamped`, `InvalidOperation`, `DivisionByZero`, `Inexact`, `Rounded`, `Subnormal`, `Overflow`, `Underflow` and `FloatOperation`.

Every signal pairs a flag with a trap enabler. Hitting a signal sets its flag to one; thereafter, should the trap enabler equal one, an exception fires. Because flags are sticky, you must clear them before tracking a computation.

See also

- IBM’s General Decimal Arithmetic Specification, [The General Decimal Arithmetic Specification](https://speleotrove.com/decimal/decarith.html).

[Subject index](INDEX.md) · [Continue](decimal-quickstart-overview.md)
