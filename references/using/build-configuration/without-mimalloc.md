# --without-mimalloc

--without-mimalloc

Switch off the fast [mimalloc](https://docs.python.org/3.14/c-api/memory.html#mimalloc) allocator (on by default).

You cannot combine this option with `--disable-gil`, because mimalloc is required by the [free-threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) build.

Refer as well to the [`PYTHONMALLOC`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONMALLOC) environment variable.

[Subject index](INDEX.md) · [Previous source section](with-tail-call-interp.md) · [Following source section](without-pymalloc.md)
