# Controlling the Garbage Collector State

### Controlling the Garbage Collector State

For steering garbage collection runs, the C-API offers the functions below.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyGC_Collect(void)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Carry out a full garbage collection, so long as the garbage collector is enabled. (Note that [`gc.collect()`](https://docs.python.org/3.14/library/gc.html#gc.collect) runs one no matter what.)

Hands back the count of collected objects plus those unreachable objects that cannot be collected. When the garbage collector is off or already in the middle of a collection, it returns `0` at once. Any errors arising during garbage collection are routed to [`sys.unraisablehook`](https://docs.python.org/3.14/library/sys.html#sys.unraisablehook). This function throws no exceptions.

 int PyGC_Enable(void)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

Switch the garbage collector on, in the manner of [`gc.enable()`](https://docs.python.org/3.14/library/gc.html#gc.enable). Hands back the prior state — 0 meaning disabled, 1 meaning enabled.

Added in version 3.10.

 int PyGC_Disable(void)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

Switch the garbage collector off, in the manner of [`gc.disable()`](https://docs.python.org/3.14/library/gc.html#gc.disable). Reports the prior state as 0 when disabled and 1 when enabled.

Added in version 3.10.

 int PyGC_IsEnabled(void)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

Check where the garbage collector stands, in the manner of [`gc.isenabled()`](https://docs.python.org/3.14/library/gc.html#gc.isenabled). Reports the present state as 0 when disabled and 1 when enabled.

Added in version 3.10.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-tpflags-have-gc-to-pyobject-gc-newvar.md) · [Previous source contract](pyobject-gc-new-to-py-visit.md) · [Following source contract](pyunstable-gc-visitobjects.md)
