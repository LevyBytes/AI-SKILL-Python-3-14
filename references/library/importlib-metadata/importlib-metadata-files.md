# importlib.metadata: `importlib.metadata.files()`

### Distribution files

 importlib.metadata.files(*distribution_name*)

Return the complete set of files held within the named distribution package.

Raises `PackageNotFoundError` when the named distribution package is not installed in the current Python environment.

Returns [`None`](https://docs.python.org/3.14/library/constants.html#None) when the distribution is located but the installation database entries reporting the files tied to the distribution package are absent.

[Subject index](INDEX.md) · [Previous](importlib-metadata-version.md) · [Continue](importlib-metadata-packagepath-class.md) · [Owning module, declaration or section: importlib.metadata](importlib-metadata-packagenotfounderror.md)
