# datetime: `timedelta.microseconds`, `timedelta.total_seconds()`

timedelta.microseconds

Between 0 and 999,999 inclusive.

Supported operations:

| Operation | Result |
| --- | --- |
| `t1 = t2 + t3` | `t2` added to `t3`. Afterwards both `t1 - t2 == t3` and `t1 - t3 == t2` hold. (1) |
| `t1 = t2 - t3` | `t3` subtracted from `t2`. Afterwards both `t1 == t2 - t3` and `t2 == t1 + t3` hold. (1)(6) |
| `t1 = t2 * i or t1 = i * t2` | An integer times the delta. Afterwards `t1 // i == t2` holds, so long as `i != 0`. |
|  | More broadly, `t1 * i == t1 * (i-1) + t1` holds. (1) |
| `t1 = t2 * f or t1 = f * t2` | A float times the delta. Its result gets rounded to whichever multiple of timedelta.resolution is closest, ties going to even. |
| `f = t2 / t3` | Division (3) of total span `t2` by the unit interval `t3`. Yields a `float` object. |
| `t1 = t2 / f or t1 = t2 / i` | The delta over a float or an int. Its result gets rounded to whichever multiple of timedelta.resolution is closest, ties going to even. |
| `t1 = t2 // i` or `t1 = t2 // t3` | Takes the floor and drops whatever remainder is left. With the second form, the value returned is an integer. (3) |
| `t1 = t2 % t3` | The remainder is computed as a `timedelta` object. (3) |
| `q, r = divmod(t1, t2)` | Derives both quotient and remainder: `q = t1 // t2` (3) plus `r = t1 % t2`. Here `q` comes back an integer while `r` is a `timedelta` object. |
| `+t1` | Hands back a `timedelta` object holding the very same value. (2) |
| `-t1` | Equivalent to `timedelta(-t1.days, -t1.seconds, -t1.microseconds)`, and to `t1 * -1`. (1)(4) |
| `abs(t)` | Equivalent to `+t` when `t.days >= 0`, and to `-t` when `t.days < 0`. (2) |
| `str(t)` | Hands back a string shaped like `[D day[s], ][H]H:MM:SS[.UUUUUU]`, with D turning negative whenever `t` is negative. (5) |
| `repr(t)` | Hands back a string rendering of the `timedelta` object written as a constructor call carrying canonical attribute values. |

Notes:

1.

This is exact but may overflow.

2.

This is exact and cannot overflow.

3.

Division by zero raises [`ZeroDivisionError`](https://docs.python.org/3.14/library/exceptions.html#ZeroDivisionError).

4.

`-timedelta.max` is not representable as a `timedelta` object.

5.

The string forms of `timedelta` objects get normalized along the same lines as their internal form. That yields rather odd output for negative timedeltas. As an illustration:

```python
>>> timedelta(hours=-5)
datetime.timedelta(days=-1, seconds=68400)
>>> print(_)
-1 day, 19:00:00

```

6.

The expression `t2 - t3` always matches the expression `t2 + (-t3)`, except where t3 equals `timedelta.max`; there the first form yields a result whereas the second overflows.

Beyond the operations above, `timedelta` objects also permit some additions and subtractions involving `date` and `datetime` objects (see below).

Changed in version 3.2: Dividing one `timedelta` object by another `timedelta` object now works for both floor division and true division, and so do remainder operations together with the [`divmod()`](https://docs.python.org/3.14/library/functions.html#divmod) function. Multiplying a `timedelta` object by a [`float`](https://docs.python.org/3.14/library/functions.html#float) object, and dividing it by one via true division, are now supported as well.

`timedelta` objects support equality and order comparisons.

Within Boolean contexts, a `timedelta` object counts as true exactly when it differs from `timedelta(0)`.

Instance methods:

 timedelta.total_seconds()

Give back how many seconds the duration holds altogether. Equivalent to `td / timedelta(seconds=1)`. Should you want a unit interval that isn’t seconds, apply the division form yourself (for instance, `td / timedelta(microseconds=1)`).

Bear in mind that across very long spans (beyond roughly 270 years on most platforms) this method gives up microsecond precision.

Added in version 3.2.

[Subject index](INDEX.md) · [Previous](timedelta-min-to-timedelta-seconds.md) · [Continue](examples-of-usage-timedelta.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: datetime.timedelta](datetime-timedelta-class.md) · [Owning module, declaration or section: `timedelta` objects](timedelta-objects.md)
