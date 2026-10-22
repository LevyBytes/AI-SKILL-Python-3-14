# string.templatelib.Template: `iter()`

iter(template)

Walk through the template, producing every non-empty string and `Interpolation` in proper sequence:

```python
>>> cheese = 'Camembert'
>>> list(t'Ah! We do have {cheese}.')
['Ah! We do have ', Interpolation('Camembert', 'cheese', None, ''), '.']

```

Caution

During iteration, empty strings are left **out**:

```python
>>> response = 'We do have '
>>> cheese = 'Camembert'
>>> list(t'Ah! {response}{cheese}.')
['Ah! ',
 Interpolation('We do have ', 'response', None, ''),
 Interpolation('Camembert', 'cheese', None, ''),
 '.']

```

 template + other

 template += other

Join this template onto another one, handing back a fresh `Template` instance:

```python
>>> cheese = 'Camembert'
>>> list(t'Ah! ' + t'We do have {cheese}.')
['Ah! We do have ', Interpolation('Camembert', 'cheese', None, ''), '.']

```

Joining a `Template` to a `str` is **not** allowed, the reason being that it stays ambiguous whether such a string ought to count as a static piece or as an interpolation. To combine a `Template` with a string, you have two choices: enclose the string in a `Template` of its own (so it reads as static text) or hand it to an `Interpolation` (so it reads as dynamic):

```python
>>> from string.templatelib import Interpolation, Template
>>> template = t'Ah! '
>>> # Treat 'We do have ' as a static string
>>> template += Template('We do have ')
>>> # Treat cheese as an interpolation
>>> cheese = 'Camembert'
>>> template += Template(Interpolation(cheese, 'cheese'))
>>> list(template)
['Ah! We do have ', Interpolation('Camembert', 'cheese', None, '')]

```

[Subject index](INDEX.md) · [Previous](string-templatelib-template-new.md) · [Continue](string-templatelib-interpolation-class.md) · [Owning module, declaration or section: string.templatelib](string-templatelib-support-for-template-string-literals.md) · [Owning module, declaration or section: string.templatelib.Template](string-templatelib-template-class.md) · [Owning module, declaration or section: Types](string-templatelib-template-class.md)
