# Cyclic Isolate Destruction

### Cyclic Isolate Destruction

The lines below set out the life stages of a hypothetical [cyclic isolate](https://docs.python.org/3.14/glossary.html#term-cyclic-isolate) that lingers on past the finalization or clearing of each of its member objects. A cyclic isolate that travels through every one of these stages constitutes a memory leak; it ought to disappear once every object is cleared, if not before that. A cyclic isolate can disappear either because its reference cycle gets severed or because finalizer resurrection ends the objects' isolation (refer to [`tp_finalize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_finalize)).

1.

**Reachable** (not yet a cyclic isolate): Every object sits in its ordinary, reachable condition. A reference cycle might be present, yet an external reference keeps the objects from being isolated so far.

2.

**Unreachable but consistent:** The last reference reaching in from outside the cyclic cluster of objects is gone, which isolates the objects (and so a cyclic isolate comes into being). Not one of the cluster's objects has been finalized or cleared as yet. The cyclic isolate stays in this condition until some later run of the garbage collector (not inevitably the upcoming run, since that run may skip scanning every object).

3.

**Mix of finalized and not finalized:** The objects within a cyclic isolate get finalized one by one, so there is a stretch during which the cyclic isolate holds a blend of finalized and non-finalized objects. The order of finalization is unspecified and may therefore look arbitrary. A finalized object has to act sensibly while non-finalized objects engage with it, and a non-finalized object has to cope with the finalization of any arbitrary subset of the things it references.

4.

**All finalized:** Each object within a cyclic isolate is finalized prior to any of them being cleared.

5.

**Mix of finalized and cleared:** The objects may be cleared one after another or in parallel (though with the [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) held); in either case, certain ones will complete ahead of others. A finalized object has to cope with the clearing of a subset of the things it references. [**PEP 442**](https://peps.python.org/pep-0442/) names this stage "cyclic trash".

6.

**Leaked:** Should a cyclic isolate persist once every object in the group has been both finalized and cleared, the objects stay uncollectable forever (refer to [`gc.garbage`](https://docs.python.org/3.14/library/gc.html#gc.garbage)). A cyclic isolate arriving at this stage is a bug—it signals that the participating objects' [`tp_clear`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_clear) methods have not severed the reference cycle as they were obliged to.

Were [`tp_clear`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_clear) absent, Python would possess no safe means of severing a reference cycle. Merely tearing down an object inside a cyclic isolate would leave a dangling pointer behind, which provokes undefined behavior once an object that references the destroyed object is itself torn down. The clearing step turns object destruction into a two-phase affair: `tp_clear` runs first to partly tear down the objects just enough to untangle them from one another, and then [`tp_dealloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_dealloc) runs to finish the destruction.

In contrast to clearing, finalization is not one of the phases of destruction. A finalized object is still obliged to act correctly by continuing to honor the contracts it was designed for. An object's finalizer may run any Python code at all, and it is even permitted to forestall the looming destruction by attaching a reference. Call order is the finalizer's only tie to destruction—when it runs, it does so ahead of destruction, which opens with [`tp_clear`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_clear) (where called) and ends with [`tp_dealloc`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_dealloc).

Finalization is not required in order to safely reclaim the objects within a cyclic isolate, yet its presence simplifies designing types that act sensibly when objects get cleared. Clearing an object may unavoidably leave it in a damaged, partly torn-down condition—invoking any of the cleared object's methods or reading any of its attributes might be unsafe. Thanks to finalization, the only objects that can ever engage with cleared objects are finalized ones; non-finalized objects are assured of engaging solely with non-cleared (though potentially finalized) objects.

To recap the possible interactions:

- A non-finalized object may hold references to or receive references from non-finalized and finalized objects, but never to or from cleared objects.

- A finalized object may hold references to or receive references from non-finalized, finalized, and cleared objects.

- A cleared object may hold references to or receive references from finalized and cleared objects, but never to or from non-finalized objects.

In the absence of any reference cycles, an object can simply be torn down the moment its last reference is gone; the finalization and clearing steps are not needed to safely reclaim objects no longer in use. Even so, automatically invoking [`tp_finalize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_finalize) and [`tp_clear`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_clear) ahead of destruction regardless can prove handy, because designing a type becomes simpler when every object consistently goes through the identical chain of events whether or not it was part of a cyclic isolate. For now Python invokes `tp_finalize` and `tp_clear` solely as required to destroy a cyclic isolate; a later release may alter this.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](object-life-cycle.md) · [Previous source contract](life-events.md) · [Following source contract](pyobject-callfinalizer-to-pyobject-callfinalizerfromdealloc.md)
