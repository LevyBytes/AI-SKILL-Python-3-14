# Python 3.8.0 alpha 1 / core and builtins / exceptions

[bpo-33237](https://bugs.python.org/issue?@action=redirect&bpo=33237): Made the [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) message clearer for a partially initialized module.

[bpo-29743](https://bugs.python.org/issue?@action=redirect&bpo=29743): Raise [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) rather than [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) when a negative `_length_` appears in a [`ctypes.Array`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Array) subclass. Likewise, raise [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) rather than [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) for a non-integer `_length_`. Original patch by Oren Milman.

[bpo-35029](https://bugs.python.org/issue?@action=redirect&bpo=35029): A [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning) thrown as an exception while code is being generated will now be turned into a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) so that errors are reported more clearly.

[bpo-32912](https://bugs.python.org/issue?@action=redirect&bpo=32912): For invalid escape sequences inside string and bytes literals, a [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning) is now produced rather than a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning).

[bpo-34850](https://bugs.python.org/issue?@action=redirect&bpo=34850): The compiler will now emit a [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning) whenever identity checks (`is` and `is not`) are applied to certain literal kinds (for example strings, ints). Such checks may happen to succeed by chance under CPython, yet the language spec offers no guarantee. The warning recommends that users switch to equality tests (`==` and `!=`).

[bpo-23722](https://bugs.python.org/issue?@action=redirect&bpo=23722): A [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) is now thrown whenever a custom metaclass omits the `__classcell__` entry from the namespace handed to `type.__new__`. Across Python 3.6–3.7 a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) was issued instead.

[bpo-35504](https://bugs.python.org/issue?@action=redirect&bpo=35504): Repair segfaults plus [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError)s raised while deleting certain attributes. Patch by Zackery Spytz.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
