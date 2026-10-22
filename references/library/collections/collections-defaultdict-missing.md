# collections / defaultdict objects: `__missing__()`

__missing__(*key*, */*)

When the `default_factory` attribute equals `None`, a [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) exception is raised, carrying the *key* as its argument.

When `default_factory` is something other than `None`, it gets invoked with no arguments to produce a default value for the supplied *key*; that value is then stored in the dictionary under the *key* and handed back.

Should the call to `default_factory` throw an exception, that exception travels upward untouched.

The [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__) method of the [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) class invokes this method whenever the requested key is absent; whatever `__missing__()` returns or raises becomes the return value or exception of `__getitem__()`.

Keep in mind that `__missing__()` does *not* fire for operations other than [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__). Consequently [`get()`](https://docs.python.org/3.14/library/stdtypes.html#dict.get) behaves like it does on ordinary dictionaries, handing back `None` as the default rather than consulting `default_factory`.

`defaultdict` objects expose the following instance variable:

 default_factory

The `__missing__()` method consults this attribute; it gets its starting value from the constructor’s first argument when one is supplied, or otherwise from `None`.

Changed in version 3.9: Added merge (`|`) and update (`|=`) operators, specified in [**PEP 584**](https://peps.python.org/pep-0584/).

[Subject index](INDEX.md) · [Previous](defaultdict-class-contract.md) · [Continue](defaultdict-examples.md) · [Owning module, declaration or section: collections](collections-container-datatypes.md) · [Owning module, declaration or section: collections.defaultdict; collections.defaultdict; collections.defaultdict](defaultdict-class-contract.md) · [Owning module, declaration or section: `defaultdict` objects](defaultdict-class-contract.md)
