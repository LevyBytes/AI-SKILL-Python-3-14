# Python 3.12.0 alpha 1 / core and builtins / collections and iteration

[gh-91052](https://github.com/python/cpython/issues/91052): Provide an API for subscribing to modification events on chosen dictionaries.

[gh-97752](https://github.com/python/cpython/issues/97752): Resolve potential data corruption or crashes triggered by reading the `f_back` member on freshly-created generator or coroutine frames.

[gh-94262](https://github.com/python/cpython/issues/94262): Skips building frame objects for incomplete frames. Stops generator and closure creation from being visible to Python and C extensions, which restores how 3.10 and earlier behaved.

[gh-94192](https://github.com/python/cpython/issues/94192): Corrects an error on dictionary literals whose value is an invalid expression.

[gh-92777](https://github.com/python/cpython/issues/92777): Specializes `LOAD_METHOD` on objects holding lazy dictionaries. Ken Jin wrote the patch.

[gh-92236](https://github.com/python/cpython/issues/92236): Drops the bogus "LINE" event emitted at the start of a generator or coroutine, observable to tracing functions written in C.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
