# dataclasses: `dataclasses.InitVar`

*class *dataclasses.InitVar

The `InitVar[T]` type annotations mark variables that are init-only. Any field annotated with `InitVar` counts as a pseudo-field; consequently such fields are neither handed back by the `fields()` function nor used for anything beyond being added as parameters to [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) and an optional `__post_init__()`.

[Subject index](INDEX.md) · [Previous](dataclasses-field-class.md) · [Continue](dataclasses-fields-to-dataclasses-astuple.md) · [Owning module, declaration or section: dataclasses](dataclasses-data-classes.md) · [Owning module, declaration or section: Module contents](module-contents-signature-and-initial-contract.md)
