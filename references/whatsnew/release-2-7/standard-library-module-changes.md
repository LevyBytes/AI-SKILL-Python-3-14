# What’s New in Python 2.7 / New and Improved Modules - bdb, binascii, bz2, collections

### New and Improved Modules

Just like every release, the Python standard library picked up a batch of improvements and fixes. What follows is a selective rundown of the more noteworthy changes, listed in alphabetical order by module. For the full accounting, read the `Misc/NEWS` file in the source tree or comb through the Subversion logs.

- The base debugging class [`Bdb`](https://docs.python.org/3.14/library/bdb.html#bdb.Bdb) in the [`bdb`](https://docs.python.org/3.14/library/bdb.html#module-bdb) module learned how to skip over modules. Its constructor now accepts an iterable of glob-style patterns like `django.*`, and the debugger will refuse to step into any stack frame whose module matches one of them. (Provided by Maru Newby following a suggestion from Senthil Kumaran; [bpo-5142](https://bugs.python.org/issue?@action=redirect&bpo=5142).)

- The [`binascii`](https://docs.python.org/3.14/library/binascii.html#module-binascii) module now speaks the buffer API, letting it operate on [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) instances and comparable buffer objects. (Back-ported from 3.x by Florent Xicluna; [bpo-7703](https://bugs.python.org/issue?@action=redirect&bpo=7703).)

- Refreshed module: `bsddb` moved up from 4.7.2devel9 to release 4.8.4 of [the pybsddb package](https://www.jcea.es/programacion/pybsddb.htm). This version improves Python 3.x compatibility, fixes assorted bugs, and brings in several additional BerkeleyDB flags and methods. (Refreshed by Jesús Cea Avión; [bpo-8156](https://bugs.python.org/issue?@action=redirect&bpo=8156). You can read the pybsddb changelog at [https://hg.jcea.es/pybsddb/file/tip/ChangeLog](https://hg.jcea.es/pybsddb/file/tip/ChangeLog).)

- [`BZ2File`](https://docs.python.org/3.14/library/bz2.html#bz2.BZ2File) in the [`bz2`](https://docs.python.org/3.14/library/bz2.html#module-bz2) module now honors the context management protocol, which lets you write `with bz2.BZ2File(...) as f:`. (Provided by Hagen Fürstenau; [bpo-3860](https://bugs.python.org/issue?@action=redirect&bpo=3860).)

- A new class: [`Counter`](https://docs.python.org/3.14/library/collections.html#collections.Counter), found in the [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) module, comes in handy for counting things. A `Counter` mostly acts like a dictionary, except that a missing key yields zero rather than triggering a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError):

```pycon
>>> from collections import Counter
>>> c = Counter()
>>> for letter in 'here is a sample of english text':
...   c[letter] += 1
...
>>> c
Counter({' ': 6, 'e': 5, 's': 3, 'a': 2, 'i': 2, 'h': 2,
'l': 2, 't': 2, 'g': 1, 'f': 1, 'm': 1, 'o': 1, 'n': 1,
'p': 1, 'r': 1, 'x': 1})
>>> c['e']
5
>>> c['z']
0

```

[Subject index](INDEX.md) · [Previous source section](optimizations.md) · [Release/subject declaration](the-future-for-python-2-x.md) · [Following release/subject continuation](counter-collections-config-and-cookie-changes.md)
