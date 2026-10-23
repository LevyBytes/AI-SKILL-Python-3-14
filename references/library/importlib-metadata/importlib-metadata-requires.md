# importlib.metadata - Distribution requirements

### Distribution requirements

 importlib.metadata.requires(*distribution_name*)

Return the declared dependency specifiers for the named distribution package.

Raises `PackageNotFoundError` when the named distribution package is not installed in the current Python environment.

To get the complete set of requirements for a [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package), call the `requires()` function:

```python
>>> requires('wheel')
["pytest (>=3.0.0) ; extra == 'test'", "pytest-cov ; extra == 'test'"]

```

[Subject index](INDEX.md) · [Previous](importlib-metadata-packagepath-class.md) · [Continue](importlib-metadata-packages-distributions.md) · [Owning module, declaration or section: importlib.metadata](importlib-metadata-packagenotfounderror.md)
