# Template String Literals (t-strings)

### Template String Literals (t-strings)

An *t-string* (formally a *template string literal*) is a string literal carrying a `t` or `T` prefix.

These strings abide by the same syntax and evaluation rules as formatted string literals, save for the following differences:

- In place of evaluating to a `str` object, template string literals evaluate to a [`string.templatelib.Template`](https://docs.python.org/3.14/library/string.templatelib.html#string.templatelib.Template) object.

- The [`format()`](https://docs.python.org/3.14/library/functions.html#format) protocol goes unused. Rather, the format specifier and conversions (if present) are handed to a fresh [`Interpolation`](https://docs.python.org/3.14/library/string.templatelib.html#string.templatelib.Interpolation) object built for each evaluated expression. The code that processes the resulting [`Template`](https://docs.python.org/3.14/library/string.templatelib.html#string.templatelib.Template) object decides on its own how format specifiers and conversions should be handled.

- Format specifiers that contain nested replacement fields are evaluated eagerly, ahead of being handed to the [`Interpolation`](https://docs.python.org/3.14/library/string.templatelib.html#string.templatelib.Interpolation) object. Take, for instance, an interpolation written as `{amount:.{precision}f}`: it will evaluate the inner expression `{precision}` so as to settle the value of the `format_spec` attribute. Were `precision` to be `2`, the resulting format specifier would come out as `'.2f'`.

-

[Subject index](INDEX.md) · [Previous](format-specifier.md) · [Required continuation of the source contract](printf-string-formatting-overview.md)
