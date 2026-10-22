# typing: Annotated metadata and validation example

Annotated[&lt;type&gt;, &lt;metadata&gt;]

Below is an example showing how you might apply `Annotated` to attach metadata to type annotations if you were performing range analysis:

```python
@dataclass
class ValueRange:
    lo: int
    hi: int

T1 = Annotated[int, ValueRange(-10, 5)]
T2 = Annotated[T1, ValueRange(-20, 3)]

```

`Annotated`'s first argument has to be a valid type. You can hand over several metadata elements, since `Annotated` accepts a variable number of arguments. The ordering of the metadata elements is kept and counts toward equality checks:

```python
@dataclass
class ctype:
     kind: str

a1 = Annotated[int, ValueRange(3, 10), ctype("char")]
a2 = Annotated[int, ctype("char"), ValueRange(3, 10)]

assert a1 != a2  # Order matters

```

The tool consuming the annotations gets to decide whether the client may attach several metadata elements to a single annotation and how those annotations should be combined.

Nested `Annotated` types get flattened, with the metadata elements ordered beginning from the innermost annotation outward:

```python
assert Annotated[Annotated[int, ValueRange(3, 10)], ctype("char")] == Annotated[
    int, ValueRange(3, 10), ctype("char")
]

```

This behavior is suspended, though, for `Annotated` types reached by way of a type alias, so as not to compel evaluation of the `TypeAliasType` beneath:

```python
type From3To10[T] = Annotated[T, ValueRange(3, 10)]
assert Annotated[From3To10[int], ctype("char")] != Annotated[
   int, ValueRange(3, 10), ctype("char")
]

```

Duplicated metadata elements are not removed:

```python
assert Annotated[int, ValueRange(3, 10)] != Annotated[
    int, ValueRange(3, 10), ValueRange(3, 10)
]

```

`Annotated` can be used with nested and generic aliases:

>

```python
@dataclass
class MaxLen:
    value: int

type Vec[T] = Annotated[list[tuple[T, T]], MaxLen(10)]

# When used in a type annotation, a type checker will treat "V" the same as
# ``Annotated[list[tuple[int, int]], MaxLen(10)]``:
type V = Vec[int]

```

`Annotated` cannot be used with an unpacked `TypeVarTuple`:

```python
type Variadic[*Ts] = Annotated[*Ts, Ann1] = Annotated[T1, T2, T3, ..., Ann1]  # NOT valid

```

in which `T1`, `T2`, — stand for `TypeVars`. It fails because Annotated ought to receive just a single type.

Out of the box, `get_type_hints()` removes the metadata from annotations. Supply `include_extras=True` to keep the metadata intact:

>

[Subject index](INDEX.md) · [Previous](typing-readonly-to-typing-annotated.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Special forms](typing-union-class.md) · [Required continuation of the source contract](typing-annotated.md)
