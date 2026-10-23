# typing - Annotating callable objects

### Annotating callable objects

You can annotate functions — and any other [callable](https://docs.python.org/3.14/glossary.html#term-callable) objects — with [`collections.abc.Callable`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Callable) or the deprecated `typing.Callable`. The notation `Callable[[int], str]` describes a function accepting one [`int`](https://docs.python.org/3.14/library/functions.html#int) parameter and producing a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str).

By way of example:

```python
from collections.abc import Callable, Awaitable

def feeder(get_next_item: Callable[[], str]) -> None:
    ...  # Body

def async_query(on_success: Callable[[int], None],
                on_error: Callable[[int, Exception], None]) -> None:
    ...  # Body

async def on_update(value: str) -> None:
    ...  # Body

callback: Callable[[str], Awaitable[None]] = on_update

```

Exactly two entries are required in the subscription: the list of arguments followed by the return type. For the argument list, supply a list of types, a `ParamSpec`, `Concatenate`, or an ellipsis (`...`). A single type stands as the return type.

Should the argument list be a bare ellipsis `...`, that signals a callable carrying any parameter list at all would pass:

```python
def concat(x: str, y: str) -> str:
    return x + y

x: Callable[..., str]
x = str     # OK
x = concat  # Also OK

```

Some signatures lie beyond what `Callable` can describe — for instance functions accepting a variable number of arguments, overloaded functions, or functions with keyword-only parameters. You can capture such signatures, though, by writing a `Protocol` class that defines a [`__call__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__call__) method:

```python
from collections.abc import Iterable
from typing import Protocol

class Combiner(Protocol):
    def __call__(self, *vals: bytes, maxlen: int | None = None) -> list[bytes]: ...

def batch_proc(data: Iterable[bytes], cb_results: Combiner) -> bytes:
    for item in data:
        ...

def good_cb(*vals: bytes, maxlen: int | None = None) -> list[bytes]:
    ...
def bad_cb(*vals: bytes, maxitems: int | None) -> list[bytes]:
    ...

batch_proc([], good_cb)  # OK
batch_proc([], bad_cb)   # Error! Argument 2 has incompatible type because of
                         # different name and kind in the callback

```

When a callable receives other callables as arguments, `ParamSpec` lets it state that their parameter types track one another. And where such a callable inserts or strips arguments relative to the callables it wraps, the `Concatenate` operator applies. The respective forms are `Callable[ParamSpecVariable, ReturnType]` and `Callable[Concatenate[Arg1Type, Arg2Type, ..., ParamSpecVariable], ReturnType]`.

Changed in version 3.10: `Callable` now supports `ParamSpec` and `Concatenate`. See [**PEP 612**](https://peps.python.org/pep-0612/) for more details.

See also

The documentation for `ParamSpec` and `Concatenate` provides examples of usage in `Callable`.

[Subject index](INDEX.md) · [Previous](newtype.md) · [Continue](generics.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md)
