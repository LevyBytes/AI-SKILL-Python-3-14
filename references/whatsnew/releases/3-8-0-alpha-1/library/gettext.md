# Python 3.8.0 alpha 1 / library / gettext

[bpo-33710](https://bugs.python.org/issue?@action=redirect&bpo=33710): Marked the `l*gettext()` functions and methods within the [`gettext`](https://docs.python.org/3.14/library/gettext.html#module-gettext) module as deprecated. They hand back encoded bytes rather than Unicode strings and are leftovers from the Python 2 era. Likewise deprecated the functions and methods that set the charset for the `l*gettext()` functions and methods.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
