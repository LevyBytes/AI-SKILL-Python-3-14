# What's New In Python 3.3 / decimal

### decimal

[bpo-7652](https://bugs.python.org/issue?@action=redirect&bpo=7652) - integrate fast native decimal arithmetic.

Stefan Krah authored both the C-module and libmpdec.

For arbitrary precision, correctly rounded decimal floating-point arithmetic, the decimal module’s new C version folds in the high speed libmpdec library. IBM’s General Decimal Arithmetic Specification is what libmpdec conforms to.

Speedups stretch from roughly 10x on database-heavy workloads up to 100x where the work is numerically intensive. Treat those figures as the typical wins at the standard precisions chosen for decimal floating-point math. Because callers can configure precision themselves, the actual numbers will shift. As one illustration, integer bignum arithmetic can show gaps far wider than these.

Read the table below purely as a sample. You can find the benchmarks at [https://www.bytereef.org/mpdecimal/quickstart.html](https://www.bytereef.org/mpdecimal/quickstart.html).

>
|  | decimal.py | _decimal | speedup |
| --- | --- | --- | --- |
| pi | 42.02s | 0.345s | 120x |
| telco | 172.19s | 5.68s | 30x |
| psycopg | 3.57s | 0.29s | 12x |

[Subject index](INDEX.md) · [Previous source section](datetime.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](decimal-features.md)
