# Search and replace

### Search and replace

A second routine job is locating every match of a pattern and swapping each one for some other string. The [`sub()`](https://docs.python.org/3.14/library/re.html#re.Pattern.sub) method accepts a replacement value (either a string or a function) together with the string that is to be processed.

 .sub(*replacement*, *string*[, *count=0*])

Hands back the string you get once the leftmost non-overlapping matches of the RE within *string* are swapped for the replacement *replacement*. Where the pattern turns up nowhere, *string* comes back untouched.

The optional *count* argument caps how many pattern occurrences get swapped; *count* has to be a non-negative integer. Its default of 0 means every occurrence is swapped.

Below is a basic example using the [`sub()`](https://docs.python.org/3.14/library/re.html#re.Pattern.sub) method. It swaps colour names for the word `colour`:

```python
>>> p = re.compile('(blue|white|red)')
>>> p.sub('colour', 'blue socks and red shoes')
'colour socks and colour shoes'
>>> p.sub('colour', 'blue socks and red shoes', count=1)
'colour socks and red shoes'

```

The [`subn()`](https://docs.python.org/3.14/library/re.html#re.Pattern.subn) method performs identical work but hands back a 2-tuple holding the freshly built string together with a count of how many swaps occurred:

[Subject index](INDEX.md) · [Following source continuation](search-and-replace-continuation.md) · [Previous source context](splitting-strings.md)
