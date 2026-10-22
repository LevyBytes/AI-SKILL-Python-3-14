# Per-thread reference counting can delay freeing objects

#### Per-thread reference counting can delay freeing objects

The free-threaded build adds “per-thread reference counting” for a handful of chosen object types as well, in order to dodge contention on the reference-count fields of objects that are shared a lot. Instead of touching one shared reference count, each thread keeps a private local array of counts, keyed by a unique id given to the object. The actual reference count gets worked out only by adding up the per-thread totals once an object's local count falls to zero. At the moment, per-thread reference counting applies to:

- heap type objects (that is, classes created in Python)

- code objects

- the `__dict__` of module objects

Since the per-thread counts have to be folded back into the object before it can be deallocated, objects relying on per-thread reference counting usually get freed later than they would under the standard build. Concretely, such an object generally stays alive until the thread that held a reference reaches a safe point — for instance, the “eval breaker” portion of the bytecode evaluator — or finishes. A call to [`gc.collect()`](https://docs.python.org/3.14/library/gc.html#gc.collect) folds the per-thread counts together and lets these objects be released.

[Subject index](INDEX.md) · [Previous source context](free-threaded-reference-counting-and-lifetimes.md)
