# Python 3.14.0 alpha 1 / core and builtins / hashlib

[gh-99108](https://github.com/python/cpython/issues/99108): Blake2 inside Python's hashlib now always draws on the vendored HACL* library. libb2 is no longer recognized by Python as an optional dependency for Blake2.

We brought HACL* up to its newest version, and now vendor the 128-bit and 256-bit wide vector implementations of Blake2 from HACL*, which engage on x86/x64 toolchains whenever the needed CPU features show up at runtime.

The 128-bit wide vector implementation of Blake2 from HACL* is also capable of running on ARM NEON and Power8, yet without proof of a speedup these stay turned off (for now).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
