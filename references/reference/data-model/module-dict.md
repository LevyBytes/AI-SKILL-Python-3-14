# module.__dict__

module.__dict__

The module’s namespace expressed as a dictionary object. Distinctly among the attributes covered here, `__dict__` is not reachable as a global variable from inside a module; it is reachable only as an attribute on module objects.

**CPython implementation detail:** Owing to how CPython clears module dictionaries, the module dictionary gets cleared once the module leaves scope, even when live references to the dictionary remain. As a workaround, copy the dictionary or hold on to the module while working with its dictionary directly.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](modules.md) · [Owning language section](module-dictionaries.md) · [Previous source section](module-dictionaries.md) · [Following source section](custom-classes.md)
