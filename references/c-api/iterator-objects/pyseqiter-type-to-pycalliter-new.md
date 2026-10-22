# Iterator Objects

## Iterator Objects

### Iterator Objects

Two all-purpose iterator objects ship with Python. The first is a sequence iterator that operates over any sequence offering the [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) method. The second pairs a callable object with a sentinel value, invoking the callable to produce each item and stopping the iteration once the callable yields the sentinel.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PySeqIter_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The type object for the iterators produced by `PySeqIter_New()` and by the single-argument variant of the [`iter()`](https://docs.python.org/3.14/library/functions.html#iter) built-in function applied to built-in sequence types.

 int PySeqIter_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

Yields true when *op* has the type `PySeqIter_Type`. This function always succeeds.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PySeqIter_New([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *seq)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hands back an iterator that operates over a general sequence object, *seq*. Iteration stops at the point the sequence throws [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) during the subscripting operation.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyCallIter_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The type object for the iterators produced by `PyCallIter_New()` and by the two-argument variant of the [`iter()`](https://docs.python.org/3.14/library/functions.html#iter) built-in function.

 int PyCallIter_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

Yields true when *op* has the type `PyCallIter_Type`. This function always succeeds.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyCallIter_New([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *callable, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *sentinel)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hands back a fresh iterator. The leading parameter, *callable*, may be any Python callable object that accepts no parameters; invoking it each time should yield the iteration's next item. The moment *callable* yields a value equal to *sentinel*, iteration stops.

[Subject index](INDEX.md) · [Previous source contract](../iterator-protocol/pysendresult-to-pyiter-send.md) · [Following source contract](pyrange-type-to-pyrange-check.md)
