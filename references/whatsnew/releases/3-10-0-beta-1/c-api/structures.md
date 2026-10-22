# Python 3.10.0 beta 1 / c api / structures

[bpo-43753](https://bugs.python.org/issue?@action=redirect&bpo=43753): The [`Py_Is(x, y)`](https://docs.python.org/3.14/c-api/structures.html#c.Py_Is) function was added to check whether the *x* object is the *y* object, matching `x is y` in Python. Also added were [`Py_IsNone()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_IsNone), [`Py_IsTrue()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_IsTrue), and [`Py_IsFalse()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_IsFalse) to check whether an object is, in turn, the `None` singleton, the `True` singleton, or the `False` singleton. Victor Stinner supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
