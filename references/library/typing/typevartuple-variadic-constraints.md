# typing - Building generic types and type aliases - Contract: Be aware, though, that no more than a single type variable tuple is allowed within one list of type arguments or type parameters:

Be aware, though, that no more than a single type variable tuple is allowed within one list of type arguments or type parameters:

```python
x: tuple[*Ts, *Ts]            # Not valid
class Array[*Shape, *Shape]:  # Not valid
    pass

```

Lastly, an unpacked type variable tuple is usable as the type annotation for `*args`:

```python
def call_soon[*Ts](
    callback: Callable[[*Ts], None],
    *args: *Ts
) -> None:
    ...
    callback(*args)

```

Unlike non-unpacked annotations on `*args` - say `*args: int`, which would dictate that *every* argument is `int` - the annotation `*args: *Ts` lets you reference the types of the *individual* arguments within `*args`. Doing so here lets us guarantee that the types of the `*args` handed to `call_soon` line up with the types of the (positional) arguments of `callback`.

Refer to [**PEP 646**](https://peps.python.org/pep-0646/) for more on type variable tuples.

[Subject index](INDEX.md) · [Previous](typing-typevartuple-class.md) · [Continue](type-variable-tuple-default-evaluation.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: typing.TypeVarTuple](typing-typevartuple-class.md) · [Owning module, declaration or section: Building generic types and type aliases](typing-generic-class.md)
