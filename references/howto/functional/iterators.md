# Iterators

### Iterators

I'll begin by examining a Python language feature that lays an essential groundwork for authoring functional-style programs: iterators.

An iterator is an object that stands for a stream of data; it hands back the data a single element at a time. Any Python iterator has to provide a method named [`__next__()`](https://docs.python.org/3.14/library/stdtypes.html#iterator.__next__) which takes no arguments and consistently returns the stream's next element. When the stream holds no further elements, `__next__()` is required to raise the [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) exception. That said, iterators need not be finite; writing an iterator that yields an unending stream of data is entirely sensible.

The built-in [`iter()`](https://docs.python.org/3.14/library/functions.html#iter) function accepts any object and attempts to hand back an iterator that will produce the object's contents or elements, raising [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) when the object can't be iterated. A number of Python's built-in data types are iterable, the two most frequent being lists and dictionaries. An object earns the label [iterable](https://docs.python.org/3.14/glossary.html#term-iterable) when an iterator can be obtained for it.

You're free to try out the iteration interface by hand:

```python
>>> L = [1, 2, 3]
>>> it = iter(L)
>>> it
<...iterator object at ...>
>>> it.__next__()  # same as next(it)
1
>>> next(it)
2
>>> next(it)
3
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>

```

Several different settings in Python call for iterable objects, with the [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) statement being the foremost. Within the statement `for X in Y`, Y has to be an iterator or some object from which [`iter()`](https://docs.python.org/3.14/library/functions.html#iter) can build an iterator. The following two statements behave identically:

```python
for i in iter(obj):
    print(i)

for i in obj:
    print(i)

```

Iterators can be turned into lists or tuples by means of the [`list()`](https://docs.python.org/3.14/library/stdtypes.html#list) or [`tuple()`](https://docs.python.org/3.14/library/stdtypes.html#tuple) constructor functions:

```python
>>> L = [1, 2, 3]
>>> iterator = iter(L)
>>> t = tuple(iterator)
>>> t
(1, 2, 3)

```

Iterators work with sequence unpacking too: provided you know an iterator will yield N elements, you can unpack them into an N-tuple:

```python
>>> L = [1, 2, 3]
>>> iterator = iter(L)
>>> a, b, c = iterator
>>> a, b, c
(1, 2, 3)

```

Built-in functions like [`max()`](https://docs.python.org/3.14/library/functions.html#max) and [`min()`](https://docs.python.org/3.14/library/functions.html#min) accept a lone iterator argument and hand back the biggest or smallest element. The `"in"` and `"not in"` operators handle iterators as well: `X in iterator` evaluates true when X turns up in the stream the iterator yields. You'll hit clear trouble if the iterator runs forever; `max()`, `min()` will never come back, and should element X never show up in the stream, the `"in"` and `"not in"` operators won't return either.

Keep in mind that an iterator only moves forward; there's no mechanism to retrieve the prior element, restart the iterator, or duplicate it. Iterator objects may optionally offer these extra abilities, yet the iterator protocol mandates only the [`__next__()`](https://docs.python.org/3.14/library/stdtypes.html#iterator.__next__) method. Functions can thus drain the entire output of an iterator, and should you wish to do something else with that same stream, you'll need to build a fresh iterator.

[Subject index](INDEX.md) · [Previous source context](composability.md) · [Following source context](data-types-that-support-iterators.md)
