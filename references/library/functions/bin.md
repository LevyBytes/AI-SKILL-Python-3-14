# Built-in Functions

bin(*integer*, */*)

Turn an integer into a binary string carrying the “0b” prefix. What you get is a legal Python expression. Should *integer* not be a Python `int` object, it must supply an [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) method returning an integer. A few examples follow:

```python
>>> bin(3)
'0b11'
>>> bin(-10)
'-0b1010'

```

Whether or not you want that “0b” prefix, either of the approaches below will serve.

```python
>>> format(14, '#b'), format(14, 'b')
('0b1110', '1110')
>>> f'{14:#b}', f'{14:b}'
('0b1110', '1110')

```

Consult [`enum.bin()`](https://docs.python.org/3.14/library/enum.html#enum.bin) as well, for showing negative numbers in twos-complement form.

Refer to `format()` too for further detail.

[Subject index](INDEX.md) · [Previous](INDEX.md) · [Continue](bool-class.md) · [Owning module, declaration or section: Built-in Functions](INDEX.md)
