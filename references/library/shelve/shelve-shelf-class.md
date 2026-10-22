# shelve: `shelve.Shelf`

### Restrictions

- Whichever database package gets picked (be it [`dbm.ndbm`](https://docs.python.org/3.14/library/dbm.html#module-dbm.ndbm) or [`dbm.gnu`](https://docs.python.org/3.14/library/dbm.html#module-dbm.gnu)) comes down to which interface happens to be on hand. For that reason, opening the database straight through [`dbm`](https://docs.python.org/3.14/library/dbm.html#module-dbm) is not safe. On top of that, the database inherits (regrettably) whatever caps `dbm` carries when it is the one in play — which means the objects kept in the database (in their pickled form) had better stay on the small side, and now and again a key collision can make the database turn down updates.

- There is no provision in the `shelve` module for *concurrent* read/write access to shelved objects. (Several read accesses happening at once pose no problem.) While one program holds a shelf open for writing, no second program ought to have it open for either reading or writing. You can lean on Unix file locking to address this, though its behavior shifts from one Unix release to another and it demands familiarity with whichever database build is in use.

- Under macOS, [`dbm.ndbm`](https://docs.python.org/3.14/library/dbm.html#module-dbm.ndbm) may quietly wreck the database file as updates land, and that damage can trigger outright crashes the next time you attempt a read from the database.

 *class *shelve.Shelf(*dict*, *protocol=None*, *writeback=False*, *keyencoding='utf-8'*)

This is a subclass of [`collections.abc.MutableMapping`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.MutableMapping), and it tucks pickled values away inside the *dict* object.

By default, value serialization runs through pickles built with [`pickle.DEFAULT_PROTOCOL`](https://docs.python.org/3.14/library/pickle.html#pickle.DEFAULT_PROTOCOL). You may pin down which pickle protocol version applies by way of the *protocol* parameter. The [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) docs walk through those protocols at length.

Should the *writeback* parameter be `True`, the object keeps a cache covering every entry you touch and flushes them back into the *dict* whenever sync and close occur. That opens the door to working naturally with mutable entries, though it can eat up a good deal more memory and stretch out how long sync and close run.

What the *keyencoding* parameter sets is the encoding applied to keys ahead of their use against the dict underneath.

You can equally drive a `Shelf` object as a context manager; go that route and it shuts itself the moment the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) block finishes.

Changed in version 3.2: the *keyencoding* parameter arrived; up to that point keys had always been encoded as UTF-8.

Changed in version 3.4: Added context manager support.

Changed in version 3.10: the default pickle protocol has switched over to [`pickle.DEFAULT_PROTOCOL`](https://docs.python.org/3.14/library/pickle.html#pickle.DEFAULT_PROTOCOL).

[Subject index](INDEX.md) · [Previous](shelve-open-to-shelf-close.md) · [Continue](shelve-bsddbshelf-class.md) · [Owning module, declaration or section: shelve](shelve-open-to-shelf-close.md)
