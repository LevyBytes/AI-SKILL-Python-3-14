# What’s New in Python 2.3 / New, Improved, and Deprecated Modules - array, bz2, datetime, doctest, getopt, grp, gzip, heapq, pwd, resource, unittest, zlib

### New, Improved, and Deprecated Modules

As is customary, Python's standard library picked up numerous improvements and bug fixes. Below is a partial roundup of the most noteworthy changes, arranged alphabetically by module name. Check the `Misc/NEWS` file within the source tree for a fuller list of changes, or browse the CVS logs for every detail.

- The [`array`](https://docs.python.org/3.14/library/array.html#module-array) module can now hold arrays of Unicode characters via the `'u'` format character. Arrays additionally support the `+=` assignment operator to append the contents of another array, and the `*=` assignment operator to repeat an array. (Contributed by Jason Orendorff.)

- Version 4.1.6 of the [PyBSDDB](https://pybsddb.sourceforge.net) package now stands in for the `bsddb` module, offering a fuller interface to the transactional capabilities of the BerkeleyDB library.

The module's former version was renamed `bsddb185` and is no longer compiled automatically; you'll need to edit `Modules/Setup` to turn it on. Bear in mind that the new `bsddb` package aims for compatibility with the old module, so please report bugs if you run into any incompatibilities. When you move to Python 2.3, if the fresh interpreter is built against a newer version of the underlying BerkeleyDB library, you will almost surely need to migrate your database files to the new version. The distribution's `Tools/scripts` directory provides the new scripts `db2pickle.py` and `pickle2db.py`, which make this reasonably straightforward. If you have already been working with the PyBSDDB package and importing it as `bsddb3`, you will need to update your `import` statements to import it as `bsddb`.

- The fresh [`bz2`](https://docs.python.org/3.14/library/bz2.html#module-bz2) module wraps the bz2 data compression library. Data compressed with bz2 is generally smaller than the equivalent [`zlib`](https://docs.python.org/3.14/library/zlib.html#module-zlib)-compressed data. (Contributed by Gustavo Niemeyer.)

- A collection of standard date/time types now lives in the new [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime) module. Consult the next section for further details.

- The Distutils `Extension` class now accepts an additional constructor argument called *depends* for naming extra source files on which an extension relies. This allows Distutils to rebuild the module whenever any of the dependency files change. As an example, if `sampmodule.c` pulls in the header file `sample.h`, you would build the `Extension` object as follows:

```python
ext = Extension("samp",
                sources=["sampmodule.c"],
                depends=["sample.h"])

```

Editing `sample.h` would in turn trigger the module to be rebuilt. (Contributed by Jeremy Hylton.)

- Some additional minor Distutils changes: it now inspects the [`CC`](https://docs.python.org/3.14/using/configure.html#envvar-CC), [`CFLAGS`](https://docs.python.org/3.14/using/configure.html#envvar-CFLAGS), `CPP`, [`LDFLAGS`](https://docs.python.org/3.14/using/configure.html#envvar-LDFLAGS), and [`CPPFLAGS`](https://docs.python.org/3.14/using/configure.html#envvar-CPPFLAGS) environment variables, applying them to override what Python's configuration specifies (contributed by Robert Weber).

- In the past the [`doctest`](https://docs.python.org/3.14/library/doctest.html#module-doctest) module looked for test cases only inside the docstrings of public methods and functions, but private ones now get examined as well. The [`DocTestSuite()`](https://docs.python.org/3.14/library/doctest.html#doctest.DocTestSuite) function builds a [`unittest.TestSuite`](https://docs.python.org/3.14/library/unittest.html#unittest.TestSuite) object out of a collection of `doctest` tests.

- The new `gc.get_referents(object)` function hands back a list of every object that *object* references.

- The [`getopt`](https://docs.python.org/3.14/library/getopt.html#module-getopt) module acquired a new function, [`gnu_getopt()`](https://docs.python.org/3.14/library/getopt.html#getopt.gnu_getopt), accepting the same arguments as the existing [`getopt()`](https://docs.python.org/3.14/library/getopt.html#getopt.getopt) function but applying GNU-style scanning mode. The existing `getopt()` halts option processing the moment a non-option argument turns up, whereas GNU-style mode keeps going, so options and arguments may be interleaved. For instance:

```python
>>> getopt.getopt(['-f', 'filename', 'output', '-v'], 'f:v')
([('-f', 'filename')], ['output', '-v'])
>>> getopt.gnu_getopt(['-f', 'filename', 'output', '-v'], 'f:v')
([('-f', 'filename'), ('-v', '')], ['output'])

```

(Contributed by Peter ??strand.)

- The [`grp`](https://docs.python.org/3.14/library/grp.html#module-grp), [`pwd`](https://docs.python.org/3.14/library/pwd.html#module-pwd), and [`resource`](https://docs.python.org/3.14/library/resource.html#module-resource) modules now hand back enhanced tuples:

```python
>>> import grp
>>> g = grp.getgrnam('amk')
>>> g.gr_name, g.gr_gid
('amk', 500)

```

- The [`gzip`](https://docs.python.org/3.14/library/gzip.html#module-gzip) module can now cope with files larger than 2 GiB.

- The new [`heapq`](https://docs.python.org/3.14/library/heapq.html#module-heapq) module supplies an implementation of a heap queue algorithm. A heap is an array-style data structure that holds items in a partially ordered arrangement where, for each index *k*, `heap[k] <= heap[2*k+1]` and `heap[k] <= heap[2*k+2]`. That makes pulling off the smallest item fast, while adding a fresh item and keeping the heap property intact costs *O*(log *n*). (Consult [https://xlinux.nist.gov/dads//HTML/priorityque.html](https://xlinux.nist.gov/dads//HTML/priorityque.html) for further detail on the priority queue data structure.)

The [`heapq`](https://docs.python.org/3.14/library/heapq.html#module-heapq) module offers [`heappush()`](https://docs.python.org/3.14/library/heapq.html#heapq.heappush) and [`heappop()`](https://docs.python.org/3.14/library/heapq.html#heapq.heappop) functions to add and remove items while keeping the heap property intact atop some other mutable Python sequence type. The example below is built around an ordinary Python list:

[Subject index](INDEX.md) · [Previous source section](optimizations.md) · [Next source section](idle-iterators-networking-and-system-module-changes.md) · [Release/subject declaration](standard-set-type.md)
