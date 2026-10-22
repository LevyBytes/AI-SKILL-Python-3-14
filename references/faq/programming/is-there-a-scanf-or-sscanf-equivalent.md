# Is there a `scanf()` or `sscanf()` equivalent?

### Is there a `scanf()` or `sscanf()` equivalent?

Nothing exactly like it.

For straightforward input parsing, the simplest route is usually to break the line into whitespace-separated words with the [`split()`](https://docs.python.org/3.14/library/stdtypes.html#str.split) method on string objects, then turn the decimal strings into numbers via [`int()`](https://docs.python.org/3.14/library/functions.html#int) or [`float()`](https://docs.python.org/3.14/library/functions.html#float). `split()` accepts an optional “sep” parameter, handy whenever the line relies on something besides whitespace as its separator.

When the parsing gets more involved, regular expressions outdo C’s `sscanf` in power and fit the job better.

[Subject index](INDEX.md)
