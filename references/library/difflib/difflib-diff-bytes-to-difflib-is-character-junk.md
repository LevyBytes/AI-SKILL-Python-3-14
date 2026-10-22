# difflib: `difflib.diff_bytes()`, `difflib.IS_LINE_JUNK()`, `difflib.IS_CHARACTER_JUNK()`

`difflib.diff_bytes(dfunc, a, b, fromfile=b'', tofile=b'', fromfiledate=b'', tofiledate=b'', n=3, lineterm=b'\n')`

Contrast *a* and *b* (lists of bytes objects) by way of *dfunc*; yield a sequence of delta lines (also bytes) laid out in whatever format *dfunc* returns. *dfunc* must be a callable, usually either `unified_diff()` or `context_diff()`.

This lets you contrast data whose encoding is unknown or inconsistent. Every input apart from *n* must be a bytes object, not str. It works by losslessly turning all inputs (except *n*) into str, then calling `dfunc(a, b, fromfile, tofile, fromfiledate, tofiledate, n, lineterm)`. The output from *dfunc* is afterward turned back into bytes, so the delta lines you get keep the same unknown/inconsistent encodings as *a* and *b*.

Added in version 3.5.

 difflib.IS_LINE_JUNK(*line*)

Hand back `True` for ignorable lines. The line *line* counts as ignorable when *line* is blank or holds a single `'#'`; otherwise it is not ignorable. Served as a default for the *linejunk* parameter of `ndiff()` in earlier versions.

 difflib.IS_CHARACTER_JUNK(*ch*)

Hand back `True` for ignorable characters. The character *ch* counts as ignorable when *ch* is a space or tab; otherwise it is not ignorable. Serves as a default for the *charjunk* parameter of `ndiff()`.

See also

[Pattern Matching: The Gestalt Approach](https://jacobfilipp.com/DrDobbs/articles/DDJ/1988/8807/8807c/8807c.htm)

A write-up of a related algorithm by John W. Ratcliff and D. E. Metzener. It appeared in Dr. Dobb's Journal in July, 1988.

[Subject index](INDEX.md) · [Previous](difflib-ndiff-to-difflib-unified-diff.md) · [Continue](difflib-sequencematcher-class.md) · [Owning module, declaration or section: difflib](difflib-sequencematcher-class.md)
