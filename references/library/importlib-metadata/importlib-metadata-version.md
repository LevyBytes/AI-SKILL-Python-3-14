# importlib.metadata — Distribution versions

### Distribution versions

 importlib.metadata.version(*distribution_name*)

Return the installed distribution package [version](https://packaging.python.org/en/latest/specifications/core-metadata/#version) for the named distribution package.

Raises `PackageNotFoundError` when the named distribution package is not installed in the current Python environment.

The `version()` function is the fastest route to a [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package)’s version number, returned as a string:

```python
>>> version('wheel')
'0.32.3'

```

[Subject index](INDEX.md) · [Previous](importlib-metadata-packagemetadata-class.md) · [Continue](importlib-metadata-files.md) · [Owning module, declaration or section: importlib.metadata](importlib-metadata-packagenotfounderror.md)
