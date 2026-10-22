# 3.2.13.4. Slice objects

#### 3.2.13.4. Slice objects

For `__getitem__()` methods, slices are represented using slice objects. The built-in [`slice()`](https://docs.python.org/3.14/library/functions.html#slice) function likewise produces them.

Special read-only attributes: the lower bound is [`start`](https://docs.python.org/3.14/library/functions.html#slice.start); the upper bound is [`stop`](https://docs.python.org/3.14/library/functions.html#slice.stop); the step value is [`step`](https://docs.python.org/3.14/library/functions.html#slice.step); whenever one is left out it becomes `None`. Any type at all is permitted for these attributes.

A single method is offered by slice objects:

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](internal-types.md) · [Previous source section](traceback-tb-next.md) · [Following source section](slice-indices.md)
