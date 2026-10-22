# LDFLAGS_NODIST

LDFLAGS_NODIST

`LDFLAGS_NODIST` works just the way `CFLAGS_NODIST` does. Reach for it whenever a linker flag ought *not* to remain in `LDFLAGS` after Python has been installed ([gh-65320](https://github.com/python/cpython/issues/65320)).

Specifically, keep this out of `LDFLAGS`:

- the compiler flag `-L` (which sets the search path for libraries). The `-L` flags get applied left to right, so anything in `LDFLAGS` would override the `-L` flags a user or package supplies.

[Subject index](INDEX.md) · [Previous source section](configure-ldflags.md) · [Following source section](configure-ldflags-nodist.md)
