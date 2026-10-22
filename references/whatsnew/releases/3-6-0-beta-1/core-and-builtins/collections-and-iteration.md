# Python 3.6.0 beta 1 / core and builtins / collections and iteration

[bpo-27812](https://bugs.python.org/issue?@action=redirect&bpo=27812): Clear a generator’s frame’s backreference to the generator properly, heading off crashes inside frame.clear().

[bpo-23722](https://bugs.python.org/issue?@action=redirect&bpo=23722): The __class__ cell that a zero-argument super() relies on is now set up by type.__new__ instead of __build_class__, so class methods that depend on it behave correctly even when invoked from metaclass methods while a class is being created. Martin Teichmann wrote the patch.

[bpo-28071](https://bugs.python.org/issue?@action=redirect&bpo=28071): Provide an early-out for differencing against an empty set.

[bpo-26058](https://bugs.python.org/issue?@action=redirect&bpo=26058): Give the builtin dict type a new private version, bumped on every dictionary creation and on every dictionary change. This realizes PEP 509.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
