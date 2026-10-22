# Special Attributes

### Special Attributes

To a number of object types the implementation attaches a few special read-only attributes wherever they make sense. A portion of these go unreported by the [`dir()`](https://docs.python.org/3.14/library/functions.html#dir) built-in function.

 definition.__name__

The class, function, method, descriptor, or generator instance’s name.

 definition.__qualname__

The [qualified name](https://docs.python.org/3.14/glossary.html#term-qualified-name) belonging to the class, function, method, descriptor, or generator instance.

Added in version 3.3.

 definition.__module__

The name of the module where a class or function got defined.

 definition.__doc__

A class or function’s documentation string, or `None` when none exists.

 definition.__type_params__

The [type parameters](https://docs.python.org/3.14/reference/compound_stmts.html#type-params) belonging to generic classes, functions, and [type aliases](https://docs.python.org/3.14/library/typing.html#type-aliases). When a class or function is not generic, this will be an empty tuple.

Added in version 3.12.

[Subject index](INDEX.md) · [Previous](internal-objects.md) · [Continue](integer-string-conversion-length-limitation.md)
