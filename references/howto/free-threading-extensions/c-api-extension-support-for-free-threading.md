# C API Extension Support for Free Threading

# Free Threading Extensions

### C API Extension Support for Free Threading

Beginning with version 3.13, CPython can execute while the [global interpreter lock](https://docs.python.org/3.14/glossary.html#term-global-interpreter-lock) (GIL) is switched off — a build option referred to as [free threading](https://docs.python.org/3.14/glossary.html#term-free-threading). The pages that follow walk through what it takes to make a C API extension work under that build.

[Subject index](INDEX.md) · [Following source context](identifying-the-free-threaded-build-in-c.md)
