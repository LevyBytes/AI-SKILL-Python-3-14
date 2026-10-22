# typing: `typing.Pattern`, `typing.Match`

#### Aliases to other concrete types

 *class *typing.Pattern

 *class *typing.Match

Deprecated aliases that map to the values returned by [`re.compile()`](https://docs.python.org/3.14/library/re.html#re.compile) and [`re.match()`](https://docs.python.org/3.14/library/re.html#re.match).

Both these types (along with their related functions) are generic over `AnyStr`. You can specialise `Pattern` as `Pattern[str]` or `Pattern[bytes]`, and likewise `Match` as `Match[str]` or `Match[bytes]`.

Deprecated since version 3.9: Classes `Pattern` and `Match` from [`re`](https://docs.python.org/3.14/library/re.html#module-re) now support `[]`. See [**PEP 585**](https://peps.python.org/pep-0585/) and [Generic Alias Type](https://docs.python.org/3.14/library/stdtypes.html#types-genericalias).

[Subject index](INDEX.md) · [Previous](typing-deque-class.md) · [Continue](typing-text-class.md) · [Owning module, declaration or section: typing](typing-support-for-type-hints.md)
