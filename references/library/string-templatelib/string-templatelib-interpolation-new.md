# string.templatelib.Interpolation: Template literal construction and value structure

__new__(*value: [object](https://docs.python.org/3.14/library/functions.html#object)*, *expression: [str](https://docs.python.org/3.14/library/stdtypes.html#str)*, *conversion: [Literal](https://docs.python.org/3.14/library/typing.html#typing.Literal)['a', 'r', 's'] | [None](https://docs.python.org/3.14/library/constants.html#None) = None*, *format_spec: [str](https://docs.python.org/3.14/library/stdtypes.html#str) = ''*)

Assemble a fresh `Interpolation` object out of its constituent pieces.

Parameters:

- **value** – The interpolation's evaluated, in-scope outcome.

- **expression** – Either the text of a valid Python expression or an empty string.

- **conversion** – Whichever [conversion](https://docs.python.org/3.14/library/string.html#formatstrings) applies, picked from `None`, `'a'`, `'r'`, or `'s'`.

- **format_spec** – An optional, free-form string acting as the [format specification](https://docs.python.org/3.14/library/string.html#formatspec) for showing the value.

[Subject index](INDEX.md) · [Previous](string-templatelib-interpolation-class.md) · [Continue](string-templatelib-convert.md) · [Owning module, declaration or section: string.templatelib](string-templatelib-support-for-template-string-literals.md) · [Owning module, declaration or section: string.templatelib.Interpolation](string-templatelib-interpolation-class.md) · [Owning module, declaration or section: Types](string-templatelib-template-class.md)
