# pkgutil: `pkgutil.walk_packages()`, `pkgutil.get_data()`, `pkgutil.resolve_name()`

pkgutil.walk_packages(*path=None*, *prefix=''*, *onerror=None*)

Hands back `ModuleInfo` for every module reached recursively on *path*, or — when *path* is `None` — for all modules that can be reached.

The *path* argument has to be either `None` or a list of directories in which to search for modules.

The *prefix* argument is a string prepended to each module name as it's emitted.

Bear in mind that this function has to import each *package* (though *not* every module!) along the supplied *path*, so that it can read the `__path__` attribute and locate submodules.

The *onerror* argument is a function invoked with a single argument — the name of the package then being imported — whenever an exception crops up during an attempt to import a package. With no *onerror* function provided, any [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError)s get swallowed silently, whereas every other exception propagates and brings the search to a halt.

Examples:

```python
# list all modules python can access
walk_packages()

# list all submodules of ctypes
walk_packages(ctypes.__path__, ctypes.__name__ + '.')

```

Note

Works solely with a [finder](https://docs.python.org/3.14/glossary.html#term-finder) that defines an `iter_modules()` method. Because that interface departs from the standard, the module bundles its own implementations covering [`importlib.machinery.FileFinder`](https://docs.python.org/3.14/library/importlib.html#importlib.machinery.FileFinder) and [`zipimport.zipimporter`](https://docs.python.org/3.14/library/zipimport.html#zipimport.zipimporter).

Changed in version 3.3: Rebuilt to sit directly on [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) in place of relying on the package's internal [**PEP 302**](https://peps.python.org/pep-0302/) import emulation.

 pkgutil.get_data(*package*, *resource*)

Pulls a resource out of a package.

It wraps the [loader](https://docs.python.org/3.14/glossary.html#term-loader) [`get_data`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.ResourceLoader.get_data) API. Pass the package's name as the *package* argument, written in ordinary module form (`foo.bar`). Give the *resource* argument as a relative filename that uses `/` for its path separator.

What comes back is a binary string holding the contents of the resource you asked for.

The function leans on the [loader](https://docs.python.org/3.14/glossary.html#term-loader) method [`get_data()`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.FileLoader.get_data) so that it works for modules residing on the filesystem and equally for ones living in zip files, databases, or elsewhere.

When a package sits on the filesystem and has already been imported, this roughly amounts to:

```python
d = os.path.dirname(sys.modules[package].__file__)
data = open(os.path.join(d, resource), 'rb').read()

```

Much as the [`open()`](https://docs.python.org/3.14/library/functions.html#open) function does, `get_data()` is able to traverse parent directories (`../`) along with absolute paths (those opening with `/` or `C:/`, say). It can reach build/install artifacts such as `.py` and `.pyc` files, or files bearing [`reserved filenames`](https://docs.python.org/3.14/library/os.path.html#os.path.isreserved). For the sake of compatibility with loaders that aren't filesystem-based, steer clear of these capabilities.

Warning

This function expects trusted input. It performs no check that *resource* truly “belongs” to *package*.

Where the *resource* path comes from a user, think about validating it — for instance, insist on an alphanumeric filename with a recognized extension, or set up and consult a roster of known resources.

Should the package prove impossible to locate or load, or should it rely on a [loader](https://docs.python.org/3.14/glossary.html#term-loader) lacking [`get_data`](https://docs.python.org/3.14/library/importlib.html#importlib.abc.ResourceLoader.get_data) support, then `None` comes back. Notably, the loader behind [namespace packages](https://docs.python.org/3.14/glossary.html#term-namespace-package) offers no `get_data`.

See also

For organized access to a module's resources, turn to the [`importlib.resources`](https://docs.python.org/3.14/library/importlib.resources.html#module-importlib.resources) module.

 pkgutil.resolve_name(*name*)

Turns a name into an object.

The standard library leans on this capability in many spots (see [bpo-12915](https://bugs.python.org/issue?@action=redirect&bpo=12915)), and comparable capability shows up in popular third-party packages too, among them setuptools, Django and Pyramid.

The *name* is expected to arrive as a string matching one of the patterns below, where W is shorthand for any valid Python identifier and dot denotes a literal period within these pseudo-regexes:

-

[Subject index](INDEX.md) · [Previous](pkgutil-moduleinfo-class-to-pkgutil-iter-modules.md) · [Continue](w.md) · [Owning module, declaration or section: pkgutil](pkgutil-moduleinfo-class-to-pkgutil-iter-modules.md)
