# string.templatelib — Types — Code example: >>> cheese = 'Camembert'

```python
>>> cheese = 'Camembert'
>>> template = t'Ah! We do have {cheese}.'
>>> template.interpolations
(Interpolation('Camembert', 'cheese', None, ''),)

```

The `interpolations` tuple is allowed to be empty, and it always holds one item less than the `strings` tuple does:

```python
>>> t'Red Leicester'.interpolations
()

```

 values*: [tuple](https://docs.python.org/3.14/library/stdtypes.html#tuple)[[object](https://docs.python.org/3.14/library/functions.html#object), ...]*

A tuple gathering every interpolated value found in the template.

```python
>>> cheese = 'Camembert'
>>> template = t'Ah! We do have {cheese}.'
>>> template.values
('Camembert',)

```

In length, the `values` tuple matches the `interpolations` tuple exactly. It is invariably the same as `tuple(i.value for i in template.interpolations)`.

Methods

[Subject index](INDEX.md) · [Previous](string-templatelib-template-class.md) · [Continue](string-templatelib-template-new.md) · [Owning module, declaration or section: string.templatelib](string-templatelib-support-for-template-string-literals.md) · [Owning module, declaration or section: string.templatelib.Template](string-templatelib-template-class.md) · [Owning module, declaration or section: Types](string-templatelib-template-class.md)
