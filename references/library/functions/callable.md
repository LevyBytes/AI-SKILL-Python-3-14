# callable

callable(*object*, */*)

Give back [`True`](https://docs.python.org/3.14/library/constants.html#True) when the *object* argument looks callable, and [`False`](https://docs.python.org/3.14/library/constants.html#False) otherwise. A `True` result still leaves open the chance that a call will fail, yet a `False` result guarantees calling *object* can never work. Keep in mind that classes are callable (calling one yields a fresh instance); instances are callable when their class defines a [`__call__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__call__) method.

Added in version 3.2: Python 3.0 dropped this function at first, and version 3.2 then restored it.

[Builtin task index](INDEX.md).
