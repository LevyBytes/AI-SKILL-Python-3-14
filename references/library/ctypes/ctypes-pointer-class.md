# ctypes: `ctypes._Pointer`

`*class *ctypes._Pointer`

The private, abstract base class underlying pointers.

You obtain concrete pointer types by handing the target type to `POINTER()`; `pointer()` performs this step for you automatically.

When a pointer targets an array, you can read and write its elements via ordinary subscript and slice access. A pointer object carries no size, so [`len()`](https://docs.python.org/3.14/library/functions.html#len) raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). A negative subscript reads from the memory sitting *before* the pointer (just as in C), while an out-of-range subscript will likely crash with an access violation (should you be fortunate).

`_type_`

States the type that is pointed at.

`contents`

Gives back the object the pointer is aimed at. Writing to this attribute redirects the pointer onto the newly assigned object.

[Subject index](INDEX.md) · [Previous](ctypes-array-class-to-ctypes-array.md) · [Continue](ctypes-argumenterror-to-ctypes-comerror.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md) · [Owning module, declaration or section: Arrays and pointers](ctypes-array-class-to-ctypes-array.md)
