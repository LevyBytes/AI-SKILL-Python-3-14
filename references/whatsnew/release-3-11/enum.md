# What's New In Python 3.11 / enum — enum, re, types

### enum

- `EnumMeta` was renamed to [`EnumType`](https://docs.python.org/3.14/library/enum.html#enum.EnumType) (`EnumMeta` stays available as an alias).

- [`StrEnum`](https://docs.python.org/3.14/library/enum.html#enum.StrEnum) was added; its members work as strings -- and indeed have to be strings.

- [`ReprEnum`](https://docs.python.org/3.14/library/enum.html#enum.ReprEnum) was added; it touches only the [`__repr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__repr__) of members, while [`__str__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__str__) and [`__format__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__format__) (as called by [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str), [`format()`](https://docs.python.org/3.14/library/functions.html#format) and [f-string](https://docs.python.org/3.14/glossary.html#term-f-string)s) keep yielding their literal values instead of names.

- [`Enum.__format__()`](https://docs.python.org/3.14/library/enum.html#enum.Enum.__format__) (the fallback used by [`format()`](https://docs.python.org/3.14/library/functions.html#format), [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) and [f-string](https://docs.python.org/3.14/glossary.html#term-f-string)s) was changed so its output always lines up with [`Enum.__str__()`](https://docs.python.org/3.14/library/enum.html#enum.Enum.__str__): enums descending from [`ReprEnum`](https://docs.python.org/3.14/library/enum.html#enum.ReprEnum) give back the member's value, whereas every other enum gives the enum plus member name (for instance `Color.RED`).

- A fresh *boundary* class parameter was added to [`Flag`](https://docs.python.org/3.14/library/enum.html#enum.Flag) enums, together with the [`FlagBoundary`](https://docs.python.org/3.14/library/enum.html#enum.FlagBoundary) enum and its choices, governing the treatment of out-of-range flag values.

- The [`verify()`](https://docs.python.org/3.14/library/enum.html#enum.verify) enum decorator landed alongside the [`EnumCheck`](https://docs.python.org/3.14/library/enum.html#enum.EnumCheck) enum and its choices, letting you test enum classes for a handful of named constraints.

- The [`member()`](https://docs.python.org/3.14/library/enum.html#enum.member) and [`nonmember()`](https://docs.python.org/3.14/library/enum.html#enum.nonmember) decorators were added, guaranteeing that the wrapped object does or does not become an enum member.

- The [`property()`](https://docs.python.org/3.14/library/enum.html#enum.property) decorator was added; it behaves like [`property()`](https://docs.python.org/3.14/library/functions.html#property) but is tailored to enums. Prefer it over [`types.DynamicClassAttribute()`](https://docs.python.org/3.14/library/types.html#types.DynamicClassAttribute).

- The [`global_enum()`](https://docs.python.org/3.14/library/enum.html#enum.global_enum) enum decorator was added; it tweaks [`__repr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__repr__) and [`__str__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__str__) so members read as belonging to their module instead of the enum class. As an illustration, `'re.ASCII'` shows up for the [`ASCII`](https://docs.python.org/3.14/library/re.html#re.ASCII) member of [`re.RegexFlag`](https://docs.python.org/3.14/library/re.html#re.RegexFlag) in place of `'RegexFlag.ASCII'`.

- [`Flag`](https://docs.python.org/3.14/library/enum.html#enum.Flag) was enhanced to handle [`len()`](https://docs.python.org/3.14/library/functions.html#len), iteration, and [`in`](https://docs.python.org/3.14/reference/expressions.html#in)/[`not in`](https://docs.python.org/3.14/reference/expressions.html#not-in) across its members. To give one case, this expression now holds: `len(AFlag(3)) == 2 and list(AFlag(3)) == (AFlag.ONE, AFlag.TWO)`

- [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum) and [`Flag`](https://docs.python.org/3.14/library/enum.html#enum.Flag) were changed so members get established prior to the [`__init_subclass__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init_subclass__) call; [`dir()`](https://docs.python.org/3.14/library/functions.html#dir) now also surfaces methods and similar attributes drawn from mixed-in data types.

- [`Flag`](https://docs.python.org/3.14/library/enum.html#enum.Flag) was changed to treat only primary values (powers of two) as canonical, while composite values (`3`, `6`, `10`, etc.) count as aliases; flags that are inverted get folded into their positive counterpart.

[Subject index](INDEX.md) · [Previous source section](datetime.md) · [Next source section](fcntl.md) · [Release/subject declaration](summary-release-highlights.md)
