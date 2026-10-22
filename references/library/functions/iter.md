# iter

iter(*iterable*, */*)

 iter(*callable*, *sentinel*, */*)

Yield an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator) object. How the first argument gets handled hinges entirely on whether a second argument is supplied. When only one argument is passed, that lone argument has to be a collection object honoring the [iterable](https://docs.python.org/3.14/glossary.html#term-iterable) protocol (the [`__iter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__iter__) method), or else honoring the sequence protocol (the [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) method accepting integer indices that begin at `0`). When neither protocol is honored, [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) gets raised. Should the second argument, *sentinel*, be supplied, then the first argument is required to be a callable object. In that scenario the resulting iterator invokes *callable* with zero arguments on every invocation of its [`__next__()`](https://docs.python.org/3.14/library/stdtypes.html#iterator.__next__) method; when the returned value matches *sentinel*, [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) gets raised, and otherwise that value is handed back.

See also [Iterator Types](https://docs.python.org/3.14/library/stdtypes.html#typeiter).

A handy use of the two-argument form of `iter()` is constructing a block-reader. As an illustration, here is code that reads fixed-width blocks out of a binary database file until end of file arrives:

```python
from functools import partial
with open('mydata.db', 'rb') as f:
    for block in iter(partial(f.read, 64), b''):
        process_block(block)

```

[Builtin task index](INDEX.md).
