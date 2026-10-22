# Python 3.9.0 alpha 1 / core and builtins / functions and types

[bpo-37231](https://bugs.python.org/issue?@action=redirect&bpo=37231): Routing type slots toward special methods (such as invoking `__mul__` for `x * y`) has been accelerated.

[bpo-36974](https://bugs.python.org/issue?@action=redirect&bpo=36974): Provided distinct vectorcall functions covering each calling convention used by builtin functions and methods. Call performance benefits as a result.

[bpo-36922](https://bugs.python.org/issue?@action=redirect&bpo=36922): Slot functions now optimize every callable bearing `Py_TPFLAGS_METHOD_DESCRIPTOR`, not solely instances of `function`.

[bpo-36974](https://bugs.python.org/issue?@action=redirect&bpo=36974): The `tp_vectorcall_offset` slot is now inherited without condition so that `super().__call__()` keeps working when the base class relies on vectorcall.

[bpo-37994](https://bugs.python.org/issue?@action=redirect&bpo=37994): Stopped the silencing of arbitrary errors whenever an attribute lookup fails across several places. The only thing that ought to be silenced is AttributeError.

[bpo-36871](https://bugs.python.org/issue?@action=redirect&bpo=36871): Strengthened error handling in the assert_has_calls and assert_has_awaits methods belonging to mocks. Repaired a defect in which any error raised while binding the expected calls onto the mock's spec was quietly discarded, producing misleading error output.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
