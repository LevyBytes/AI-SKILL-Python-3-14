# typing — Other special directives — Signature and initial contract

*class *typing.TypedDict(*dict*)

A special construct for attaching type hints to a dictionary. Once the program runs, “`TypedDict` instances” are nothing more than [`dicts`](https://docs.python.org/3.14/library/stdtypes.html#dict).

A `TypedDict` declares a dictionary type whose every instance is expected to carry a fixed set of keys, each paired with a value of one consistent type. Type checkers enforce this expectation, but it is never verified at runtime. Usage:

```python
class Point2D(TypedDict):
    x: int
    y: int
    label: str

a: Point2D = {'x': 1, 'y': 2, 'label': 'good'}  # OK
b: Point2D = {'z': 3, 'label': 'bad'}           # Fails type check

assert Point2D(x=1, y=2, label='first') == dict(x=1, y=2, label='first')

```

You can also build a `TypedDict` through function-call syntax. The literal [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) must be supplied as the second argument:

```python
Point2D = TypedDict('Point2D', {'x': int, 'y': int, 'label': str})

```

With this functional syntax you can define keys that are not valid [identifiers](https://docs.python.org/3.14/reference/lexical_analysis.html#identifiers) — for instance when they are keywords or contain hyphens, or when the key names must avoid being [mangled](https://docs.python.org/3.14/reference/expressions.html#private-name-mangling) the way ordinary private names are:

```python
# raises SyntaxError
class Point2D(TypedDict):
    in: int  # 'in' is a keyword
    x-y: int  # name with hyphens

class Definition(TypedDict):
    __schema: str  # mangled to `_Definition__schema`

# OK, functional syntax
Point2D = TypedDict('Point2D', {'in': int, 'x-y': int})
Definition = TypedDict('Definition', {'__schema': str})  # not mangled

```

Every key is required in a `TypedDict` by default. You can flag particular keys as optional with `NotRequired`:

```python
class Point2D(TypedDict):
    x: int
    y: int
    label: NotRequired[str]

# Alternative syntax
Point2D = TypedDict('Point2D', {'x': int, 'y': int, 'label': NotRequired[str]})

```

So a `Point2D` `TypedDict` is permitted to leave out the `label` key.

You can likewise make every key optional by default by giving a totality of `False`:

```python
class Point2D(TypedDict, total=False):
    x: int
    y: int

# Alternative syntax
Point2D = TypedDict('Point2D', {'x': int, 'y': int}, total=False)

```

So a `Point2D` `TypedDict` may omit any of its keys. For the `total` argument's value, a type checker need only handle a literal `False` or `True`. The default is `True`, which makes every item declared in the class body required.

Specific keys of a `total=False` `TypedDict` can be flagged as required by means of `Required`:

[Subject index](INDEX.md) · [Previous](other-special-directives-closable-and-named.md) · [Continue](typed-dictionary-optional-fields-example.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Other special directives](type-construction-directives.md)
