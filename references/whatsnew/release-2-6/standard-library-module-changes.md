# What’s New in Python 2.6 / New and Improved Modules - cmath, collections, urllib.parse

### New and Improved Modules

Just like every release, the standard library that ships with Python picked up an assortment of improvements and fixes. What follows is a selected rundown of the more significant changes, ordered alphabetically by the name of the module. For an exhaustive accounting, read the `Misc/NEWS` file in the source tree, or page through the Subversion logs for every last detail.

- Active maintenance has resumed on the `asyncore` and `asynchat` modules, and several patches and fixes landed. (Maintained by Josiah Carlson; see [bpo-1736190](https://bugs.python.org/issue?@action=redirect&bpo=1736190) for one patch.)

- The `bsddb` module picked up a fresh maintainer too, Jesús Cea Avión, and you can now obtain the package on its own. Its home page lives at [www.jcea.es/programacion/pybsddb.htm](https://www.jcea.es/programacion/pybsddb.htm). Because the package ships releases far more often than Python does, the intent is to drop it from the standard library when Python 3.0 arrives.

The `bsddb.dbshelve` module now picks the top pickling protocol on offer rather than capping itself at protocol 1. (Contributed by W. Barnes.)

- The `cgi` module will now pull variables out of the query string attached to an HTTP POST request. That allows form actions whose URLs carry query strings, for instance “/cgi-bin/add.py?category=1”. (Contributed by Alexandre Fiori and Nubis; [bpo-1817](https://bugs.python.org/issue?@action=redirect&bpo=1817).)

The `parse_qs()` and `parse_qsl()` functions have moved out of the `cgi` module and into the [`urlparse`](https://docs.python.org/3.14/library/urllib.parse.html#module-urllib.parse) module. The copies that remain in the `cgi` module will emit [`PendingDeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#PendingDeprecationWarning) messages under 2.6 ([bpo-600362](https://bugs.python.org/issue?@action=redirect&bpo=600362)).

- Mark Dickinson and Christian Heimes contributed a thorough overhaul of the [`cmath`](https://docs.python.org/3.14/library/cmath.html#module-cmath) module. It gained five new functions:

  - `polar()` turns a complex number into polar form, handing back the modulus and the argument of that complex number.

  - `rect()` works in reverse, taking a modulus and argument pair and rebuilding the matching complex number.

  - `phase()` hands back the argument (otherwise known as the angle) of a complex number.

  - `isnan()` yields True when either the real or the imaginary component of its argument is a NaN.

  - `isinf()` yields True when either the real or the imaginary component of its argument is infinite.

The rework also strengthened the numerical reliability of the [`cmath`](https://docs.python.org/3.14/library/cmath.html#module-cmath) module. Across every function, the real and imaginary portions of the outputs are correct to within a handful of units of least precision (ulps) wherever that can be achieved. The specifics are in [bpo-1381](https://bugs.python.org/issue?@action=redirect&bpo=1381). The branch cuts for `asinh()`, `atanh()`: and `atan()` were fixed as well.

The module’s test suite grew considerably; close to 2000 fresh test cases put the algebraic functions through their paces.

When run on IEEE 754 platforms, the [`cmath`](https://docs.python.org/3.14/library/cmath.html#module-cmath) module now treats IEEE 754 special values and floating-point exceptions the way Annex ‘G’ of the C99 standard prescribes.

- The [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) module introduces a fresh data type: `namedtuple(typename, fieldnames)` is a factory function producing subclasses of the ordinary tuple whose fields can be reached by name in addition to index. Here is an example:

```python
>>> var_type = collections.namedtuple('variable',
...             'id name type size')
>>> # Names are separated by spaces or commas.
>>> # 'id, name, type, size' would also work.
>>> var_type._fields
('id', 'name', 'type', 'size')

>>> var = var_type(1, 'frequency', 'int', 4)
>>> print var[0], var.id    # Equivalent
1 1
>>> print var[2], var.type  # Equivalent
int int
>>> var._asdict()
{'size': 4, 'type': 'int', 'id': 1, 'name': 'frequency'}
>>> v2 = var._replace(name='amplitude')
>>> v2
variable(id=1, name='amplitude', type='int', size=4)

```

A number of spots in the standard library that used to hand back plain tuples were reworked to hand back `namedtuple()` instances instead. As one case, the `Decimal.as_tuple()` method now hands back a named tuple carrying `sign`, `digits`, and `exponent` fields.

(Contributed by Raymond Hettinger.)

- A second update to the [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) module is that the `deque` type now accepts an optional *maxlen* argument; when given, the deque is held to at most *maxlen* items. Pushing further items onto a deque already at capacity drops the oldest items.

[Subject index](INDEX.md) · [Previous source section](interpreter-changes.md) · [Next source section](new-and-improved-modules-and-affecting-the-rest-of-the-line.md) · [Release/subject declaration](python-3-0.md)
