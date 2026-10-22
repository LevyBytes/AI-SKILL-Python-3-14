# Built-in Functions

delattr(*object*, *name*, */*)

Consider this the counterpart of `setattr()`. Its arguments are an object together with a string, where the string has to name one of that object’s attributes. The function strips away the named attribute, so long as the object permits that. For instance, `delattr(x, 'foobar')` does the same thing as `del x.foobar`. *name* is not required to be a Python identifier (refer to `setattr()`).

[Subject index](INDEX.md) · [Previous](complex-class-to-complex-class.md) · [Continue](dict-class-to-dict-class.md) · [Owning module, declaration or section: Built-in Functions](INDEX.md)
