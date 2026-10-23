# Defining Extension Types: Assorted Topics - tp_name, Py_ssize_t, tp_basicsize, tp_itemsize, PyTypeObject, tp_doc

That really is a *lot* of methods. Still, there's no need for alarm – whenever you have a type you'd like to define, it's overwhelmingly likely that only a small subset of these will require an implementation.

By this stage you can probably anticipate the plan: we'll walk through these and explain the assorted handlers in more depth. The sequence we use won't match how they're laid out in the structure, since a great deal of historical baggage shapes the way those fields are ordered. Frequently the simplest route is to locate an existing example that contains the fields you're after, then adjust the values so they fit your new type.

```c
const char *tp_name; /* For printing */

```

This is the type's name – which, as the prior chapter noted, surfaces in a number of spots, overwhelmingly for diagnostic reasons. Pick a value that will prove useful when you find yourself in such a spot!

```c
Py_ssize_t tp_basicsize, tp_itemsize; /* For allocation */

```

These two fields inform the runtime about the amount of memory to set aside whenever fresh objects of this type get created. Built into Python is a degree of support for structures of variable length (consider strings and tuples), and that's exactly the role the [`tp_itemsize`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_itemsize) field plays. We'll return to this point later.

```c
const char *tp_doc;

```

This is where you can stash a string (or a pointer to one) to be handed back whenever a Python script reads `obj.__doc__` in order to obtain the doc string.

We've now reached the fundamental type methods – those that the majority of extension types will provide.

[Subject index](INDEX.md) · [Previous source section](type-layout-inheritance-allocation-and-cache.md) · [Next source section](finalization-and-de-allocation-and-tp-finalize.md) · [Owning section and setup](defining-extension-types-assorted-topics-pytypeobject.md)
