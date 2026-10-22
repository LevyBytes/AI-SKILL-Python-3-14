# Defining Getters and Setters

### Defining Getters and Setters

 type PyGetSetDef

* Belongs to the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable), with every member included.*

A structure that sets up property-style access on a type. The write-up of the [`PyTypeObject.tp_getset`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_getset) slot is worth consulting too.

 const char *name

attribute name

 getter get

C function to get the attribute.

 setter set

An optional C function that writes or removes the attribute. Leaving it `NULL` makes the attribute read-only.

 const char *doc

optional docstring

 void *closure

An optional pointer to user data that supplies extra context to the getter and setter.

 typedef PyObject *(*getter)(PyObject*, void*)

* Belongs to the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A `get` function is handed a single PyObject* argument (the instance) together with a user data pointer (its matching `closure`):

On success it ought to hand back a fresh reference; on failure it returns `NULL` having set an exception.

 typedef int (*setter)(PyObject*, PyObject*, void*)

* Belongs to the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

A `set` function receives a pair of PyObject* arguments (the instance plus the value being assigned) along with a user data pointer (its matching `closure`):

When the attribute is meant to be removed, that second argument arrives as `NULL`. It ought to give back `0` upon success, or `-1` with an exception already set when it fails.

[Subject index](INDEX.md) · [Previous source contract](member-types.md)
