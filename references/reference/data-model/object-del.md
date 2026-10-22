# object.__del__(*self*)

object.__del__(*self*)

Invoked when the instance is on the verge of being destroyed. This goes by finalizer or (incorrectly) destructor as well. Where a base class supplies a `__del__()` method, the derived class’s `__del__()` method, if any, has to call it explicitly so the base class portion of the instance is deleted properly.

You can (though it is discouraged!) have the `__del__()` method delay the instance’s destruction by forging a new reference to it. This goes by object *resurrection*. Whether `__del__()` is invoked a second time once a resurrected object is again about to be destroyed depends on the implementation; the present [CPython](https://docs.python.org/3.14/glossary.html#term-CPython) implementation invokes it only once.

There is no assurance that `__del__()` methods get invoked for objects still in existence when the interpreter shuts down. [`weakref.finalize`](https://docs.python.org/3.14/library/weakref.html#weakref.finalize) gives a simple means of registering a cleanup function that fires when an object is garbage collected.

Note

`del x` does not invoke `x.__del__()` straight away — instead the former drops the reference count for `x` by one, while the latter fires solely once the reference count of `x` hits zero.

**CPython implementation detail:** A reference cycle can keep an object’s reference count from dropping to zero. When that happens, the [cyclic garbage collector](https://docs.python.org/3.14/glossary.html#term-garbage-collection) detects and removes the cycle at a later point. Reference cycles frequently arise when an exception is caught inside a local variable. The frame’s locals then point at the exception, which points at its own traceback, which in turn points at the locals of every frame captured within the traceback.

See also

Documentation for the [`gc`](https://docs.python.org/3.14/library/gc.html#module-gc) module.

Warning

Given the delicate conditions in which `__del__()` methods get invoked, any exceptions arising while they run are disregarded, and a warning is emitted to `sys.stderr` in their place. Specifically:

- `__del__()` may run while arbitrary code executes, which includes any arbitrary thread. Should `__del__()` have to acquire a lock or reach for some other blocking resource, a deadlock can result, since whatever code was interrupted in order to run `__del__()` might already hold that resource.

- `__del__()` may run as the interpreter shuts down. Because of that, the global variables it relies on (other modules among them) might already be gone or reset to `None`. Python promises that any globals named with a leading single underscore get cleared from their module ahead of the rest; provided nothing else still references such globals, this can help ensure that imported modules remain reachable by the time the `__del__()` method runs.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](object-new.md) · [Following source contract continuation](object-repr.md) · [Previous source section](object-init.md) · [Following source section](object-repr.md)
