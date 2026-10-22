# importlib.metadata: `importlib.metadata.PackagePath`

*class *importlib.metadata.PackagePath

A [`pathlib.PurePath`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath) derived object that adds `dist`, `size`, and `hash` properties matching the distribution package’s installation metadata for that file.

The `files()` function accepts a [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package) name and returns every file the distribution installed. Each file comes back as a `PackagePath` instance. For instance:

```python
>>> util = [p for p in files('wheel') if 'util.py' in str(p)][0]
>>> util
PackagePath('wheel/util.py')
>>> util.size
859
>>> util.dist
<importlib.metadata._hooks.PathDistribution object at 0x101e0cef0>
>>> util.hash
<FileHash mode: sha256 value: bYkw5oMccfazVCoYQwKkkemoVyMAFoR34mmKBx8R1NI>

```

Having obtained the file, you can also read what it holds:

```python
>>> print(util.read_text())
import base64
import sys
...
def as_bytes(s):
    if isinstance(s, text_type):
        return s.encode('utf-8')
    return s

```

The `locate()` method is also available for getting the file’s absolute path:

```python
>>> util.locate()
PosixPath('/home/gustav/example/lib/site-packages/wheel/util.py')

```

When the metadata file that lists files (`RECORD` or `SOURCES.txt`) is absent, `files()` returns [`None`](https://docs.python.org/3.14/library/constants.html#None). A caller might want to wrap calls to `files()` in [always_iterable](https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.always_iterable) or otherwise protect against this case when the target distribution is not guaranteed to carry the metadata.

[Subject index](INDEX.md) · [Previous](importlib-metadata-files.md) · [Continue](importlib-metadata-requires.md) · [Owning module, declaration or section: importlib.metadata](importlib-metadata-packagenotfounderror.md) · [Owning module, declaration or section: Distribution files](importlib-metadata-files.md)
