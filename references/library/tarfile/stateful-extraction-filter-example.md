# tarfile — Stateful extraction filter example

### Stateful extraction filter example

Although *tarfile*'s extraction methods accept a plain *filter* callable, custom filters can be richer objects that keep internal state. Writing them as context managers, to be used in the following way, can come in handy:

```python
with StatefulFilter() as filter_func:
    tar.extractall(path, filter=filter_func)

```

One way to write such a filter is, for example:

```python
class StatefulFilter:
    def __init__(self):
        self.file_count = 0

    def __enter__(self):
        return self

    def __call__(self, member, path):
        self.file_count += 1
        return member

    def __exit__(self, *exc_info):
        print(f'{self.file_count} files extracted')

```

[Subject index](INDEX.md) · [Previous](supporting-older-python-versions.md) · [Continue](command-line-interface.md) · [Owning module, declaration or section: tarfile](tarfile-read-and-write-tar-archive-files.md)
