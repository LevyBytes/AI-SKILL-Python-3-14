# Python 3.6.0 alpha 1 / build / concurrent

[bpo-24421](https://bugs.python.org/issue?@action=redirect&bpo=24421): Build Modules/_math.c a single time, ahead of compiling the extensions. Earlier, a concurrent math and cmath build could leave it failing to compile correctly.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
