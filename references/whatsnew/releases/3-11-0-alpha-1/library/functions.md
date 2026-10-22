# Python 3.11.0 alpha 1 / library / functions

[bpo-44752](https://bugs.python.org/issue?@action=redirect&bpo=44752): `rcompleter` avoids calling [`getattr()`](https://docs.python.org/3.14/library/functions.html#getattr) on [`property`](https://docs.python.org/3.14/library/functions.html#property) objects so as to sidestep the side-effect of running the matching method.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
