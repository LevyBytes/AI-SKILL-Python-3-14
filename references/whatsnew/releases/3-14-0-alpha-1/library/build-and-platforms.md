# Python 3.14.0 alpha 1 / library / build and platforms

[gh-124171](https://github.com/python/cpython/issues/124171): Introduces a workaround for defective `fmod()` implementations on Windows that drop the zero sign (for instance `fmod(-10, 1)` yields `0.0`). Sergey B Kirpichev provided the patch.

[gh-118760](https://github.com/python/cpython/issues/118760): Errors triggered when invoking Tkinter bindings under Windows are now corrected.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
