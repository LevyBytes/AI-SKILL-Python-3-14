# Python 3.13.0 alpha 1 / library / gettext

[bpo-18319](https://bugs.python.org/issue?@action=redirect&bpo=18319): Guaranteed that `gettext(msg)` fetches translations even when a plural form is present. Put differently: `gettext(msg) == ngettext(msg, '', 1)`.

[gh-110519](https://github.com/python/cpython/issues/110519): The deprecation warning regarding a non-integer number inside [`gettext`](https://docs.python.org/3.14/library/gettext.html#module-gettext) now consistently points to the line in user code where the gettext function or method gets invoked. Earlier it might instead point to a line within `gettext` itself.

[gh-62519](https://github.com/python/cpython/issues/62519): Have [`gettext.pgettext()`](https://docs.python.org/3.14/library/gettext.html#gettext.pgettext) consult plural definitions whenever a translation cannot be located.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
