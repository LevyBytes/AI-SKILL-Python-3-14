# itertools: `itertools.filterfalse()`, `itertools.groupby()`

itertools.filterfalse(*predicate*, *iterable*)

Make an iterator that screens elements from the *iterable*, keeping only the ones for which the *predicate* yields a false value. When *predicate* is `None`, the items that are false are kept. Roughly equivalent to:

```python
def filterfalse(predicate, iterable):
    # filterfalse(lambda x: x<5, [1,4,6,3,8]) → 6 8

    if predicate is None:
        predicate = bool

    for x in iterable:
        if not predicate(x):
            yield x

```

 itertools.groupby(*iterable*, *key=None*)

Make an iterator that hands back successive keys together with groups taken from the *iterable*. The *key* is a function that derives a key value for every element. When left unspecified or set to `None`, *key* falls back to an identity function that returns the element as-is. As a rule, the iterable should already be sorted on that same key function.

How `groupby()` behaves resembles the Unix `uniq` filter. It opens a break, or a fresh group, each time the key function's value shifts (which is the reason the data normally has to be sorted beforehand using the same key function). This is unlike SQL's GROUP BY, which gathers common elements no matter how they were ordered in the input.

The group that gets returned is itself an iterator drawing on the same underlying iterable as `groupby()`. Since that source is shared, advancing the `groupby()` object makes the earlier group disappear. Therefore, whenever that data will be wanted afterward, capture it into a list:

```python
groups = []
uniquekeys = []
data = sorted(data, key=keyfunc)
for k, g in groupby(data, keyfunc):
    groups.append(list(g))      # Store group iterator as a list
    uniquekeys.append(k)

```

`groupby()` is roughly equivalent to:

```python
def groupby(iterable, key=None):
    # [k for k, g in groupby('AAAABBBCCDAABBB')] → A B C D A B
    # [list(g) for k, g in groupby('AAAABBBCCD')] → AAAA BBB CC D

    keyfunc = (lambda x: x) if key is None else key
    iterator = iter(iterable)
    exhausted = False

    def _grouper(target_key):
        nonlocal curr_value, curr_key, exhausted
        yield curr_value
        for curr_value in iterator:
            curr_key = keyfunc(curr_value)
            if curr_key != target_key:
                return
            yield curr_value
        exhausted = True

    try:
        curr_value = next(iterator)
    except StopIteration:
        return
    curr_key = keyfunc(curr_value)

    while not exhausted:
        target_key = curr_key
        curr_group = _grouper(target_key)
        yield curr_key, curr_group
        if curr_key == target_key:
            for _ in curr_group:
                pass

```

[Subject index](INDEX.md) · [Previous](itertools-compress-to-itertools-dropwhile.md) · [Continue](itertools-islice-to-itertools-pairwise.md) · [Owning module, declaration or section: itertools](itertools-functions-creating-iterators-for-efficient-looping.md) · [Owning module, declaration or section: Itertool Functions](itertools-accumulate.md)
