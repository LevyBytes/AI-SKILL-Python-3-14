# string: `string.Template`

### Template strings ($-strings)

Note

What's covered here arrived in Python 2.4: a no-frills templating approach resting on regular expressions. It came along before [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format), [formatted string literals](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings), and [template string literals](https://docs.python.org/3.14/library/string.templatelib.html#template-strings).

Don't confuse it with template string literals (t-strings), a Python 3.14 addition. Those produce [`string.templatelib.Template`](https://docs.python.org/3.14/library/string.templatelib.html#string.templatelib.Template) objects, which live in the [`string.templatelib`](https://docs.python.org/3.14/library/string.templatelib.html#module-string.templatelib) module.

Template strings give you the more basic string substitutions spelled out in [**PEP 292**](https://peps.python.org/pep-0292/). One leading use for them is internationalization (i18n), since there the plainer syntax and behavior makes translation easier than Python's other built-in string formatting facilities do. For a library that builds on template strings to do i18n, have a look at the [flufl.i18n](https://flufli18n.readthedocs.io/en/latest/) package.

Template strings allow `$`-based substitutions, governed by the rules below:

- `$$` is an escape; it is replaced with a single `$`.

- `$identifier` designates a substitution placeholder tied to a mapping key of `"identifier"`. Out of the box, `"identifier"` is held to any case-insensitive ASCII alphanumeric string (underscores allowed) whose first character is an underscore or an ASCII letter. The placeholder specification ends at the first non-identifier character following the `$` character.

- `${identifier}` amounts to the same thing as `$identifier`. You need it where valid identifier characters trail the placeholder yet don't belong to it — for example `"${noun}ification"`.

Should `$` turn up anywhere else in the string, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) gets raised.

The `string` module furnishes a `Template` class that puts these rules into effect. Here are the methods of `Template`:

 *class *string.Template(*template*)

A lone argument goes to the constructor, namely the template string.

[Subject index](INDEX.md) · [Previous](text-alignment-format-examples.md) · [Continue](string-template-substitute-to-string-template-get-identifiers.md) · [Owning module, declaration or section: string](string-common-string-operations.md)
