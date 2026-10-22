# Python 3.6.0 alpha 1 / library / numeric behavior

[bpo-23517](https://bugs.python.org/issue?@action=redirect&bpo=23517): The fromtimestamp() and utcfromtimestamp() methods belonging to datetime.datetime now round microseconds to the nearest value, with ties landing on the nearest even integer (ROUND_HALF_EVEN) — matching round(float) — in place of rounding down toward -Infinity (ROUND_FLOOR).

[bpo-25995](https://bugs.python.org/issue?@action=redirect&bpo=25995): The number of FDs consumed by os.walk() is no longer proportional to how deep the tree goes.

[bpo-19883](https://bugs.python.org/issue?@action=redirect&bpo=19883): Corrected possible integer overflows within zipimport.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
