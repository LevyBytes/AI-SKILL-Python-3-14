# typing — Deprecated aliases

### Deprecated aliases

A number of deprecated aliases pointing at already-existing standard library classes are declared by this module. They were first added to the `typing` module so that these generic classes could be parameterized with `[]`. That purpose disappeared in Python 3.9, though, once the matching pre-existing classes gained their own `[]` support (see [**PEP 585**](https://peps.python.org/pep-0585/)).

As of Python 3.9 these duplicate types carry a deprecated status. Even so, although removing the aliases remains a possibility down the road, no such removal is planned right now. Consequently the interpreter raises no deprecation warnings for them at present.

Should a decision ever be made to drop these deprecated aliases, the interpreter will emit a deprecation warning across no fewer than two releases ahead of the actual removal. Until Python 3.14 at the earliest, the aliases are promised to stay in the `typing` module free of any deprecation warnings.

When a program under inspection declares a minimum Python version of 3.9 or later, type checkers are urged to mark any use of the deprecated types.

[Subject index](INDEX.md) · [Previous](constant.md) · [Continue](typing-dict-class.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md)
