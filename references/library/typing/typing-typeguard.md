# typing: `typing.TypeGuard`

typing.TypeGuard

Special typing construct for marking user-defined type predicate functions.

Type predicate functions are functions you define that report whether their argument is an instance of some particular type. The mechanics of `TypeGuard` resemble those of `TypeIs`, yet it influences type checking behavior in subtly distinct ways (described below).

Declaring `-> TypeGuard` informs the static type checker, for any given function, that:

1.

The return value is a boolean.

2.

Should the return value be `True`, the type of its argument becomes the type written inside `TypeGuard`.

Type variables are supported by `TypeGuard` too. Consult [**PEP 647**](https://peps.python.org/pep-0647/) for more details.

By way of illustration:

```python
def is_str_list(val: list[object]) -> TypeGuard[list[str]]:
    '''Determines whether all objects in the list are strings'''
    return all(isinstance(x, str) for x in val)

def func1(val: list[object]):
    if is_str_list(val):
        # Type of ``val`` is narrowed to ``list[str]``.
        print(" ".join(val))
    else:
        # Type of ``val`` remains as ``list[object]``.
        print("Not a list of strings!")

```

Here is how `TypeIs` and `TypeGuard` diverge:

- `TypeIs` demands that the narrowed type be a subtype of the input type, whereas `TypeGuard` imposes no such requirement. The chief motivation is to permit moves like narrowing `list[object]` down to `list[str]`, even though the latter is not a subtype of the former, because `list` is invariant.

- Once a `TypeGuard` function returns `True`, type checkers narrow the variable's type down to precisely the `TypeGuard` type. Once a `TypeIs` function returns `True`, type checkers may deduce a more exact type by blending the variable's previously known type with the `TypeIs` type. (In technical terms, this goes by the name intersection type.)

- Once a `TypeGuard` function returns `False`, type checkers are unable to narrow the variable's type whatsoever. Once a `TypeIs` function returns `False`, type checkers can narrow the variable's type so that the `TypeIs` type is excluded.

Added in version 3.10.

[Subject index](INDEX.md) · [Previous](typing-typeis.md) · [Continue](typing-unpack.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Special forms](typing-union-class.md)
