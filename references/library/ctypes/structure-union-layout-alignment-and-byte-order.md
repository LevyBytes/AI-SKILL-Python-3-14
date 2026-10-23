# ctypes - Structure/union layout, alignment and byte order

### Structure/union layout, alignment and byte order

By default, the fields of a Structure and a Union are laid out exactly as the C compiler would arrange them. You can override that behavior completely by declaring a `_layout_` class attribute in the subclass definition; see the attribute documentation for the details.

By assigning the class attributes `_pack_` and/or `_align_`, you can cap the alignment applied to the fields and/or to the structure as a whole, respectively. See the attribute documentation for the details.

`ctypes` adopts the native byte order for Structures and Unions. When you need to build structures with a non-native byte order, you can choose from the `BigEndianStructure`, `LittleEndianStructure`, `BigEndianUnion`, and `LittleEndianUnion` base classes. None of these classes may contain pointer fields.

[Subject index](INDEX.md) · [Previous](structures-and-unions.md) · [Continue](bit-fields-in-structures-and-unions.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)
