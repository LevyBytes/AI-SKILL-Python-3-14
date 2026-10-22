# What’s New In Python 3.12 / PEP 695: Type Parameter Syntax — typing

### New Features

### PEP 695: Type Parameter Syntax

Declaring generic classes and functions under [**PEP 484**](https://peps.python.org/pep-0484/) relied on a wordy form that obscured where type parameters were in scope and demanded that variance be spelled out by hand.

[**PEP 695**](https://peps.python.org/pep-0695/) introduces a new, more compact and explicit way to create [generic classes](https://docs.python.org/3.14/reference/compound_stmts.html#generic-classes) and [functions](https://docs.python.org/3.14/reference/compound_stmts.html#generic-functions):

```python
def max[T](args: Iterable[T]) -> T:
    ...

class list[T]:
    def __getitem__(self, index: int, /) -> T:
        ...

    def append(self, element: T) -> None:
        ...

```

Beyond that, the PEP adds a fresh route for declaring [type aliases](https://docs.python.org/3.14/library/typing.html#type-aliases) through the [`type`](https://docs.python.org/3.14/reference/simple_stmts.html#type) statement, which builds an instance of [`TypeAliasType`](https://docs.python.org/3.14/library/typing.html#typing.TypeAliasType):

```python
type Point = tuple[float, float]

```

Type aliases can also be [generic](https://docs.python.org/3.14/reference/compound_stmts.html#generic-type-aliases):

```python
type Point[T] = tuple[T, T]

```

By way of the new syntax you may declare [`TypeVarTuple`](https://docs.python.org/3.14/library/typing.html#typing.TypeVarTuple) and [`ParamSpec`](https://docs.python.org/3.14/library/typing.html#typing.ParamSpec) parameters, plus [`TypeVar`](https://docs.python.org/3.14/library/typing.html#typing.TypeVar) parameters carrying bounds or constraints:

```python
type IntFunc[**P] = Callable[P, int]  # ParamSpec
type LabeledTuple[*Ts] = tuple[str, *Ts]  # TypeVarTuple
type HashableSequence[T: Hashable] = Sequence[T]  # TypeVar with bound
type IntOrStrSequence[T: (int, str)] = Sequence[T]  # TypeVar with constraints

```

For type aliases declared this way, the alias value as well as a type variable’s bound and constraints get computed only when needed (refer to [lazy evaluation](https://docs.python.org/3.14/reference/executionmodel.html#lazy-evaluation)). As a result, a type alias can reference other types that appear later within the same file.

A type parameter introduced by a type parameter list is in scope throughout the declaration itself and any nested scopes, yet stays absent from the surrounding scope. As an illustration, such parameters work inside the type annotations of a generic class’s methods or within the class body. Even so, they are unavailable at module scope once the class has been defined. The runtime semantics of type parameters are described thoroughly at [Type parameter lists](https://docs.python.org/3.14/reference/compound_stmts.html#type-params).

To make these scoping rules work, a fresh category of scope arrives, the [annotation scope](https://docs.python.org/3.14/reference/executionmodel.html#annotation-scopes). For the most part annotation scopes act like function scopes, though their interaction with surrounding class scopes differs. Starting in Python 3.13, [annotations](https://docs.python.org/3.14/glossary.html#term-annotation) too will be computed within annotation scopes.

See [**PEP 695**](https://peps.python.org/pep-0695/) for more details.

(PEP authored by Eric Traut. Implemented by Jelle Zijlstra together with Eric Traut and additional contributors in [gh-103764](https://github.com/python/cpython/issues/103764).)

[Subject index](INDEX.md) · [Previous source section](tokenization-and-library-highlights.md) · [Next source section](pep-701-syntactic-formalization-of-f-strings.md) · [Release/subject declaration](summary-release-highlights.md)
