# What’s New In Python 3.12 / sys - sys, sys.monitoring

### sys

- Add the [`sys.monitoring`](https://docs.python.org/3.14/library/sys.monitoring.html#module-sys.monitoring) namespace, surfacing the new PEP 669 monitoring API. (Contributed by Mark Shannon in [gh-103082](https://github.com/python/cpython/issues/103082).)

- Add [`sys.activate_stack_trampoline()`](https://docs.python.org/3.14/library/sys.html#sys.activate_stack_trampoline) together with [`sys.deactivate_stack_trampoline()`](https://docs.python.org/3.14/library/sys.html#sys.deactivate_stack_trampoline) for turning stack profiler trampolines on and off, plus [`sys.is_stack_trampoline_active()`](https://docs.python.org/3.14/library/sys.html#sys.is_stack_trampoline_active) for checking whether stack profiler trampolines are running. (Contributed by Pablo Galindo together with Christian Heimes, plus further work from Gregory P. Smith [Google] and Mark Shannon in [gh-96123](https://github.com/python/cpython/issues/96123).)

- Add [`sys.last_exc`](https://docs.python.org/3.14/library/sys.html#sys.last_exc), carrying the most recent unhandled exception that got raised (handy for post-mortem debugging). Deprecate the trio of fields holding that same data in older form: [`sys.last_type`](https://docs.python.org/3.14/library/sys.html#sys.last_type), [`sys.last_value`](https://docs.python.org/3.14/library/sys.html#sys.last_value) and [`sys.last_traceback`](https://docs.python.org/3.14/library/sys.html#sys.last_traceback). (Contributed by Irit Katriel in [gh-102778](https://github.com/python/cpython/issues/102778).)

- [`sys._current_exceptions()`](https://docs.python.org/3.14/library/sys.html#sys._current_exceptions) now hands back a mapping going from thread-id to an exception instance instead of to a `(typ, exc, tb)` tuple. (Contributed by Irit Katriel in [gh-103176](https://github.com/python/cpython/issues/103176).)

-

[`sys.setrecursionlimit()`](https://docs.python.org/3.14/library/sys.html#sys.setrecursionlimit) and [`sys.getrecursionlimit()`](https://docs.python.org/3.14/library/sys.html#sys.getrecursionlimit). Only Python-level code is now bound by the recursion limit. Builtin functions sidestep it entirely; a separate safeguard instead keeps their recursion from crashing the virtual machine.

[Subject index](INDEX.md) · [Previous source section](statistics.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](tempfile.md)
