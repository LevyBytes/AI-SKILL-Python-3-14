# dataclasses — Class variables

### Class variables

A rare situation in which `@dataclass` truly examines a field's type occurs when it checks whether that field counts as a class variable in the sense of [**PEP 526**](https://peps.python.org/pep-0526/). The test it applies is whether the field's type is [`typing.ClassVar`](https://docs.python.org/3.14/library/typing.html#typing.ClassVar). A field marked `ClassVar` drops out of the field set entirely and the dataclass machinery pays it no attention. These `ClassVar` pseudo-fields never show up in the output of the module-level `fields()` function.

[Subject index](INDEX.md) · [Previous](dataclasses-post-init.md) · [Continue](init-only-variables.md) · [Owning module, declaration or section: dataclasses](dataclasses-data-classes.md)
