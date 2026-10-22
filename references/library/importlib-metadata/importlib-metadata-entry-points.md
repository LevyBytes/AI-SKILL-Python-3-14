# importlib.metadata: `importlib.metadata.entry_points()`

### Entry points

 importlib.metadata.entry_points(***select_params*)

Returns an `EntryPoints` instance covering entry points for the current environment. Whatever keyword parameters you pass go to the `select()` method to be matched against the attributes of the individual entry point definitions.

Note: querying for entry points by their `EntryPoint.dist` attribute is not yet supported (because distinct `Distribution` instances do not currently compare equal, even when their attributes match)

[Subject index](INDEX.md) · [Previous](functional-api.md) · [Continue](importlib-metadata-entrypoints-class.md) · [Owning module, declaration or section: importlib.metadata](importlib-metadata-packagenotfounderror.md)
