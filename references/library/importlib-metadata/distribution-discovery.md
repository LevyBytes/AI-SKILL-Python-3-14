# importlib.metadata — Distribution Discovery

### Distribution Discovery

By default, this package ships built-in support for discovering metadata of file system and zip file [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package)s. This metadata finder search defaults to `sys.path`, yet it reads those values somewhat differently from how the rest of the import machinery does. In particular:

- `importlib.metadata` does not honor [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) objects on `sys.path`.

- `importlib.metadata` will incidentally honor [`pathlib.Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) objects on `sys.path` even though those values are skipped for imports.

[Subject index](INDEX.md) · [Previous](importlib-metadata-distribution-class.md) · [Continue](implementing-custom-providers.md) · [Owning module, declaration or section: importlib.metadata](importlib-metadata-packagenotfounderror.md)
