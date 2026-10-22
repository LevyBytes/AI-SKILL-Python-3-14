# iterator protocol C API: `PyIter_Check()`, `PyAIter_Check()`, `PyIter_NextItem()`, `PyIter_Next()`

# Iter, Iterator, Lifecycle

## Overview

Covers: Iterator Protocol; Iterator Objects; Object Life Cycle.

## Iterator Protocol

### Iterator Protocol

A pair of dedicated functions exists for handling iterators.

 int PyIter_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.8.*

Yields a non-zero result when the object *o* may be handed to `PyIter_NextItem()` without risk, and `0` if it cannot. This function always succeeds.

 int PyAIter_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

Yields a non-zero result when the object *o* implements the `AsyncIterator` protocol, otherwise `0`. This function always succeeds.

Added in version 3.10.

 int PyIter_NextItem([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *iter, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **item)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.14.*

On success, yields `1` and points *item* at a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) holding the next value produced by the iterator *iter*. When nothing further is left, yields `0` and assigns *item* the value `NULL`. On error, yields `-1`, assigns *item* the value `NULL`, and raises an exception.

Added in version 3.14.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyIter_Next([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This represents the legacy form of `PyIter_NextItem()`, kept around so existing code keeps working. Reach for `PyIter_NextItem()` instead.

Hands back the iterator *o*'s next value. According to `PyIter_Check()`, the object has to be an iterator (verifying that is the caller's responsibility). When nothing remains, `NULL` comes back and no exception is set. Should fetching the item fail, `NULL` comes back and the exception is propagated.

[Subject index](INDEX.md) · [Following source contract](pysendresult-to-pyiter-send.md)
