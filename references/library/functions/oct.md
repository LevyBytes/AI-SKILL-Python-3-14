# Built-in Functions

oct(*integer*, */*)

Turn an integer number into an octal string carrying the prefix “0o”. What results is a valid Python expression. When *integer* is not a Python `int` object, it must supply an [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) method yielding an integer. As an example:

```python
>>> oct(8)
'0o10'
>>> oct(-56)
'-0o70'

```

Should you wish to turn an integer number into an octal string with or without the “0o” prefix, you may use either of the approaches below.

```python
>>> '%#o' % 10, '%o' % 10
('0o12', '12')
>>> format(10, '#o'), format(10, 'o')
('0o12', '12')
>>> f'{10:#o}', f'{10:o}'
('0o12', '12')

```

See also `format()` for more information.

[Subject index](INDEX.md) · [Previous](object-class.md) · [Continue](open.md) · [Owning module, declaration or section: Built-in Functions](INDEX.md)
