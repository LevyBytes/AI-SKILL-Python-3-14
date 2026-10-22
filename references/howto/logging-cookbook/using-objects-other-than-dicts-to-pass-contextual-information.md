# Using objects other than dicts to pass contextual information

#### Using objects other than dicts to pass contextual information

Handing an actual dict to a [`LoggerAdapter`](https://docs.python.org/3.14/library/logging.html#logging.LoggerAdapter) isn't required — you could instead pass an instance of a class that defines `__getitem__` and `__iter__` so that, as far as logging is concerned, it behaves like a dict. This comes in handy when you want the values produced dynamically (since the values stored in a dict would stay fixed).

[Subject index](INDEX.md) · [Previous source context](using-loggeradapters-to-impart-contextual-information.md) · [Following source context](using-filters-to-impart-contextual-information.md)
