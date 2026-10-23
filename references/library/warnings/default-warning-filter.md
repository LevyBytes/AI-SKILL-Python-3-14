# warnings - Default Warning Filter

### Default Warning Filter

Out of the box, Python sets up a handful of warning filters; you can override them with the [`-W`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-W) command-line option, the [`PYTHONWARNINGS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONWARNINGS) environment variable, and calls to `filterwarnings()`.

For ordinary release builds, these are the entries in the default warning filter (listed from highest precedence to lowest):

```python
default::DeprecationWarning:__main__
ignore::DeprecationWarning
ignore::PendingDeprecationWarning
ignore::ImportWarning
ignore::ResourceWarning

```

For a [debug build](https://docs.python.org/3.14/using/configure.html#debug-build), there are no default warning filters at all.

Changed in version 3.2: alongside [`PendingDeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#PendingDeprecationWarning), [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) is from now on ignored by default.

Changed in version 3.7: when raised straight from code running in `__main__`, [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) is once more displayed by default.

Changed in version 3.7: [`BytesWarning`](https://docs.python.org/3.14/library/exceptions.html#BytesWarning) has dropped out of the default filter list; instead it is set up through [`sys.warnoptions`](https://docs.python.org/3.14/library/sys.html#sys.warnoptions) whenever [`-b`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-b) appears twice.

[Subject index](INDEX.md) · [Previous](describing-warning-filters.md) · [Continue](overriding-the-default-filter.md) · [Owning module, declaration or section: warnings](warnings-warning-control.md)
