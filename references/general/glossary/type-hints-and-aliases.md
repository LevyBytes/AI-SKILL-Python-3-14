# Type hints and aliases

Open when checking Python definitions for type hints and aliases.

## type hint

An annotation stating which type is anticipated for a variable, for a class attribute, or for the parameter or return value of a function.

Type hints are optional and Python does not enforce them, yet they prove useful to static type checkers. They can additionally help IDEs with code completion and refactoring.

Type hints on global variables, class attributes, and functions - though not on local variables - can be reached using [`typing.get_type_hints()`](https://docs.python.org/3.14/library/typing.html#typing.get_type_hints).

See [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) and [**PEP 484**](https://peps.python.org/pep-0484/), which describe this functionality.

## type alias

A synonym for a type, brought about by assigning the type to an identifier.

Type aliases come in handy for tidying up type hints. As an example:

```python
def remove_gray_shades(
        colors: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    pass

```

could be rendered more legible like so:

```python
Color = tuple[int, int, int]

def remove_gray_shades(colors: list[Color]) -> list[Color]:
    pass

```

See [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) and [**PEP 484**](https://peps.python.org/pep-0484/), which describe this functionality.

## generic type

A type admitting parameterization; typically a [container class](https://docs.python.org/3.14/reference/datamodel.html#sequence-types) like [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) or [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict). It serves type hints and annotations.

Further particulars appear in [generic alias types](https://docs.python.org/3.14/library/stdtypes.html#types-genericalias), [**PEP 483**](https://peps.python.org/pep-0483/), [**PEP 484**](https://peps.python.org/pep-0484/), [**PEP 585**](https://peps.python.org/pep-0585/), and the [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module.

## static type checker

An outside tool that parses Python code and examines it, on the lookout for problems like wrong types. See also type hints and the [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module.

[Glossary context index](INDEX.md).
