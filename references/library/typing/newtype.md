# typing - NewType

### NewType

To mint separate types, apply the `NewType` helper:

```python
from typing import NewType

UserId = NewType('UserId', int)
some_id = UserId(524313)

```

To the static type checker, the freshly created type behaves as though it subclassed the original — a handy way to surface logic mistakes:

```python
def get_user_name(user_id: UserId) -> str:
    ...

# passes type checking
user_a = get_user_name(UserId(42351))

# fails type checking; an int is not a UserId
user_b = get_user_name(-1)

```

All `int` operations remain available on a value typed `UserId`, though each such operation yields an `int`. So a `UserId` can stand in anywhere an `int` is wanted, while you are still blocked from constructing a `UserId` through an invalid route:

```python
# 'output' is of type 'int', not 'UserId'
output = UserId(23413) + UserId(54341)

```

Bear in mind that only the static type checker imposes these checks. During execution, `Derived = NewType('Derived', Base)` produces a `Derived` callable that hands straight back whatever argument it receives. So writing `Derived(some_value)` neither builds a new class nor costs much more than an ordinary function call.

Stated exactly, at runtime `some_value is Derived(some_value)` always evaluates to true.

Subtyping `Derived` is not permitted:

```python
from typing import NewType

UserId = NewType('UserId', int)

# Fails at runtime and does not pass type checking
class AdminUserId(UserId): pass

```

That said, you can build a `NewType` on top of an already-‘derived’ `NewType`:

```python
from typing import NewType

UserId = NewType('UserId', int)

ProUserId = NewType('ProUserId', UserId)

```

and `ProUserId` will typecheck just as you would expect.

Consult [**PEP 484**](https://peps.python.org/pep-0484/) for fuller detail.

Note

Remember that adopting a type alias asserts that two types are *equivalent*. Writing `type Alias = Original` causes the static type checker to see `Alias` as *exactly equivalent* to `Original` everywhere. That comes in handy for trimming down complicated type signatures.

`NewType`, by contrast, asserts that one type is a *subtype* of another. Writing `Derived = NewType('Derived', Original)` causes the static type checker to view `Derived` as a *subclass* of `Original`, so an `Original` value is rejected anywhere a `Derived` value is required. That comes in handy for heading off logic errors at little runtime expense.

Added in version 3.5.2.

Changed in version 3.10: Where `NewType` was once a function, it became a class. Consequently, invoking `NewType` now carries a little extra runtime cost compared with an ordinary function.

Changed in version 3.11: Calling `NewType` once again performs at the speed it had under Python 3.9.

[Subject index](INDEX.md) · [Previous](type-aliases.md) · [Continue](annotating-callable-objects.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md)
