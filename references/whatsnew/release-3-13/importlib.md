# What's New In Python 3.13 / importlib

### importlib

-

These [`importlib.resources`](https://docs.python.org/3.14/library/importlib.resources.html#module-importlib.resources) functions can now reach into a directory (or whole tree) of resources by accepting several positional arguments. For the text readers, *encoding* and *errors* have become keyword-only:

  - [`is_resource()`](https://docs.python.org/3.14/library/importlib.resources.html#importlib.resources.is_resource)

  - [`open_binary()`](https://docs.python.org/3.14/library/importlib.resources.html#importlib.resources.open_binary)

  - [`open_text()`](https://docs.python.org/3.14/library/importlib.resources.html#importlib.resources.open_text)

  - [`path()`](https://docs.python.org/3.14/library/importlib.resources.html#importlib.resources.path)

  - [`read_binary()`](https://docs.python.org/3.14/library/importlib.resources.html#importlib.resources.read_binary)

  - [`read_text()`](https://docs.python.org/3.14/library/importlib.resources.html#importlib.resources.read_text)

Their deprecation has been lifted, and removal is no longer planned. (Contributed by Petr Viktorin in [gh-116608](https://github.com/python/cpython/issues/116608).)

- [`contents()`](https://docs.python.org/3.14/library/importlib.resources.html#importlib.resources.contents) keeps its deprecated status, with the richer [`Traversable`](https://docs.python.org/3.14/library/importlib.resources.abc.html#importlib.resources.abc.Traversable) API preferred instead. Even so, removing it is no longer planned. (Contributed by Petr Viktorin in [gh-116608](https://github.com/python/cpython/issues/116608).)

[Subject index](INDEX.md) · [Previous source section](glob.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](io.md)
