# 6.2.8. Dictionary displays

### 6.2.8. Dictionary displays

A dictionary display is a possibly empty run of dict items (key/value pairs) wrapped in curly braces:

```text

dict_display:       "{" [dict_item_list | dict_comprehension] "}"
dict_item_list:     dict_item ("," dict_item)* [","]
dict_item:          expression ":" expression | "**" or_expr
dict_comprehension: expression ":" expression comp_for
```

A dictionary display produces a new dictionary object.

When a comma-separated run of dict items is provided, they are evaluated left to right to set up the dictionary's entries: each key object acts as a key into the dictionary under which the matching value is stored. Therefore you may list the same key several times across the dict item list, and the value the final dictionary holds for that key is whichever one came last.

A double asterisk `**` signals *dictionary unpacking*. What it operates on has to be a [mapping](https://docs.python.org/3.14/glossary.html#term-mapping). Every item of that mapping is folded into the new dictionary. Values supplied later overwrite values already placed by earlier dict items and earlier dictionary unpackings.

Added in version 3.5: Unpacking into dictionary displays, originally proposed by [**PEP 448**](https://peps.python.org/pep-0448/).

Unlike list and set comprehensions, a dict comprehension calls for two expressions split by a colon, followed by the usual ?for? and ?if? clauses. As the comprehension executes, the key and value elements it produces are placed into the new dictionary in their order of production.

The limits on what types the key values may take appear earlier, in the section [The standard type hierarchy](https://docs.python.org/3.14/reference/datamodel.html#types). (In short, the key type needs to be [hashable](https://docs.python.org/3.14/glossary.html#term-hashable), ruling out every mutable object.) Conflicts among duplicate keys go unnoticed; for any given key value, the value kept is the last one stored (the one furthest right in the display text).

Changed in version 3.8: Before Python 3.8, the order in which a dict comprehension evaluated its key versus its value had no firm definition; CPython happened to evaluate the value ahead of the key. From 3.8 onward the key comes first, then the value, per the proposal in [**PEP 572**](https://peps.python.org/pep-0572/).

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](atoms.md) · [Previous source section](set-displays.md) · [Following source section](generator-expressions.md)
