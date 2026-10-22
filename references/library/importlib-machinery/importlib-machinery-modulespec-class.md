# importlib.machinery — `importlib.machinery` – Importers and path hooks

*class *importlib.machinery.ModuleSpec(*name*, *loader*, ***, *origin=None*, *loader_state=None*, *is_package=None*)

A specification describing a module's import-system-related state. It is ordinarily surfaced as the module's [`__spec__`](https://docs.python.org/3.14/reference/datamodel.html#module.__spec__) attribute. A number of these attributes are likewise reachable straight off a module: for instance, `module.__spec__.origin == module.__file__`. Keep in mind, though, that even when the *values* normally line up, they can diverge, because nothing keeps the two objects in sync. As one example, a module's [`__file__`](https://docs.python.org/3.14/reference/datamodel.html#module.__file__) can be changed at runtime without that change carrying over automatically to the module's `__spec__.origin`, and the reverse holds too.

Added in version 3.4.

 name

The module's fully qualified name (see [`module.__name__`](https://docs.python.org/3.14/reference/datamodel.html#module.__name__)). A [finder](https://docs.python.org/3.14/glossary.html#term-finder) must in every case assign this attribute some non-empty string.

 loader

The [loader](https://docs.python.org/3.14/glossary.html#term-loader) that loads the module (see [`module.__loader__`](https://docs.python.org/3.14/reference/datamodel.html#module.__loader__)). A [finder](https://docs.python.org/3.14/glossary.html#term-finder) must in every case populate this attribute.

 origin

The location the [loader](https://docs.python.org/3.14/glossary.html#term-loader) should use to load the module (see [`module.__file__`](https://docs.python.org/3.14/reference/datamodel.html#module.__file__)). For modules loaded out of a `.py` file, for instance, this holds the filename. The [finder](https://docs.python.org/3.14/glossary.html#term-finder) should always assign this attribute a value the loader can meaningfully use. In the rare situation where none exists (as with namespace packages), it should be set to `None`.

 submodule_search_locations

A (possibly empty) [sequence](https://docs.python.org/3.14/glossary.html#term-sequence) of strings listing the locations where a package's submodules are to be found (see [`module.__path__`](https://docs.python.org/3.14/reference/datamodel.html#module.__path__)). Usually this list holds just one directory.

The [finder](https://docs.python.org/3.14/glossary.html#term-finder) should give this attribute a sequence, even an empty one, to signal to the import system that the module is a package. For modules that are not packages it should be `None`. Later it is set automatically to a special object in the case of namespace packages.

 loader_state

The [finder](https://docs.python.org/3.14/glossary.html#term-finder) may give this attribute an object carrying extra, module-specific data for use while the module is loaded. Failing that, it should be set to `None`.

 cached

The filename of a compiled rendition of the module's code (see [`module.__cached__`](https://docs.python.org/3.14/reference/datamodel.html#module.__cached__)). The [finder](https://docs.python.org/3.14/glossary.html#term-finder) should always set this attribute, though it may be `None` for modules with no need to keep compiled code on disk.

 parent

(Read-only) The fully qualified name of the package containing the module (or the empty string when the module is top-level). See [`module.__package__`](https://docs.python.org/3.14/reference/datamodel.html#module.__package__). When the module is itself a package, this equals `name`.

 has_location

`True` when the spec's `origin` points to a loadable location, and `False` otherwise. The value shapes how `origin` is read and how the module's [`__file__`](https://docs.python.org/3.14/reference/datamodel.html#module.__file__) gets filled in.

[Subject index](INDEX.md) · [Previous](importlib-machinery-namespaceloader-class.md) · [Continue](importlib-machinery-appleframeworkloader-class.md) · [Owning module, declaration or section: importlib.machinery](importable-file-suffixes.md)
