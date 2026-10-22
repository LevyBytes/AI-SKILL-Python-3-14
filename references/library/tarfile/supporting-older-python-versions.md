# tarfile — Supporting older Python versions

### Supporting older Python versions

Extraction filters arrived in Python 3.12, though they may be backported to earlier releases as security updates. Rather than testing the Python version, determine whether the feature is present with something like `hasattr(tarfile, 'data_filter')`.

The examples that follow demonstrate how to handle Python releases both with and without the feature. Keep in mind that assigning `extraction_filter` carries over to any operations that come afterward.

- Fully trusted archive:

```python
my_tarfile.extraction_filter = (lambda member, path: member)
my_tarfile.extractall()

```

- Apply the `'data'` filter when it exists, but fall back to the Python 3.11 behavior (`'fully_trusted'`) when this feature is absent:

```python
my_tarfile.extraction_filter = getattr(tarfile, 'data_filter',
                                       (lambda member, path: member))
my_tarfile.extractall()

```

- Apply the `'data'` filter; *fail* when it is absent:

```python
my_tarfile.extractall(filter=tarfile.data_filter)

```

or:

```python
my_tarfile.extraction_filter = tarfile.data_filter
my_tarfile.extractall()

```

- Apply the `'data'` filter; *warn* when it is absent:

```python
if hasattr(tarfile, 'data_filter'):
    my_tarfile.extractall(filter='data')
else:
    # remove this when no longer needed
    warn_the_user('Extracting may be unsafe; consider updating Python')
    my_tarfile.extractall()

```

[Subject index](INDEX.md) · [Previous](hints-for-further-verification.md) · [Continue](stateful-extraction-filter-example.md) · [Owning module, declaration or section: tarfile](tarfile-read-and-write-tar-archive-files.md)
