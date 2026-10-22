# reprlib: `Repr.fillvalue`, `Repr.maxlevel`, `Repr.maxdict`, `Repr.maxlist`, `Repr.maxtuple`, `Repr.maxset`, `Repr.maxfrozenset`, `Repr.maxdeque`, `Repr.maxarray`, `Repr.maxlong`, `Repr.maxstring`, `Repr.maxother`

### Repr Objects

A `Repr` instance carries several attributes that let you set size limits for the representations of various object types, along with methods that format particular object types.

 Repr.fillvalue

This is the string shown for recursive references. Its default value is `...`.

Added in version 3.11.

 Repr.maxlevel

The cap on depth when building recursive representations. Its default value is `6`.

 Repr.maxdict

 Repr.maxlist

 Repr.maxtuple

 Repr.maxset

 Repr.maxfrozenset

 Repr.maxdeque

 Repr.maxarray

Caps on the entry count shown for each named object type. By default `maxdict` is `4`, `maxarray` is `5`, and every other one is `6`.

 Repr.maxlong

The most characters allowed in an integer's representation. Digits get trimmed away from the middle. Its default value is `40`.

 Repr.maxstring

The cap on how many characters appear in the string's representation. Bear in mind that the "normal" representation of the string serves as the character source: when escape sequences are required in the representation, shortening the representation may mangle them. Its default value is `30`.

 Repr.maxother

This cap governs the size of object types that have no dedicated formatting method on the `Repr` object. It works much like `maxstring`. Its default value is `20`.

[Subject index](INDEX.md) · [Previous](reprlib-repr-class-to-reprlib-repr.md) · [Continue](repr-indent-to-repr-repr-type.md) · [Owning module, declaration or section: reprlib](reprlib-repr-class-to-reprlib-repr.md)
