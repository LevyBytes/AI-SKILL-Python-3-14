# 8.10.1. Generic functions

### 8.10.1. Generic functions

Generic functions are declared as follows:

```python
def func[T](arg: T): ...

```

This syntax is equivalent to:

```python
annotation-def TYPE_PARAMS_OF_func():
    T = typing.TypeVar("T")
    def func(arg: T): ...
    func.__type_params__ = (T,)
    return func
func = TYPE_PARAMS_OF_func()

```

Here `annotation-def` marks an [annotation scope](https://docs.python.org/3.14/reference/executionmodel.html#annotation-scopes), which is in fact never bound to any name at runtime. (The translation takes one further liberty: rather than going through attribute access on the [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module, the syntax directly builds an instance of [`typing.TypeVar`](https://docs.python.org/3.14/library/typing.html#typing.TypeVar).)

A generic function’s annotations are evaluated inside the annotation scope set up for declaring the type parameters, whereas the function’s defaults and decorators are not.

The example below shows the scoping rules for these situations, plus additional flavors of type parameters:

```python
@decorator
def func[T: int, *Ts, **P](*args: *Ts, arg: Callable[P, T] = some_default):
    ...

```

Apart from the [lazy evaluation](https://docs.python.org/3.14/reference/executionmodel.html#lazy-evaluation) of the [`TypeVar`](https://docs.python.org/3.14/library/typing.html#typing.TypeVar) bound, this is equivalent to:

```python
DEFAULT_OF_arg = some_default

annotation-def TYPE_PARAMS_OF_func():

    annotation-def BOUND_OF_T():
        return int
    # In reality, BOUND_OF_T() is evaluated only on demand.
    T = typing.TypeVar("T", bound=BOUND_OF_T())

    Ts = typing.TypeVarTuple("Ts")
    P = typing.ParamSpec("P")

    def func(*args: *Ts, arg: Callable[P, T] = DEFAULT_OF_arg):
        ...

    func.__type_params__ = (T, Ts, P)
    return func
func = decorator(TYPE_PARAMS_OF_func())

```

The capitalized names like `DEFAULT_OF_arg` are not actually bound at runtime.

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Owning language section](type-parameter-lists.md) · [Previous source section](type-parameter-lists.md) · [Following source section](generic-classes.md)
