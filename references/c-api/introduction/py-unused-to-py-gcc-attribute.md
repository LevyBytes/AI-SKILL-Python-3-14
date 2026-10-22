# General utility macros

### General utility macros

The macros below cover everyday chores that aren't tied to Python specifically.

 Py_UNUSED(arg)

Apply this to arguments left unused inside a function definition so the compiler stops warning. Example: `int func(int a, int Py_UNUSED(b)) { return a; }`.

Added in version 3.4.

 Py_GCC_ATTRIBUTE(name)

Apply a GCC attribute *name* while concealing it from compilers without GCC attribute support (MSVC among them).

Under a GCC compiler this expands to `__attribute__((*name)*)`, while on compilers lacking GCC attribute support it expands to nothing.

[Subject index](INDEX.md) · [Previous source contract](pydoc-strvar-to-pydoc-var.md) · [Following source contract](py-abs-to-py-charmask.md)
