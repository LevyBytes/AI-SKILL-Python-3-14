# CFLAGS_NODIST

CFLAGS_NODIST

`CFLAGS_NODIST` serves the build of the interpreter and the stdlib C extensions. Reach for it whenever a compiler flag ought *not* to remain in `CFLAGS` after Python has been installed ([gh-65320](https://github.com/python/cpython/issues/65320)).

Specifically, keep these out of `CFLAGS`:

- the compiler flag `-I` (which sets the search path for include files). The `-I` flags get applied left to right, so anything in `CFLAGS` would override the `-I` flags a user or package supplies.

- hardening flags like `-Werror`, since distributions have no way to guarantee that user-installed packages live up to such stricter standards.

Added in version 3.5.

[Subject index](INDEX.md) · [Previous source section](cflags.md) · [Following source section](compileall-opts.md)
