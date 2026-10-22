# Python 3.14.0 alpha 2 / core and builtins / collections and iteration

[gh-90370](https://github.com/python/cpython/issues/90370): Skip building a throwaway tuple for the vararg when passing arguments through Argument Clinic generated code (provided the arguments are either vararg or positional-only).

[gh-118423](https://github.com/python/cpython/issues/118423): Introduce a fresh `INSTRUCTION_SIZE` macro into the cases generator that reports the size of the current instruction.

[gh-125038](https://github.com/python/cpython/issues/125038): Resolve a crash that occurred while iterating a generator expression once `gi_frame.f_locals` had been changed directly. Patch by Mikhail Efimov.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
