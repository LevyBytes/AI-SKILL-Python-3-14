# Free-threaded reference counting can cause objects to live longer

#### Free-threaded reference counting can cause objects to live longer

Under the standard build, an object is usually deallocated the moment its reference count hits zero. The free-threaded build instead applies “biased reference counting”, which gives a fast path to objects “owned” by the running thread and a slow path to everything else. Further specifics live in [**PEP 703**](https://peps.python.org/pep-0703/). Whenever an object's reference count lands in a “queued” state, its deallocation may be put off. That queued state gets cleared by the “eval breaker” portion of the bytecode evaluator.

On top of that, the free-threaded build offers an alternative reference-counting scheme called “deferred reference counting”. You switch it on by setting a flag per individual object. The types below have deferred reference counting turned on:

- module objects

- top-level functions within a module

- class methods declared in the class scope

- descriptor objects

- thread-local objects produced by [`threading.local`](https://docs.python.org/3.14/library/threading.html#threading.local)

With deferred reference counting active, references coming from Python function stacks don't count toward the reference total. The point of this is to trim the cost of reference counting, particularly for objects shared among several threads. Since stack references go uncounted, an object using deferred reference counting isn't freed right away once its internal count reaches zero. Instead, the following GC run inspects it, and it is released only if no stack references remain. So such objects get cleaned up by the GC rather than at the customary moment when the reference count drops to zero.

[Subject index](INDEX.md) · [Previous source context](mimalloc-allocator-vs-pymalloc.md) · [Following source context](per-thread-reference-counting-can-delay-freeing-objects.md)
