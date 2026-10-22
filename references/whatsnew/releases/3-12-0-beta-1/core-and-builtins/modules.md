# Python 3.12.0 beta 1 / core and builtins / modules

[gh-102700](https://github.com/python/cpython/issues/102700): Permit built-in modules to act as submodules. That makes it possible to link submodules statically into a CPython binary.

[gh-99113](https://github.com/python/cpython/issues/99113): Multi-phase init extension modules can now signal that they work in subinterpreters owning their own GIL. To do so, supply `Py_MOD_PER_INTERPRETER_GIL_SUPPORTED` as the value of the `Py_mod_multiple_interpreters` module def slot. Without that, a module by default cannot be imported into such subinterpreters. (Neither the main interpreter nor subinterpreters lacking their own GIL are affected.) Beyond the isolation that multi-phase init already typically demands, per-interpreter GIL support adds a single further requirement: thread-safety. Should the module link against outside dependencies whose libraries hold any state that is not thread-safe, the module must take on the extra work of making it thread-safe. Such situations should be rare.

[gh-104108](https://github.com/python/cpython/issues/104108): Multi-phase init extension modules can now declare whether they genuinely support multiple interpreters. Such modules are assumed by default to work across several interpreters. For the rare module that does not, the new `Py_mod_multiple_interpreters` module def slot is available. A value of `0` signals that the module lacks support; `1` signals that it has support. `1` is the default.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
