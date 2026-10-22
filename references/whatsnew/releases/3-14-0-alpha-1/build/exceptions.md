# Python 3.14.0 alpha 1 / build / exceptions

[gh-118943](https://github.com/python/cpython/issues/118943): Close a potential race condition in parallel builds set up with `--enable-experimental-jit`, where one process moving `jit_stencils.h.new` over to `jit_stencils.h` could trigger [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError) in another.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
