# What’s New In Python 3.5 / re — re

### re

Within lookbehind assertions, you may now use references and conditional references aimed at fixed-length groups:

```python
>>> import re
>>> pat = re.compile(r'(a|b).(?<=\1)c')
>>> pat.match('aac')
<_sre.SRE_Match object; span=(0, 3), match='aac'>
>>> pat.match('bbc')
<_sre.SRE_Match object; span=(0, 3), match='bbc'>

```

Serhiy Storchaka implemented this (see [bpo-9179](https://bugs.python.org/issue?@action=redirect&bpo=9179)).

Regular expressions may now declare more than 100 capturing groups; the prior ceiling has been lifted. Serhiy Storchaka made this change (see [bpo-22437](https://bugs.python.org/issue?@action=redirect&bpo=22437)).

Rather than raising an exception, the [`sub()`](https://docs.python.org/3.14/library/re.html#re.sub) plus [`subn()`](https://docs.python.org/3.14/library/re.html#re.subn) functions now substitute empty strings for any group that did not match. Serhiy Storchaka authored this (see [bpo-1519638](https://bugs.python.org/issue?@action=redirect&bpo=1519638)).

To convey richer detail about a failure, the [`re.error`](https://docs.python.org/3.14/library/re.html#re.PatternError) exceptions gained fresh attributes — [`msg`](https://docs.python.org/3.14/library/re.html#re.PatternError.msg), [`pattern`](https://docs.python.org/3.14/library/re.html#re.PatternError.pattern), [`pos`](https://docs.python.org/3.14/library/re.html#re.PatternError.pos), [`lineno`](https://docs.python.org/3.14/library/re.html#re.PatternError.lineno), and [`colno`](https://docs.python.org/3.14/library/re.html#re.PatternError.colno):

```python
>>> re.compile("""
...     (?x)
...     .++
... """)
Traceback (most recent call last):
   ...
sre_constants.error: multiple repeat at position 16 (line 3, column 7)

```

Serhiy Storchaka contributed it (see [bpo-22578](https://bugs.python.org/issue?@action=redirect&bpo=22578)).

[Subject index](INDEX.md) · [Previous source section](poplib.md) · [Next source section](readline.md) · [Release/subject declaration](summary-release-highlights.md)
