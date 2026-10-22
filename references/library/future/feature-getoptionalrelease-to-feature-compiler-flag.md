# __future__: `_Feature.getOptionalRelease()`, `_Feature.getMandatoryRelease()`, `_Feature.compiler_flag`

_Feature.getOptionalRelease()

*OptionalRelease* captures the earliest release that accepted the feature.

 _Feature.getMandatoryRelease()

When a *MandatoryRelease* still lies ahead, *MandatoryRelease* forecasts the release at which the feature is slated to join the language.

Otherwise *MandatoryRelease* notes the release where the feature entered the language; from that release forward, modules can rely on the feature without a future statement, though such imports remain permitted.

*MandatoryRelease* can additionally hold `None`, signaling that a planned feature was abandoned or that its fate is still undecided.

 _Feature.compiler_flag

*CompilerFlag* is the (bitfield) flag meant to be handed as the fourth argument to the built-in function [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) so the feature works in dynamically compiled code. That flag lives in the `_Feature.compiler_flag` attribute on `_Feature` instances.

See also

[Future statements](https://docs.python.org/3.14/reference/simple_stmts.html#future)

The way the compiler handles future imports.

[**PEP 236**](https://peps.python.org/pep-0236/) - Back to the __future__

Where the __future__ mechanism was first proposed.

[Subject index](INDEX.md) · [Previous](future-feature-class.md) · [Continue](../main/main-top-level-code-environment.md) · [Owning module, declaration or section: __future__](future-future-statement-definitions.md) · [Owning module, declaration or section: __future__._Feature](future-feature-class.md) · [Owning module, declaration or section: Module Contents](future-feature-class.md)
