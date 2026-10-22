# How do you implement persistent objects in Python?

### How do you implement persistent objects in Python?

The [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) library module tackles this broadly (you still cannot stash items such as open files, sockets, or windows), while the [`shelve`](https://docs.python.org/3.14/library/shelve.html#module-shelve) library module layers pickle together with (g)dbm to build durable mappings that hold arbitrary Python objects.

[Subject index](INDEX.md)
