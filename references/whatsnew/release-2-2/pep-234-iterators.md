# What’s New in Python 2.2 / PEP 234: Iterators — readline

### PEP 234: Iterators

One more noteworthy addition in 2.2 is an iteration interface present at both the C and Python layers. Objects get to spell out how callers may loop across them.

Up through Python 2.1, the standard route to making `for item in obj` function was to define a [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) method along these lines:

```python
def __getitem__(self, index):
    return <next item>

```

[`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) is more fittingly meant to spell out an indexing operation on an object, letting you write `obj[5]` to fetch the sixth element. Leaning on it purely to prop up [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) loops is a bit deceptive. Picture some file-like object that wants to be iterated over; the *index* parameter is basically pointless, since the class likely takes for granted that a run of `__getitem__()` calls arrives with *index* bumped up by one each round. Put another way, the mere existence of the `__getitem__()` method is no promise that `file[5]` will randomly fetch the sixth element, even though by rights it ought to.

Under Python 2.2, iteration can stand on its own, and [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) methods can be confined to classes that genuinely do allow random access. The core notion behind iterators is simple. A new built-in function, `iter(obj)` or `iter(C, sentinel)`, serves to fetch an iterator. `iter(obj)` yields an iterator over the object *obj*, whereas `iter(C, sentinel)` yields an iterator that keeps calling the callable *C* until it hands back *sentinel*, marking that the iterator has finished.

Python classes are able to define an `__iter__()` method, which ought to build and return a fresh iterator for the object; if the object already serves as its own iterator, this method can merely return `self`. As a rule, iterators are typically their own iterators. Extension types coded in C can supply a [`tp_iter`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_iter) function to return an iterator, while extension types meaning to act as iterators can supply a [`tp_iternext`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_iternext) function.

So, when all’s said and done, what is it that iterators actually do? They carry one mandatory method, [`next()`](https://docs.python.org/3.14/library/functions.html#next), which takes no arguments and hands back the next value. Once there are no remaining values to deliver, a call to `next()` should raise the [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) exception.

```python
>>> L = [1,2,3]
>>> i = iter(L)
>>> print i
<iterator object at 0x8116870>
>>> i.next()
1
>>> i.next()
2
>>> i.next()
3
>>> i.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
StopIteration
>>>

```

Within 2.2, Python’s [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) statement no longer demands a sequence; it demands something from which [`iter()`](https://docs.python.org/3.14/library/functions.html#iter) can produce an iterator. For the sake of backward compatibility and convenience, an iterator gets built automatically for sequences that don’t supply `__iter__()` or a [`tp_iter`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_iter) slot, so `for i in [1,2,3]` keeps working. Everywhere the Python interpreter walks over a sequence, it’s been reworked to lean on the iterator protocol. As a result you can pull off things like this:

```python
>>> L = [1,2,3]
>>> i = iter(L)
>>> a,b,c = i
>>> a,b,c
(1, 2, 3)

```

Iterator support reached a few of Python’s core types as well. Calling [`iter()`](https://docs.python.org/3.14/library/functions.html#iter) on a dictionary gives back an iterator that loops across its keys:

```python
>>> m = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
...      'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
>>> for key in m: print key, m[key]
...
Mar 3
Feb 2
Aug 8
Sep 9
May 5
Jun 6
Jul 7
Jan 1
Apr 4
Nov 11
Dec 12
Oct 10

```

That’s merely the out-of-the-box behaviour. When you’d rather walk over keys, values, or key/value pairs, you can call the `iterkeys()`, `itervalues()`, or `iteritems()` methods outright to obtain a fitting iterator. In a small related tweak, the [`in`](https://docs.python.org/3.14/reference/expressions.html#in) operator now applies to dictionaries, so `key in dict` is now the same as `dict.has_key(key)`.

Files supply an iterator too, one that keeps calling the [`readline()`](https://docs.python.org/3.14/library/readline.html#module-readline) method until the file holds no further lines. That lets you now read each line of a file with code like this:

```python
for line in file:
    # do something for each line
    ...

```

[Subject index](INDEX.md) · [Previous source section](related-links.md) · [Release/subject declaration](introduction.md) · [Following release/subject continuation](iterator-direction-and-container-implementations.md)
