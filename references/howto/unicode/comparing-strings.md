# Comparing Strings

### Comparing Strings

Unicode introduces extra complexity into string comparison, since one and the same set of characters may be represented by differing sequences of code points. As an example, a letter such as ‘ê’ may appear as the single code point U+00EA, or as U+0065 U+0302, which combines the code point for ‘e’ with a code point for ‘COMBINING CIRCUMFLEX ACCENT’. Printed out, they look identical, yet one is a string of length 1 while the other is of length 2.

For case-insensitive comparison, one option is the [`casefold()`](https://docs.python.org/3.14/library/stdtypes.html#str.casefold) string method, which transforms a string into a case-insensitive form by way of an algorithm laid out in the Unicode Standard. That algorithm handles certain characters specially, such as the German letter ‘ß’ (code point U+00DF), which turns into the pair of lowercase letters ‘ss’.

```python
>>> street = 'Gürzenichstraße'
>>> street.casefold()
'gürzenichstrasse'

```

A second option is the [`normalize()`](https://docs.python.org/3.14/library/unicodedata.html#unicodedata.normalize) function from the [`unicodedata`](https://docs.python.org/3.14/library/unicodedata.html#module-unicodedata) module, which converts strings into one of several normal forms, where letters trailed by a combining character are swapped for single characters. You can apply `normalize()` to run string comparisons that won’t wrongly flag inequality when two strings make use of combining characters in differing ways:

```python
import unicodedata

def compare_strs(s1, s2):
    def NFD(s):
        return unicodedata.normalize('NFD', s)

    return NFD(s1) == NFD(s2)

single_char = 'ê'
multiple_chars = '\N{LATIN SMALL LETTER E}\N{COMBINING CIRCUMFLEX ACCENT}'
print('length of first string=', len(single_char))
print('length of second string=', len(multiple_chars))
print(compare_strs(single_char, multiple_chars))

```

Running it gives:

```shell
$ python compare-strs.py
length of first string= 1
length of second string= 2
True

```

The first argument handed to the [`normalize()`](https://docs.python.org/3.14/library/unicodedata.html#unicodedata.normalize) function is a string naming the wanted normalization form, which may be any one of ‘NFC’, ‘NFKC’, ‘NFD’, and ‘NFKD’.

The Unicode Standard further lays out how to carry out caseless comparisons:

```python
import unicodedata

def compare_caseless(s1, s2):
    def NFD(s):
        return unicodedata.normalize('NFD', s)

    return NFD(NFD(s1).casefold()) == NFD(NFD(s2).casefold())

# Example usage
single_char = 'ê'
multiple_chars = '\N{LATIN CAPITAL LETTER E}\N{COMBINING CIRCUMFLEX ACCENT}'

print(compare_caseless(single_char, multiple_chars))

```

This prints `True`. (Why call `NFD()` two times? Because a handful of characters cause [`casefold()`](https://docs.python.org/3.14/library/stdtypes.html#str.casefold) to give back a non-normalized string, so the result has to be normalized once more. Section 3.13 of the Unicode Standard offers a discussion along with an example.)

[Subject index](INDEX.md) · [Previous source context](unicode-properties.md) · [Following source context](unicode-regular-expressions.md)
