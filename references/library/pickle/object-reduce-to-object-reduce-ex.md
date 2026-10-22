# pickle: `object.__reduce__()`, `object.__reduce_ex__()`

object.__reduce__()

The interface as it stands today is defined as follows. The `__reduce__()` method accepts no argument and must return either a string or, preferably, a tuple (the result is commonly called the "reduce value").

A returned string is read as the name of a global variable. That string ought to be the object's local name within its module; to determine the module, the pickle module walks the module namespace: for an `obj` being pickled, `__module__` is read straight off `obj`, dropping back to reading it off the type of `obj` when no `__module__` instance attribute is present. This behaviour tends to be useful for singletons.

When a tuple is returned, it has to contain between two and six items. Optional items may either be left out, or `None` may be supplied as their value. The meaning of each item, in order, is:

- A callable object that gets invoked to build the object's first version.

- A tuple of arguments meant for that callable object. Supply an empty tuple when the callable takes no argument.

- Optionally, the object's state, which gets passed to the object's `__setstate__()` method as described earlier. When the object lacks such a method, this value must instead be a dictionary, and it gets merged into the object's [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#object.__dict__) attribute.

- Optionally, an iterator (not a sequence) that yields items one after another. Each item gets added to the object either through `obj.append(item)` or, in bulk, through `obj.extend(list_of_items)`. This is chiefly for list subclasses, though other classes may use it provided they expose [`append()`](https://docs.python.org/3.14/library/stdtypes.html#sequence.append) and [`extend()`](https://docs.python.org/3.14/library/stdtypes.html#sequence.extend) methods with the right signature. (Whether `append()` or `extend()` is chosen depends on the pickle protocol version in use as well as on how many items are being appended, so both have to be available.)

- Optionally, an iterator (not a sequence) that yields successive key-value pairs. Each pair gets written into the object via `obj[key] = value`. This is chiefly for dictionary subclasses, though other classes may use it provided they implement [`__setitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__setitem__).

- Optionally, a callable with a `(obj, state)` signature. This callable lets the user steer, in code, how the state of a particular object is updated, in place of using `obj`'s static `__setstate__()` method. When it is not `None`, this callable wins out over `obj`'s `__setstate__()`.

Added in version 3.8: The optional sixth tuple item, `(obj, state)`, was added.

 object.__reduce_ex__(*protocol*)

As an alternative, a `__reduce_ex__()` method may be defined. The lone difference is that this method should take one integer argument, the protocol version. Where it is defined, pickle picks it ahead of the `__reduce__()` method. Furthermore, `__reduce__()` automatically turns into a synonym for the extended form. The principal reason to use this method is to supply reduce values that stay backwards-compatible with older Python releases.

[Subject index](INDEX.md) · [Previous](object-getnewargs-to-object-setstate.md) · [Continue](external-object-persistence-overview.md) · [Owning module, declaration or section: pickle](pickle-python-object-serialization.md) · [Owning module, declaration or section: Pickling Class Instances](object-getnewargs-ex.md)
