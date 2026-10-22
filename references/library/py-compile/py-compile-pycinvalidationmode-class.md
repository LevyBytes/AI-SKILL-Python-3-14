# py_compile: `py_compile.PycInvalidationMode`

*class *py_compile.PycInvalidationMode

An enumeration of the possible methods the interpreter can apply to decide whether a bytecode file is current with a source file. The `.pyc` file records the wanted invalidation mode within its header. See [Cached bytecode invalidation](https://docs.python.org/3.14/reference/import.html#pyc-invalidation) for more on how Python invalidates `.pyc` files at runtime.

Added in version 3.7.

 TIMESTAMP

The `.pyc` file carries the timestamp and size of the source file, which Python checks against the source file's metadata at runtime to decide whether the `.pyc` file needs regenerating.

 CHECKED_HASH

The `.pyc` file carries a hash of the source file content, which Python checks against the source at runtime to decide whether the `.pyc` file needs regenerating.

 UNCHECKED_HASH

As with `CHECKED_HASH`, the `.pyc` file carries a hash of the source file content. Python, though, will at runtime presume the `.pyc` file is current and skip validating the `.pyc` against the source file altogether.

This option pays off when the `.pycs` are held current by some system outside Python, such as a build system.

[Subject index](INDEX.md) · [Previous](py-compile-pycompileerror-to-py-compile-compile.md) · [Continue](command-line-interface.md) · [Owning module, declaration or section: py_compile](py-compile-pycompileerror-to-py-compile-compile.md)
