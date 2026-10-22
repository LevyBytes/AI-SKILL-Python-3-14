# 9.1. A Word About Names and Objects

### 9.1. A Word About Names and Objects

Each object has its own identity, and several names — possibly across several scopes — may be bound to one and the same object. Other languages call this aliasing. Newcomers to Python tend not to notice it at first, and it can be set aside without harm while working with immutable basic types (numbers, strings, tuples). For mutable objects, though — lists, dictionaries, and most other types — aliasing can shape the semantics of Python code in ways that may catch you off guard. Programs typically take advantage of this, because in certain ways aliases act like pointers. Passing an object, for instance, costs little since the implementation only hands over a pointer; and should a function alter an object it received as an argument, that change is visible to the caller — so Python avoids needing two separate argument-passing schemes the way Pascal does.

[Subject index](INDEX.md) · [Previous source section](classes.md) · [Following source section](python-scopes-and-namespaces.md)
