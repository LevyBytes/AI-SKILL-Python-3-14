# Python next / core and builtins / build and platforms

[gh-151546](https://github.com/python/cpython/issues/151546): Repair the stack limit verification whenever Python links against musl (for example Alpine Linux). The stack size that the linker configures is now used to derive the stack limits. Victor Stinner authored the change.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
