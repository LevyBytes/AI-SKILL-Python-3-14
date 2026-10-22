# typing: `typing.ClassVar`, `typing.Final`, `typing.Required`, `typing.NotRequired`

typing.ClassVar

Special type construct to mark class variables.

As brought in by [**PEP 526**](https://peps.python.org/pep-0526/), wrapping a variable annotation in ClassVar signals that the attribute in question is meant to serve as a class variable and ought not be assigned on instances of that class. Usage:

```python
class Starship:
    stats: ClassVar[dict[str, int]] = {} # class variable
    damage: int = 10                     # instance variable

```

`ClassVar` accepts only types and cannot be further subscribed.

`ClassVar` is no class on its own, so it works with neither [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) nor [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass). `ClassVar` leaves Python's runtime behavior untouched, yet static type checkers can make use of it. As an illustration, a type checker may report the snippet below as an error:

```python
enterprise_d = Starship(3000)
enterprise_d.stats = {} # Error, setting class variable on instance
Starship.stats = {}     # This is OK

```

Added in version 3.5.3.

Changed in version 3.13: nesting `ClassVar` within `Final` is now allowed, and the reverse holds too.

 typing.Final

Special typing construct to indicate final names to type checkers.

No scope may reassign a final name. A final name set inside a class scope cannot be overridden by any subclass.

For example:

```python
MAX_SIZE: Final = 9000
MAX_SIZE += 1  # Error reported by type checker

class Connection:
    TIMEOUT: Final[int] = 10

class FastConnector(Connection):
    TIMEOUT = 1  # Error reported by type checker

```

None of these properties are enforced while the program runs. See [**PEP 591**](https://peps.python.org/pep-0591/) for more details.

Added in version 3.8.

Changed in version 3.13: nesting `Final` within `ClassVar` is now allowed, and the reverse holds too.

 typing.Required

Special typing construct to mark a `TypedDict` key as required.

Its primary value lies with `total=False` TypedDicts. See `TypedDict` and [**PEP 655**](https://peps.python.org/pep-0655/) for more details.

Added in version 3.11.

 typing.NotRequired

Special typing construct to mark a `TypedDict` key as potentially missing.

See `TypedDict` and [**PEP 655**](https://peps.python.org/pep-0655/) for more details.

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](typing-literal.md) · [Continue](typing-readonly-to-typing-annotated.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Special forms](typing-union-class.md)
