# Python 3.13.0 beta 1 / core and builtins / compiler and parser

[gh-118465](https://github.com/python/cpython/issues/118465): The compiler now fills the fresh `__firstlineno__` field on a class with the line number marking the opening line of that class definition.

[gh-116767](https://github.com/python/cpython/issues/116767): Stop the compiler crash on an "async with" carrying many context managers.

[gh-118306](https://github.com/python/cpython/issues/118306): Move JIT compilation onto LLVM 18

[gh-117901](https://github.com/python/cpython/issues/117901): Provide the compiler's codegen an option to retain nested instruction sequences so they can be introspected.

[gh-117549](https://github.com/python/cpython/issues/117549): Avoid designated initializer syntax inside inline functions within internal headers. Such syntax trips up C++ or MSVC users who have not yet adopted the newest C++ standard (C++20). One internal header, pycore_backoff.h, gets pulled in (by way of pycore_code.h) by certain important third-party software that does exactly this for performance.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
