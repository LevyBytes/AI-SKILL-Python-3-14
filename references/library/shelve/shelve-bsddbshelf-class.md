# shelve: `shelve.BsdDbShelf`

*class *shelve.BsdDbShelf(*dict*, *protocol=None*, *writeback=False*, *keyencoding='utf-8'*)

A subclass of `Shelf` that surfaces the `first()`, `next()`, `previous()`, `last()` and `set_location()` methods. You will find these in the third-party `bsddb` module out of [pybsddb](https://www.jcea.es/programacion/pybsddb.htm), though no other database modules carry them. Whatever *dict* object you feed the constructor has to provide those methods. The usual way to arrange that is to call one among `bsddb.hashopen()`, `bsddb.btopen()` or `bsddb.rnopen()`. As for the optional *protocol*, *writeback*, and *keyencoding* parameters, they read exactly as they do for the `Shelf` class.

[Subject index](INDEX.md) · [Previous](shelve-shelf-class.md) · [Continue](shelve-dbfilenameshelf-class.md) · [Owning module, declaration or section: shelve](shelve-open-to-shelf-close.md) · [Owning module, declaration or section: Restrictions](shelve-shelf-class.md)
