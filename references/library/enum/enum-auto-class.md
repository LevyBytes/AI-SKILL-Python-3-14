# enum: `enum.auto`, `enum.property`, `enum.unique`, `enum.verify`, `enum.member`, `enum.nonmember`, `enum.global_enum`

### Utilities and decorators

 *class *enum.auto

Wherever you would write a value, *auto* may stand in instead. Once it appears, the *Enum* machinery invokes that `Enum`’s `_generate_next_value_()` to obtain a fitting value. Under `Enum` and `IntEnum` the fitting value is one more than the preceding value; under `Flag` and `IntFlag` it is the smallest power-of-two exceeding the largest value so far; under `StrEnum` it is the member’s name lowercased. Stay cautious whenever *auto()* is interleaved with values you spell out by hand.

Resolution of *auto* instances happens solely at the outermost level of an assignment, whether standing alone or inside a tuple:

- `FIRST = auto()` succeeds (auto() becomes `1`);

- `SECOND = auto(), -2` succeeds (auto turns into `2`, hence `2, -2` builds the `SECOND` enum member;

- `THREE = [auto(), -3]` does *not* succeed (`[<auto instance>, -3]` is what builds the `THREE` enum member)

Changed in version 3.11.1: Earlier releases required `auto()` to stand alone on the assignment line for it to behave correctly.

To tailor the values that *auto* produces, override `_generate_next_value_`.

Note

as of 3.13 the stock `_generate_next_value_` consistently yields the top member value plus 1, and it errors out should any member hold an incompatible type.

 @enum.property

Comparable to the built-in *property*, this decorator is tailored to enumerations. Thanks to it, member attributes are free to share names with the members themselves.

Note

the *property* and the member have to live in distinct classes; the *value* and *name* attributes, say, belong to the *Enum* class, while *Enum* subclasses are then able to declare members called `value` and `name`.

Added in version 3.11.

 @enum.unique

A [`class`](https://docs.python.org/3.14/reference/compound_stmts.html#class) decorator made just for enumerations. It scans an enumeration’s `__members__`, collecting whatever aliases turn up; should any surface, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) carrying the specifics is raised:

```python
>>> from enum import Enum, unique
>>> @unique
... class Mistake(Enum):
...     ONE = 1
...     TWO = 2
...     THREE = 3
...     FOUR = 3
...
Traceback (most recent call last):
...
ValueError: duplicate values found in <enum 'Mistake'>: FOUR -> THREE

```

 @enum.verify

A [`class`](https://docs.python.org/3.14/reference/compound_stmts.html#class) decorator aimed at enumerations. You pick members of `EnumCheck` to declare which constraints get verified against the decorated enumeration.

Added in version 3.11.

 @enum.member

A decorator meant for enums: whatever it wraps is turned into a member.

Added in version 3.11.

 @enum.nonmember

A decorator meant for enums: whatever it wraps is kept from becoming a member.

Added in version 3.11.

 @enum.global_enum

A decorator that adjusts an enum’s [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) and [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) so members read as attached to the module rather than the class. Reserve it for cases where the enum members are published into the module’s global namespace (consult [`re.RegexFlag`](https://docs.python.org/3.14/library/re.html#re.RegexFlag) for one illustration).

Added in version 3.11.

[Subject index](INDEX.md) · [Previous](supported-sunder-names.md) · [Continue](enum-show-flag-values-to-enum-bin.md) · [Owning module, declaration or section: enum](enum-support-for-enumerations.md)
