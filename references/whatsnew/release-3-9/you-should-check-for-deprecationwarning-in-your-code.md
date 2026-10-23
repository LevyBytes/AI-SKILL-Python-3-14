# What's New In Python 3.9 / You should check for DeprecationWarning in your code - collections, collections.abc, devmode, warnings

### You should check for DeprecationWarning in your code

While Python 2.7 remained supported, much functionality inside Python 3 stayed present to preserve compatibility with the 2.7 series. Now that 2 has reached its end, those compatibility shims are either gone or scheduled to disappear shortly. The majority raised a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) warning across many years. As an illustration, reaching for `collections.Mapping` rather than `collections.abc.Mapping` triggers a `DeprecationWarning` going back to Python 3.3, which shipped in 2012.

Exercise your program under the [`-W`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-W) `default` command-line flag so that [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) and [`PendingDeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#PendingDeprecationWarning) surface, or run `-W` `error` to promote them into failures. The [Warnings Filter](https://docs.python.org/3.14/library/warnings.html#warning-filter) lets you suppress warnings originating in third-party code.

This is the final release that ships those Python 2 compatibility shims, granting maintainers of Python projects additional runway to plan dropping Python 2 and to wire in Python 3.9 support.

The aliases pointing at [Abstract Base Classes](https://docs.python.org/3.14/library/collections.abc.html#collections-abstract-base-classes) inside the [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) module ? for instance `collections.Mapping` aliasing [`collections.abc.Mapping`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Mapping) ? survive one final release for the sake of compatibility. Python 3.10 will drop them.

As broader advice, exercise your test suite under the [Python Development Mode](https://docs.python.org/3.14/library/devmode.html#devmode), which assists in readying your code for compatibility with the upcoming Python release.

Note: this Python version also dropped a batch of deprecations that predated it. Consult the Removed section.

[Subject index](INDEX.md) · [Previous source section](summary-release-highlights.md) · [Next source section](dictionary-merge-update-operators.md) · [Release/subject declaration](summary-release-highlights.md)
