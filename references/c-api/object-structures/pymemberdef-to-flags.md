# Accessing attributes of extension types

### Accessing attributes of extension types

 type PyMemberDef

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) (including all members).*

A structure describing an attribute of a type that maps onto a C struct member. As you define a class, place a NULL-terminated array of these structures into the [`tp_members`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_members) slot.

Listed in order, its fields are:

 const char *name

Name of the member. The end of a `PyMemberDef[]` array is signaled by a NULL value.

Keep the string static; nothing copies it.

 int type

The member's type within the C struct. The allowed values appear under Member types.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) offset

How many bytes into the type's object struct the member sits.

 int flags

Zero or more of the Member flags, OR-ed together bitwise.

[Subject index](INDEX.md) · [Previous source contract](pycfunction-getflags-to-pycfunction-get-self.md) · [Following source contract](doc.md)
