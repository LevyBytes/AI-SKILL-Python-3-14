# What's New In Python 3.2 / Documentation - datetime, functools, itertools, re

### Documentation

Ongoing work keeps making the documentation better.

- Lengthy sections such as [Built-in Functions](https://docs.python.org/3.14/library/functions.html#built-in-funcs) now carry a table of quick links right at the top. For [`itertools`](https://docs.python.org/3.14/library/itertools.html#module-itertools), those links come paired with tables of cheatsheet-style summaries, giving an overview and a memory jog without forcing you to wade through every doc.

- There are times when reading the pure Python source code complements the documentation nicely, so a great many modules now sport quick links pointing to the freshest version of their source. As one example, the [`functools`](https://docs.python.org/3.14/library/functools.html#module-functools) module documentation puts a quick link near the top labelled:

>

**Source code** [Lib/functools.py](https://github.com/python/cpython/tree/3.14/Lib/functools.py).

(Contributed by Raymond Hettinger; see [rationale](https://rhettinger.wordpress.com/2011/01/28/open-your-source-more/).)

- More examples and recipes now fill the docs. Notably, the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module carries a thorough section, [Regular Expression Examples](https://docs.python.org/3.14/library/re.html#re-examples). In the same way, the [`itertools`](https://docs.python.org/3.14/library/itertools.html#module-itertools) module keeps gaining fresh [Itertools Recipes](https://docs.python.org/3.14/library/itertools.html#itertools-recipes).

- A pure-Python auxiliary implementation now accompanies the [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime) module. Nothing about its functionality changed. It simply supplies an alternate implementation that is easier to read.

(Contributed by Alexander Belopolsky in [bpo-9528](https://bugs.python.org/issue?@action=redirect&bpo=9528).)

- The neglected `Demo` directory is gone. A few demos were folded into the documentation, certain ones shifted over to the `Tools/demo` directory, and the rest were dropped entirely.

(Contributed by Georg Brandl in [bpo-7962](https://bugs.python.org/issue?@action=redirect&bpo=7962).)

[Subject index](INDEX.md) · [Previous source section](codecs.md) · [Next source section](idle.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
