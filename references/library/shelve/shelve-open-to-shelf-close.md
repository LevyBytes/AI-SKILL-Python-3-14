# shelve — `shelve` — Python object persistence

## shelve — Python object persistence

### `shelve` — Python object persistence

**Source code:** [Lib/shelve.py](https://github.com/python/cpython/tree/3.14/Lib/shelve.py)

---

What a “shelf” amounts to is a durable object that behaves like a dictionary. Where it parts ways with “dbm” databases is that a shelf's values (mind you, not its keys) may be more or less any Python object at all — whatever the [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) module is able to process. That stretches to cover the bulk of class instances, self-referential data structures, and objects that hold heaps of sub-objects shared among themselves. As for the keys, they stay plain strings.

 shelve.open(*filename*, *flag='c'*, *protocol=None*, *writeback=False*)

Open up a durable dictionary. Whatever filename you hand in serves as the base name for the database sitting underneath. One side effect is that an extension might get tacked onto the filename and that several files might end up created. Out of the box, the backing database file opens for both reading and writing. That optional *flag* parameter carries the very same meaning as the *flag* parameter belonging to [`dbm.open()`](https://docs.python.org/3.14/library/dbm.html#dbm.open).

By default, value serialization runs through pickles built with [`pickle.DEFAULT_PROTOCOL`](https://docs.python.org/3.14/library/pickle.html#pickle.DEFAULT_PROTOCOL). You may pin down which pickle protocol version applies by way of the *protocol* parameter.

Owing to how Python works, a shelf has no way of detecting the moment a mutable persistent-dictionary entry gets changed. As shipped, an altered object is committed *only* at the point it is assigned into the shelf (consult the Example). Switch the optional *writeback* parameter on with `True`, and now every entry you touch is held in a memory cache as well, then flushed back during `sync()` and `close()`; that does make tweaking mutable entries in the persistent dictionary more convenient, yet once a great many entries get touched it can devour enormous quantities of memory for the cache and drag the close step out badly, because each touched entry is flushed back (nothing can tell which touched entries are mutable, let alone which were truly mutated).

Changed in version 3.10: the default pickle protocol has switched over to [`pickle.DEFAULT_PROTOCOL`](https://docs.python.org/3.14/library/pickle.html#pickle.DEFAULT_PROTOCOL).

Changed in version 3.11: Accepts [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) for filename.

Note

Never count on the shelf shutting itself; once you are done with it, invoke `close()` yourself every time, or else drive `shelve.open()` through a context manager:

```python
with shelve.open('spam') as db:
    db['eggs'] = 'eggs'

```

Warning

Since [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) sits behind the `shelve` module, pulling in a shelf from a source you do not trust is unsafe. Just as with pickle, the act of loading a shelf may run arbitrary code.

Most of the methods and operations that dictionaries offer carry over to Shelf objects too (copying, constructors, and the `|` and `|=` operators being the exceptions). That smooths the move from scripts built on dictionaries toward ones that call for durable storage.

On top of those, a pair of further methods is available:

 Shelf.sync()

Flush every cached entry back out, provided the shelf was opened with *writeback* turned to [`True`](https://docs.python.org/3.14/library/constants.html#True). Beyond that, clear the cache and, where it can be done, bring the on-disk persistent dictionary into sync. The system fires this off on its own whenever the shelf gets shut via `close()`.

 Shelf.close()

Bring the persistent *dict* object into sync and then shut it. Any operation attempted against a shelf already closed raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError).

See also

[Persistent dictionary recipe](https://code.activestate.com/recipes/576642-persistent-dict-with-multiple-standard-file-format/) that leans on broadly available storage formats while keeping the pace of built-in dictionaries.

[Subject index](INDEX.md) · [Continue](shelve-shelf-class.md)
