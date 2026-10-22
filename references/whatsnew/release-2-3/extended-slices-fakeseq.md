# Python 2.3 changes: Extended slice objects and custom sequence support

Or you can put slice objects straight into subscripts:

```python
>>> range(10)[slice(0, 5, 2)]
[0, 2, 4]

```

To make it easier to implement sequences supporting extended slicing, slice objects gained a method `indices(length)` that, supplied the length of a sequence, returns a `(start, stop, step)` tuple you can pass straight to [`range()`](https://docs.python.org/3.14/library/stdtypes.html#range). `indices()` deals with omitted and out-of-bounds indices the same way regular slices do (and that harmless-sounding phrase conceals a thicket of confusing details!). Here's how the method is meant to be used:

```python
class FakeSeq:
    ...
    def calc_item(self, i):
        ...
    def __getitem__(self, item):
        if isinstance(item, slice):
            indices = item.indices(len(self))
            return FakeSeq([self.calc_item(i) for i in range(*indices)])
        else:
            return self.calc_item(i)

```

This example further reveals that the built-in [`slice`](https://docs.python.org/3.14/library/functions.html#slice) object has become the slice type's type object and ceased to be a function. That mirrors Python 2.2, in which [`int`](https://docs.python.org/3.14/library/functions.html#int), [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), and the rest went through the very same change.

[Subject index](INDEX.md) · [Previous source section](extended-slices.md) · [Next source section](other-language-changes.md) · [Release/subject declaration](standard-set-type.md) · [Release/subject declaration](extended-slices.md)
