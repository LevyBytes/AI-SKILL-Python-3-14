# typing - Functions and decorators - Contract: Type checkers recognize the following optional parameters on field specifiers:

Type checkers recognize the following optional parameters on field specifiers:

  **Recognised parameters for field specifiers**
| Parameter name | Description |
| --- | --- |
| `init` | Says whether the synthesized `__init__` method ought to carry the field. Left unset, `init` defaults to `True`. |
| `default` | Supplies the field's default value. |
| `default_factory` | Supplies a runtime callback yielding the field's default value. With neither `default` nor `default_factory` given, the field is taken to lack a default and a value has to be passed at the time the class is instantiated. |
| `factory` | An alias for the `default_factory` parameter on field specifiers. |
| `kw_only` | Says whether the field ought to be flagged as keyword-only. Set to `True`, the field becomes keyword-only; set to `False`, it does not. Left unset, the `kw_only` value from the object decorated with `dataclass_transform` applies, and failing that the `kw_only_default` value on `dataclass_transform` applies. |
| `alias` | Supplies a substitute name for the field. That substitute name appears in the synthesized `__init__` method. |

At runtime the decorator stashes its arguments in the `__dataclass_transform__` attribute on the object it decorates. Beyond that it produces no runtime effect.

See [**PEP 681**](https://peps.python.org/pep-0681/) for more details.

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](functions-and-decorators-signature-and-initial-contract.md) · [Continue](typing-get-overloads-to-typing-clear-overloads.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Functions and decorators](typing-cast-to-typing-assert-never.md) · [Owning module, declaration or section: @typing.dataclass_transform](functions-and-decorators-signature-and-initial-contract.md)
