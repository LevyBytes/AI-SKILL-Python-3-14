# What's New In Python 3.10 / enum — enum

### enum

For [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum), [`__repr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__repr__) now produces `enum_name.member_name` while [`__str__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__str__) now produces `member_name`. Where stdlib enums are exposed as module constants, their [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) reads `module_name.member_name`. (Contributed by Ethan Furman in [bpo-40066](https://bugs.python.org/issue?@action=redirect&bpo=40066).)

Add [`enum.StrEnum`](https://docs.python.org/3.14/library/enum.html#enum.StrEnum) to cover enums whose members are all strings. (Contributed by Ethan Furman in [bpo-41816](https://bugs.python.org/issue?@action=redirect&bpo=41816).)

[Subject index](INDEX.md) · [Previous source section](encodings.md) · [Next source section](fileinput.md) · [Release/subject declaration](summary-release-highlights.md)
