# What's new in Python 3.14 / functools - functools

### functools

- The [`Placeholder`](https://docs.python.org/3.14/library/functools.html#functools.Placeholder) sentinel was added. Pair it with the [`partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial) or [`partialmethod()`](https://docs.python.org/3.14/library/functools.html#functools.partialmethod) functions to hold a slot for positional arguments inside the resulting [partial object](https://docs.python.org/3.14/library/functools.html#partial-objects). (Contributed by Dominykas Grigonis in [gh-119127](https://github.com/python/cpython/issues/119127).)

- You can now pass the *initial* parameter of [`reduce()`](https://docs.python.org/3.14/library/functools.html#functools.reduce) as a keyword argument. (Contributed by Sayandip Dutta in [gh-125916](https://github.com/python/cpython/issues/125916).)

[Subject index](INDEX.md) · [Previous source section](fractions.md) · [Next source section](getopt.md) · [Release/subject declaration](summary-release-highlights.md)
