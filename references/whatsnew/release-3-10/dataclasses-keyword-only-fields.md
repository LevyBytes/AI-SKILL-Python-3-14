# What's New In Python 3.10 / dataclasses / Keyword-only fields

#### Keyword-only fields

The generated __init__ method can now have keyword-only fields, which dataclasses supports. Several approaches exist for marking fields as keyword-only.

One option declares that the whole set of fields is keyword-only:

```python
from dataclasses import dataclass

@dataclass(kw_only=True)
class Birthday:
    name: str
    birthday: datetime.date

```

Within the generated __init__ method, both `name` and `birthday` show up as keyword-only parameters.

Alternatively, keyword-only can be set field by field:

```python
from dataclasses import dataclass, field

@dataclass
class Birthday:
    name: str
    birthday: datetime.date = field(kw_only=True)

```

In this case `birthday` alone is keyword-only. When you apply `kw_only` to individual fields, keep in mind that fields get re-ordered, since keyword-only fields have to come after the ones that are not keyword-only. The complete dataclasses documentation spells out the specifics.

A further choice marks every field that comes after a KW_ONLY marker as keyword-only. Odds are this will end up being the usage you reach for most:

```python
from dataclasses import dataclass, KW_ONLY

@dataclass
class Point:
    x: float
    y: float
    _: KW_ONLY
    z: float = 0.0
    t: float = 0.0

```

In this case, `z` and `t` count as keyword-only parameters, but `x` and `y` do not. (Contributed by Eric V. Smith in [bpo-43532](https://bugs.python.org/issue?@action=redirect&bpo=43532).)

[Subject index](INDEX.md) · [Previous source section](dataclasses-slots.md) · [Next source section](distutils.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](dataclasses-slots.md)
