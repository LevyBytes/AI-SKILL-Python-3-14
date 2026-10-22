# importlib.metadata — Implementing Custom Providers

### Implementing Custom Providers

`importlib.metadata` covers two API surfaces — one for *consumers* and one for *providers*. The majority of users are consumers, taking in metadata that the packages supply. Other use cases exist, though, where users want to surface metadata by some alternative mechanism, such as next to a custom importer. A scenario like that calls for a *custom provider*.

Since [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package) metadata is not reachable via [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) searches or package loaders directly, a distribution’s metadata is located through import system [finders](https://docs.python.org/3.14/reference/import.html#finders-and-loaders). To locate a distribution package’s metadata, `importlib.metadata` consults the list of [meta path finders](https://docs.python.org/3.14/glossary.html#term-meta-path-finder) on [`sys.meta_path`](https://docs.python.org/3.14/library/sys.html#sys.meta_path).

The implementation wires hooks into the `PathFinder`, serving metadata for distribution packages discovered on the file system.

The abstract class [`importlib.abc.MetaPathFinder`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.MetaPathFinder) sets out the interface Python’s import system expects of finders. `importlib.metadata` widens this protocol by checking for an optional `find_distributions` callable on the finders from [`sys.meta_path`](https://docs.python.org/3.14/library/sys.html#sys.meta_path) and exposes this widened interface as the `DistributionFinder` abstract base class, which declares this abstract method:

```python
@abc.abstractmethod
def find_distributions(context=DistributionFinder.Context()) -> Iterable[Distribution]:
    """Return an iterable of all Distribution instances capable of
    loading the metadata for packages for the indicated ``context``.
    """

```

The `DistributionFinder.Context` object exposes `.path` and `.name` properties giving the path to search and the name to match, and it may carry other relevant context the consumer is after.

Concretely, when you want distribution package metadata to be found in a location away from the file system, subclass `Distribution` and fill in the abstract methods. A custom finder then returns instances of that derived `Distribution` from its `find_distributions()` method.

[Subject index](INDEX.md) · [Previous](distribution-discovery.md) · [Continue](example.md) · [Owning module, declaration or section: importlib.metadata](importlib-metadata-packagenotfounderror.md)
