# dataclasses - Init-only variables

### Init-only variables

A second case in which `@dataclass` reads a type annotation is to decide whether a field is an init-only variable. The check it makes is whether the field's type happens to be `InitVar`. When the field carries that `InitVar` type, it becomes a pseudo-field termed an init-only field. Since it is not an actual field, the module-level `fields()` function omits it. Such init-only fields turn into parameters on the synthesized [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) method and get forwarded to the optional `__post_init__()` method. Beyond that, dataclasses make no use of them.

As an illustration, imagine a field whose value gets pulled from a database whenever none is supplied at the moment the class is instantiated:

```python
@dataclass
class C:
    i: int
    j: int | None = None
    database: InitVar[DatabaseType | None] = None

    def __post_init__(self, database):
        if self.j is None and database is not None:
            self.j = database.lookup('j')

c = C(10, database=my_database)

```

Here, calling `fields()` yields `Field` objects covering `i` along with `j`, while `database` is left out.

[Subject index](INDEX.md) · [Previous](class-variables.md) · [Continue](frozen-instances.md) · [Owning module, declaration or section: dataclasses](dataclasses-data-classes.md)
