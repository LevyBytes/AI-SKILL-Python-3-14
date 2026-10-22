# Lifetime of the Module State

### Lifetime of the Module State

Once a module object is garbage-collected, its module state gets freed. For every pointer into (some portion of) the module state, you have to keep a reference to the module object.

Most of the time this poses no trouble, since types built with [`PyType_FromModuleAndSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromModuleAndSpec), along with their instances, retain a reference to the module. Even so, you have to be careful with reference counting whenever you reference module state from elsewhere, such as the callbacks of external libraries.

[Subject index](INDEX.md) · [Previous source context](module-state-access-from-slot-methods-getters-and-setters.md) · [Following source context](open-issues.md)
