# importlib.util: `importlib.util.module_from_spec()`, `importlib.util.spec_from_loader()`, `importlib.util.spec_from_file_location()`, `importlib.util.source_hash()`, `importlib.util._incompatible_extension_module_restrictions()`

Locate the [spec](https://docs.python.org/3.14/glossary.html#term-module-spec) belonging to a module, where the search may be taken relative to the given **package** name. Should the module already sit in [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules), the value `sys.modules[name].__spec__` is handed back (the exception being a spec that is unset or equals `None`, which prompts a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError)). When that is not the case, a lookup proceeds across [`sys.meta_path`](https://docs.python.org/3.14/library/sys.html#sys.meta_path). Whenever nothing turns up, the call yields `None`.

When **name** designates a submodule (it carries a dot), the parent gets imported on your behalf without prompting.

Both **name** and **package** carry the identical meaning they have in `import_module()`.

Added in version 3.4.

Changed in version 3.7: Now produces [`ModuleNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#ModuleNotFoundError) rather than [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) whenever **package** turns out not to be a genuine package (that is, it has no [`__path__`](https://docs.python.org/3.14/reference/datamodel.html#module.__path__) attribute).

 importlib.util.module_from_spec(*spec*)

Build a fresh module from **spec** together with `spec.loader.create_module`.

Whenever `spec.loader.create_module` yields something other than `None`, attributes that already exist are left untouched. On top of that, accessing **spec** or assigning an attribute on the module will not surface an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) even if one would otherwise arise.

Reach for this routine rather than [`types.ModuleType`](https://docs.python.org/3.14/library/types.html#types.ModuleType) when building a module, because **spec** lets it populate as many of the import-governed attributes as it can.

Added in version 3.5.

 importlib.util.spec_from_loader(*name*, *loader*, ***, *origin=None*, *is_package=None*)

A factory routine that produces a `ModuleSpec` instance derived from a loader. Its parameters carry the same significance as those on ModuleSpec. To complete whatever the spec is missing, the routine draws on whichever [loader](https://docs.python.org/3.14/glossary.html#term-loader) APIs are at hand, for instance `InspectLoader.is_package()`.

Added in version 3.4.

 importlib.util.spec_from_file_location(*name*, *location*, ***, *loader=None*, *submodule_search_locations=None*)

A factory routine that produces a `ModuleSpec` instance derived from a file's path. Anything absent from the spec gets supplied by drawing on loader APIs together with the assumption that the module lives in a file.

Added in version 3.4.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 importlib.util.source_hash(*source_bytes*)

Hand back, as bytes, the hash computed over *source_bytes*. Inside its header, a hash-based `.pyc` file stores the `source_hash()` taken over the contents of the matching source file.

Added in version 3.7.

 importlib.util._incompatible_extension_module_restrictions(***, *disable_check*)

A context manager able to set aside, for a short while, the compatibility check applied to extension modules. The check runs by default and trips whenever a single-phase init module is loaded inside a subinterpreter. It likewise trips for a multi-phase init module lacking declared support for a per-interpreter GIL once that module is loaded into an interpreter holding its own GIL.

Keep in mind that this routine exists to serve a rare scenario, and one that will probably disappear before long. Odds are good that this isn't the thing you came here to find.

The very same behavior is achievable by supplying the rudimentary multi-phase init interface ([**PEP 489**](https://peps.python.org/pep-0489/)) and then falsely declaring support for multiple interpreters (or a per-interpreter GIL).

Warning

Turning the check off through this routine risks surprising behavior and outright crashes. Confine its use strictly to extension module development.

Added in version 3.12.

[Subject index](INDEX.md) · [Continue](importlib-util-lazyloader-class.md) · [Owning module, declaration or section: importlib.util](importlib-util-magic-number-to-importlib-util-find-spec.md) · [Owning module, declaration or section: importlib.util.find_spec](importlib-util-magic-number-to-importlib-util-find-spec.md) · [Preceding source contract and version conditions](importlib-util-magic-number-to-importlib-util-find-spec.md)
