# Iteration and comprehensions

Open when checking Python definitions for iteration and comprehensions.

## iterable

An object able to hand back its members one by one. Among the iterables are every sequence type (for instance [`list`](https://docs.python.org/3.14/library/stdtypes.html#list), [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), and [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple)) plus certain non-sequence types such as [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict), file objects, and objects of whatever classes you write carrying an [`__iter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__iter__) method or a [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) method that realizes sequence semantics.

You may use iterables within a [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) loop and in plenty of other spots where a sequence is wanted ([`zip()`](https://docs.python.org/3.14/library/functions.html#zip), [`map()`](https://docs.python.org/3.14/library/functions.html#map), ?). Handing an iterable object to the built-in function [`iter()`](https://docs.python.org/3.14/library/functions.html#iter) returns an iterator for that object. Such an iterator is good for a single pass across the set of values. While working with iterables, you usually need not call `iter()` yourself or bother with iterator objects. The `for` statement handles that on its own, quietly creating an unnamed temporary variable that holds the iterator for the loop's duration. See also iterator, sequence, and generator.

## iterator

An object that stands for a stream of data. Calling the iterator's [`__next__()`](https://docs.python.org/3.14/library/stdtypes.html#iterator.__next__) method over and over (or feeding it to the built-in function [`next()`](https://docs.python.org/3.14/library/functions.html#next)) yields the stream's successive items. Once no further data remain, a [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) exception arises in their place. At that stage the iterator object is spent, and every later call to its `__next__()` method merely raises `StopIteration` once more. Every iterator must supply an [`__iter__()`](https://docs.python.org/3.14/library/stdtypes.html#iterator.__iter__) method handing back the iterator object itself, so each iterator is iterable too and fits nearly anywhere other iterables are taken. A notable exception is code that tries to iterate more than once. Pass a container object (a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list), say) to the [`iter()`](https://docs.python.org/3.14/library/functions.html#iter) function or run it through a [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for) loop, and it hands back a brand-new iterator on each occasion. Trying that with an iterator simply hands back the very same spent iterator object from the prior pass, so it looks like an empty container.

You can read more in [Iterator Types](https://docs.python.org/3.14/library/stdtypes.html#typeiter).

**CPython implementation detail:** The rule that an iterator must define [`__iter__()`](https://docs.python.org/3.14/library/stdtypes.html#iterator.__iter__) is not enforced uniformly by CPython. Note as well that free-threaded CPython makes no promise of thread-safe behavior for iterator operations.

## generator

A function that hands back a generator iterator. It resembles an ordinary function aside from holding [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) expressions that emit a sequence of values consumable in a for-loop or fetchable individually through the [`next()`](https://docs.python.org/3.14/library/functions.html#next) function.

Generally it denotes a generator function, although in certain settings it may indicate a *generator iterator*. Where the meaning could be unclear, spelling out the full terms removes the ambiguity.

## generator iterator

An object that a generator function brings into being.

Every [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) pauses processing for the moment, retaining the execution state (covering local variables and any pending try-statements). On resuming, the *generator iterator* continues from where it stopped (unlike functions, which begin afresh at each call).

## generator expression

An expression yielding an iterator. It resembles an ordinary expression trailed by a `for` clause that names a loop variable and range, plus an optional `if` clause. Taken together the expression emits values for an enclosing function:

```python
>>> sum(i*i for i in range(10))         # sum of squares 0, 1, 4, ... 81
285

```

## list comprehension

A terse way to handle some or all of a sequence's elements and hand back a list holding the outcomes. `result = ['{:#04x}'.format(x) for x in range(256) if x % 2 == 0]` builds a list of strings holding even hexadecimal numbers (0x..) spanning 0 through 255. Supplying the [`if`](https://docs.python.org/3.14/reference/compound_stmts.html#if) clause is optional. When you leave it out, every element of `range(256)` is processed.

## dictionary comprehension

A succinct construct for working through some or all of an iterable's elements, yielding a dictionary built from the outcome. `results = {n: n ** 2 for n in range(10)}` produces a dictionary in which key `n` maps to value `n ** 2`. See [Displays for lists, sets and dictionaries](https://docs.python.org/3.14/reference/expressions.html#comprehensions).

## set comprehension

A terse means of working through all or some of the items in an iterable and giving back a set holding the outcomes. `results = {c for c in 'abracadabra' if c not in 'abc'}` produces the set of strings `{'r', 'd'}`. See [Displays for lists, sets and dictionaries](https://docs.python.org/3.14/reference/expressions.html#comprehensions).

## key function

A key function, also called a collation function, is a callable handing back a value used in sorting or ordering. To illustrate, [`locale.strxfrm()`](https://docs.python.org/3.14/library/locale.html#locale.strxfrm) serves to make a sort key attuned to locale-specific sort conventions.

Several tools across Python take key functions to govern how elements get ordered or grouped. Among them are [`min()`](https://docs.python.org/3.14/library/functions.html#min), [`max()`](https://docs.python.org/3.14/library/functions.html#max), [`sorted()`](https://docs.python.org/3.14/library/functions.html#sorted), [`list.sort()`](https://docs.python.org/3.14/library/stdtypes.html#list.sort), [`heapq.merge()`](https://docs.python.org/3.14/library/heapq.html#heapq.merge), [`heapq.nsmallest()`](https://docs.python.org/3.14/library/heapq.html#heapq.nsmallest), [`heapq.nlargest()`](https://docs.python.org/3.14/library/heapq.html#heapq.nlargest), and [`itertools.groupby()`](https://docs.python.org/3.14/library/itertools.html#itertools.groupby).
A key function can be produced in a number of ways. As one illustration, the [`str.casefold()`](https://docs.python.org/3.14/library/stdtypes.html#str.casefold) method works as a key function when you want sorts that ignore case. A key function can also be assembled out of a [`lambda`](https://docs.python.org/3.14/reference/expressions.html#lambda) expression like `lambda r: (r[0], r[2])`. Three further constructors of key functions are [`operator.attrgetter()`](https://docs.python.org/3.14/library/operator.html#operator.attrgetter), [`operator.itemgetter()`](https://docs.python.org/3.14/library/operator.html#operator.itemgetter), and [`operator.methodcaller()`](https://docs.python.org/3.14/library/operator.html#operator.methodcaller). For worked examples covering the construction and use of key functions, consult the [Sorting HOW TO](https://docs.python.org/3.14/howto/sorting.html#sortinghowto).

[Glossary context index](INDEX.md).
