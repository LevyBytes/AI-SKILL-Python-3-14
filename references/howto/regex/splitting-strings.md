# Splitting strings

### Splitting strings

A pattern's [`split()`](https://docs.python.org/3.14/library/re.html#re.Pattern.split) method tears a string apart at each spot the RE matches and returns a list of the resulting fragments. It resembles the string [`split()`](https://docs.python.org/3.14/library/stdtypes.html#str.split) method yet affords far broader latitude over the delimiters you may split on; string `split()` can split only on whitespace or on a fixed string. As you'd anticipate, a module-level [`re.split()`](https://docs.python.org/3.14/library/re.html#re.split) function exists as well.

 .split(*string*[, *maxsplit=0*])

Break *string* apart at every match of the regular expression. Should the RE contain capturing parentheses, what those captured comes back as well within the produced list. Given a nonzero *maxsplit*, no more than that many splits get carried out.

By supplying a value for *maxsplit* you can cap how many splits get made. With *maxsplit* nonzero, no more than *maxsplit* splits happen, and what's left of the string comes back as the list's last element. In the example that follows, the delimiter is any run of non-alphanumeric characters.

```python
>>> p = re.compile(r'\W+')
>>> p.split('This is a test, short and sweet, of split().')
['This', 'is', 'a', 'test', 'short', 'and', 'sweet', 'of', 'split', '']
>>> p.split('This is a test, short and sweet, of split().', 3)
['This', 'is', 'a', 'test, short and sweet, of split().']

```

At times you care not only about the text lying between delimiters but also about what the delimiter itself was. When capturing parentheses appear in the RE, their values come back as part of the list too. Set the following calls side by side:

```python
>>> p = re.compile(r'\W+')
>>> p2 = re.compile(r'(\W+)')
>>> p.split('This... is a test.')
['This', 'is', 'a', 'test', '']
>>> p2.split('This... is a test.')
['This', '... ', 'is', ' ', 'a', ' ', 'test', '.', '']

```

The module-level [`re.split()`](https://docs.python.org/3.14/library/re.html#re.split) function takes the RE to use as its first argument but is otherwise identical.

```python
>>> re.split(r'[\W]+', 'Words, words, words.')
['Words', 'words', 'words', '']
>>> re.split(r'([\W]+)', 'Words, words, words.')
['Words', ', ', 'words', ', ', 'words', '.', '']
>>> re.split(r'[\W]+', 'Words, words, words.', 1)
['Words', 'words, words.']

```

[Subject index](INDEX.md) · [Previous source context](modifying-strings.md) · [Following source context](search-and-replace.md)
