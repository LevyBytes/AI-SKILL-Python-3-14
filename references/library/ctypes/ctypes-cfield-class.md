# ctypes: `ctypes.CField`

*class *ctypes.CField(**args*, ***kw*)

Descriptor for the fields of a `Structure` and `Union`. For instance:

```python
>>> class Color(Structure):
...     _fields_ = (
...         ('red', c_uint8),
...         ('green', c_uint8),
...         ('blue', c_uint8),
...         ('intense', c_bool, 1),
...         ('blinking', c_bool, 1),
...    )
...
>>> Color.red
<ctypes.CField 'red' type=c_ubyte, ofs=0, size=1>
>>> Color.green.type
<class 'ctypes.c_ubyte'>
>>> Color.blue.byte_offset
2
>>> Color.intense
<ctypes.CField 'intense' type=c_bool, ofs=3, bit_size=1, bit_offset=0>
>>> Color.blinking.bit_offset
1

```

Every attribute is read-only.

`CField` objects come into being through `_fields_`; do not instantiate the class on your own.

[Subject index](INDEX.md) · [Previous](structured-data-types-ctypes-structure.md) · [Owning module, declaration or section: ctypes](ctypes-a-foreign-function-library-for-python.md) · [Owning module, declaration or section: Structured data types](ctypes-union-class.md) · [Required continuation of the source contract](structured-data-types-ctypes-cfield.md)
