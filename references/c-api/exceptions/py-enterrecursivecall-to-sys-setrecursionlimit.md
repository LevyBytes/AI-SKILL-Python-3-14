# Recursion Control

### Recursion Control

This pair of functions lets you make recursive calls safely at the C level, whether inside the interpreter core or within extension modules. You need them whenever the recursive code path might not run any Python code — Python code keeps track of its own recursion depth on its own. There is no need for them in *tp_call* implementations either, since the [call protocol](https://docs.python.org/3.14/c-api/call.html#call) already manages recursion on your behalf.

 int Py_EnterRecursiveCall(const char *where)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.9.*

Flags the spot at which a recursive call at the C level is about to happen.

Next, the function tests whether the stack limit has been hit. Should that be so, it sets a [`RecursionError`](https://docs.python.org/3.14/library/exceptions.html#RecursionError) and hands back a nonzero result; if not, it gives back zero.

Pass *where* as a UTF-8 encoded string — for instance `" in instance check"` — which gets appended to the [`RecursionError`](https://docs.python.org/3.14/library/exceptions.html#RecursionError) text produced once the recursion depth limit is exceeded.

See also

The [`PyUnstable_ThreadState_SetStackProtection()`](https://docs.python.org/3.14/c-api/threads.html#c.PyUnstable_ThreadState_SetStackProtection) function.

Changed in version 3.9: Starting with this release, the [limited API](https://docs.python.org/3.14/c-api/stable.html#limited-c-api) exposes this function as well.

 void Py_LeaveRecursiveCall(void)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.9.*

Closes out a `Py_EnterRecursiveCall()`. You must invoke it exactly one time for every *successful* `Py_EnterRecursiveCall()` call.

Changed in version 3.9: Starting with this release, the [limited API](https://docs.python.org/3.14/c-api/stable.html#limited-c-api) exposes this function as well.

Writing a correct [`tp_repr`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_repr) for container types calls for extra care around recursion. Beyond guarding the stack, `tp_repr` must also keep tabs on the objects it visits so that cycles are caught. The two functions below exist to make that possible — in essence they are the C-side counterpart of [`reprlib.recursive_repr()`](https://docs.python.org/3.14/library/reprlib.html#reprlib.recursive_repr).

 int Py_ReprEnter([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *object)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Called at the beginning of the [`tp_repr`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_repr) implementation to detect cycles.

When the object was seen before, a positive integer comes back. Your [`tp_repr`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_repr) code should then hand back a string object that signals a cycle — for example, [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) objects render as `{...}` while [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) objects render as `[...]`.

A negative integer comes back once the recursion limit has been hit, and at that point the [`tp_repr`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_repr) code will normally hand back `NULL`.

Otherwise, the function returns zero and the [`tp_repr`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_repr) implementation can continue normally.

 void Py_ReprLeave([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *object)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Closes out a `Py_ReprEnter()`. You must invoke it exactly one time for every `Py_ReprEnter()` call that came back with zero.

 int Py_GetRecursionLimit(void)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Retrieve the recursion limit in effect for the active interpreter. You can change it through `Py_SetRecursionLimit()`. That limit exists to stop the Python interpreter stack from expanding without bound.

This function cannot fail, and the caller must hold an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state).

See also

[`sys.getrecursionlimit()`](https://docs.python.org/3.14/library/sys.html#sys.getrecursionlimit)

 void Py_SetRecursionLimit(int new_limit)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Set the recursion limit for the current interpreter.

This function cannot fail, and the caller must hold an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state).

See also

[`sys.setrecursionlimit()`](https://docs.python.org/3.14/library/sys.html#sys.setrecursionlimit)

[Subject index](INDEX.md) · [Previous source contract](unicode-exception-reason-accessors.md) · [Following source contract](exception-and-warning-types.md)
