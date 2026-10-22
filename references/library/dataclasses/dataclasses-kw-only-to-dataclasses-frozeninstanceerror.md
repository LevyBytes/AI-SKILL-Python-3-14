# dataclasses: `dataclasses.KW_ONLY`, `dataclasses.FrozenInstanceError`

dataclasses.KW_ONLY

A sentinel value put to use as a type annotation. Every field positioned after a pseudo-field whose type is `KW_ONLY` becomes a keyword-only field. Note that a pseudo-field of type `KW_ONLY` is otherwise disregarded entirely. The name of such a field is included in that. Convention has it that a name of `_` is given to a `KW_ONLY` field. Keyword-only fields stand for [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) parameters that have to be given as keywords whenever the class is instantiated.

For this example, the fields `y` and `z` become keyword-only fields:

```python
@dataclass
class Point:
    x: float
    _: KW_ONLY
    y: float
    z: float

p = Point(0, y=1.5, z=2.0)

```

Within one dataclass, declaring more than a single field whose type is `KW_ONLY` is an error.

Added in version 3.10.

 *exception *dataclasses.FrozenInstanceError

[Subject index](INDEX.md) · [Previous](dataclasses-make-dataclass-to-dataclasses-missing.md) · [Owning module, declaration or section: dataclasses](dataclasses-data-classes.md) · [Owning module, declaration or section: Module contents](module-contents-signature-and-initial-contract.md) · [Required continuation of the source contract](dataclasses-post-init.md)
