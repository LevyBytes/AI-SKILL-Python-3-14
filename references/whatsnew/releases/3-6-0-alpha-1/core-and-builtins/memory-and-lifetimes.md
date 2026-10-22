# Python 3.6.0 alpha 1 / core and builtins / memory and lifetimes

[bpo-26718](https://bugs.python.org/issue?@action=redirect&bpo=26718): Calling super.__init__ repeatedly no longer leaks memory. NOTE: A direct call of super.__init__ is not endorsed!

[bpo-23601](https://bugs.python.org/issue?@action=redirect&bpo=23601): Julian Taylor made dict key object allocation faster by routing it through Python's small object allocator.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
