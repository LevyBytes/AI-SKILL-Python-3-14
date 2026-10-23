# What's New In Python 3.13 / doctest - doctest

### doctest

- [`doctest`](https://docs.python.org/3.14/library/doctest.html#module-doctest) output henceforth carries color by default. Manage this through the fresh [`PYTHON_COLORS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_COLORS) environment variable together with the standard [`NO_COLOR`](https://no-color.org/) and [`FORCE_COLOR`](https://force-color.org/) environment variables. Refer additionally to [Controlling color](https://docs.python.org/3.14/using/cmdline.html#using-on-controlling-color). (Contributed by Hugo van Kemenade in [gh-117225](https://github.com/python/cpython/issues/117225).)

- The [`DocTestRunner.run()`](https://docs.python.org/3.14/library/doctest.html#doctest.DocTestRunner.run) method henceforth tallies how many tests were skipped. Add the [`DocTestRunner.skips`](https://docs.python.org/3.14/library/doctest.html#doctest.DocTestRunner.skips) and [`TestResults.skipped`](https://docs.python.org/3.14/library/doctest.html#doctest.TestResults.skipped) attributes. (Contributed by Victor Stinner in [gh-108794](https://github.com/python/cpython/issues/108794).)

[Subject index](INDEX.md) · [Previous source section](dis.md) · [Next source section](email.md) · [Release/subject declaration](summary-release-highlights.md)
