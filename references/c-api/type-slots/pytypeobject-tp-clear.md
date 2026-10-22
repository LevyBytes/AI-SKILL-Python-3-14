# inquiry PyTypeObject.tp_clear

[inquiry](https://docs.python.org/3.14/c-api/gcsupport.html#c.inquiry) [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject).tp_clear

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_tp_clear` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

An optional pointer to a clear routine. Its signature is:

```c
int tp_clear(PyObject *);

```

This routine exists to sever the reference cycles that form a [cyclic isolate](https://docs.python.org/3.14/glossary.html#term-cyclic-isolate), allowing the objects to be torn down safely. After clearing, an object is only partly destroyed; it is no longer required to uphold the design invariants it maintains during ordinary operation.

`tp_clear` need not discard references to objects that cannot take part in reference cycles, such as Python strings or Python integers. Even so, clearing every reference can be handy, letting you write the type’s `tp_dealloc` function so it calls `tp_clear` and avoids repeating code. (Bear in mind that `tp_clear` may already have run. Favor idempotent calls such as [`Py_CLEAR()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_CLEAR).)

Place any substantial cleanup in `tp_finalize` rather than in `tp_clear`.

Note

Should `tp_clear` not manage to break a reference cycle, the objects making up the [cyclic isolate](https://docs.python.org/3.14/glossary.html#term-cyclic-isolate) can stay uncollectable forever (“leak”). Refer to [`gc.garbage`](https://docs.python.org/3.14/library/gc.html#gc.garbage).

Note

Referents (whether direct or indirect) may already have been cleared; there is no guarantee that they sit in a consistent state.

Note

Any thread may call the `tp_clear` function.

Note

There is no guarantee that an object gets cleared automatically before its destructor (`tp_dealloc`) runs.

The ways this function diverges from the destructor (`tp_dealloc`) are these:

- Clearing an object aims to drop references to other objects that could form part of a reference cycle. The destructor’s aim, by contrast, is broader: it has to free *all* resources the object holds, which covers references to objects that cannot be part of a reference cycle (integers, say) as well as the object’s own storage (by invoking `tp_free`).

- At the moment `tp_clear` runs, other objects may yet hold references to the one being cleared. For that reason, `tp_clear` must not free the object’s own storage (`tp_free`). The destructor, in contrast, runs only when no (strong) references remain, and so is responsible for safely tearing down the object itself by freeing it.

- It is possible that `tp_clear` is never invoked automatically. The destructor of an object, however, will be invoked automatically at some point once the object becomes unreachable (that is, either no references to the object remain or the object belongs to a [cyclic isolate](https://docs.python.org/3.14/glossary.html#term-cyclic-isolate)).

No promises are offered regarding when, whether, or how frequently Python clears an object on its own, apart from these:

- Python will not clear an object on its own while it stays reachable, that is, while a reference to it exists and it does not belong to a [cyclic isolate](https://docs.python.org/3.14/glossary.html#term-cyclic-isolate).

- Python will not clear an object on its own unless it has already been finalized automatically (see `tp_finalize`). (Should the finalizer revive the object, it may or may not undergo automatic finalization once more before being cleared.)

- When an object belongs to a [cyclic isolate](https://docs.python.org/3.14/glossary.html#term-cyclic-isolate), Python will refrain from clearing it automatically as long as any member of that cyclic isolate has yet to be finalized automatically (`tp_finalize`).

- Python holds off on destroying an object until every automatic call to its `tp_clear` function has finished. This guarantees that severing a reference cycle does not leave the `self` pointer invalid while `tp_clear` is still running.

- Python will never invoke `tp_clear` automatically more than once at the same time.

For now, CPython clears objects automatically only when it must, to break reference cycles within a [cyclic isolate](https://docs.python.org/3.14/glossary.html#term-cyclic-isolate), though later versions may clear objects routinely ahead of their destruction.

Considered as a whole, every `tp_clear` function across the system has to cooperate to break all reference cycles. This is a subtle matter, so when there is any doubt, provide a `tp_clear` function. As an illustration, the tuple type ships no `tp_clear` function, since one can demonstrate that no reference cycle can be built solely out of tuples. As a result, the `tp_clear` functions belonging to other types must break any cycle that involves a tuple. That fact isn’t obvious at first glance, and there is seldom a sound reason to skip implementing `tp_clear`.

A `tp_clear` implementation should release the instance’s references to whichever of its members may be Python objects, and reset the pointers to those members to `NULL`, following this example:

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pytypeobject-tp-name-to-pytypeobject-tp-itemsize.md) · [Previous source contract](pytypeobject-tp-traverse.md) · [Following source contract](pytypeobject-tp-richcompare-to-py-return-richcompare.md)
