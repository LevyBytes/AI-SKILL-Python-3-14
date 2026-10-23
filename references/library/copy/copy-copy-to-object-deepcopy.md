# copy: `copy.copy()`, `copy.deepcopy()`, `copy.replace()`, `copy.Error`, `object.__copy__()`, `object.__deepcopy__()`

## copy - Shallow and deep copy operations

### `copy` - Shallow and deep copy operations

**Source code:** [Lib/copy.py](https://github.com/python/cpython/tree/3.14/Lib/copy.py)

---

In Python an assignment statement does not duplicate objects; it merely binds a target to an object. Where a collection is mutable or carries mutable items, a copy may be called for so that altering one copy leaves the other untouched. Generic shallow and deep copy operations, described further on, are what this module supplies.

Interface summary:

 copy.copy(*obj*)

Hand back a shallow copy of *obj*.

 copy.deepcopy(*obj*[, *memo*])

Hand back a deep copy of *obj*.

 copy.replace(*obj*, */*, ***changes*)

Builds a fresh object matching *obj*'s type, with its fields swapped for the values drawn from *changes*.

Added in version 3.13.

 *exception *copy.Error

Raised for module specific errors.

Only with compound objects — those holding further objects inside them, such as lists or class instances — does the distinction between shallow and deep copying actually matter:

- A *shallow copy* makes a new compound object and, as far as it can, fills it with *references* pointing to the objects that the original held.

- A *deep copy* builds a new compound object and, working recursively, places *copies* of the original's objects inside it.

Deep copying tends to bring two complications that shallow copying never does:

- Recursive objects — compound ones that refer back to themselves whether directly or by some indirect path — can spin into a recursive loop.

- Since a deep copy reproduces all of it, the copy can end up grabbing too much — for instance data that was supposed to stay shared across copies.

The `deepcopy()` function avoids these problems by:

- maintaining a `memo` dictionary that tracks objects already duplicated in the present copying pass; and

- allowing classes written by users to override how copying happens or which components get copied.

Types such as module, method, stack trace, stack frame, file, socket, window, and the like are left uncopied by this module. Functions and classes it does “copy”, both shallowly and deeply, simply by handing back the original object as-is — which matches how the [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) module handles them.

For many collections you can produce a shallow copy through the matching `copy()` method — for example [`list.copy()`](https://docs.python.org/3.14/library/stdtypes.html#list.copy), [`dict.copy()`](https://docs.python.org/3.14/library/stdtypes.html#dict.copy), or [`set.copy()`](https://docs.python.org/3.14/library/stdtypes.html#set.copy) — and for sequences like lists or bytearrays by slicing the whole thing (`sequence[:]`). Bear in mind, though, that these methods and slicing may yield a base-type instance when you copy a subclass instance, while `copy.copy()` ordinarily gives back an instance of the very same type.

The interfaces a class uses to steer pickling are the same ones it can use to steer copying. Consult the write-up of the [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) module for these methods. Indeed, the `copy` module draws on the pickle functions registered through the [`copyreg`](https://docs.python.org/3.14/library/copyreg.html#module-copyreg) module.

A class that wants to supply its own copy implementation can do so by defining the special methods `__copy__()` and `__deepcopy__()`.

 object.__copy__(*self*)

Invoked to carry out the shallow copy; it receives no extra arguments.

 object.__deepcopy__(*self*, *memo*)

Invoked to carry out the deep copy; a single argument, the *memo* dictionary, is handed to it. Whenever the `__deepcopy__` implementation has to deep-copy a component, it ought to call `deepcopy()` passing that component first and the *memo* dictionary second. Regard the *memo* dictionary as an opaque object.

The `copy.replace()` function is narrower in scope than `copy()` and `deepcopy()`: it works only with named tuples built by [`namedtuple()`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple), with [`dataclasses`](https://docs.python.org/3.14/library/dataclasses.html#module-dataclasses), and with any other class that defines the `__replace__()` method.

[Subject index](INDEX.md) · [Continue](object-replace.md)
