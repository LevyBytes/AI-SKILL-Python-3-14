# importlib.metadata — Example

### Example

Picture a custom finder that loads Python modules out of a database:

```python
class DatabaseImporter(importlib.abc.MetaPathFinder):
    def __init__(self, db):
        self.db = db

    def find_spec(self, fullname, target=None) -> ModuleSpec:
        return self.db.spec_from_name(fullname)

sys.meta_path.append(DatabaseImporter(connect_db(...)))

```

That importer presumably now makes importable modules available from a database, but it provides neither metadata nor entry points. For this custom importer to provide metadata as well, it would also need to implement `DistributionFinder`:

```python
from importlib.metadata import DistributionFinder

class DatabaseImporter(DistributionFinder):
    ...

    def find_distributions(self, context=DistributionFinder.Context()):
        query = dict(name=context.name) if context.name else {}
        for dist_record in self.db.query_distributions(query):
            yield DatabaseDistribution(dist_record)

```

Here `query_distributions` would yield records for each distribution the database serves that matches the query. As an example, were `requests-1.0` present in the database, `find_distributions` would yield a `DatabaseDistribution` for `Context(name='requests')` or `Context(name=None)`.

To keep things simple, this example disregards `context.path`. The `path` attribute defaults to `sys.path` and holds the collection of import paths to weigh in the search. A `DatabaseImporter` might well operate with no regard for a search path. Provided the importer does no partitioning, the “path” would be beside the point. To bring out the purpose of `path`, the example would have to show a more involved `DatabaseImporter` whose behavior shifted according to `sys.path`/`PYTHONPATH`. In that situation, the `find_distributions` ought to honor the `context.path` and yield only the `Distribution`s relevant to that path.

`DatabaseDistribution`, then, would resemble this:

```python
class DatabaseDistribution(importlib.metadata.Distribution):
    def __init__(self, record):
        self.record = record

    def read_text(self, filename):
        """
        Read a file like "METADATA" for the current distribution.
        """
        if filename == "METADATA":
            return f"""Name: {self.record.name}
Version: {self.record.version}
"""
        if filename == "entry_points.txt":
            return "\n".join(
              f"""[{ep.group}]\n{ep.name}={ep.value}"""
              for ep in self.record.entry_points)

    def locate_file(self, path):
        raise RuntimeError("This distribution has no file system")

```

This minimal implementation ought to supply metadata and entry points for packages the `DatabaseImporter` serves, assuming the `record` provides fitting `.name`, `.version`, and `.entry_points` attributes.

The `DatabaseDistribution` might also expose further metadata files, such as `RECORD` (required for `Distribution.files`) or override how `Distribution.files` is implemented. Look to the source for more inspiration.

[Subject index](INDEX.md) · [Previous](implementing-custom-providers.md) · [Owning module, declaration or section: importlib.metadata](importlib-metadata-packagenotfounderror.md)
