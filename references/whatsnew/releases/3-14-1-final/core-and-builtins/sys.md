# Python 3.14.1 final / core and builtins / sys

[gh-140431](https://github.com/python/cpython/issues/140431): Resolve a crash inside Python’s [garbage collector](https://docs.python.org/3.14/glossary.html#term-garbage-collection) caused by partially initialized [coroutine](https://docs.python.org/3.14/glossary.html#term-coroutine) objects once coroutine origin tracking depth has been turned on ([`sys.set_coroutine_origin_tracking_depth()`](https://docs.python.org/3.14/library/sys.html#sys.set_coroutine_origin_tracking_depth)).

[gh-141579](https://github.com/python/cpython/issues/141579): Correct [`sys.activate_stack_trampoline()`](https://docs.python.org/3.14/library/sys.html#sys.activate_stack_trampoline) so it gives proper support to the `perf_jit` backend. Pablo Galindo supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
