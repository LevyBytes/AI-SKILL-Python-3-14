# configparser — Customizing Parser Behaviour — Contract: Spotting this gets especially tricky for the user if she edits the file in a proportional font.

Spotting this gets especially tricky for the user if she edits the file in a proportional font. That's the reason that, whenever your application has no need for values containing blank lines, you ought to think about forbidding them. Doing so makes blank lines split keys every time. With the example above, that would yield two keys, `key` and `this`.

- *default_section*, default value: `configparser.DEFAULTSECT` (that is: `"DEFAULT"`)

Setting aside a special section of default values to serve other sections or to feed interpolation is one of this library's potent ideas, enabling users to compose rich declarative configurations. Ordinarily this section goes by `"DEFAULT"`, but you may retarget it to whatever other valid section name you like. Common picks include `"general"` or `"common"`. Whatever name you give is what gets used to recognize default sections while reading from any source, and likewise when configuration is written back to a file. To read its present value use the `parser_instance.default_section` attribute, which can also be changed while running (say, to translate files between formats).

- *interpolation*, default value: `configparser.BasicInterpolation`

You can tailor interpolation behaviour by handing in a custom handler through the *interpolation* argument. `None` switches interpolation off entirely, while `ExtendedInterpolation()` delivers a richer flavor modeled on `zc.buildout`. The dedicated documentation section covers this in greater depth. For `RawConfigParser`, the default is `None`.

- *converters*, default value: not set

Config parsers come with option value getters that handle type conversion. The built-in set is `getint()`, `getfloat()`, and `getboolean()`. When you want additional getters, you can define them in a subclass or hand over a dictionary whose every key names a converter and whose every value is a callable carrying out that conversion. As an example, supplying `{'decimal': decimal.Decimal}` attaches `getdecimal()` to the parser object as well as to all section proxies. Put differently, you'd then be able to write both `parser_instance.getdecimal('section', 'key', fallback=0)` and `parser_instance['section'].getdecimal('key', 0)`.

When a converter has to reach the parser's state, you can write it as a method on a config parser subclass. Provided that method's name begins with `get`, it surfaces on every section proxy in the dict-compatible form (compare the `getdecimal()` example above).

You can take customization further by overriding the default values of these parser attributes. Because the defaults are set on the classes, subclasses or plain attribute assignment can override them.

[Subject index](INDEX.md) · [Previous](delimiters-and-comment-prefixes.md) · [Continue](configparser-boolean-states.md) · [Owning module, declaration or section: configparser](configparser-configuration-file-parser.md) · [Owning module, declaration or section: Customizing Parser Behaviour](parser-customization-overview.md)
