# string.templatelib - Types - Signature and initial contract

### Types

 *class *string.templatelib.Template

A `Template` class captures what a template string holds. Being immutable, its attributes can never be reassigned once set.

Most often you produce a `Template` instance through the [template string literal syntax](https://docs.python.org/3.14/reference/lexical_analysis.html#t-strings). That syntax mirrors [f-strings](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings) exactly, the sole change being a `t` prefix where an `f` would normally sit:

```python
>>> cheese = 'Red Leicester'
>>> template = t"We're fresh out of {cheese}, sir."
>>> type(template)
<class 'string.templatelib.Template'>

```

Internally a template is kept as runs of literal `strings` alongside dynamic `interpolations`, while a `values` attribute carries the values belonging to those interpolations:

```python
>>> cheese = 'Camembert'
>>> template = t'Ah! We do have {cheese}.'
>>> template.strings
('Ah! We do have ', '.')
>>> template.interpolations
(Interpolation('Camembert', ...),)
>>> template.values
('Camembert',)

```

There is always one extra item in the `strings` tuple compared with `interpolations` and `values`, since each interpolation “belongs” in the gap between two strings. Lining the tuples up against each other can make this clearer

```python
template.strings:  ('Ah! We do have ',              '.')
template.values:   (                   'Camembert',    )

```

Attributes

 strings*: [tuple](https://docs.python.org/3.14/library/stdtypes.html#tuple)[[str](https://docs.python.org/3.14/library/stdtypes.html#str), ...]*

Holds, as a [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple), the template's fixed literal strings.

```python
>>> cheese = 'Camembert'
>>> template = t'Ah! We do have {cheese}.'
>>> template.strings
('Ah! We do have ', '.')

```

Note that empty strings *do* appear within the tuple:

```python
>>> response = 'We do have '
>>> cheese = 'Camembert'
>>> template = t'Ah! {response}{cheese}.'
>>> template.strings
('Ah! ', '', '.')

```

You will never find the `strings` tuple empty, and it consistently carries one string beyond what the `interpolations` and `values` tuples hold:

```python
>>> t''.strings
('',)
>>> t''.values
()
>>> t'{'cheese'}'.strings
('', '')
>>> t'{'cheese'}'.values
('cheese',)

```

 interpolations*: [tuple](https://docs.python.org/3.14/library/stdtypes.html#tuple)[Interpolation, ...]*

Holds, as a [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple), the interpolations belonging to the template.

[Subject index](INDEX.md) · [Continue](types-code-example-cheese-camembert.md) · [Owning module, declaration or section: string.templatelib](string-templatelib-support-for-template-string-literals.md)
