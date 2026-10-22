# typing: `typing.Text`

*class *typing.Text

Deprecated alias for [`str`](https://docs.python.org/3.14/library/stdtypes.html#str).

The role of `Text` is to give Python 2 code a forward-compatible route: under Python 2, `Text` aliases `unicode`.

Reach for `Text` when you want to signal that a value has to hold a unicode string in a way that works across both Python 2 and Python 3:

```python
def add_unicode_checkmark(text: Text) -> Text:
    return text + u' \u2713'

```

Added in version 3.5.2.

Deprecated since version 3.11: With Python 2 support gone, and with most type checkers having dropped type checking of Python 2 code as well, there is no current plan to remove this alias, yet users are advised to choose [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) over `Text`.

[Subject index](INDEX.md) · [Previous](typing-pattern-class-to-typing-match-class.md) · [Continue](typing-abstractset-class.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md) · [Owning module, declaration or section: Aliases to other concrete types](typing-pattern-class-to-typing-match-class.md)
