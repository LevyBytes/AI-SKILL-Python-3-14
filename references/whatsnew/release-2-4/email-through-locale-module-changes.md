# What’s New in Python 2.4 / New, Improved, and Deprecated Modules — email, heapq, http, imaplib, itertools, locale

The [`email`](https://docs.python.org/3.14/library/email.html#module-email) package was bumped to version 3.0, which dropped several deprecated APIs and ends support for Python releases before 2.3. The package's 3.0 version employs a new incremental parser for MIME messages, found in the `email.FeedParser` module. This new parser doesn't need the whole message loaded into memory, and it doesn't raise exceptions when a message is malformed; rather, it logs any issues in the message's `defect` attribute. (Developed by Anthony Baxter, Barry Warsaw, Thomas Wouters, and others.)

- The [`heapq`](https://docs.python.org/3.14/library/heapq.html#module-heapq) module has been ported to C. The tenfold speed boost that resulted makes the module appropriate for processing large volumes of data. The module also picked up two new functions, `nlargest()` and `nsmallest()`, which leverage heaps to locate the N largest or smallest values within a dataset and avoid the cost of a complete sort. (Contributed by Raymond Hettinger.)

- The [`httplib`](https://docs.python.org/3.14/library/http.html#module-http) module now holds constants for the HTTP status codes laid out across assorted HTTP-related RFC documents. These constants bear names like `OK`, `CREATED`, `CONTINUE`, and `MOVED_PERMANENTLY`; run pydoc to see the complete list. (Contributed by Andrew Eland.)

- The [`imaplib`](https://docs.python.org/3.14/library/imaplib.html#module-imaplib) module now backs IMAP's THREAD command (contributed by Yves Dionne) plus new `deleteacl()` and `myrights()` methods (contributed by Arnaud Mazin).

- The [`itertools`](https://docs.python.org/3.14/library/itertools.html#module-itertools) module picked up a `groupby(iterable[, *func*])` function. *iterable* is whatever can be looped over to produce a series of elements, while the optional *func* parameter names a function receiving an element and yielding a key value; absent that, the key simply equals the element itself. `groupby()` then bundles the elements into subsequences sharing matching key values, and returns a series of 2-tuples holding the key value together with an iterator over the subsequence.

Here is an example to make this point clearer. The *key* function simply reports whether a number is even or odd, so `groupby()` ends up returning consecutive runs of odd or even numbers.

```python
>>> import itertools
>>> L = [2, 4, 6, 7, 8, 9, 11, 12, 14]
>>> for key_val, it in itertools.groupby(L, lambda x: x % 2):
...    print key_val, list(it)
...
0 [2, 4, 6]
1 [7]
0 [8]
1 [9, 11]
0 [12, 14]
>>>

```

`groupby()` is generally applied to sorted input. The logic behind `groupby()` resembles the Unix `uniq` filter, which makes it useful for removing, counting, or spotting duplicate elements:

```python
>>> word = 'abracadabra'
>>> letters = sorted(word)   # Turn string into a sorted list of letters
>>> letters
['a', 'a', 'a', 'a', 'a', 'b', 'b', 'c', 'd', 'r', 'r']
>>> for k, g in itertools.groupby(letters):
...    print k, list(g)
...
a ['a', 'a', 'a', 'a', 'a']
b ['b', 'b']
c ['c']
d ['d']
r ['r', 'r']
>>> # List unique letters
>>> [k for k, g in groupby(letters)]
['a', 'b', 'c', 'd', 'r']
>>> # Count letter occurrences
>>> [(k, len(list(g))) for k, g in groupby(letters)]
[('a', 5), ('b', 2), ('c', 1), ('d', 1), ('r', 2)]

```

(Contributed by Hye-Shik Chang.)

- [`itertools`](https://docs.python.org/3.14/library/itertools.html#module-itertools) also picked up a function called `tee(iterator, N)` that yields *N* independent iterators each replicating *iterator*. When *N* is left out, the default value is 2.

```python
>>> L = [1,2,3]
>>> i1, i2 = itertools.tee(L)
>>> i1,i2
(<itertools.tee object at 0x402c2080>, <itertools.tee object at 0x402c2090>)
>>> list(i1)               # Run the first iterator to exhaustion
[1, 2, 3]
>>> list(i2)               # Run the second iterator to exhaustion
[1, 2, 3]

```

Be aware that `tee()` must retain copies of the values the iterator produces; in the worst case it could end up retaining every one of them. For that reason it should be applied carefully whenever the leading iterator may race far ahead of the trailing iterator across a lengthy stream of inputs. Should the gap be wide, you might just as well reach for [`list()`](https://docs.python.org/3.14/library/stdtypes.html#list) instead. Whenever the iterators stay close to each other, `tee()` is the perfect fit. Likely uses include bookmarking, windowing, or lookahead iterators. (Contributed by Raymond Hettinger.)

- Several functions were introduced into the [`locale`](https://docs.python.org/3.14/library/locale.html#module-locale) module, including `bind_textdomain_codeset()` for designating a specific encoding and a family of `l*gettext()` functions that hand back messages in the selected encoding. (Contributed by Gustavo Niemeyer.)

[Subject index](INDEX.md) · [Previous source section](new-improved-and-deprecated-modules.md) · [Next source section](logging-basicconfig-keywords.md) · [Release/subject declaration](pep-218-built-in-set-objects.md) · [Release/subject declaration](new-improved-and-deprecated-modules.md)
