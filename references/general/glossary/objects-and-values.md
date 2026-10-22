# Objects and values

Open when checking Python definitions for objects and values.

## object

Any data carrying state (attributes or value) together with defined behavior (methods). It is likewise the ultimate base class of every new-style class.

## type

An object's type fixes what sort of object it is; every object carries a type. You can reach an object's type through its [`__class__`](https://docs.python.org/3.14/reference/datamodel.html#object.__class__) attribute, or pull it back with `type(obj)`.

## attribute

A value tied to an object and ordinarily reached by name through dotted expressions. For instance, should an object *o* carry an attribute *a*, you would refer to it as *o.a*.

An object can be given an attribute whose name does not qualify as an identifier per [Names (identifiers and keywords)](https://docs.python.org/3.14/reference/lexical_analysis.html#identifiers), say by means of [`setattr()`](https://docs.python.org/3.14/library/functions.html#setattr), provided the object permits it. An attribute like this cannot be reached through a dotted expression and would instead have to be fetched using [`getattr()`](https://docs.python.org/3.14/library/functions.html#getattr).

## mutable

An object whose state may shift while the program runs. Inside multi-threaded programs, mutable objects shared across threads call for careful synchronization so race conditions are avoided. See also immutable, thread-safe, and concurrent modification.

## immutable

An object whose value is fixed. Numbers, strings, and tuples are among the immutable objects. Such an object admits no alteration. Storing a different value means a fresh object must be made. They matter greatly wherever a constant hash value is required, such as a dictionary key. Because their state cannot be changed after creation, immutable objects are inherently thread-safe, removing any worry about poorly synchronized concurrent modification.

## hashable

An object counts as *hashable* when it carries a hash value that stays constant throughout its lifetime (this calls for a [`__hash__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__hash__) method) and can be measured against other objects (this calls for an [`__eq__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__eq__) method). Any hashable objects comparing equal are obliged to share the same hash value.

Being hashable lets an object act as a dictionary key or a set member, since the hash value is what those data structures use under the hood.

The bulk of Python's immutable built-in objects are hashable; mutable containers like lists or dictionaries are not; immutable containers like tuples and frozensets stay hashable only when their elements are. Objects that instantiate user-defined classes are hashable by default. Every such object compares unequal (save against itself), and its hash value follows from its [`id()`](https://docs.python.org/3.14/library/functions.html#id).

## complex number

A generalization of the well-known real number system, in which every number is given as the sum of a real component and an imaginary component. An imaginary number is a real-valued multiple of the imaginary unit (that is, the square root of `-1`), which mathematics commonly denotes `i` and engineering denotes `j`. Python supports complex numbers natively, expressing them with that second notation; you write the imaginary component with a `j` suffix, for example `3+1j`. For complex counterparts of the [`math`](https://docs.python.org/3.14/library/math.html#module-math) module, reach for [`cmath`](https://docs.python.org/3.14/library/cmath.html#module-cmath). Working with complex numbers is a rather advanced mathematical capability. If no need for them comes to mind, you can almost surely leave them aside without trouble.

## contiguous

A buffer counts as contiguous precisely when it is either *C-contiguous* or *Fortran contiguous*. Buffers of zero dimensions are both C and Fortran contiguous. Within one-dimensional arrays, the items have to sit adjacent to one another in memory, ordered by rising indexes beginning at zero. Within multidimensional C-contiguous arrays, the final index changes most rapidly as items are traversed by memory address. By contrast, within Fortran contiguous arrays it is the first index that changes most rapidly.

## bytes-like object

An object that backs the [Buffer Protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects) and is able to export a C-contiguous buffer. Every [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray), and [`array.array`](https://docs.python.org/3.14/library/array.html#array.array) object falls under this, along with a great many ordinary [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) objects. You can apply bytes-like objects across a variety of operations dealing with binary data; among these are compression, writing to a binary file, and transmitting over a socket.

Certain operations call for the binary data to be mutable. Such objects are frequently described in the documentation as "read-write bytes-like objects". A [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) and a [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) of a `bytearray` serve as examples of mutable buffer objects. Still other operations expect the binary data to live in immutable objects ("read-only bytes-like objects"); [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and a `memoryview` of a `bytes` object are examples of these.

[Glossary context index](INDEX.md).
