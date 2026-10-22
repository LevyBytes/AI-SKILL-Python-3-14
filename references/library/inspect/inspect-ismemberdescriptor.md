# inspect: `inspect.ismemberdescriptor()`

inspect.ismemberdescriptor(*object*)

Return `True` if the object is a member descriptor.

**CPython implementation detail:** In extension modules, member descriptors are the attributes set up through [`PyMemberDef`](https://docs.python.org/3.14/c-api/structures.html#c.PyMemberDef) structures. On Python implementations that lack such types, this method always comes back `False`.

[Subject index](INDEX.md) · [Previous](inspect-isasyncgenfunction-to-inspect-isgetsetdescriptor.md) · [Continue](inspect-getdoc-to-inspect-cleandoc.md) · [Owning module, declaration or section: inspect](inspect-inspect-live-objects.md) · [Owning module, declaration or section: Types and members](types-and-members-section-introduction-and-initial-examples.md)
