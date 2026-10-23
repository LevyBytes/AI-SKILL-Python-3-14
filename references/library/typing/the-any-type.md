# typing - The `Any` type

### The `Any` type

`Any` is a type of a special sort. A static type checker counts every type as assignable to `Any`, and `Any` as assignable to every type in turn.

So you may carry out any operation or method call on a value typed `Any` and bind the outcome to any variable whatsoever:

```python
from typing import Any

a: Any = None
a = []          # OK
a = 2           # OK

s: str = ''
s = a           # OK

def foo(item: Any) -> int:
    # Passes type checking; 'item' could be any type,
    # and that type might have a 'bar' method
    item.bar()
    ...

```

Observe that the type checker performs no validation when a value typed as `Any` is assigned into a narrower type. As an illustration, the static checker raised no complaint about assigning `a` into `s`, despite `s` being annotated as [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) yet holding an [`int`](https://docs.python.org/3.14/library/functions.html#int) once the program actually runs!

On top of that, any function lacking a declared return type or parameter annotations will silently fall back to `Any`:

```python
def legacy_parser(text):
    ...
    return data

# A static type checker will treat the above
# as having the same signature as:
def legacy_parser(text: Any) -> Any:
    ...
    return data

```

Because of this, `Any` serves as an *escape hatch* in situations where you have to blend dynamically typed and statically typed portions of code together.

Compare how `Any` acts against how [`object`](https://docs.python.org/3.14/library/functions.html#object) acts. Like `Any`, every type counts as a subtype of `object`. The difference is that, with `Any`, the opposite also holds — whereas `object` is *not* a subtype of all other types.

So when a value carries the type [`object`](https://docs.python.org/3.14/library/functions.html#object), a type checker turns down nearly every operation performed on it, and handing it to a variable (or returning it) where a narrower type is expected counts as a type error. As an example:

```python
def hash_a(item: object) -> int:
    # Fails type checking; an object does not have a 'magic' method.
    item.magic()
    ...

def hash_b(item: Any) -> int:
    # Passes type checking
    item.magic()
    ...

# Passes type checking, since ints and strs are subclasses of object
hash_a(42)
hash_a("foo")

# Passes type checking, since Any is assignable to all types
hash_b(42)
hash_b("foo")

```

Reach for [`object`](https://docs.python.org/3.14/library/functions.html#object) when you want to express that a value may hold any type while staying type-safe. Reach for `Any` when you want to express that a value is dynamically typed.

[Subject index](INDEX.md) · [Previous](paramspec-generic-class-example.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Continue](nominal-vs-structural-subtyping.md)
