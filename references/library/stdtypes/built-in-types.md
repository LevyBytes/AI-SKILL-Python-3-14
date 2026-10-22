# Built-in Types

### Built-in Types

What follows documents the standard types that ship inside the interpreter.

The chief built-in types fall into these groups: numerics, sequences, mappings, classes, instances and exceptions.

A number of collection classes can be mutated. Their methods that insert, remove, or reorder members in place, returning no specific element, hand back `None` rather than the collection object itself.

Many object types share certain operations; nearly every object, for instance, can be checked for equality, evaluated for truth value, and turned into a string (either via the [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) function or the marginally distinct `str()` function). That second function gets called implicitly whenever an object is printed through the [`print()`](https://docs.python.org/3.14/library/functions.html#print) function.

[Subject index](INDEX.md) · [Continue](truth-value-testing.md)
