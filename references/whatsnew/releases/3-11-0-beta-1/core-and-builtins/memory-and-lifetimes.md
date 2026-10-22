# Python 3.11.0 beta 1 / core and builtins / memory and lifetimes

[gh-92036](https://github.com/python/cpython/issues/92036): Resolve a subinterpreter crash tied to the garbage collector. Whenever a subinterpreter goes away, stop tracking every object its GC had tracked. So that deallocator functions which assume the GC still tracks their objects do not crash, intentionally leak a strong reference to those objects, which keeps them from ever being freed and stops their deallocators from running. Victor Stinner authored the patch.

[gh-91632](https://github.com/python/cpython/issues/91632): Resolve a small memory leak during shutdown by freeing the memory of the `generic_alias_iterator` type. Donghee Na authored the patch.

[bpo-43950](https://bugs.python.org/issue?@action=redirect&bpo=43950): Adopt one compact table covering line starts, line ends and column offsets. This halves how much memory location info consumes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
