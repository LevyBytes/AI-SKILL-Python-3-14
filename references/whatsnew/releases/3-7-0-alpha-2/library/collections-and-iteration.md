# Python 3.7.0 alpha 2 / library / collections and iteration

[bpo-27541](https://bugs.python.org/issue?@action=redirect&bpo=27541): Reprs for subclasses of certain collection and iterator classes (`bytearray`, `array.array`, `collections.deque`, `collections.defaultdict`, `itertools.count`, `itertools.repeat`) now carry the real type name in place of hardcoded base class names.

[bpo-27494](https://bugs.python.org/issue?@action=redirect&bpo=27494): Let 2to3 tolerate a trailing comma within generator expressions. As an illustration, `set(x for x in [],)` is now permitted.

[bpo-30346](https://bugs.python.org/issue?@action=redirect&bpo=30346): Once the groupby iterator advances, an iterator that itertools.groupby() yielded now becomes exhausted.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
