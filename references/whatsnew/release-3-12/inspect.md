# What’s New In Python 3.12 / inspect — inspect

### inspect

- Add [`inspect.markcoroutinefunction()`](https://docs.python.org/3.14/library/inspect.html#inspect.markcoroutinefunction) for tagging sync functions that hand back a [coroutine](https://docs.python.org/3.14/glossary.html#term-coroutine), so they cooperate with [`inspect.iscoroutinefunction()`](https://docs.python.org/3.14/library/inspect.html#inspect.iscoroutinefunction). (Contributed by Carlton Gibson in [gh-99247](https://github.com/python/cpython/issues/99247).)

- Add [`inspect.getasyncgenstate()`](https://docs.python.org/3.14/library/inspect.html#inspect.getasyncgenstate) along with [`inspect.getasyncgenlocals()`](https://docs.python.org/3.14/library/inspect.html#inspect.getasyncgenlocals) to find out the present state of asynchronous generators. (Contributed by Thomas Krennwallner in [gh-79940](https://github.com/python/cpython/issues/79940).)

- [`inspect.getattr_static()`](https://docs.python.org/3.14/library/inspect.html#inspect.getattr_static) runs considerably quicker now. The bulk of calls should clock in at no less than 2x the speed seen in Python 3.11. (Contributed by Alex Waygood in [gh-103193](https://github.com/python/cpython/issues/103193).)

[Subject index](INDEX.md) · [Previous source section](importlib-resources.md) · [Next source section](itertools.md) · [Release/subject declaration](summary-release-highlights.md)
