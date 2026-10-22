# typing: `typing.ParamSpecArgs`, `typing.ParamSpecKwargs`

*class *typing.ParamSpecArgs

 *class *typing.ParamSpecKwargs

The arguments and keyword-arguments attributes belonging to a `ParamSpec`. A `ParamSpec`'s `P.args` attribute is an instance of `ParamSpecArgs`, while `P.kwargs` is an instance of `ParamSpecKwargs`. They exist for runtime introspection and carry no special meaning for static type checkers.

Invoking `get_origin()` on either object hands back the original `ParamSpec`:

```pycon
>>> from typing import ParamSpec, get_origin
>>> P = ParamSpec("P")
>>> get_origin(P.args) is P
True
>>> get_origin(P.kwargs) is P
True

```

Added in version 3.10.

[Subject index](INDEX.md) · [Previous](parameter-specification-default-evaluation.md) · [Continue](typing-typealiastype-class.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Building generic types and type aliases](typing-generic-class.md)
