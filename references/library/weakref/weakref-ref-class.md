# weakref: `weakref.ref`

# Weakref

### `weakref` - Weak references

**Source code:** [Lib/weakref.py](https://github.com/python/cpython/tree/3.14/Lib/weakref.py)

---

The `weakref` module lets a Python programmer set up *weak references* pointing at objects.

Throughout what follows, the term *referent* denotes the object that a weak reference points to.

Holding only a weak reference to an object will not keep that object alive: once the sole references left to a referent are weak ones, [garbage collection](https://docs.python.org/3.14/glossary.html#term-garbage-collection) is at liberty to tear the referent down and repurpose its memory. That said, right up until the object is genuinely torn down the weak reference can still yield it, even with no strong references in play.

Weak references are chiefly handy for building caches or mappings that hold large objects, in cases where you would rather a large object not stay alive merely on account of sitting in a cache or mapping.

Picture, for instance, having several large binary image objects that you want to label by name. Were you to use a plain Python dictionary mapping names onto images, or images onto names, those image objects would linger alive simply because they served as values or keys in the dictionaries. The `WeakKeyDictionary` and `WeakValueDictionary` classes that the `weakref` module offers are the alternative: they lean on weak references to assemble mappings that do not keep objects alive just for being present in the mapping objects. Suppose an image object sits as a value inside a `WeakValueDictionary`; once the only references left to that image object are the weak ones held by weak mappings, garbage collection is free to reclaim it, and the matching entries in those weak mappings are quietly dropped.

Internally, `WeakKeyDictionary` and `WeakValueDictionary` are built on weak references, attaching callback functions to those weak references that alert the weak dictionaries the moment a key or value gets reclaimed by garbage collection. `WeakSet` fulfills the [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) interface while holding its elements through weak references, much as a `WeakKeyDictionary` does.

`finalize` gives you an uncomplicated way to enroll a cleanup function that fires once an object is garbage collected. It is easier to work with than wiring a callback onto a bare weak reference, because the module sees to it on its own that the finalizer stays alive until the object is collected.

For most programs, reaching for one of these weak container types or for `finalize` is all that is called for – you rarely have to fashion your own weak references by hand. The `weakref` module surfaces the low-level machinery only for the sake of more advanced use.

Weak references cannot be made to every object. Among those that do accept weak references are class instances, functions authored in Python (though not in C), instance methods, sets, frozensets, certain [file objects](https://docs.python.org/3.14/glossary.html#term-file-object), [generators](https://docs.python.org/3.14/glossary.html#term-generator), type objects, sockets, arrays, deques, regular expression pattern objects, and code objects.

Changed in version 3.2: Gained support for thread.lock, threading.Lock, and code objects.

A number of built-in types, [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) and [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) among them, lack direct weak-reference support, yet they can pick it up via subclassing:

```python
class Dict(dict):
    pass

obj = Dict(red=1, green=2, blue=3)   # this object is weak referenceable

```

**CPython implementation detail:** Certain other built-in types, [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) and [`int`](https://docs.python.org/3.14/library/functions.html#int) for example, refuse weak references even after being subclassed.

Extension types are readily fitted with weak-reference support; refer to [Weak Reference Support](https://docs.python.org/3.14/extending/newtypes.html#weakref-support).

Once `__slots__` is declared on a given type, weak-reference support switches off unless a `'__weakref__'` string also appears among the strings in that `__slots__` declaration. Consult the [__slots__ documentation](https://docs.python.org/3.14/reference/datamodel.html#slots) for the particulars.

 *class *weakref.ref(*object*[, *callback*])

Hand back a weak reference aimed at *object*. So long as the referent is still alive, you recover the original object by calling the reference object; once the referent is gone, calling the reference object yields [`None`](https://docs.python.org/3.14/library/constants.html#None) instead. Where *callback* is supplied and is not `None`, and the weakref object that came back is still alive, that callback fires just as the object is about to be finalized; the weak reference object alone is passed to the callback, and the referent will already be unavailable.

You may build many weak references against one and the same object. The callbacks enrolled for those weak references fire in order from the most recently enrolled callback back to the oldest enrolled one.

Any exception a callback throws is recorded on the standard error output but cannot be propagated; it is treated in precisely the manner of an exception thrown from an object's [`__del__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__del__) method.

Weak references count as [hashable](https://docs.python.org/3.14/glossary.html#term-hashable) whenever the *object* is hashable, and they hold on to their hash value even once the *object* has been deleted. Where [`hash()`](https://docs.python.org/3.14/library/functions.html#hash) is first invoked only after the *object* is gone, the call throws [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

Weak references permit equality checks though not ordering ones. While the referents remain alive, two references stand in the same equality relationship that their referents do (the *callback* notwithstanding). If either referent has been deleted, the references are equal solely when the reference objects are one and the same object.

This is a type you can subclass, not a factory function.

Weak references are [generic](https://docs.python.org/3.14/library/typing.html#generics) with respect to the type of object they point at.

[Subject index](INDEX.md) · [Continue](weakref-weak-references.md)
