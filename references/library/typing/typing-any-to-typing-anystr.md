# typing: `typing.Any`, `typing.AnyStr`

### Special typing primitives

#### Special types

The following may serve as types within annotations. Subscription via `[]` is unsupported for them.

 typing.Any

Special type indicating an unconstrained type.

- Every type is assignable to `Any`.

- `Any` is assignable to every type.

Changed in version 3.11: `Any` is now permitted as a base class. That comes in handy for dodging type checker errors on classes that are highly dynamic or able to duck type anywhere.

 typing.AnyStr

A constrained type variable.

Definition:

```python
AnyStr = TypeVar('AnyStr', str, bytes)

```

`AnyStr` is intended for functions that can take either [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) arguments while forbidding the two from being combined.

For example:

```python
def concat(a: AnyStr, b: AnyStr) -> AnyStr:
    return a + b

concat("foo", "bar")    # OK, output has type 'str'
concat(b"foo", b"bar")  # OK, output has type 'bytes'
concat("foo", b"bar")   # Error, cannot mix str and bytes

```

Be aware that, the name notwithstanding, `AnyStr` bears no relation to the `Any` type, and it does not signify "any string" either. Specifically, `AnyStr` and `str | bytes` differ from one another and serve different purposes:

```python
# Invalid use of AnyStr:
# The type variable is used only once in the function signature,
# so cannot be "solved" by the type checker
def greet_bad(cond: bool) -> AnyStr:
    return "hi there!" if cond else b"greetings!"

# The better way of annotating this function:
def greet_proper(cond: bool) -> str | bytes:
    return "hi there!" if cond else b"greetings!"

```

Deprecated since version 3.13, will be removed in version 3.18: Superseded by the new [type parameter syntax](https://docs.python.org/3.14/reference/compound_stmts.html#type-params). Rather than importing `AnyStr`, write `class A[T: (str, bytes)]: ...`. See [**PEP 695**](https://peps.python.org/pep-0695/) for more details.

Come Python 3.16, `typing.__all__` will drop `AnyStr`, and accessing it or importing it out of `typing` will trigger deprecation warnings while the program runs. Python 3.18 will drop `AnyStr` from `typing` altogether.

[Subject index](INDEX.md) · [Continue](typing-literalstring-to-typing-noreturn.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md)
