# typing: `typing.NewType`

*class *typing.NewType(*name*, *tp*)

Helper class to create low-overhead distinct types.

To a type checker, a `NewType` counts as its own separate type. Yet at runtime, invoking a `NewType` simply returns the supplied argument untouched.

Usage:

```python
UserId = NewType('UserId', int)  # Declare the NewType "UserId"
first_user = UserId(1)  # "UserId" returns the argument unchanged at runtime

```

 __module__

The name of the module where the new type was defined.

 __name__

The new type's name.

 __supertype__

The underlying type on which the new type rests.

Added in version 3.5.2.

Changed in version 3.10: `NewType` became a class rather than a function.

[Subject index](INDEX.md) · [Previous](typing-namedtuple-class.md) · [Continue](typing-protocol-class.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Other special directives](type-construction-directives.md)
