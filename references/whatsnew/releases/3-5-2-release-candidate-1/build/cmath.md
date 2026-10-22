# Python 3.5.2 release candidate 1 / build / cmath

[bpo-24421](https://bugs.python.org/issue?@action=redirect&bpo=24421): Modules/_math.c is now compiled a single time, ahead of building extensions. It had previously risked failing to compile correctly whenever the math and cmath builds ran at the same time.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
