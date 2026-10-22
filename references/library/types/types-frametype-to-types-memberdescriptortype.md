# types: `types.FrameType`, `types.GetSetDescriptorType`, `types.MemberDescriptorType`

types.FrameType

The type of [frame objects](https://docs.python.org/3.14/reference/datamodel.html#frame-objects), like the one found at [`tb.tb_frame`](https://docs.python.org/3.14/reference/datamodel.html#traceback.tb_frame) when `tb` is a traceback object.

 types.GetSetDescriptorType

The type of objects declared in extension modules via `PyGetSetDef`, [`FrameType.f_locals`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_locals) or `array.array.typecode` for instance. This type serves as the descriptor for object attributes; it fills the same role as the [`property`](https://docs.python.org/3.14/library/functions.html#property) type, only for classes declared in extension modules.

 types.MemberDescriptorType

The type of objects declared in extension modules via `PyMemberDef`, `datetime.timedelta.days` for instance. This type serves as the descriptor for simple C data members that go through standard conversion functions; it fills the same role as the [`property`](https://docs.python.org/3.14/library/functions.html#property) type, only for classes declared in extension modules.

What is more, whenever a class is declared carrying a [`__slots__`](https://docs.python.org/3.14/reference/datamodel.html#object.__slots__) attribute, an instance of `MemberDescriptorType` is attached to the class as an attribute for each slot. That is what lets the slot show up in the class’s [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#type.__dict__).

**CPython implementation detail:** Under other Python implementations, this type might be the very same as `GetSetDescriptorType`.

[Subject index](INDEX.md) · [Previous](types-tracebacktype-class.md) · [Continue](types-mappingproxytype-class-to-types-mappingproxytype-hash.md) · [Owning module, declaration or section: types](types-dynamic-type-creation-and-names-for-built-in-types.md) · [Owning module, declaration or section: Standard Interpreter Types](types-nonetype-class-to-types-asyncgeneratortype.md)
