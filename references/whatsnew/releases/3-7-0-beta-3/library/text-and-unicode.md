# Python 3.7.0 beta 3 / library / text and unicode

[bpo-33134](https://bugs.python.org/issue?@action=redirect&bpo=33134): While computing a dataclass's __hash__, rely on the lookup table to hold the function that returns the __hash__ value. That improves on looking up a string and then testing that string to decide the action.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
