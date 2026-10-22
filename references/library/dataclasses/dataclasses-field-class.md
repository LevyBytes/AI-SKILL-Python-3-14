# dataclasses: `dataclasses.Field`

*class *dataclasses.Field

Every defined field is described by a `Field` object. Such objects come into being internally and are handed back by the module-level `fields()` method (covered below). A `Field` object should never be instantiated directly by users. These are its documented attributes:

- `name`: The name of the field.

- `type`: The type of the field.

- `default`, `default_factory`, `init`, `repr`, `hash`, `compare`, `metadata`, and `kw_only` carry the same meaning and values they hold within the `field()` function.

Further attributes may be present, yet they are private and must not be inspected or depended upon.

[Subject index](INDEX.md) · [Previous](dataclasses-field.md) · [Continue](dataclasses-initvar-class.md) · [Owning module, declaration or section: dataclasses](dataclasses-data-classes.md) · [Owning module, declaration or section: Module contents](module-contents-signature-and-initial-contract.md)
