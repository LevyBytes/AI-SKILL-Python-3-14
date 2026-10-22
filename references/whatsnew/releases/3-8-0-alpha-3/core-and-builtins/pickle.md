# Python 3.8.0 alpha 3 / core and builtins / pickle

[bpo-36262](https://bugs.python.org/issue?@action=redirect&bpo=36262): Close an improbable memory leak during string-to-float conversion inside the `_Py_dg_strtod()` function that backs `float(str)`, `complex(str)`, [`pickle.load()`](https://docs.python.org/3.14/library/pickle.html#pickle.load), [`marshal.load()`](https://docs.python.org/3.14/library/marshal.html#marshal.load), and so on.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
