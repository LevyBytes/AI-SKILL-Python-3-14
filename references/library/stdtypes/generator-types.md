# Generator Types

### Generator Types

Python's [generator](https://docs.python.org/3.14/glossary.html#term-generator)s offer a tidy route to fulfilling the iterator protocol. When a container object's [`__iter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__iter__) method takes the form of a generator, it will return an iterator object on its own (a generator object, strictly speaking) that furnishes both the `__iter__()` and [`__next__()`](https://docs.python.org/3.14/reference/expressions.html#generator.__next__) methods. You can read more on generators in [the documentation for the yield expression](https://docs.python.org/3.14/reference/expressions.html#yieldexpr).

[Subject index](INDEX.md) · [Previous](container-iter-to-iterator-next.md) · [Continue](sequence-types-list-tuple-range.md)
