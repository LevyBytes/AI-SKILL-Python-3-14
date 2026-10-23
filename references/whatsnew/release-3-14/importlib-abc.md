# What's new in Python 3.14 / importlib.abc - importlib, importlib.resources.abc

### importlib.abc

- The following deprecated [`importlib.abc`](https://docs.python.org/3.14/library/importlib.html#module-importlib.abc) classes have been dropped:

  - `ResourceReader` (use [`TraversableResources`](https://docs.python.org/3.14/library/importlib.resources.abc.html#importlib.resources.abc.TraversableResources))

  - `Traversable` (use [`Traversable`](https://docs.python.org/3.14/library/importlib.resources.abc.html#importlib.resources.abc.Traversable))

  - `TraversableResources` (use [`TraversableResources`](https://docs.python.org/3.14/library/importlib.resources.abc.html#importlib.resources.abc.TraversableResources))

(Contributed by Jason R. Coombs and Hugo van Kemenade in [gh-93963](https://github.com/python/cpython/issues/93963).)

[Subject index](INDEX.md) · [Previous source section](email.md) · [Next source section](itertools.md) · [Release/subject declaration](summary-release-highlights.md)
