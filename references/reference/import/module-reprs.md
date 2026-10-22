# 5.4.5. Module reprs

### 5.4.5. Module reprs

Every module ships with a serviceable repr out of the box; nevertheless, by way of the attributes described above plus those in the module's spec, you gain more explicit say over how module objects are represented.

Should the module carry a spec (`__spec__`), the import machinery attempts to build a repr from it. Where that attempt fails, or where no spec exists, the import system assembles a fallback repr out of whatever the module makes available. It tries feeding `module.__name__`, `module.__file__`, and `module.__loader__` into the repr, substituting defaults wherever a piece is absent.

These are the precise rules in force:

- When the module carries a `__spec__` attribute, that spec's data drives the repr. The "name", "loader", "origin", and "has_location" attributes get consulted.

- When the module carries a `__file__` attribute, it contributes to the module's repr.

- When the module lacks `__file__` yet has a `__loader__` that isn't `None`, the loader's repr becomes part of the module's repr.

- Failing all that, the module's `__name__` alone is what appears in the repr.

Changed in version 3.12: deprecated back in Python 3.4, `module_repr()` was dropped in Python 3.12, so it no longer participates when a module's repr is being worked out.

[Subject index](INDEX.md) · [Owning language section](the-import-system.md) · [Owning language section](loading.md) · [Previous source section](path-attributes-on-modules.md) · [Following source section](cached-bytecode-invalidation.md)
