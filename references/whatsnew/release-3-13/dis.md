# What's New In Python 3.13 / dis — dis

### dis

- Alter what [`dis`](https://docs.python.org/3.14/library/dis.html#module-dis) module functions print so that jump targets and exception handlers appear as logical labels in place of offsets. You can bring the offsets back through the fresh [`-O`](https://docs.python.org/3.14/library/dis.html#cmdoption-dis-O) command-line option or via the *show_offsets* argument. (Contributed by Irit Katriel in [gh-112137](https://github.com/python/cpython/issues/112137).)

- [`get_instructions()`](https://docs.python.org/3.14/library/dis.html#dis.get_instructions) henceforth stops rendering cache entries as standalone instructions. They instead arrive folded into the [`Instruction`](https://docs.python.org/3.14/library/dis.html#dis.Instruction), under the fresh *cache_info* field. The *show_caches* argument passed to `get_instructions()` is deprecated and henceforth does nothing. (Contributed by Irit Katriel in [gh-112962](https://github.com/python/cpython/issues/112962).)

[Subject index](INDEX.md) · [Previous source section](dbm.md) · [Next source section](doctest.md) · [Release/subject declaration](summary-release-highlights.md)
