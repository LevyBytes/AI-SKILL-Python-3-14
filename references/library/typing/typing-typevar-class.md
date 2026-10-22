# typing: `typing.TypeVar`

*class *typing.TypeVar(*name*, **constraints*, *bound=None*, *covariant=False*, *contravariant=False*, *infer_variance=False*, *default=typing.NoDefault*)

Type variable.

The recommended route for building a type variable is through the dedicated syntax for [generic functions](https://docs.python.org/3.14/reference/compound_stmts.html#generic-functions), [generic classes](https://docs.python.org/3.14/reference/compound_stmts.html#generic-classes), and [generic type aliases](https://docs.python.org/3.14/reference/compound_stmts.html#generic-type-aliases):

```python
class Sequence[T]:  # T is a TypeVar
    ...

```

That same syntax serves to define bounded and constrained type variables as well:

```python
class StrSequence[S: str]:  # S is a TypeVar with a `str` upper bound;
    ...                     # we can say that S is "bounded by `str`"

class StrOrBytesSequence[A: (str, bytes)]:  # A is a TypeVar constrained to str or bytes
    ...

```

That said, when you want reusable type variables, you can equally build them by hand, in this fashion:

```python
T = TypeVar('T')  # Can be anything
S = TypeVar('S', bound=str)  # Can be any subtype of str
A = TypeVar('A', str, bytes)  # Must be exactly str or bytes

```

Type variables are present chiefly to serve static type checkers. They act as the parameters of generic types and likewise for generic function and type alias definitions. Refer to `Generic` for further detail about generic types. Here is how generic functions operate:

```python
def repeat[T](x: T, n: int) -> Sequence[T]:
    """Return a list containing n references to x."""
    return [x]*n

def print_capitalized[S: str](x: S) -> S:
    """Print x capitalized, and return x."""
    print(x.capitalize())
    return x

def concatenate[A: (str, bytes)](x: A, y: A) -> A:
    """Add two strings or bytes objects together."""
    return x + y

```

Keep in mind that a type variable may be *bounded*, *constrained*, or neither, yet it can never be both bounded *and* constrained at once.

When type variables come into being through the [type parameter syntax](https://docs.python.org/3.14/reference/compound_stmts.html#type-params), or when `infer_variance=True` is supplied, type checkers infer their variance. Type variables you build by hand can be tagged covariant or contravariant explicitly by supplying `covariant=True` or `contravariant=True`. Absent that, hand-built type variables default to invariant. Refer to [**PEP 484**](https://peps.python.org/pep-0484/) and [**PEP 695**](https://peps.python.org/pep-0695/) for further detail.

Bounded type variables and constrained type variables behave differently in a number of significant respects. Choosing a *bounded* type variable means the `TypeVar` gets resolved to the narrowest type available:

```python
x = print_capitalized('a string')
reveal_type(x)  # revealed type is str

class StringSubclass(str):
    pass

y = print_capitalized(StringSubclass('another string'))
reveal_type(y)  # revealed type is StringSubclass

z = print_capitalized(45)  # error: int is not a subtype of str

```

A type variable's upper bound may be a concrete type, an abstract type (ABC or Protocol), or even a union of several types:

```python
# Can be anything with an __abs__ method
def print_abs[T: SupportsAbs](arg: T) -> None:
    print("Absolute value:", abs(arg))

U = TypeVar('U', bound=str|bytes)  # Can be any subtype of the union str|bytes
V = TypeVar('V', bound=SupportsAbs)  # Can be anything with an __abs__ method

```

Choosing a *constrained* type variable, on the other hand, means the `TypeVar` may only ever resolve to exactly one of the supplied constraints:

[Subject index](INDEX.md) · [Previous](typing-generic-class.md) · [Continue](generic-concatenation-type-example.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Building generic types and type aliases](typing-generic-class.md)
