# Python 3.11.0 alpha 1 / core and builtins / numeric behavior

[bpo-44297](https://bugs.python.org/issue?@action=redirect&bpo=44297): Guarantee the line number is assigned upon entry to a comprehension scope. That way, backtraces that include generator expressions report the right line number.

[bpo-44376](https://bugs.python.org/issue?@action=redirect&bpo=44376): Exact integer exponentiation (such as `i**2` or `pow(i, 2)`) with a small exponent now runs much faster, since overhead in those cases was cut.

[bpo-44954](https://bugs.python.org/issue?@action=redirect&bpo=44954): Resolved a corner-case bug in which `float.fromhex('0x.8p-1074')` got rounded in the wrong direction.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
