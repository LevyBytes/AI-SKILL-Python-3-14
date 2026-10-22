# shelve: `shelve.DbfilenameShelf`

*class *shelve.DbfilenameShelf(*filename*, *flag='c'*, *protocol=None*, *writeback=False*)

A subclass of `Shelf` that takes a *filename* in place of a dict-like object. Opening the file underneath happens through [`dbm.open()`](https://docs.python.org/3.14/library/dbm.html#dbm.open). By default the file is brought into being and opened for reading as well as writing. The optional *flag* parameter reads the same way it does for the `open()` function. Likewise the optional *protocol* and *writeback* parameters carry the same meaning they hold for the `Shelf` class.

[Subject index](INDEX.md) · [Previous](shelve-bsddbshelf-class.md) · [Continue](example.md) · [Owning module, declaration or section: shelve](shelve-open-to-shelf-close.md) · [Owning module, declaration or section: Restrictions](shelve-shelf-class.md)
