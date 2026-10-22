# struct: `struct.Struct`

### Classes

On top of those, the `struct` module sets out this type:

`*class *struct.Struct(*format*)`

Hand back a fresh Struct object that reads and writes binary data following the format string *format*. Building a `Struct` object a single time and then invoking its methods runs faster than passing the same format to the module-level functions over and over, because the format string is compiled just once.

Note

The compiled forms of the format strings most recently fed to the module-level functions are held in a cache, which means programs leaning on only a handful of format strings have no reason to fuss over keeping one `Struct` instance around to reuse.

These methods and attributes belong to compiled Struct objects:

[Subject index](INDEX.md) · [Previous](standard-formats.md) · [Continue](struct-struct-pack-to-struct-struct-iter-unpack.md) · [Owning module, declaration or section: struct](struct-interpret-bytes-as-packed-binary-data.md)
