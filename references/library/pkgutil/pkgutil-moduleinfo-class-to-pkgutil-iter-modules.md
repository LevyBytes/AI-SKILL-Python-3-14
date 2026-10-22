# pkgutil: `pkgutil.ModuleInfo`, `pkgutil.extend_path()`, `pkgutil.get_importer()`, `pkgutil.iter_importers()`, `pkgutil.iter_modules()`

## pkgutil — Package extension utility

### `pkgutil` — Package extension utility

**Source code:** [Lib/pkgutil.py](https://github.com/python/cpython/tree/3.14/Lib/pkgutil.py)

---

Aimed at the import system, this module supplies helper utilities, with a focus on supporting packages.

 *class *pkgutil.ModuleInfo(*module_finder*, *name*, *ispkg*)

A namedtuple carrying a short rundown of a module's details.

Added in version 3.6.

 pkgutil.extend_path(*path*, *name*)

Broadens the search path covering the modules that make up a package. The way it's meant to be used is by dropping the code below into a package's `__init__.py`:

```python
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

```

Wherever a directory on [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) holds a subdirectory whose name equals the package name, that subdirectory gets appended to the package's [`__path__`](https://docs.python.org/3.14/reference/datamodel.html#module.__path__). It comes in handy when you'd like to spread the pieces of one logical package across several directories.

On top of that, it hunts for `*.pkg` files whose start has `*` standing in for the *name* argument. This behaves much like `*.pth` files (consult the [`site`](https://docs.python.org/3.14/library/site.html#module-site) module for further detail), the difference being that it gives no special treatment to lines that open with `import`. A `*.pkg` file is taken at face value: aside from passing over blank lines and disregarding comments, every entry the `*.pkg` file holds joins the path whether or not it actually exists on the filesystem (and that is intentional).

Should the supplied path not be a list (as happens with frozen packages), it comes back untouched. The original path stays as-is; what you receive is a broadened copy, with new items only ever tacked onto the end of that copy.

The code presumes [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path) is a sequence. Any entries of `sys.path` that aren't strings pointing at directories that exist get skipped. Unicode entries on `sys.path` that fail when treated as filenames can lead this function to raise an exception (matching how [`os.path.isdir()`](https://docs.python.org/3.14/library/os.path.html#os.path.isdir) behaves).

 pkgutil.get_importer(*path_item*)

Fetches a [finder](https://docs.python.org/3.14/glossary.html#term-finder) tied to the supplied *path_item*.

Whenever a path hook freshly builds that finder, it lands in the [`sys.path_importer_cache`](https://docs.python.org/3.14/library/sys.html#sys.path_importer_cache).

You can wipe the cache by hand, in whole or in part, should a fresh scan of [`sys.path_hooks`](https://docs.python.org/3.14/library/sys.html#sys.path_hooks) be called for.

Changed in version 3.3: Reworked to build straight on [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib), no longer leaning on the package's in-house [**PEP 302**](https://peps.python.org/pep-0302/) import emulation.

 pkgutil.iter_importers(*fullname=''*)

Produces [finder](https://docs.python.org/3.14/glossary.html#term-finder) objects matching the supplied module name.

Where *fullname* holds a `'.'`, the finders apply to the package that contains *fullname*; otherwise you get every registered top-level finder (that is, the ones sitting on both [`sys.meta_path`](https://docs.python.org/3.14/library/sys.html#sys.meta_path) and [`sys.path_hooks`](https://docs.python.org/3.14/library/sys.html#sys.path_hooks)).

When the named module lives within a package, calling this function imports that package as a side effect.

Give no module name and the function turns out every top-level finder.

Changed in version 3.3: Now built straight atop [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) instead of depending on the package's internal [**PEP 302**](https://peps.python.org/pep-0302/) import emulation.

 pkgutil.iter_modules(*path=None*, *prefix=''*)

Hands back `ModuleInfo` for each submodule found on *path*, or — when *path* is `None` — for every top-level module sitting on [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path).

The *path* argument has to be either `None` or a list of directories in which to search for modules.

The *prefix* argument is a string prepended to each module name as it's emitted.

Note

This only functions with a [finder](https://docs.python.org/3.14/glossary.html#term-finder) that supplies an `iter_modules()` method. Since that interface is non-standard, the module ships implementations of its own for [`importlib.machinery.FileFinder`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.FileFinder) as well as [`zipimport.zipimporter`](https://docs.python.org/3.14/library/zipimport.html#zipimport.zipimporter).

Changed in version 3.3: Switched to resting directly on [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) rather than counting on the package's own internal [**PEP 302**](https://peps.python.org/pep-0302/) import emulation.

[Subject index](INDEX.md) · [Continue](pkgutil-walk-packages-to-pkgutil-resolve-name.md)
