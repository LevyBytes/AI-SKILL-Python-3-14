# 8.10. Type parameter lists

### 8.10. Type parameter lists

Added in version 3.12.

Changed in version 3.13: Default values became supported (see [**PEP 696**](https://peps.python.org/pep-0696/)).

```text

type_params:  "[" type_param ("," type_param)* "]"
type_param:   typevar | typevartuple | paramspec
typevar:      identifier (":" expression)? ("=" expression)?
typevartuple: "*" identifier ("=" expression)?
paramspec:    "**" identifier ("=" expression)?
```

A type parameter list may be attached to functions (coroutines included), classes, and [type aliases](https://docs.python.org/3.14/reference/simple_stmts.html#type):

```python
def max[T](args: list[T]) -> T:
    ...

async def amax[T](args: list[T]) -> T:
    ...

class Bag[T]:
    def __iter__(self) -> Iterator[T]:
        ...

    def add(self, arg: T) -> None:
        ...

type ListOrSet[T] = list[T] | set[T]

```

Semantically, what this signals is that a type variable parameterizes the function, class, or type alias as generic. Static type checkers are the main consumers of that information; while running, generic objects behave for the most part like their non-generic equivalents.

Type parameters get declared inside square brackets (`[]`) placed right after the name of the function, class, or type alias. They are reachable inside the scope of the generic object yet nowhere outside it. So, given a declaration `def func[T](): pass`, the name `T` does not exist at module scope. The semantics of generic objects are laid out below with greater precision. A special function — technically an [annotation scope](https://docs.python.org/3.14/reference/executionmodel.html#annotation-scopes) — that surrounds the creation of the generic object is what models the scope of the type parameters.

Each generic function, class, and type alias carries a [`__type_params__`](https://docs.python.org/3.14/library/stdtypes.html#definition.__type_params__) attribute that lists its type parameters.

There are three kinds of type parameter:

- [`typing.TypeVar`](https://docs.python.org/3.14/library/typing.html#typing.TypeVar), brought in by a plain name (such as `T`). To a type checker, this represents, semantically, a single type.

- [`typing.TypeVarTuple`](https://docs.python.org/3.14/library/typing.html#typing.TypeVarTuple), brought in by a name carrying one leading asterisk (such as `*Ts`). Semantically it denotes a tuple holding any number of types.

- [`typing.ParamSpec`](https://docs.python.org/3.14/library/typing.html#typing.ParamSpec), brought in by a name carrying two leading asterisks (such as `**P`). Semantically it denotes the parameters belonging to a callable.

A [`typing.TypeVar`](https://docs.python.org/3.14/library/typing.html#typing.TypeVar) declaration can specify *bounds* and *constraints* by writing a colon (`:`) and then an expression. One expression following the colon gives a bound (e.g. `T: int`). Semantically, that confines the `typing.TypeVar` to types that are a subtype of the bound. A parenthesized tuple of expressions after the colon gives a set of constraints (e.g. `T: (str, bytes)`). Every member of that tuple ought to be a type (and again, runtime does not enforce this). A constrained type variable may take on only one of the types named in its constraint list.

When `typing.TypeVar`s are declared via the type parameter list syntax, their bounds and constraints stay unevaluated at the time the generic object is built; evaluation happens only when the value is explicitly read through the `__bound__` and `__constraints__` attributes. To make this work, the bounds or constraints are evaluated within a separate [annotation scope](https://docs.python.org/3.14/reference/executionmodel.html#annotation-scopes).

Neither [`typing.TypeVarTuple`](https://docs.python.org/3.14/library/typing.html#typing.TypeVarTuple)s nor [`typing.ParamSpec`](https://docs.python.org/3.14/library/typing.html#typing.ParamSpec)s may carry bounds or constraints.

Each of the three flavors of type parameter may additionally have a *default value*, applied whenever the type parameter is left unspecified. You add it by writing a single equals sign (`=`) followed by an expression. As with the bounds and constraints of type variables, the default value stays unevaluated when the object is built and is evaluated only once the type parameter’s `__default__` attribute is read. For this purpose, the default value is evaluated within a separate [annotation scope](https://docs.python.org/3.14/reference/executionmodel.html#annotation-scopes). When a type parameter is given no default value, its `__default__` attribute is set to the special sentinel object [`typing.NoDefault`](https://docs.python.org/3.14/library/typing.html#typing.NoDefault).

The example below shows the full set of allowed type parameter declarations:

```python
def overly_generic[
   SimpleTypeVar,
   TypeVarWithDefault = int,
   TypeVarWithBound: int,
   TypeVarWithConstraints: (str, bytes),
   *SimpleTypeVarTuple = (int, float),
   **SimpleParamSpec = (str, bytearray),
](
   a: SimpleTypeVar,
   b: TypeVarWithDefault,
   c: TypeVarWithBound,
   d: Callable[SimpleParamSpec, TypeVarWithConstraints],
   *e: SimpleTypeVarTuple,
): ...

```

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Previous source section](the-async-with-statement.md) · [Following source section](generic-functions.md)
