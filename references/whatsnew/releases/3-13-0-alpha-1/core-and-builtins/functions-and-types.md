# Python 3.13.0 alpha 1 / core and builtins / functions and types

[gh-109219](https://github.com/python/cpython/issues/109219): Compiling type param scopes that reference a name which is likewise free within an inner scope is now fixed.

[gh-106213](https://github.com/python/cpython/issues/106213): Reworked how Emscripten call trampolines operate so they stay compatible with Wasm/JS Promise integration.

[gh-105840](https://github.com/python/cpython/issues/105840): Head off possible crashes while specializing function calls that carry too many `__defaults__`.

[gh-105678](https://github.com/python/cpython/issues/105678): Divide the `MAKE_FUNCTION` instruction into a pair: `MAKE_FUNCTION`, which builds the function, and `SET_FUNCTION_ATTRIBUTE`, which applies the attributes onto it. Doing so regularizes the stack effect of `MAKE_FUNCTION` to make optimization and code generation easier.

[gh-109118](https://github.com/python/cpython/issues/109118): An interpreter crash triggered when a NameError fires inside a generic class's type parameters is now fixed.

[gh-91095](https://github.com/python/cpython/issues/91095): Specializes calls to the majority of Python classes. Concretely, any class deriving from `object`, or from another Python class, that does not override `__new__`.

The specialized instruction carries out the following:

  1.

Creates the object (by calling `object.__new__`)

  2.

Pushes a shim frame to the frame stack (to cleanup after `__init__`)

  3.

Pushes the frame for `__init__` to the frame stack

Speeds up the instantiation of most Python classes.

[gh-91051](https://github.com/python/cpython/issues/91051): An abort / segfault that occurred when all eight type watcher slots were in use, on platforms whose `char` is signed by default, is now fixed.

[gh-107526](https://github.com/python/cpython/issues/107526): The conversion of `vars`, `dir`, `next`, `getattr`, and `iter` over to argument clinic was reverted.

[gh-107758](https://github.com/python/cpython/issues/107758): The `dump_stack()` routine that the `lltrace` feature (low-level interpreter debugging) uses was hardened against recursion by guaranteeing it never invokes a `__repr__` method written in Python. The comparable output for Tier-2 uops was also moved to `stdout` (rather than `stderr`) to align with the `lltrace` code in ceval.c.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
