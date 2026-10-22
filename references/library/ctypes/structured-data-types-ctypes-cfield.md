# ctypes: CField names, types, offsets and bit-field descriptors

Added in version 3.14: In earlier releases, descriptors carried just `offset` and `size` attributes plus a readable string form; the `CField` class could not be reached on its own.

`name`

The field's name, given as a string.

`type`

The field's type, given as a ctypes class.

`offset`

`byte_offset`

The field's offset, measured in bytes.

When dealing with bitfields, this gives the offset of the byte-aligned *storage unit* underneath; refer to `bit_offset`.

`byte_size`

The field's size, measured in bytes.

When dealing with bitfields, this gives the size of the *storage unit* underneath. As a rule it matches the size of the bitfield's type.

`size`

When the field is not a bitfield, the same as `byte_size`.

When it is a bitfield, this holds a backwards-compatible bit-packed value rolling together `bit_size` and `bit_offset`. You are encouraged to reach for the explicit attributes in its place.

`is_bitfield`

True when this is in fact a bitfield.

`bit_offset`

`bit_size`

Where a bitfield sits inside its *storage unit* — that is, somewhere within the `byte_size` bytes of memory that begin at `byte_offset`.

To pull out the field's value, interpret the storage unit as an integer, [shift left](https://docs.python.org/3.14/reference/expressions.html#shifting) by `bit_offset`, and keep the `bit_size` least significant bits.

When the field is not a bitfield, `bit_offset` comes out as zero and `bit_size` equals `byte_size * 8`.

`is_anonymous`

True when this field is anonymous — meaning it holds nested sub-fields meant to be folded into an enclosing structure or union.

[Subject index](INDEX.md) · [Continue](ctypes-array-class-to-ctypes-array.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md) · [Owning module, declaration or section: ctypes.CField](ctypes-cfield-class.md) · [Owning module, declaration or section: Structured data types](ctypes-union-class.md) · [Preceding source contract and version conditions](ctypes-cfield-class.md)
