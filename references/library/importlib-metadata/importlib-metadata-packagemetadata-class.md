# importlib.metadata: `importlib.metadata.PackageMetadata`

*class *importlib.metadata.PackageMetadata

A concrete realization of the [PackageMetadata protocol](https://importlib-metadata.readthedocs.io/en/latest/api.html#importlib_metadata.PackageMetadata).

Beyond offering the defined protocol methods and attributes, subscripting the instance behaves the same as calling the `get()` method.

Every [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package) carries some metadata, which the `metadata()` function lets you pull out:

```python
>>> wheel_metadata = metadata('wheel')

```

The keys of the structure returned name the metadata keywords, while the values come straight from the distribution metadata, unparsed:

```python
>>> wheel_metadata['Requires-Python']
'>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*'

```

`PackageMetadata` additionally offers a `json` attribute that gives back all the metadata in a JSON-compatible shape per [**PEP 566**](https://peps.python.org/pep-0566/):

```python
>>> wheel_metadata.json['requires_python']
'>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*'

```

The complete set of metadata that is available is not documented here. Consult the PyPA [Core metadata specification](https://packaging.python.org/en/latest/specifications/core-metadata/#core-metadata) for more detail.

Changed in version 3.10: The `Description` is now folded into the metadata where it is shown via the payload. Line continuation characters have been stripped out.

The `json` attribute was added.

[Subject index](INDEX.md) · [Previous](importlib-metadata-metadata.md) · [Continue](importlib-metadata-version.md) · [Owning module, declaration or section: importlib.metadata](importlib-metadata-packagenotfounderror.md) · [Owning module, declaration or section: Distribution metadata](importlib-metadata-metadata.md)
