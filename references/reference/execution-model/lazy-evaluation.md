# 4.2.4. Lazy evaluation

### 4.2.4. Lazy evaluation

The bulk of annotation scopes undergo *lazy evaluation*. That covers annotations, the values of type aliases built via the [`type`](https://docs.python.org/3.14/reference/simple_stmts.html#type) statement, and the bounds, constraints, and default values of type variables built via the [type parameter syntax](https://docs.python.org/3.14/reference/compound_stmts.html#type-params). What this means is that they go unevaluated at the moment the type alias or type variable is created, and at the moment the annotation-bearing object is created. They are evaluated solely when the need arises — for instance, on accessing the `__value__` attribute of a type alias.

Example:

```pycon
>>> type Alias = 1/0
>>> Alias.__value__
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
>>> def func[T: 1/0](): pass
>>> T = func.__type_params__[0]
>>> T.__bound__
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero

```

For this case the exception fires solely when the type alias has its `__value__` attribute accessed, or when the type variable has its `__bound__` attribute accessed.

Where this behavior earns its keep is chiefly with references to types not yet defined at the time the type alias or type variable is created. Lazy evaluation, for one, makes it possible to build mutually recursive type aliases:

```python
from typing import Literal

type SimpleExpr = int | Parenthesized
type Parenthesized = tuple[Literal["("], Expr, Literal[")"]]
type Expr = SimpleExpr | tuple[SimpleExpr, Literal["+", "-"], Expr]

```

Values that are lazily evaluated get evaluated in annotation scope, so any names appearing inside the lazily evaluated value are looked up just as if they had been used in the scope that immediately encloses it.

Added in version 3.12.

[Subject index](INDEX.md) · [Owning language section](structure-of-a-program.md) · [Owning language section](binding-of-names.md) · [Previous source section](annotation-scopes.md) · [Following source section](builtins-and-restricted-execution.md)
