# String bounds, immutability, length and further operations

Reaching for an index that overshoots produces an error:

```python
>>> word[42]  # the word only has 6 characters
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range

```

Slice indexes that fall out of range, by contrast, are tolerated cleanly during slicing:

```python
>>> word[4:42]
'on'
>>> word[42:]
''

```

Strings in Python are unchangeable - they are [immutable](https://docs.python.org/3.14/glossary.html#term-immutable). Hence, writing to an indexed slot within a string brings about an error:

```python
>>> word[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> word[2:] = 'py'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

```

Whenever a different string is what you require, build a fresh one:

```python
>>> 'J' + word[1:]
'Jython'
>>> word[:2] + 'py'
'Pypy'

```

Calling the built-in [`len()`](https://docs.python.org/3.14/library/functions.html#len) function gives back a string's length:

```python
>>> s = 'supercalifragilisticexpialidocious'
>>> len(s)
34

```

See also

[Text Sequence Type - str](https://docs.python.org/3.14/library/stdtypes.html#textseq)

Strings count as *sequence types*, and they support the shared operations that such types provide.

[String Methods](https://docs.python.org/3.14/library/stdtypes.html#string-methods)

Strings come with a wide array of methods covering basic transformations and searching.

[f-strings](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings)

String literals carrying embedded expressions.

[Format string syntax](https://docs.python.org/3.14/library/string.html#formatstrings)

Details on formatting strings with [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format).

[printf-style String Formatting](https://docs.python.org/3.14/library/stdtypes.html#old-string-formatting)

The legacy formatting behavior triggered when a string sits as the left operand of the `%` operator gets fuller treatment here.

[Subject index](INDEX.md) · [Previous source section](string-indexing-slicing-defaults-and-slice-boundaries.md) · [Following source section](list-indexing-concatenation-mutation-and-append.md) · [Related tutorial example and explanation](string-quotation-escapes-raw-strings-and-multiline-literals.md) · [Related tutorial example and explanation](string-repetition-and-literal-versus-variable-concatenation.md) · [Related tutorial example and explanation](string-indexing-slicing-defaults-and-slice-boundaries.md) · [word string definition and indexing](string-indexing-slicing-defaults-and-slice-boundaries.md)
