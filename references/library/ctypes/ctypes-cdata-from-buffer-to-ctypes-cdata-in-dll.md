# ctypes._CData: `from_buffer()`, `from_buffer_copy()`, `from_address()`, `from_param()`, `in_dll()`

from_buffer(*source*[, *offset*])

This method hands back a ctypes instance that shares the *source* object's buffer. The *source* object is required to support the writeable buffer interface. The optional *offset* parameter gives a byte offset into the source buffer; it defaults to zero. Should the source buffer fall short in size, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `ctypes.cdata/buffer` with arguments `pointer`, `size`, `offset`.

 from_buffer_copy(*source*[, *offset*])

This method builds a ctypes instance by copying the buffer out of the *source* object buffer, which has to be readable. The optional *offset* parameter gives a byte offset into the source buffer; it defaults to zero. Should the source buffer fall short in size, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `ctypes.cdata/buffer` with arguments `pointer`, `size`, `offset`.

 from_address(*address*)

This method hands back a ctypes type instance backed by the memory at *address*, which has to be an integer.

This method, along with others that call it indirectly, raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `ctypes.cdata` with argument `address`.

 from_param(*obj*)

This method converts *obj* into a ctypes type. It gets called with the real object passed in a foreign function call whenever the type appears in that foreign function's `argtypes` tuple; it has to give back an object usable as a function call parameter.

Every ctypes data type ships a default version of this classmethod that ordinarily returns *obj* when *obj* is an instance of the type. Certain types take other objects too.

 in_dll(*library*, *name*)

This method hands back a ctypes type instance exported from a shared library. *name* identifies the symbol exporting the data, and *library* is the loaded shared library.

Shared class variables of ctypes data types:

 __pointer_type__

The pointer type produced by invoking `POINTER()` on the matching ctypes data type. When no pointer type has yet been produced, this attribute is absent.

Added in version 3.14.

Shared instance variables of ctypes data types:

 _b_base_

At times ctypes data instances do not own their memory block; instead they use a portion of a base object's memory block. The read-only `_b_base_` member is the root ctypes object that holds title to the memory block.

 _b_needsfree_

This read-only variable holds true when the ctypes data instance itself allocated the memory block, and false otherwise.

 _objects

This member is either `None` or a dictionary holding Python objects that must remain alive so the memory block contents stay valid. The object exists purely for debugging; never alter what this dictionary holds.

[Subject index](INDEX.md) · [Previous](ctypes-cdata-class.md) · [Continue](ctypes-simplecdata-class.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md) · [Owning module, declaration or section: ctypes._CData](ctypes-cdata-class.md) · [Owning module, declaration or section: Data types](ctypes-cdata-class.md)
