# configparser: `configparser.ConfigParser`

### ConfigParser Objects

 `*class *configparser.ConfigParser(*defaults=None*, *dict_type=dict*, *allow_no_value=False*, ***, *delimiters=('=', ':')*, *comment_prefixes=('#', ';')*, *inline_comment_prefixes=None*, *strict=True*, *empty_lines_in_values=True*, *default_section=configparser.DEFAULTSECT*, *interpolation=BasicInterpolation()*, *converters={}*, *allow_unnamed_section=False*)`

The principal configuration parser. Supplying *defaults* seeds the dictionary of intrinsic defaults. Supplying *dict_type* selects the dictionary class used to build the objects for the section list, for the options inside a section, and for the default values.

Supplying *delimiters* defines the set of substrings that separate keys from values. Supplying *comment_prefixes* defines the set of substrings that introduce comments on otherwise blank lines; such comments may be indented. Supplying *inline_comment_prefixes* defines the set of substrings that introduce comments on lines that are not empty.

With *strict* set to `True` (the default), the parser rejects any duplicate section or option while reading from one source (file, string or dictionary), raising `DuplicateSectionError` or `DuplicateOptionError`. With *empty_lines_in_values* set to `False` (default: `True`), every blank line terminates an option; otherwise blank lines inside a multiline option are preserved as part of the value. With *allow_no_value* set to `True` (default: `False`), valueless options are permitted; their stored value is `None` and they are written without the trailing delimiter.

Supplying *default_section* names the special section that stores defaults for the other sections and for interpolation (its usual name is `"DEFAULT"`). You can read and modify this value at runtime via the `default_section` instance attribute. Doing so won't re-process an already parsed config file, but it does apply when you write parsed settings out to a fresh config file.

You can tailor interpolation by passing a custom handler through the *interpolation* argument. Passing `None` disables interpolation outright, while `ExtendedInterpolation()` supplies a richer variant modeled on `zc.buildout`. The dedicated documentation section covers this further.

Every option name involved in interpolation is run through the `optionxform()` method, exactly as any other option name reference would be. For example, with the default `optionxform()` implementation (which lowercases option names), the values `foo %(bar)s` and `foo %(BAR)s` mean the same thing.

Supplying *converters* expects a dictionary in which each key names a type converter and each value is a callable that performs the conversion from string to the target datatype. Each converter receives its own matching `get*()` method on the parser object and on section proxies.

Supplying *allow_unnamed_section* as `True` (default: `False`) lets the first section name be left out. See the "Unnamed Sections" section.

You can load multiple configurations into one `ConfigParser`, with the configuration added most recently holding the highest priority. For any clashing keys, the value comes from the more recent configuration while keys that existed before are kept. The example that follows reads an `override.ini` file, which overrides any clashing keys from the `example.ini` file.

```ini
[DEFAULT]
ServerAliveInterval = -1

```

```pycon
>>> config_override = configparser.ConfigParser()
>>> config_override['DEFAULT'] = {'ServerAliveInterval': '-1'}
>>> with open('override.ini', 'w') as configfile:
...     config_override.write(configfile)
...
>>> config_override = configparser.ConfigParser()
>>> config_override.read(['example.ini', 'override.ini'])
['example.ini', 'override.ini']
>>> print(config_override.get('DEFAULT', 'ServerAliveInterval'))
-1

```

Changed in version 3.1: The default *dict_type* is [`collections.OrderedDict`](https://docs.python.org/3.14/library/collections.html#collections.OrderedDict).

Changed in version 3.2: these arguments first appeared — *allow_no_value*, *delimiters*, *comment_prefixes*, *strict*, *empty_lines_in_values*, *default_section* and *interpolation*.

Changed in version 3.5: The *converters* argument was added.

Changed in version 3.7: The *defaults* argument gets read via `read_dict()`, which keeps parser behavior consistent: keys and values that aren't strings are implicitly turned into strings.

Changed in version 3.8: Because insertion order is now preserved, the default *dict_type* is [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict).

Changed in version 3.13: A `MultilineContinuationError` is raised whenever *allow_no_value* is `True` and a valueless key is carried on with an indented line.

Changed in version 3.13: The *allow_unnamed_section* argument was added.

[Subject index](INDEX.md) · [Previous](legacy-api-examples-code-example-import-configparser.md) · [Continue](config-parser-defaults-sections-and-get.md) · [Owning module, declaration or section: configparser](configparser-configuration-file-parser.md)
