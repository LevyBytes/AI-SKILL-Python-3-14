# object.__mro_entries__(*self*, *bases*)

#### 3.3.3.2. Resolving MRO entries

 object.__mro_entries__(*self*, *bases*)

When a base listed in a class definition is not itself an instance of [`type`](https://docs.python.org/3.14/library/functions.html#type), an `__mro_entries__()` method is looked for on that base. If such an `__mro_entries__()` method exists, then during class creation the base is replaced by whatever the call to `__mro_entries__()` returns. That method receives the original bases tuple by way of the *bases* parameter and has to give back a tuple of classes to use in place of the base. The tuple it returns may be empty, in which case the original base is simply dropped.

See also

[`types.resolve_bases()`](https://docs.python.org/3.14/library/types.html#types.resolve_bases)

Dynamically resolve bases that are not instances of [`type`](https://docs.python.org/3.14/library/functions.html#type).

[`types.get_original_bases()`](https://docs.python.org/3.14/library/types.html#types.get_original_bases)

Retrieve a class's "original bases" prior to modifications by `__mro_entries__()`.

[**PEP 560**](https://peps.python.org/pep-0560/)

Core support for typing module and generic types.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](customizing-class-creation.md) · [Previous source section](metaclasses.md) · [Following source section](determining-the-appropriate-metaclass.md)
