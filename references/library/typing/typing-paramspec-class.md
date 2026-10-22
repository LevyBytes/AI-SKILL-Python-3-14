# typing: `typing.ParamSpec`

*class *typing.ParamSpec(*name*, ***, *bound=None*, *covariant=False*, *contravariant=False*, *default=typing.NoDefault*)

Parameter specification variable. A specialized version of type variables.

Inside [type parameter lists](https://docs.python.org/3.14/reference/compound_stmts.html#type-params), you can declare parameter specifications using two asterisks (`**`):

```python
type IntFunc[**P] = Callable[P, int]

```

To stay compatible with Python 3.11 and earlier, `ParamSpec` objects may instead be built as follows:

```python
P = ParamSpec('P')

```

Parameter specification variables are present chiefly to serve static type checkers. Their job is to carry the parameter types of one callable across to another callable — a pattern that turns up regularly in higher order functions and decorators. They hold only when used within `Concatenate`, or as the first argument to `Callable`, or as parameters of user-defined Generics. Refer to `Generic` for further detail about generic types.

Say you want to attach simple logging to a function: you can build a decorator `add_logging` that records function calls. The parameter specification variable signals to the type checker that the callable fed into the decorator and the fresh callable it hands back share inter-dependent type parameters:

```python
from collections.abc import Callable
import logging

def add_logging[T, **P](f: Callable[P, T]) -> Callable[P, T]:
    '''A type-safe decorator to add logging to a function.'''
    def inner(*args: P.args, **kwargs: P.kwargs) -> T:
        logging.info(f'{f.__name__} was called')
        return f(*args, **kwargs)
    return inner

@add_logging
def add_two(x: float, y: float) -> float:
    '''Add two numbers together.'''
    return x + y

```

[Subject index](INDEX.md) · [Previous](type-variable-tuple-default-evaluation.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Building generic types and type aliases](typing-generic-class.md) · [Required continuation of the source contract](parameter-specification-default-evaluation.md)
