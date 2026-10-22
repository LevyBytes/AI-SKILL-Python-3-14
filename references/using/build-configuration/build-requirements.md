# 3.1. Build Requirements

### 3. Configure Python

### 3.1. Build Requirements

The following are prerequisites for compiling CPython:

- A [C11](https://en.cppreference.com/w/c/11) compiler. The [Optional C11 features](https://en.wikipedia.org/wiki/C11_(C_standard_revision)#Optional_features) need not be present.

- Under Windows, you must have Microsoft Visual Studio 2017 or a newer release.

- Handling of [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754) floating-point values together with [floating-point Not-a-Number (NaN)](https://en.wikipedia.org/wiki/NaN#Floating_point).

- Thread handling.

Changed in version 3.5: Under Windows, the minimum is now Visual Studio 2015 or a later version.

Changed in version 3.6: Particular C99 capabilities, such as `<stdint.h>` plus `static inline` functions, became mandatory.

Changed in version 3.7: Threading support became mandatory.

Changed in version 3.11: A C11 compiler plus IEEE 754 and NaN handling became mandatory. Under Windows, the requirement is Visual Studio 2017 or newer.

Consult as well [**PEP 7**](https://peps.python.org/pep-0007/) “Style Guide for C Code” along with [**PEP 11**](https://peps.python.org/pep-0011/) “CPython platform support”.

[Subject index](INDEX.md) · [Following source section](requirements-for-optional-modules.md)
