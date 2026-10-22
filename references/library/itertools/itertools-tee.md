# itertools: `itertools.tee()`

itertools.tee(*iterable*, *n=2*)

Return *n* independent iterators from a single iterable.

Roughly equivalent to:

```python
def tee(iterable, n=2):
    if n < 0:
        raise ValueError
    if n == 0:
        return ()
    iterator = _tee(iterable)
    result = [iterator]
    for _ in range(n - 1):
        result.append(_tee(iterator))
    return tuple(result)

class _tee:

    def __init__(self, iterable):
        it = iter(iterable)
        if isinstance(it, _tee):
            self.iterator = it.iterator
            self.link = it.link
        else:
            self.iterator = it
            self.link = [None, None]

    def __iter__(self):
        return self

    def __next__(self):
        link = self.link
        if link[1] is None:
            link[0] = next(self.iterator)
            link[1] = [None, None]
        value, self.link = link
        return value

```

Whenever the input *iterable* happens to already be a tee iterator object, every member of the returned tuple is built as though it came out of the original upstream `tee()` call. This "flattening step" lets nested `tee()` calls draw on one shared underlying data chain and run off a single update step in place of a whole chain of calls.

[Subject index](INDEX.md) · [Previous](itertools-repeat-to-itertools-takewhile.md) · [Owning module, declaration or section: itertools](itertools-functions-creating-iterators-for-efficient-looping.md) · [Owning module, declaration or section: Itertool Functions](itertools-accumulate.md) · [Required continuation of the source contract](itertools-zip-longest.md)
