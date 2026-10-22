# Python 3.9.0 alpha 1 / build / stdtypes

[bpo-37760](https://bugs.python.org/issue?@action=redirect&bpo=37760): The `Tools/unicode/makeunicodedata.py` script, used to turn information drawn from the Unicode Character Database into generated code and data that the methods of [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) and the [`unicodedata`](https://docs.python.org/3.14/library/unicodedata.html#module-unicodedata) module depend on, now treats every character's data as a `dataclass` carrying named attributes instead of a length-18 list of separate fields.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
