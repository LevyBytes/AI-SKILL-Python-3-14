# What’s New in Python 2.3 / PEP 302: New Import Hooks - sys

### PEP 302: New Import Hooks

Custom import hooks have been writable all the way back to Python 1.3, when the `ihooks` module arrived, yet nobody was ever truly satisfied with it, since crafting new import hooks proved hard and untidy. Several substitutes were floated, among them the `imputil` and `iu` modules, but none caught on widely and none could be used easily from C code.

[**PEP 302**](https://peps.python.org/pep-0302/) draws on what came before it, in particular Gordon McMillan's `iu` module. It adds three new entries to the [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) module:

- `sys.path_hooks` holds a list of callables; usually these are classes. Given a string holding a path, each callable either yields an importer object that handles imports off that path, or throws an [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) exception when it can't deal with the path.

- `sys.path_importer_cache` stores importer objects keyed by path, which means `sys.path_hooks` has to be walked just one time per path.

- `sys.meta_path` is a list of importer objects consulted ahead of any check against `sys.path`. It starts out empty, though user code may append objects to it. An object placed here can import extra built-in and frozen modules.

Each importer object needs one method, `find_module(fullname, path=None)`. *fullname* will hold a module or package name — for instance `string` or `distutils.core`. `find_module()` has to give back a loader object exposing a lone method, `load_module(fullname)`, which builds and returns the matching module object.

So Python's revised import logic in pseudo-code comes out roughly as follows (somewhat simplified; refer to [**PEP 302**](https://peps.python.org/pep-0302/) for every detail):

```python
for mp in sys.meta_path:
    loader = mp(fullname)
    if loader is not None:
        <module> = loader.load_module(fullname)

for path in sys.path:
    for hook in sys.path_hooks:
        try:
            importer = hook(path)
        except ImportError:
            # ImportError, so try the other path hooks
            pass
        else:
            loader = importer.find_module(fullname)
            <module> = loader.load_module(fullname)

# Not found!
raise ImportError

```

See also

[**PEP 302**](https://peps.python.org/pep-0302/) - New Import Hooks

Authored by Paul Moore together with Just van Rossum; the implementation was done by Just van Rossum.

[Subject index](INDEX.md) · [Previous source section](pep-301-package-index-and-metadata-for-distutils.md) · [Next source section](pep-305-comma-separated-files.md) · [Release/subject declaration](standard-set-type.md)
