# Python 3.5.2 release candidate 1 / core and builtins / functions and types

[bpo-4806](https://bugs.python.org/issue?@action=redirect&bpo=4806): Stop hiding the original TypeError that arises when star (`*`) unpacking is applied during function calls. Hagen Fürstenau and Daniel Urban supplied the patch this work draws on.

[bpo-25961](https://bugs.python.org/issue?@action=redirect&bpo=25961): Null characters are now forbidden inside the type name.

[bpo-20440](https://bugs.python.org/issue?@action=redirect&bpo=20440): Unsafe attribute-setting code was swapped out on a large scale in favor of the dedicated macro Py_SETREF.

[bpo-25766](https://bugs.python.org/issue?@action=redirect&bpo=25766): The special method __bytes__() now functions for str subclasses.

[bpo-25421](https://bugs.python.org/issue?@action=redirect&bpo=25421): The __sizeof__ methods on builtin types now rely on a dynamic basic size. Because of this, sys.getsize() behaves correctly for subclasses of those types that declare __slots__.

[bpo-26991](https://bugs.python.org/issue?@action=redirect&bpo=26991): Closed a possible refleak while building a function carrying annotations.

[bpo-26659](https://bugs.python.org/issue?@action=redirect&bpo=26659): Gave the builtin slice type support for cycle collection.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
