# Python 3.6.0 alpha 1 / build / compiler and parser

[bpo-22359](https://bugs.python.org/issue?@action=redirect&bpo=22359): Turn off the make rules that run _freeze_importlib and pgen during cross-compilation. What those programs emit is usually committed beside the source anyway, and it still gets regenerated whenever a native build runs. Xavier de Gaye authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
