# typing: `typing.cast()`, `typing.assert_type()`, `typing.assert_never()`

### Functions and decorators

 typing.cast(*typ*, *val*)

Cast a value to a type.

The value comes back untouched. From the type checker's perspective this declares that the returned value carries the named type, yet at runtime no verification happens on purpose (the goal is maximum speed).

 typing.assert_type(*val*, *typ*, */*)

Request that a static type checker verify the inferred type of *val* is *typ*.

It performs no work at runtime: regardless of what the argument's real type turns out to be, it simply hands back the first argument as-is, performing neither checks nor side effects.

Upon seeing an `assert_type()` call, a static type checker reports an error whenever the value's type differs from the one declared:

```python
def greet(name: str) -> None:
    assert_type(name, str)  # OK, inferred type of `name` is `str`
    assert_type(name, int)  # type checker error

```

The helper comes in handy for confirming that what the type checker believes about a script matches what the developer meant:

```python
def complex_function(arg: object):
    # Do some complex type-narrowing logic,
    # after which we hope the inferred type will be `int`
    ...
    # Test whether the type checker correctly understands our function
    assert_type(arg, int)

```

Added in version 3.11.

 typing.assert_never(*arg*, */*)

Request that a static type checker verify a given line is never reachable.

Example:

```python
def int_or_str(arg: int | str) -> None:
    match arg:
        case int():
            print("It's an int")
        case str():
            print("It's a str")
        case _ as unreachable:
            assert_never(unreachable)

```

In this snippet, the annotations let the type checker deduce that the final case is impossible to reach, since `arg` must be either an [`int`](https://docs.python.org/3.14/library/functions.html#int) or a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), and the preceding cases already handle both.

Should a type checker decide that an `assert_never()` call can actually be reached, it reports an error. As an illustration, were the annotation on `arg` written as `int | str | float` instead, the type checker would flag that `unreachable` carries the type [`float`](https://docs.python.org/3.14/library/functions.html#float). For an `assert_never` call to clear type checking, the argument supplied must have an inferred type of exactly the bottom type, `Never`, with nothing else permitted.

When invoked at runtime, it raises an exception.

See also

[Unreachable Code and Exhaustiveness Checking](https://typing.python.org/en/latest/guides/unreachable.html) has more information about exhaustiveness checking with static typing.

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](typing-io-typing-textio-and-typing-binaryio-interfaces.md) · [Continue](typing-reveal-type.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md)
