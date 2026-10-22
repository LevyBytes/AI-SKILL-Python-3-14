# String indexing, slicing defaults and slice boundaries

Strings allow *indexing* (subscripting), where index 0 picks the first character. No standalone character type exists; a character amounts to nothing more than a string of length one:

```python
>>> word = 'Python'
>>> word[0]  # character in position 0
'P'
>>> word[5]  # character in position 5
'n'

```

Negative numbers work as indices too, counting inward from the right end:

```python
>>> word[-1]  # last character
'n'
>>> word[-2]  # second-last character
'o'
>>> word[-6]
'P'

```

Keep in mind that -0 equals 0, so negative indexing begins at -1.

Past plain indexing, *slicing* is on offer as well. Where indexing fetches one character at a time, *slicing* lets you pull out a substring:

```python
>>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'

```

Slice indices come with handy defaults; leaving off the first index makes it zero, and leaving off the second index makes it the length of the string under slice.

```python
>>> word[:2]   # character from the beginning to position 2 (excluded)
'Py'
>>> word[4:]   # characters from position 4 (included) to the end
'on'
>>> word[-2:]  # characters from the second-last (included) to the end
'on'

```

Observe that the start is forever counted in while the end is forever left out. That guarantees `s[:i] + s[i:]` will forever equal `s`:

```python
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'

```

A handy mental model for slices is to picture the indices as falling *between* characters, the leftmost edge of the first character being numbered 0. The rightmost edge of the final character in a string of *n* characters then carries index *n*, as below:

```python
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1

```

That top row of figures marks where the indices 0–6 land in the string; the row beneath shows the matching negative indices. A slice running from *i* through *j* gathers up every character lying between the edges tagged *i* and *j*.

When the indices are non-negative, a slice's length equals the gap between the indices, provided both stay in bounds. As an example, `word[1:3]` has length 2.

[Subject index](INDEX.md) · [Previous source section](string-repetition-and-literal-versus-variable-concatenation.md) · [Following source section](string-bounds-immutability-length-and-further-operations.md) · [Related tutorial example and explanation](string-quotation-escapes-raw-strings-and-multiline-literals.md) · [Related tutorial example and explanation](string-repetition-and-literal-versus-variable-concatenation.md) · [Related tutorial example and explanation](string-bounds-immutability-length-and-further-operations.md)
