# typing - Annotating tuples

### Annotating tuples

With the bulk of Python containers, the typing system presumes every element shares one type. To illustrate:

```python
from collections.abc import Mapping

# Type checker will infer that all elements in ``x`` are meant to be ints
x: list[int] = []

# Type checker error: ``list`` only accepts a single type argument:
y: list[int, str] = [1, 'foo']

# Type checker will infer that all keys in ``z`` are meant to be strings,
# and that all values in ``z`` are meant to be either strings or ints
z: Mapping[str, str | int] = {}

```

Since [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) takes just one type argument, a type checker flags the `y` assignment above as an error. In the same way, [`Mapping`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Mapping) takes exactly two type arguments — the first giving the key type and the second the value type.

Tuples differ from most Python containers, though: idiomatic Python frequently builds tuples whose elements span several types. That is why the typing system gives tuples special treatment. [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple) admits *any number* of type arguments:

```python
# OK: ``x`` is assigned to a tuple of length 1 where the sole element is an int
x: tuple[int] = (5,)

# OK: ``y`` is assigned to a tuple of length 2;
# element 1 is an int, element 2 is a str
y: tuple[int, str] = (5, "foo")

# Error: the type annotation indicates a tuple of length 1,
# but ``z`` has been assigned to a tuple of length 3
z: tuple[int] = (1, 2, 3)

```

For a tuple that may run to *any* length while every element shares type `T`, write the literal ellipsis `...` as `tuple[T, ...]`. An empty tuple is `tuple[()]`. Annotating with bare `tuple` amounts to the same thing as `tuple[Any, ...]`:

```python
x: tuple[int, ...] = (1, 2)
# These reassignments are OK: ``tuple[int, ...]`` indicates x can be of any length
x = (1, 2, 3)
x = ()
# This reassignment is an error: all elements in ``x`` must be ints
x = ("foo", "bar")

# ``y`` can only ever be assigned to an empty tuple
y: tuple[()] = ()

z: tuple = ("foo", "bar")
# These reassignments are OK: plain ``tuple`` is equivalent to ``tuple[Any, ...]``
z = (1, 2, 3)
z = ()

```

[Subject index](INDEX.md) · [Previous](generics.md) · [Continue](the-type-of-class-objects.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md)
