# re: `re.Pattern`

### Regular Expression Objects

 *class *re.Pattern

Compiled regular expression object returned by `re.compile()`.

Patterns are [generic](https://docs.python.org/3.14/library/typing.html#generics) over the type of string they handle ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes)).

Changed in version 3.9: `re.Pattern` accepts `[]` for marking a Unicode (str) or bytes pattern. Consult [Generic Alias Type](https://docs.python.org/3.14/library/stdtypes.html#types-genericalias).

[Subject index](INDEX.md) · [Previous](re-patternerror.md) · [Continue](pattern-search-to-pattern-groupindex.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md)
