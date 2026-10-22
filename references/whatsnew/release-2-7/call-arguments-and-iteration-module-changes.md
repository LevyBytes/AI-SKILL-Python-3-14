# What’s New in Python 2.7 / New and Improved Modules — collections, decimal, inspect, io, itertools, json, mailbox, math, multiprocessing

New function: the [`getcallargs()`](https://docs.python.org/3.14/library/inspect.html#inspect.getcallargs) in the [`inspect`](https://docs.python.org/3.14/library/inspect.html#module-inspect) module accepts a callable plus its positional and keyword arguments, works out which of the callable's parameters each argument lands in, and returns a dictionary that maps argument names onto their values. As an illustration:

```python
>>> from inspect import getcallargs
>>> def f(a, b=1, *pos, **named):
...     pass
...
>>> getcallargs(f, 1, 2, 3)
{'a': 1, 'b': 2, 'pos': (3,), 'named': {}}
>>> getcallargs(f, a=2, x=4)
{'a': 2, 'b': 1, 'pos': (), 'named': {'x': 4}}
>>> getcallargs(f)
Traceback (most recent call last):
...
TypeError: f() takes at least 1 argument (0 given)

```

Contributed by George Sakkis; [bpo-3135](https://bugs.python.org/issue?@action=redirect&bpo=3135).

- Updated module: The [`io`](https://docs.python.org/3.14/library/io.html#module-io) library has been brought up to the version that ships with Python 3.1. For 3.1, the I/O library was rewritten from scratch in C and runs 2 to 20 times faster depending on which task is being carried out. The earlier Python implementation was renamed to the `_pyio` module.

One small change falls out of this: the [`io.TextIOBase`](https://docs.python.org/3.14/library/io.html#io.TextIOBase) class now carries an [`errors`](https://docs.python.org/3.14/library/io.html#io.TextIOBase.errors) attribute that reports the error setting in use for encoding and decoding errors (one of `'strict'`, `'replace'`, `'ignore'`).

The [`io.FileIO`](https://docs.python.org/3.14/library/io.html#io.FileIO) class now raises an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) when handed an invalid file descriptor. (Implemented by Benjamin Peterson; [bpo-4991](https://bugs.python.org/issue?@action=redirect&bpo=4991).) The [`truncate()`](https://docs.python.org/3.14/library/io.html#io.IOBase.truncate) method now keeps the file position intact; before, it would move the file position to the end of the newly sized file. (Fixed by Pascal Chambon; [bpo-6939](https://bugs.python.org/issue?@action=redirect&bpo=6939).)

- New function: `itertools.compress(data, selectors)` accepts two iterators. An element of *data* is returned when the matching value in *selectors* is true:

```python
itertools.compress('ABCDEF', [1,0,1,0,1,1]) =>
  A, C, E, F

```

New function: `itertools.combinations_with_replacement(iter, r)` produces every possible *r*-length combination of elements drawn from the iterable *iter*. In contrast to [`combinations()`](https://docs.python.org/3.14/library/itertools.html#itertools.combinations), the same element may recur within the generated combinations:

```python
itertools.combinations_with_replacement('abc', 2) =>
  ('a', 'a'), ('a', 'b'), ('a', 'c'),
  ('b', 'b'), ('b', 'c'), ('c', 'c')

```

Be aware that elements count as unique by their position within the input rather than by their actual values.

The [`itertools.count()`](https://docs.python.org/3.14/library/itertools.html#itertools.count) function has gained a *step* argument that permits incrementing by amounts other than 1. `count()` now also accepts keyword arguments and tolerates non-integer values, including floats or [`Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal) instances. (Implemented by Raymond Hettinger; [bpo-5032](https://bugs.python.org/issue?@action=redirect&bpo=5032).)

In the past, [`itertools.combinations()`](https://docs.python.org/3.14/library/itertools.html#itertools.combinations) and [`itertools.product()`](https://docs.python.org/3.14/library/itertools.html#itertools.product) raised [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) whenever *r* exceeded the length of the input iterable. That was judged to be a specification mistake, so they now hand back an empty iterator instead. (Fixed by Raymond Hettinger; [bpo-4816](https://bugs.python.org/issue?@action=redirect&bpo=4816).)

- Updated module: The [`json`](https://docs.python.org/3.14/library/json.html#module-json) module was brought up to version 2.0.9 of the simplejson package, which bundles a C extension that speeds up encoding and decoding. (Contributed by Bob Ippolito; [bpo-4136](https://bugs.python.org/issue?@action=redirect&bpo=4136).)

So that the new [`collections.OrderedDict`](https://docs.python.org/3.14/library/collections.html#collections.OrderedDict) type is supported, [`json.load()`](https://docs.python.org/3.14/library/json.html#json.load) now takes an optional *object_pairs_hook* parameter that gets invoked with each object literal that decodes into a list of pairs. (Contributed by Raymond Hettinger; [bpo-5381](https://bugs.python.org/issue?@action=redirect&bpo=5381).)

- The [`Maildir`](https://docs.python.org/3.14/library/mailbox.html#mailbox.Maildir) class in the [`mailbox`](https://docs.python.org/3.14/library/mailbox.html#module-mailbox) module now stores the timestamp of the directories it reads and re-reads a directory only when its modification time has since changed. By skipping needless directory scans, this boosts performance. (Fixed by A.M. Kuchling and Antoine Pitrou; [bpo-1607951](https://bugs.python.org/issue?@action=redirect&bpo=1607951), [bpo-6896](https://bugs.python.org/issue?@action=redirect&bpo=6896).)

- New functions: the [`math`](https://docs.python.org/3.14/library/math.html#module-math) module has gained [`erf()`](https://docs.python.org/3.14/library/math.html#math.erf) and [`erfc()`](https://docs.python.org/3.14/library/math.html#math.erfc) for the error function and its complement, [`expm1()`](https://docs.python.org/3.14/library/math.html#math.expm1), which evaluates `e**x - 1` with greater precision than calling [`exp()`](https://docs.python.org/3.14/library/math.html#math.exp) and then subtracting 1, [`gamma()`](https://docs.python.org/3.14/library/math.html#math.gamma) for the Gamma function, and [`lgamma()`](https://docs.python.org/3.14/library/math.html#math.lgamma) for the natural logarithm of the Gamma function. (Contributed by Mark Dickinson and nirinA raseliarison; [bpo-3366](https://bugs.python.org/issue?@action=redirect&bpo=3366).)

- The `Manager*` classes in the [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) module can now be handed a callable that runs each time a subprocess starts, together with a collection of arguments to pass into that callable. (Contributed by lekma; [bpo-5585](https://bugs.python.org/issue?@action=redirect&bpo=5585).)

The [`Pool`](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing.pool.Pool) class, which manages a pool of worker processes, now offers an optional *maxtasksperchild* parameter. Each worker process carries out the stated number of tasks and then exits, prompting the `Pool` to spin up a replacement worker. This helps when tasks may leak memory or other resources, or when certain tasks cause a worker to grow very large. (Contributed by Charles Cazabon; [bpo-6963](https://bugs.python.org/issue?@action=redirect&bpo=6963).)

- The `nntplib` module now handles IPv6 addresses. (Contributed by Derek Morr; [bpo-1664](https://bugs.python.org/issue?@action=redirect&bpo=1664).)

-

[Subject index](INDEX.md) · [Previous source section](ctypes-through-io-module-changes.md) · [Release/subject declaration](the-future-for-python-2-x.md) · [Release/subject declaration](standard-library-module-changes.md) · [Preceding release/subject continuation](standard-library-module-changes.md) · [Following release/subject continuation](posix-identities-and-process-module-changes.md)
