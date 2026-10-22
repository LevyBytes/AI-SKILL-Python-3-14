# dataclasses: `dataclasses.fields()`, `dataclasses.asdict()`, `dataclasses.astuple()`

dataclasses.fields(*class_or_instance*)

Hands back a tuple of `Field` objects that define the fields belonging to this dataclass. Takes either a dataclass or an instance of one. Raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) when what it receives is neither a dataclass nor an instance of one. Pseudo-fields that are `ClassVar` or `InitVar` are not handed back.

 dataclasses.asdict(*obj*, ***, *dict_factory=dict*)

Turns the dataclass *obj* into a dict (using the *dict_factory* factory function). Each dataclass becomes a dict of its fields, written as `name: value` pairs. Recursion descends into dataclasses, dicts, lists, and tuples. Anything else is copied via [`copy.deepcopy()`](https://docs.python.org/3.14/library/copy.html#copy.deepcopy).

An example applying `asdict()` to nested dataclasses:

```python
@dataclass
class Point:
     x: int
     y: int

@dataclass
class C:
     mylist: list[Point]

p = Point(10, 20)
assert asdict(p) == {'x': 10, 'y': 20}

c = C([Point(0, 0), Point(10, 4)])
assert asdict(c) == {'mylist': [{'x': 0, 'y': 0}, {'x': 10, 'y': 4}]}

```

The workaround below can be used to produce a shallow copy:

```python
{field.name: getattr(obj, field.name) for field in fields(obj)}

```

`asdict()` raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) where *obj* is not a dataclass instance.

 dataclasses.astuple(*obj*, ***, *tuple_factory=tuple*)

Turns the dataclass *obj* into a tuple (using the *tuple_factory* factory function). Each dataclass becomes a tuple of its field values. Recursion descends into dataclasses, dicts, lists, and tuples. Anything else is copied via [`copy.deepcopy()`](https://docs.python.org/3.14/library/copy.html#copy.deepcopy).

Picking up from the earlier example:

```python
assert astuple(p) == (10, 20)
assert astuple(c) == ([(0, 0), (10, 4)],)

```

The workaround below can be used to produce a shallow copy:

```python
tuple(getattr(obj, field.name) for field in dataclasses.fields(obj))

```

`astuple()` raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) where *obj* is not a dataclass instance.

[Subject index](INDEX.md) · [Previous](dataclasses-initvar-class.md) · [Continue](dataclasses-make-dataclass-to-dataclasses-missing.md) · [Owning module, declaration or section: dataclasses](dataclasses-data-classes.md) · [Owning module, declaration or section: Module contents](module-contents-signature-and-initial-contract.md)
