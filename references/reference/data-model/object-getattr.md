# object.__getattr__(*self*, *name*)

object.__getattr__(*self*, *name*)

Invoked whenever the ordinary attribute lookup ends in an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) (the cause being that `__getattribute__()` raised an `AttributeError` since *name* is neither an instance attribute nor anything in `self`’s class tree; or that `__get__()` of a *name* property raised `AttributeError`). This method should either give back the (computed) attribute value or raise an `AttributeError` exception. This method is not furnished by the [`object`](https://docs.python.org/3.14/library/functions.html#object) class itself.

Be aware that should the attribute turn up through the normal mechanism, `__getattr__()` is not invoked. (This is a deliberate asymmetry between `__getattr__()` and `__setattr__()`.) That is done both for efficiency’s sake and because otherwise `__getattr__()` would have no means of reaching the instance’s other attributes. Be aware that, at least for instance variables, you can seize full control by placing no values in the instance attribute dictionary (and instead placing them in another object). Consult the `__getattribute__()` method below for a means of truly seizing full control over attribute access.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](special-method-names.md) · [Owning language section](customizing-attribute-access.md) · [Previous source section](customizing-attribute-access.md) · [Following source section](object-getattribute.md)
