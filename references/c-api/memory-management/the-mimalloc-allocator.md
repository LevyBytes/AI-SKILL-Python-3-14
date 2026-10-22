# The mimalloc allocator

### The mimalloc allocator

Added in version 3.13.

Where the platform underneath provides the necessary support, Python can use the [mimalloc](https://github.com/microsoft/mimalloc/) allocator. mimalloc is an all-purpose allocator known for strong performance, which Daan Leijen first built to serve the runtime systems behind the Koka and Lean languages.

Whereas pymalloc is geared toward small objects of 512 bytes or under, mimalloc copes with allocations of whatever size you throw at it.

Within a [free-threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) build, mimalloc stands as both the default and the **required** allocator for the `PYMEM_DOMAIN_MEM` and `PYMEM_DOMAIN_OBJ` domains, and there is no turning it off. Such a build relies on per-thread mimalloc heaps, letting most allocation and deallocation happen without any locking.

Within the ordinary (non-free-threaded) build, mimalloc is on hand yet is not the allocator picked by default. To choose it while running, set [`PYTHONMALLOC`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONMALLOC)`=mimalloc` (or `mimalloc_debug` when you want the debug hooks bundled in). To leave it out at build time, pass the [`--without-mimalloc`](https://docs.python.org/3.14/using/configure.html#cmdoption-without-mimalloc) configure option, which cannot, however, be paired with [`--disable-gil`](https://docs.python.org/3.14/using/configure.html#cmdoption-disable-gil).

[Subject index](INDEX.md) · [Previous source contract](pyobjectarenaallocator-to-pyobject-setarenaallocator.md) · [Following source contract](pytracemalloc-track-to-pytracemalloc-untrack.md)
