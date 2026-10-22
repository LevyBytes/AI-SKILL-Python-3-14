# string.templatelib — Template strings

### Template strings

Added in version 3.14.

As a tool for bespoke string handling, template strings carry all the expressive power of Python's [f-strings](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings), yet they hand back a `Template` instance that exposes both the literal portions and the interpolated (curly-bracketed) portions of a string *before* those pieces get joined together.

You write a t-string by putting a `'t'` prefix where you would otherwise use an `'f'`, as shown here:

```pycon
>>> pi = 3.14
>>> t't-strings are new in Python {pi!s}!'
Template(
   strings=('t-strings are new in Python ', '!'),
   interpolations=(Interpolation(3.14, 'pi', 's', ''),)
)

```

[Subject index](INDEX.md) · [Previous](string-templatelib-support-for-template-string-literals.md) · [Continue](string-templatelib-template-class.md) · [Owning module, declaration or section: string.templatelib](string-templatelib-support-for-template-string-literals.md)
