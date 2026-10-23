# typing - User-defined generic types - Code example: from typing import ParamSpec, Generic

```python
from typing import ParamSpec, Generic

P = ParamSpec('P')

class Z(Generic[P]):
    ...

```

`TypeVar` and `ParamSpec` part ways in another respect too: a generic that has a single parameter specification variable will take parameter lists written either as `X[[Type1, Type2, ...]]` or as `X[Type1, Type2, ...]`, the second being allowed on aesthetic grounds. The shorter form is converted internally into the longer one, making the following equivalent:

```python
>>> class X[**P]: ...
...
>>> X[int, str]
__main__.X[[int, str]]
>>> X[[int, str]]
__main__.X[[int, str]]

```

Be aware that, in certain cases, generics built on `ParamSpec` may end up with incorrect `__parameters__` after substitution, since their main purpose is static type checking.

Changed in version 3.10: Parameter expressions may now parameterize `Generic`. Refer to `ParamSpec` together with [**PEP 612**](https://peps.python.org/pep-0612/) for fuller detail.

ABCs can be base classes of a user-defined generic class without triggering a metaclass conflict. Generic metaclasses, however, are unsupported. Results of parameterizing generics are cached, and the majority of types in the `typing` module are [hashable](https://docs.python.org/3.14/glossary.html#term-hashable) along with being comparable for equality.

[Subject index](INDEX.md) · [Previous](generic-class-inheritance-contract.md) · [Continue](the-any-type.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: User-defined generic types](user-defined-generics-overview.md)
