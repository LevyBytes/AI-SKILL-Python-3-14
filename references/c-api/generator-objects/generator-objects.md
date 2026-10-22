# generator objects C API: Generator object creation principles

## Generator Objects

### Generator Objects

Generator iterators are realized by Python through generator objects. Typically you obtain one by iterating over a function that yields values, not by calling `PyGen_New()` or `PyGen_NewWithQualName()` outright.

[Subject index](INDEX.md) · [Previous source contract](../supporting-cyclic-garbage-collection/pyunstable-gc-visitobjects.md) · [Following source contract](pygenobject-to-pygen-getcode.md)
