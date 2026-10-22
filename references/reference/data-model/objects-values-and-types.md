# 3.1. Objects, values and types

### 3. Data model

### 3.1. Objects, values and types

In Python, *objects* are the way data is abstracted. Everything that counts as data in a Python program is captured either as an object or as some relationship among objects. Code itself, too, is captured as objects.

Each object carries an identity, a type, and a value. The *identity* of an object stays fixed for the entire life of the object after creation; picture it as the spot the object occupies in memory. To compare whether two objects share an identity, use the [`is`](https://docs.python.org/3.14/reference/expressions.html#is) operator; the [`id()`](https://docs.python.org/3.14/library/functions.html#id) function gives back an integer that stands for that identity.

**CPython implementation detail:** Under CPython, what `id(x)` reports is the address in memory at which `x` resides.

The type of an object fixes which operations it can take part in (for instance, “does it have a length?”) and likewise spells out the range of values objects of that type may hold. Use the [`type()`](https://docs.python.org/3.14/library/functions.html#type) function to obtain the type of an object (and that type is itself an object). As with identity, the *type* of an object cannot be altered either. [1]

For certain objects the *value* may be altered. Objects that allow their value to be altered are termed *mutable*; objects whose value is locked in once built are termed *immutable*. (If an immutable container object holds a reference to a mutable object, then the container’s value can shift whenever that referenced object’s value shifts; even so, the container counts as immutable, since the set of objects it holds stays fixed. Hence immutability is not exactly the same thing as possessing a fixed value — the notion is subtler than that.) What governs an object’s mutability is its type; for example, numbers, strings, and tuples are immutable, whereas dictionaries and lists are mutable.

Objects never get explicitly torn down; rather, once nothing can reach them anymore, they become eligible for garbage collection. An implementation has the freedom to defer garbage collection or to skip it entirely — exactly how garbage collection works is a question of implementation quality, provided that nothing still reachable ever gets collected.

**CPython implementation detail:** At present CPython relies on reference counting paired with an (optional) deferred mechanism for spotting garbage linked in cycles; that reclaims the bulk of objects the instant they turn unreachable, though it offers no promise of reclaiming garbage that holds circular references. Consult the [`gc`](https://docs.python.org/3.14/library/gc.html#module-gc) module documentation to learn how the reclamation of cyclic garbage can be steered. Behaviour varies across other implementations, and CPython itself is liable to shift. Never lean on objects being finalized the moment they turn unreachable (which is why you ought to close files explicitly at all times).

Be aware that relying on an implementation’s tracing or debugging machinery can hold onto objects that would otherwise be collectable. Be aware too that trapping an exception with a [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try)…[`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) statement can hold objects alive.

Certain objects keep references to “external” resources, for example open files or windows. The expectation is that these resources get released once the object is garbage-collected, yet because garbage collection carries no guarantee of running, such objects additionally supply an explicit means of freeing the external resource, typically a `close()` method. We strongly advise programs to close such objects explicitly. The [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try)…[`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) statement and the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement offer handy means of doing so.

Certain objects keep references to further objects; we call these *containers*. Tuples, lists, and dictionaries are examples of containers. Those references count as part of the container’s value. Usually, speaking of a container’s value, we mean the values rather than the identities of the objects it contains; yet, speaking of a container’s mutability, only the identities of the objects it directly contains are meant. Thus, when an immutable container (say a tuple) keeps a reference to a mutable object, the container’s value shifts if that mutable object is altered.

Types govern nearly every facet of how an object behaves. Even how much object identity matters is influenced to a degree: with immutable types, operations producing fresh values are permitted to hand back a reference to any existing object sharing the same type and value, but for mutable objects that is forbidden. For instance, following `a = 1; b = 1`, *a* and *b* might or might not point to one and the same object of value one, which depends on the implementation. The reason is that [`int`](https://docs.python.org/3.14/library/functions.html#int) is an immutable type, so the reference to `1` is free to be reused. Since this behaviour hinges on the implementation in use, you should not count on it, but keep it in mind whenever you use object identity tests. By contrast, following `c = []; d = []`, *c* and *d* are guaranteed to point to two distinct, separate, freshly built empty lists. (Note that `e = f = []` binds one *single* object to *e* as well as *f*.)

[Subject index](INDEX.md) · [Following source section](the-standard-type-hierarchy.md)
