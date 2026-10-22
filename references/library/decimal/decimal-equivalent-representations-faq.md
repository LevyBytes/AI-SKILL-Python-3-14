# decimal — Decimal FAQ — Contract: Q: The same value can be written in many ways.

Q: The same value can be written in many ways. The numbers `200`, `200.000`, `2E2`, and `.02E+4` each hold the same value at differing precisions. Is there a way to convert them into a single recognizable canonical value?

A: The `normalize()` method maps every equivalent value onto one representative:

```python
>>> values = map(Decimal, '200 200.000 2E2 .02E+4'.split())
>>> [v.normalize() for v in values]
[Decimal('2E+2'), Decimal('2E+2'), Decimal('2E+2'), Decimal('2E+2')]

```

Q: At what point in a computation does rounding happen?

A: It happens *after* the computation. The decimal specification's philosophy holds that numbers are treated as exact and are built independently of the current context. They may even carry more precision than the current context. Computations run on those exact inputs, and then rounding (or another context operation) is applied to the computation's *result*:

```python
>>> getcontext().prec = 5
>>> pi = Decimal('3.1415926535')   # More than 5 digits
>>> pi                             # All digits are retained
Decimal('3.1415926535')
>>> pi + 0                         # Rounded after an addition
Decimal('3.1416')
>>> pi - Decimal('0.00005')        # Subtract unrounded numbers, then round
Decimal('3.1415')
>>> pi + 0 - Decimal('0.00005').   # Intermediate values are rounded
Decimal('3.1416')

```

Q: Certain decimal values always print in exponential notation. Is there a way to obtain a non-exponential representation?

A: For some values, exponential notation is the sole way to convey how many significant places the coefficient holds. Writing `5.0E+3` as `5000`, for instance, holds the value steady but cannot convey the original's two-place significance.

When an application has no interest in tracking significance, removing the exponent and trailing zeroes is straightforward, dropping significance yet leaving the value unchanged:

```python
>>> def remove_exponent(d):
...     return d.quantize(Decimal(1)) if d == d.to_integral() else d.normalize()

```

```python
>>> remove_exponent(Decimal('5E+3'))
Decimal('5000')

```

Q: Is there a way to turn an ordinary float into a `Decimal`?

A: Yes, every binary floating-point number can be represented exactly as a Decimal, though an exact conversion may demand more precision than intuition would suggest:

```pycon
>>> Decimal(math.pi)
Decimal('3.141592653589793115997963468544185161590576171875')

```

Q: In the middle of a complex calculation, how can I be confident I haven't ended up with a spurious result owing to insufficient precision or rounding anomalies.

A: The decimal module makes results easy to test. A best practice is to re-run calculations at greater precision and across various rounding modes. Widely diverging results point to insufficient precision, rounding mode problems, ill-conditioned inputs, or a numerically unstable algorithm.

Q: I observed that context precision applies to operation results but not to inputs. Is there anything to be wary of when mixing values of different precisions?

A: Yes. The guiding idea is that all values count as exact, and so does the arithmetic performed on them. Only the results undergo rounding. The upside for inputs is that “what you type is what you get”. The downside is that results can look strange if you forget the inputs were never rounded:

[Subject index](INDEX.md) · [Previous](decimal-faq-section-introduction-and-initial-examples.md) · [Owning module, declaration or section: decimal](decimal-decimal-fixed-point-and-floating-point-arithmetic.md) · [Owning module, declaration or section: Decimal FAQ](decimal-faq-section-introduction-and-initial-examples.md)
