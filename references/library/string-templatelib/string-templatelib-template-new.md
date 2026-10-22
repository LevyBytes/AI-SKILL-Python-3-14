# string.templatelib.Template: Interpolation construction and expression structure

__new__(**args: [str](https://docs.python.org/3.14/library/stdtypes.html#str) | Interpolation*)

Although the literal syntax is the usual route to a `Template`, you can also build one straight from the constructor:

```python
>>> from string.templatelib import Interpolation, Template
>>> cheese = 'Camembert'
>>> template = Template(
...     'Ah! We do have ', Interpolation(cheese, 'cheese'), '.'
... )
>>> list(template)
['Ah! We do have ', Interpolation('Camembert', 'cheese', None, ''), '.']

```

Should several strings arrive back to back, they get merged into one entry inside the `strings` attribute. The code below, for instance, yields a `Template` that ends up holding a single final string:

```python
>>> from string.templatelib import Template
>>> template = Template('Ah! We do have ', 'Camembert', '.')
>>> template.strings
('Ah! We do have Camembert.',)

```

When two or more interpolations come one after another, each stays its own distinct interpolation and an empty string gets slipped in to separate them. As an illustration, the next snippet builds a template carrying empty placeholders inside the `strings` attribute:

```python
>>> from string.templatelib import Interpolation, Template
>>> template = Template(
...     Interpolation('Camembert', 'cheese'),
...     Interpolation('.', 'punctuation'),
... )
>>> template.strings
('', '', '')

```

[Subject index](INDEX.md) · [Previous](types-code-example-cheese-camembert.md) · [Continue](string-templatelib-template-iter.md) · [Owning module, declaration or section: string.templatelib](string-templatelib-support-for-template-string-literals.md) · [Owning module, declaration or section: string.templatelib.Template](string-templatelib-template-class.md) · [Owning module, declaration or section: Types](string-templatelib-template-class.md)
