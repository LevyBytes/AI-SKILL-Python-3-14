# re: `re.split()`, `re.findall()`, `re.finditer()`

re.split(*pattern*, *string*, *maxsplit=0*, *flags=0*)

Break *string* apart wherever *pattern* occurs. When capturing parentheses appear in *pattern*, the text of every group in the pattern is folded into the resulting list as well. With a nonzero *maxsplit*, no more than *maxsplit* splits take place, and whatever remains of the string becomes the list's last element.

```python
>>> re.split(r'\W+', 'Words, words, words.')
['Words', 'words', 'words', '']
>>> re.split(r'(\W+)', 'Words, words, words.')
['Words', ', ', 'words', ', ', 'words', '.', '']
>>> re.split(r'\W+', 'Words, words, words.', maxsplit=1)
['Words', 'words, words.']
>>> re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
['0', '3', '9']

```

When the separator contains capturing groups and matches right at the string's start, the result opens with an empty string. An empty string likewise closes the result when the separator matches at the string's end:

```python
>>> re.split(r'(\W+)', '...words, words...')
['', '...', 'words', ', ', 'words', '...', '']

```

In this manner, the separator's components consistently land at identical relative positions in the result list.

Two empty matches cannot sit side by side, though an empty match may follow right on the heels of a non-empty one.

```pycon
>>> re.split(r'\b', 'Words, words, words.')
['', 'Words', ', ', 'words', ', ', 'words', '.']
>>> re.split(r'\W*', '...words...')
['', '', 'w', 'o', 'r', 'd', 's', '', '']
>>> re.split(r'(\W*)', '...words...')
['', '...', '', '', 'w', '', 'o', '', 'r', '', 'd', '', 's', '...', '', '', '']

```

You can adjust how the expression behaves by passing a *flags* value. Acceptable values are any of the flag variables, joined together with bitwise OR (the `|` operator).

Changed in version 3.1: introduced the optional flags argument.

Changed in version 3.7: gained the ability to split on a pattern capable of matching an empty string.

Deprecated since version 3.13: handing *maxsplit* and *flags* over as positional arguments is now deprecated. Upcoming Python releases will make them [keyword-only parameters](https://docs.python.org/3.14/glossary.html#keyword-only-parameter).

 re.findall(*pattern*, *string*, *flags=0*)

Give back every non-overlapping match of *pattern* inside *string*, as a list whose elements are strings or tuples. Scanning of *string* runs left-to-right, with matches handed back in encounter order. Empty matches make it into the result too.

What comes back hinges on how many capturing groups the pattern holds. With no groups, you get a list of strings that matched the entire pattern. With precisely one group, you get a list of strings matching that single group. When several groups exist, you get a list of tuples whose strings matched the groups. The shape of the result is untouched by non-capturing groups.

```python
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
[('width', '20'), ('height', '10')]

```

You can adjust how the expression behaves by passing a *flags* value. Acceptable values are any of the flag variables, joined together with bitwise OR (the `|` operator).

Changed in version 3.7: a non-empty match may now begin directly following an earlier empty one.

 re.finditer(*pattern*, *string*, *flags=0*)

Give back an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator) that yields `Match` objects for every non-overlapping match of the RE *pattern* within *string*. Scanning of *string* runs left-to-right, with matches handed back in encounter order. Empty matches make it into the result too.

You can adjust how the expression behaves by passing a *flags* value. Acceptable values are any of the flag variables, joined together with bitwise OR (the `|` operator).

Changed in version 3.7: a non-empty match may now begin directly following an earlier empty one.

[Subject index](INDEX.md) · [Previous](re-compile-to-re-fullmatch.md) · [Continue](re-sub-to-re-subn.md) · [Owning module, declaration or section: re](re-regular-expression-operations.md) · [Owning module, declaration or section: Functions](re-compile-to-re-fullmatch.md)
