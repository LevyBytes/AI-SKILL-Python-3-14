# -v

-v

Emit a message whenever a module gets initialized, naming the location (a filename or built-in module) it was loaded from. Supplied twice (`-vv`), it emits a message for every file checked during the search for a module. It also reports on module cleanup as the interpreter exits.

Changed in version 3.10: the [`site`](https://docs.python.org/3.14/library/site.html#module-site) module now lists which site-specific paths and `.pth` files it works through.

See also `PYTHONVERBOSE`.

[Subject index](INDEX.md) · [Previous source section](unbuffered-streams.md) · [Following source section](warning-filter.md)
