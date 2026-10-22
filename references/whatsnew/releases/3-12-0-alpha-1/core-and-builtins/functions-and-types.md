# Python 3.12.0 alpha 1 / core and builtins / functions and types

[gh-95060](https://github.com/python/cpython/issues/95060): The undocumented `PyCode_Addr2Location` function now returns properly whenever its `addrq` argument is below zero.

[gh-96636](https://github.com/python/cpython/issues/96636): Guarantee that tracing, `sys.setrace()`, switches on right away. Across the pre-release builds of 3.11, certain tracing events could go missing when tracing was turned on inside a `__del__` method or an interrupt.

[gh-96348](https://github.com/python/cpython/issues/96348): Raise a DeprecationWarning whenever [`throw()`](https://docs.python.org/3.14/reference/expressions.html#generator.throw), [`throw()`](https://docs.python.org/3.14/reference/datamodel.html#coroutine.throw) or [`athrow()`](https://docs.python.org/3.14/reference/expressions.html#agen.athrow) receive more than a single argument.

[gh-90081](https://github.com/python/cpython/issues/90081): Execute Python code in a tracer/profiler function at full speed. This addresses a slowdown seen in earlier 3.11 builds.

[gh-95778](https://github.com/python/cpython/issues/95778): The `PyLong_FromString` function was reworked to be easier to maintain and extend.

[gh-93955](https://github.com/python/cpython/issues/93955): Speeds up attribute lookups for objects carrying a custom `__getattribute__` together with `__getattr__`. Ken Jin wrote the patch.

[gh-93911](https://github.com/python/cpython/issues/93911): Specializes `LOAD_ATTR` on `property()` attributes.

[gh-93662](https://github.com/python/cpython/issues/93662): Guarantees the end column offsets stay correct for multi-line method calls. Formerly the end column could land ahead of the column offset.

[gh-94822](https://github.com/python/cpython/issues/94822): Resolves a case where metaclass descriptor lookups could be skipped whenever a same-named attribute is also present directly on the class.

[gh-94036](https://github.com/python/cpython/issues/94036): Repair the incorrect source location info on some multi-line attribute accesses and method calls.

[gh-94938](https://github.com/python/cpython/issues/94938): Repair faulty error detection in a few builtin functions whenever a keyword argument name is an instance of a str subclass carrying overloaded `__eq__` and `__hash__`. Formerly this could yield a SystemError or other unwanted behavior.

[gh-93021](https://github.com/python/cpython/issues/93021): Corrects the `__text_signature__` on `__get__()` methods written in C. Jelle Zijlstra wrote the patch.

[gh-90473](https://github.com/python/cpython/issues/90473): Lowers the default recursion limit on WASI to cope with its restricted call stack size.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
