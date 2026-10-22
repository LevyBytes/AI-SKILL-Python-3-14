# typing: `typing.Optional`, `typing.Concatenate`

typing.Optional

`Optional[X]` is equivalent to `X | None` (or `Union[X, None]`).

Keep in mind this is a separate notion from an optional argument, which is simply one carrying a default. An optional argument that has a default needs no `Optional` qualifier on its type annotation merely on account of being optional. For example:

```python
def foo(arg: int = 0) -> None:
    ...

```

Conversely, when an explicit `None` value is permitted, applying `Optional` makes sense, regardless of whether the argument itself is optional. For example:

```python
def foo(arg: Optional[int] = None) -> None:
    ...

```

Changed in version 3.10: Optional may now take the form `X | None`. See [union type expressions](https://docs.python.org/3.14/library/stdtypes.html#types-union).

 typing.Concatenate

Special form for annotating higher-order functions.

`Concatenate` may be paired with Callable and `ParamSpec` to annotate a higher-order callable that adds, drops, or reshapes the parameters of some other callable. The form to use is `Concatenate[Arg1Type, Arg2Type, ..., ParamSpecVariable]`. `Concatenate` is permitted inside Callable type hints and when instantiating user-defined generic classes that carry `ParamSpec` parameters. Whatever appears last in `Concatenate` has to be a `ParamSpec` or an ellipsis (`...`).

To take an example, suppose you want to annotate a decorator `with_lock` that hands a [`threading.Lock`](https://docs.python.org/3.14/library/threading.html#threading.Lock) to the function it wraps; `Concatenate` lets you state that `with_lock` takes a callable expecting a `Lock` as its first argument and yields a callable with a different type signature. Here the `ParamSpec` conveys that the parameter types of the returned callable hinge on the parameter types of the incoming callable:

```python
from collections.abc import Callable
from threading import Lock
from typing import Concatenate

# Use this lock to ensure that only one thread is executing a function
# at any time.
my_lock = Lock()

def with_lock[**P, R](f: Callable[Concatenate[Lock, P], R]) -> Callable[P, R]:
    '''A type-safe decorator which provides a lock.'''
    def inner(*args: P.args, **kwargs: P.kwargs) -> R:
        # Provide the lock as the first argument.
        return f(my_lock, *args, **kwargs)
    return inner

@with_lock
def sum_threadsafe(lock: Lock, numbers: list[float]) -> float:
    '''Add a list of numbers together in a thread-safe manner.'''
    with lock:
        return sum(numbers)

# We don't need to pass in the lock ourselves thanks to the decorator.
sum_threadsafe([1.1, 2.2, 3.3])

```

Added in version 3.10.

See also

- [**PEP 612**](https://peps.python.org/pep-0612/) — Parameter Specification Variables (the PEP which introduced `ParamSpec` and `Concatenate`)

- `ParamSpec`

- Annotating callable objects

[Subject index](INDEX.md) · [Previous](typing-union-class.md) · [Continue](typing-literal.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Special forms](typing-union-class.md)
