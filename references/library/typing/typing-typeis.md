# typing: `typing.TypeIs`

typing.TypeIs

Special typing construct for marking user-defined type predicate functions.

You can apply `TypeIs` as an annotation on the return type of a type predicate function you write yourself. Only one type argument is permitted by `TypeIs`. While running, functions annotated this way ought to yield a boolean and accept at least one positional argument.

The purpose of `TypeIs` is to assist *type narrowing* — a method static type checkers rely on to pin down a more exact type for an expression as control flows through a program. Narrowing typically happens by examining branching control flow and then applying the refined type across a region of code. That conditional check is occasionally called a "type predicate":

```python
def is_str(val: str | float):
    # "isinstance" type predicate
    if isinstance(val, str):
        # Type of ``val`` is narrowed to ``str``
        ...
    else:
        # Else, type of ``val`` is narrowed to ``float``.
        ...

```

On occasion it proves handy to employ your own boolean function as a type predicate. To signal this intent to static type checkers, such a function should declare `TypeIs[...]` or `TypeGuard` for its return type. The behavior of `TypeIs` is generally more intuitive than that of `TypeGuard`, though it is unavailable when the input and output types do not line up (for instance, `list[object]` to `list[int]`) or when the function will not return `True` across every instance of the narrowed type.

Declaring `-> TypeIs[NarrowedType]` informs the static type checker, for any given function, that:

1.

The return value is a boolean.

2.

Should the return value be `True`, the type of its argument becomes the intersection of the argument's original type and `NarrowedType`.

3.

Should the return value be `False`, the type of its argument is narrowed so that `NarrowedType` is excluded.

By way of illustration:

```python
from typing import assert_type, final, TypeIs

class Parent: pass
class Child(Parent): pass
@final
class Unrelated: pass

def is_parent(val: object) -> TypeIs[Parent]:
    return isinstance(val, Parent)

def run(arg: Child | Unrelated):
    if is_parent(arg):
        # Type of ``arg`` is narrowed to the intersection
        # of ``Parent`` and ``Child``, which is equivalent to
        # ``Child``.
        assert_type(arg, Child)
    else:
        # Type of ``arg`` is narrowed to exclude ``Parent``,
        # so only ``Unrelated`` is left.
        assert_type(arg, Unrelated)

```

The type placed inside `TypeIs` has to agree with the type of the function's argument; should they conflict, static type checkers will flag an error. A `TypeIs` function that is written incorrectly may produce unsound results within the type system, so it falls to the user to author these functions in a type-safe way.

When a `TypeIs` function happens to be a class or instance method, the type given in `TypeIs` corresponds to the type of the second parameter (the one following `cls` or `self`).

Put briefly, the shape `def foo(arg: TypeA) -> TypeIs[TypeB]: ...` indicates that whenever `foo(arg)` returns `True`, `arg` is an instance of `TypeB`, and whenever it returns `False`, it is not an instance of `TypeB`.

Type variables are supported by `TypeIs` as well. Further details appear in [**PEP 742**](https://peps.python.org/pep-0742/) (Narrowing types with `TypeIs`).

Added in version 3.13.

[Subject index](INDEX.md) · [Previous](typing-annotated.md) · [Continue](typing-typeguard.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Special forms](typing-union-class.md)
