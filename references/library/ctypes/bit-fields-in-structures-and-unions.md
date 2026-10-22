# ctypes — Bit fields in structures and unions

### Bit fields in structures and unions

You can create structures and unions that contain bit fields. Bit fields apply only to integer fields, and the bit width is given as the third element in the `_fields_` tuples:

```python
>>> class Int(Structure):
...     _fields_ = [("first_16", c_int, 16),
...                 ("second_16", c_int, 16)]
...
>>> print(Int.first_16)
<ctypes.CField 'first_16' type=c_int, ofs=0, bit_size=16, bit_offset=0>
>>> print(Int.second_16)
<ctypes.CField 'second_16' type=c_int, ofs=0, bit_size=16, bit_offset=16>

```

[Subject index](INDEX.md) · [Previous](structure-union-layout-alignment-and-byte-order.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md) · [Required continuation of the source contract](arrays.md)
