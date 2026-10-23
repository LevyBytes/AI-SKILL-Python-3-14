# What's New In Python 3.4 / pydoc - inspect, pydoc

### pydoc

The [`pydoc`](https://docs.python.org/3.14/library/pydoc.html#module-pydoc) module rests directly upon the [`inspect.signature()`](https://docs.python.org/3.14/library/inspect.html#inspect.signature) introspection API, so it can surface signature details for a broader range of callable objects. The same shift means `__wrapped__` attributes are factored in while rendering help text. (Contributed by Larry Hastings in [bpo-19674](https://bugs.python.org/issue?@action=redirect&bpo=19674).)

The [`pydoc`](https://docs.python.org/3.14/library/pydoc.html#module-pydoc) module stops showing the `self` parameter on already bound methods. It instead strives to always print the precise current signature of whatever callable is supplied. (Contributed by Larry Hastings in [bpo-20710](https://bugs.python.org/issue?@action=redirect&bpo=20710).)

On top of the edits applied to [`pydoc`](https://docs.python.org/3.14/library/pydoc.html#module-pydoc) itself, the way it treats custom `__dir__` methods and assorted descriptor behaviours has likewise been sharpened considerably by the deeper changes within the [`inspect`](https://docs.python.org/3.14/library/inspect.html#module-inspect) module.

Given that the [`help()`](https://docs.python.org/3.14/library/functions.html#help) builtin draws on [`pydoc`](https://docs.python.org/3.14/library/pydoc.html#module-pydoc), the edits above carry over to how `help()` behaves too.

[Subject index](INDEX.md) · [Previous source section](pty.md) · [Next source section](re.md) · [Release/subject declaration](release-highlights.md)
