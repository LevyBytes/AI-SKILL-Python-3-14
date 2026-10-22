# importlib.metadata: `importlib.metadata.Distribution`

*class *importlib.metadata.Distribution

Details of an installed distribution package.

Note: distinct `Distribution` instances do not currently compare equal, even when they pertain to the same installed distribution and therefore share the same attributes.

Although the module level API described above is the most usual and handy approach, all of that information is reachable through the `Distribution` class. `Distribution` is an abstract object standing for the metadata of a Python [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package). To obtain, for an installed distribution package, the matching concrete `Distribution` subclass instance, call the `distribution()` function:

```python
>>> from importlib.metadata import distribution
>>> dist = distribution('wheel')
>>> type(dist)
<class 'importlib.metadata.PathDistribution'>

```

So another route to the version number runs through the `Distribution` instance:

```python
>>> dist.version
'0.32.3'

```

Many more kinds of metadata are reachable on `Distribution` instances:

```python
>>> dist.metadata['Requires-Python']
'>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*'
>>> dist.metadata['License']
'MIT'

```

For editable packages, an `origin` property may carry [**PEP 610**](https://peps.python.org/pep-0610/) metadata:

```python
>>> dist.origin.url
'file:///path/to/wheel-0.32.3.editable-py3-none-any.whl'

```

The complete set of metadata that is available is not documented here. Consult the PyPA [Core metadata specification](https://packaging.python.org/en/latest/specifications/core-metadata/#core-metadata) for more detail.

Added in version 3.13: The `.origin` property was added.

[Subject index](INDEX.md) · [Previous](importlib-metadata-distribution.md) · [Continue](distribution-discovery.md) · [Owning module, declaration or section: importlib.metadata](importlib-metadata-packagenotfounderror.md) · [Owning module, declaration or section: Distributions](importlib-metadata-distribution.md)
