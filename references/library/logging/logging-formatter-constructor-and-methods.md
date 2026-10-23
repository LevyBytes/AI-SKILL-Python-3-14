# logging - logging.Formatter constructor and methods

**style** ([*str*](https://docs.python.org/3.14/library/stdtypes.html#str)): May be `'%'`, `'{'` or `'$'`, fixing the way the format string gets merged with its data: by way of one of [printf-style String Formatting](https://docs.python.org/3.14/library/stdtypes.html#old-string-formatting) (`%`), [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) (`{`) or [`string.Template`](https://docs.python.org/3.14/library/string.html#string.Template) (`$`). This bears only on *fmt* (e.g. `'%(message)s'` versus `'{message}'`), not on the actual log messages handed to the logging methods. That said, [other ways](https://docs.python.org/3.14/howto/logging-cookbook.html#formatting-styles) exist to apply `{`- and `$`-formatting to log messages.

- **validate** ([*bool*](https://docs.python.org/3.14/library/functions.html#bool)): When `True` (the default), *fmt* and *style* that are incorrect or mismatched will raise a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError); for example, `logging.Formatter('%(asctime)s - %(message)s', style='{')`.

- **defaults** ([*dict*](https://docs.python.org/3.14/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3.14/library/stdtypes.html#str)*, **Any**]*): A dictionary holding default values to apply within custom fields. For example, `logging.Formatter('%(ip)s %(message)s', defaults={"ip": None})`

Changed in version 3.2: Added the *style* parameter.

Changed in version 3.8: Added the *validate* parameter.

Changed in version 3.10: Added the *defaults* parameter.

[Subject index](INDEX.md) · [Continue](logging-formatter-format-to-logging-formatter-formatstack.md) · [Owning module, declaration or section: logging](logging-logging-facility-for-python.md) · [Owning module, declaration or section: logging.Formatter constructor and methods](logging-formatter-class.md) · [Preceding source contract and version conditions](logging-formatter-class.md)
