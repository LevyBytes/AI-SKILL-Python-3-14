# string — Format examples — Code example: >>> for align, text in zip('<^>', ['left', 'center', 'right']):

```python
>>> for align, text in zip('<^>', ['left', 'center', 'right']):
...     '{0:{fill}{align}16}'.format(text, fill=align, align=align)
...
'left<<<<<<<<<<<<'
'^^^^^center^^^^^'
'>>>>>>>>>>>right'
>>>
>>> octets = [192, 168, 0, 1]
>>> '{:02X}{:02X}{:02X}{:02X}'.format(*octets)
'C0A80001'
>>> int(_, 16)
3232235521
>>>
>>> width = 5
>>> for num in range(5,12):
...     for base in 'dXob':
...         print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
...     print()
...
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8     8    10  1000
    9     9    11  1001
   10     A    12  1010
   11     B    13  1011

```

[Subject index](INDEX.md) · [Previous](numeric-format-signs.md) · [Continue](string-template-class.md) · [Owning module, declaration or section: string](string-common-string-operations.md) · [Owning module, declaration or section: Format examples](format-examples-section-introduction-and-initial-examples.md)
