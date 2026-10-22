# difflib: `difflib.context_diff()`, `difflib.get_close_matches()`

difflib.context_diff(*a*, *b*, *fromfile=''*, *tofile=''*, *fromfiledate=''*, *tofiledate=''*, *n=3*, *lineterm='\n'*)

Contrast *a* and *b* (lists of strings); hand back a delta (a [generator](https://docs.python.org/3.14/glossary.html#term-generator) generating the delta lines) rendered as a context diff.

A context diff is a terse way to display only the lines that differ together with a handful of surrounding lines. The edits appear in a before/after layout. How many context lines accompany them is governed by *n*, whose default is three.

By default the diff control lines (the ones carrying `***` or `---`) end with a trailing newline. That is convenient because inputs built from [`io.IOBase.readlines()`](https://docs.python.org/3.14/library/io.html#io.IOBase.readlines) then yield diffs fit for passing to [`io.IOBase.writelines()`](https://docs.python.org/3.14/library/io.html#io.IOBase.writelines), since both inputs and outputs carry trailing newlines.

When your inputs lack trailing newlines, give the *lineterm* argument the value `""` so that the result comes out entirely free of newlines.

A context diff usually carries a header listing filenames and modification times. You may supply any or all of them through strings for *fromfile*, *tofile*, *fromfiledate*, and *tofiledate*. The modification times are usually written in the ISO 8601 format. Left unset, these strings default to blanks.

```python
>>> import sys
>>> from difflib import *
>>> s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
>>> s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']
>>> sys.stdout.writelines(context_diff(s1, s2, fromfile='before.py',
...                        tofile='after.py'))
*** before.py
--- after.py
***************
*** 1,4 ****
! bacon
! eggs
! ham
  guido
--- 1,4 ----
! python
! eggy
! hamster
  guido

```

See A command-line interface to difflib for a more detailed example.

 difflib.get_close_matches(*word*, *possibilities*, *n=3*, *cutoff=0.6*)

Hand back a list of the top "good enough" matches. *word* is a sequence for which close matches are wanted (typically a string), and *possibilities* is a list of sequences that *word* is matched against (typically a list of strings).

Optional argument *n* (default `3`) caps how many close matches are returned; *n* must be greater than `0`.

Optional argument *cutoff* (default `0.6`) is a float in the range [0, 1]. Any possibility that fails to score at least that close to *word* is dropped.

The top matches (at most *n* of them) drawn from the possibilities come back in a list ordered by similarity score, with the most similar leading.

```python
>>> get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy'])
['apple', 'ape']
>>> import keyword
>>> get_close_matches('wheel', keyword.kwlist)
['while']
>>> get_close_matches('pineapple', keyword.kwlist)
[]
>>> get_close_matches('accept', keyword.kwlist)
['except']

```

[Subject index](INDEX.md) · [Previous](difflib-htmldiff-class-to-difflib-htmldiff-make-table.md) · [Continue](difflib-ndiff-to-difflib-unified-diff.md) · [Owning module, declaration or section: difflib](difflib-sequencematcher-class.md)
