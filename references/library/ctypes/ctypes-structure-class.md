# ctypes: `ctypes.Structure`

*class *ctypes.Structure(**args*, ***kw*)

Abstract base class for structures in *native* byte order.

You build concrete structure and union types by subclassing one of these types and, at minimum, defining a `_fields_` class variable. `ctypes` will produce [descriptor](https://docs.python.org/3.14/glossary.html#term-descriptor)s that let you read and write the fields through direct attribute access. These are the

 _fields_

A sequence that defines the structure fields. Its items must be 2-tuples or 3-tuples. The first item gives the field name; the second item gives the field type, which may be any ctypes data type.

For integer type fields such as `c_int`, you may supply a third optional item. It has to be a small positive integer giving the field's bit width.

Field names have to be unique inside a single structure or union. This goes unchecked; when names repeat, only one of those fields is reachable.

You may set the `_fields_` class variable *after* the class statement defining the Structure subclass; this lets you create data types that reference themselves directly or indirectly:

```python
class List(Structure):
    pass
List._fields_ = [("pnext", POINTER(List)),
                 ...
                ]

```

The `_fields_` class variable may only be assigned once. Subsequent assignments will raise an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError).

On top of that, the `_fields_` class variable has to be defined before the structure or union type sees its first use: creating an instance or subclass, calling `sizeof()` on it, and so forth. Assigning `_fields_` afterward will raise an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError). When `_fields_` has not been set before such use, the structure or union ends up with no fields of its own, as though `_fields_` were empty.

Sub-subclasses of structure types inherit the base class fields together with whatever `_fields_` the sub-subclass declares, if any.

 _pack_

An optional small integer that lets you override the alignment of the structure fields within the instance.

This works only for the MSVC-compatible memory layout (refer to `_layout_`).

Setting `_pack_` to 0 amounts to leaving it unset entirely. Otherwise the value has to be a positive power of two. The result matches `#pragma pack(N)` in C, except that `ctypes` may permit a larger *n* than the compiler would accept.

`_pack_` has to be defined already when `_fields_` is assigned, or it will take no effect.

Deprecated since version 3.14, will be removed in version 3.19: Owing to history, a non-zero `_pack_` makes the MSVC-compatible layout the default. On platforms other than Windows this default is deprecated and is set to become an error in Python 3.19. When that is what you want, set `_layout_` to `'ms'` explicitly.

 _align_

An optional small integer that lets you raise the alignment of the structure as it is packed into or unpacked from memory.

The value must not be negative. The result matches `__attribute__((aligned(N)))` on GCC or `#pragma align(N)` on MSVC, except that `ctypes` may permit values the compiler would reject.

`_align_` is only able to *increase* the alignment a structure demands. A value of 0 or 1 has no effect.

Supplying values that are not powers of two is discouraged and can produce surprising behavior.

`_align_` has to be defined already when `_fields_` is assigned, or it will take no effect.

Added in version 3.13.

[Subject index](INDEX.md) · [Previous](ctypes-littleendianstructure-class.md) · [Continue](structured-data-types-ctypes-structure.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md) · [Owning module, declaration or section: Structured data types](ctypes-union-class.md)
