# Python 3.6.0 alpha 1 / core and builtins / functions and types

[bpo-25961](https://bugs.python.org/issue?@action=redirect&bpo=25961): Null characters are now disallowed inside the type name.

[bpo-20440](https://bugs.python.org/issue?@action=redirect&bpo=20440): Carry out a sweeping swap of unsafe attribute setting code for the special macro Py_SETREF.

[bpo-25766](https://bugs.python.org/issue?@action=redirect&bpo=25766): The special method __bytes__() now operates correctly within str subclasses.

[bpo-25421](https://bugs.python.org/issue?@action=redirect&bpo=25421): The __sizeof__ methods on builtin types now rely on a dynamic basic size. That lets sys.getsize() behave correctly for their subclasses that define __slots__.

[bpo-22995](https://bugs.python.org/issue?@action=redirect&bpo=22995): The default __reduce__ and __reduce_ex__ implementations now turn away builtin types whose __new__ is not defined.

[bpo-24726](https://bugs.python.org/issue?@action=redirect&bpo=24726): Repair a crash plus a leaking NULL inside repr() of an OrderedDict that had been mutated through direct calls of dict methods.

[bpo-24806](https://bugs.python.org/issue?@action=redirect&bpo=24806): Block builtin types that may not be subclassed from being subclassed by way of multiple inheritance.

[bpo-26991](https://bugs.python.org/issue?@action=redirect&bpo=26991): Repair a possible refleak when a function carrying annotations is created.

[bpo-18531](https://bugs.python.org/issue?@action=redirect&bpo=18531): A lone var-keyword argument of a dict subtype used to reach the C-defined function untouched. Conversion to an exact dict now happens instead.

[bpo-26659](https://bugs.python.org/issue?@action=redirect&bpo=26659): Give the builtin slice type support for cycle collection.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
