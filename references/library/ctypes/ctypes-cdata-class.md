# ctypes: `ctypes._CData`

### Data types

 *class *ctypes._CData

This non-public class serves as the shared base for every ctypes data type. For one thing, each ctypes type instance carries a memory block holding C compatible data; you obtain that block's address through the `addressof()` helper function. A further instance variable is surfaced as `_objects`; it holds additional Python objects that must stay alive should the memory block hold pointers.

Shared methods of ctypes data types, all of which are class methods (more precisely, methods of the [metaclass](https://docs.python.org/3.14/glossary.html#term-metaclass)):

[Subject index](INDEX.md) · [Previous](ctypes-pointer-to-ctypes-memoryview-at.md) · [Continue](ctypes-cdata-from-buffer-to-ctypes-cdata-in-dll.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md)
