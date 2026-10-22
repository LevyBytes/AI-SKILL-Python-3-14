# 3.2.13.1. Code objects

#### 3.2.13.1. Code objects

A code object stands for *byte-compiled* runnable Python code, that is, [bytecode](https://docs.python.org/3.14/glossary.html#term-bytecode). Where a function object diverges from a code object is that the function object holds an explicit reference to the function’s globals (the module where it was defined), whereas a code object carries no such context; furthermore the default values for arguments live in the function object rather than the code object (since they stand for values computed at run-time). In contrast with function objects, code objects cannot be changed and hold no references — whether direct or indirect — to mutable objects.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](internal-types.md) · [Previous source section](internal-types.md) · [Following source section](special-read-only-attributes.md)
