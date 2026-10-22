# object protocol C API: `PyUnstable_Object_IsUniqueReferencedTemporary()`, `PyUnstable_IsImmortal()`

int PyUnstable_Object_IsUniqueReferencedTemporary([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

 *This is [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api). It may change without warning in minor releases.*

Test whether *obj* is a unique temporary object. It hands back `1` when *obj* is known to be a unique temporary object, and `0` if not. The call cannot fail, yet the test is conservative and may return `0` in certain situations even where *obj* really is a unique temporary object.

When an object qualifies as a unique temporary, the current code is guaranteed to hold the sole reference to it. For arguments passed to C functions, rely on this in place of testing whether the reference count equals `1`. As of Python 3.14, the interpreter internally skips some reference count modifications while loading objects onto the operands stack, [borrowing](https://docs.python.org/3.14/glossary.html#term-borrowed-reference) references where it can; consequently a reference count of `1` on its own does not establish that a function argument is uniquely referenced.

In the following example, `my_func` receives a unique temporary object as its argument:

```c
my_func([1, 2, 3])

```

In the following example, `my_func` is **not** handed a unique temporary object as its argument, even when its refcount is `1`:

```c
my_list = [1, 2, 3]
my_func(my_list)

```

Consult as well the function [`Py_REFCNT()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_REFCNT).

Added in version 3.14.

 int PyUnstable_IsImmortal([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

 *This is [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api). It may change without warning in minor releases.*

The call hands back a non-zero result when *obj* is [immortal](https://docs.python.org/3.14/glossary.html#term-immortal), and zero if not. This function cannot fail.

Note

An object that is immortal under one CPython version carries no guarantee of being immortal under another.

Added in version 3.14.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-getconstant-to-pyobject-hasattrstringwitherror.md) · [Previous source contract](pyobject-getaiter-to-pyunstable-object-enabledeferredrefcount.md) · [Following source contract](pyunstable-tryincref-to-pyunstable-enabletryincref.md)
