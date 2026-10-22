# hex

hex(*integer*, */*)

Turn an integer number into a lowercase hexadecimal string carrying a “0x” prefix. When *integer* is not a Python `int` object, it must supply an [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) method yielding an integer. A few examples:

```python
>>> hex(255)
'0xff'
>>> hex(-42)
'-0x2a'

```

When you would like to turn an integer number into an uppercase or lower hexadecimal string with or without a prefix, you can reach for either of these approaches:

```python
>>> '%#x' % 255, '%x' % 255, '%X' % 255
('0xff', 'ff', 'FF')
>>> format(255, '#x'), format(255, 'x'), format(255, 'X')
('0xff', 'ff', 'FF')
>>> f'{255:#x}', f'{255:x}', f'{255:X}'
('0xff', 'ff', 'FF')

```

See also `format()` for more information.

Refer as well to `int()` when you want a hexadecimal string turned into an integer via base 16.

Note

To obtain a hexadecimal string representation for a float, use the [`float.hex()`](https://docs.python.org/3.14/library/stdtypes.html#float.hex) method.

[Builtin task index](INDEX.md).
