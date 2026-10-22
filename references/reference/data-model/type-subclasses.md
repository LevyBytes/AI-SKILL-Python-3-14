# type.__subclasses__()

type.__subclasses__()

Every class maintains a list of weak references pointing at its direct subclasses. Calling this method gives back a list of all of those references that remain alive. That list follows definition order. Example:

```pycon
>>> class A: pass
>>> class B(A): pass
>>> A.__subclasses__()
[<class 'B'>]

```

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](custom-classes.md) · [Owning language section](special-methods.md) · [Previous source section](type-mro.md) · [Following source section](class-instances.md)
