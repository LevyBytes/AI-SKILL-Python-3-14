# Python 3.5.0 alpha 1 / core and builtins / functions and types

[bpo-22986](https://bugs.python.org/issue?@action=redirect&bpo=22986): Permit an object's __class__ to be swapped between a dynamic type and a static type under certain circumstances.

[bpo-22847](https://bugs.python.org/issue?@action=redirect&bpo=22847): Improve method cache efficiency.

[bpo-22540](https://bugs.python.org/issue?@action=redirect&bpo=22540): Made `PyObject_IsInstance` plus `PyObject_IsSubclass` quicker for the typical situation where the second argument carries metaclass `type`.

[bpo-18711](https://bugs.python.org/issue?@action=redirect&bpo=18711): Add a new `PyErr_FormatV` function, similar to `PyErr_Format` but accepting a `va_list` argument.

[bpo-16324](https://bugs.python.org/issue?@action=redirect&bpo=16324): The _charset parameter of MIMEText now takes email.charset.Charset instances as well. Claude Paroz wrote the initial patch.

[bpo-1764286](https://bugs.python.org/issue?@action=redirect&bpo=1764286): Repaired inspect.getsource() so it copes with decorated functions. Claudiu Popa supplied the patch.

[bpo-21389](https://bugs.python.org/issue?@action=redirect&bpo=21389): Displaying the __qualname__ of the underlying function in the repr of a bound method.

[bpo-20184](https://bugs.python.org/issue?@action=redirect&bpo=20184): Argument Clinic based signature introspection added for 30 of the builtin functions.

[bpo-20179](https://bugs.python.org/issue?@action=redirect&bpo=20179): Apply Argument Clinic to bytes and bytearray. Tal Einat provided the patch.

[bpo-21897](https://bugs.python.org/issue?@action=redirect&bpo=21897): Resolved a crash involving the f_locals attribute and closure variables once frame.clear() had been invoked.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
