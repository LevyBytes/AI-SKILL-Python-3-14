# enum: `enum.show_flag_values()`, `enum.bin()`

enum.show_flag_values(*value*)

Hand back a list of every power-of-two integer that a flag *value* carries.

Added in version 3.11.

 enum.bin(*num*, *max_bits=None*)

Behaves as the built-in `bin()` does, save that negatives appear in two’s complement and the foremost bit consistently encodes sign (`0` for positive, `1` for negative).

```python
>>> import enum
>>> enum.bin(10)
'0b0 1010'
>>> enum.bin(~10)   # ~10 is -11
'0b1 0101'

```

Added in version 3.11.

---

[Subject index](INDEX.md) · [Previous](enum-auto-class.md) · [Continue](notes.md) · [Owning module, declaration or section: enum](enum-support-for-enumerations.md) · [Owning module, declaration or section: Utilities and decorators](enum-auto-class.md)
