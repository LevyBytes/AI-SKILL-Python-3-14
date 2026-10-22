# configparser: `configparser.RawConfigParser`

### RawConfigParser Objects

 `*class *configparser.RawConfigParser(*defaults=None*, *dict_type=dict*, *allow_no_value=False*, ***, *delimiters=('=', ':')*, *comment_prefixes=('#', ';')*, *inline_comment_prefixes=None*, *strict=True*, *empty_lines_in_values=True*, *default_section=configparser.DEFAULTSECT*, *interpolation=BasicInterpolation()*, *converters={}*, *allow_unnamed_section=False*)`

Legacy variant of the `ConfigParser`. Interpolation is off by default, and through its unsafe `add_section` and `set` methods, plus the legacy `defaults=` keyword argument handling, it permits non-string section names, option names, and values.

Changed in version 3.2: the following were introduced — *allow_no_value*, *delimiters*, *comment_prefixes*, *strict*, *empty_lines_in_values*, *default_section* and *interpolation*.

Changed in version 3.5: The *converters* argument was added.

Changed in version 3.8: Now that insertion order is retained, the default *dict_type* is [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict).

Changed in version 3.13: The *allow_unnamed_section* argument was added.

Note

Think about using `ConfigParser` instead, since it checks the types of the values stored internally. If interpolation isn't wanted, you can use `ConfigParser(interpolation=None)`.

[Subject index](INDEX.md) · [Previous](unnamed-sections-and-interpolation-limit.md) · [Continue](raw-config-section-and-value-mutation.md) · [Owning module, declaration or section: configparser](configparser-configuration-file-parser.md)
