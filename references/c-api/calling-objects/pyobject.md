# The Vectorcall Protocol

### The Vectorcall Protocol

Added in version 3.9.

[**PEP 590**](https://peps.python.org/pep-0590/) brought in the vectorcall protocol as a supplementary mechanism that lets calls run more efficiently.

A general guideline is that CPython favors vectorcall for its internal calls when the callable can handle it, though this is not guaranteed. On top of that, certain third-party extensions invoke *tp_call* straight away rather than going through `PyObject_Call()`. For that reason, any class offering vectorcall is also obliged to provide [`tp_call`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_call). What is more, the callable has to act identically no matter which protocol gets exercised. To accomplish that, the suggested approach is to point `tp_call` at `PyVectorcall_Call()`. It is worth stating again:

Warning

Whenever a class provides vectorcall it is **required** to supply [`tp_call`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_call) too, carrying matching semantics.

Changed in version 3.12: Reassigning a class's [`__call__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__call__) method now strips the [`Py_TPFLAGS_HAVE_VECTORCALL`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_VECTORCALL) flag away from that class. (Under the hood this only assigns [`tp_call`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_call), so the result can diverge from the vectorcall function.) On older Python releases, vectorcall ought to be reserved for [`immutable`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE) types or static ones.

There is no reason for a class to adopt vectorcall when doing so would lag behind *tp_call*. As an illustration, when the callee has to build an args tuple and a kwargs dict regardless, implementing vectorcall buys nothing.

A class wires up the vectorcall protocol by turning on the [`Py_TPFLAGS_HAVE_VECTORCALL`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_VECTORCALL) flag and pointing [`tp_vectorcall_offset`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_vectorcall_offset) at the spot within the object layout where a *vectorcallfunc* lives. That value is a pointer to a function whose signature reads:

 typedef [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *(*vectorcallfunc)([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *callable, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *const *args, size_t nargsf, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *kwnames)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.12.*

- *callable* names the object that is being invoked.

- *args* refers to a C array holding the positional arguments and then the

keyword argument values after them. When no arguments exist this may be *NULL*.

- *nargsf* counts the positional arguments, optionally combined with the

`PY_VECTORCALL_ARGUMENTS_OFFSET` flag. Recover the true positional-argument count out of *nargsf* by calling `PyVectorcall_NARGS()`.

- *kwnames* is a tuple holding the keyword-argument names;

put differently, the kwargs dict's keys. Every such name has to be a string (a `str` instance or subclass thereof) and each must be distinct. When no keyword arguments are supplied, *kwnames* may instead be *NULL*.

 PY_VECTORCALL_ARGUMENTS_OFFSET

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.12.*

When a vectorcall *nargsf* argument carries this flag, the callee gains permission to alter `args[-1]` for a moment. Put another way, within the allocated vector *args* refers to argument 1 instead of 0. Before it returns, the callee is obliged to put `args[-1]` back the way it was.

In the case of `PyObject_VectorcallMethod()`, the same flag signals instead that `args[0]` is open to modification.

Callers who can manage it cheaply — with no extra allocation — are urged to apply `PY_VECTORCALL_ARGUMENTS_OFFSET`. That lets callables like bound methods forward their calls (which tack on a leading *self* argument) with great efficiency.

Added in version 3.8.

When invoking an object that supports vectorcall, reach for a call API function exactly as you would for any callable. `PyObject_Vectorcall()` tends to be the most efficient choice.

[Subject index](INDEX.md) · [Previous source contract](the-tp-call-protocol.md) · [Following source contract](recursion-control.md)
