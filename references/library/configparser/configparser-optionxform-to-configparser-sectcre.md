# configparser: `ConfigParser.optionxform()`, `ConfigParser.SECTCRE`

```pycon
>>> custom = configparser.ConfigParser()
>>> custom['section1'] = {'funky': 'nope'}
>>> custom['section1'].getboolean('funky')
Traceback (most recent call last):
...
ValueError: Not a boolean: nope
>>> custom.BOOLEAN_STATES = {'sure': True, 'nope': False}
>>> custom['section1'].getboolean('funky')
False

```

Other Boolean pairs you might commonly use include `accept`/`reject` or `enabled`/`disabled`.

 ConfigParser.optionxform(*option*)

Each read, get, or set call runs option names through this method. By default it lowercases the name, which also means every key emerges lowercase when a configuration file is written out. If that behavior doesn't fit your needs, override the method. For instance:

```pycon
>>> config = """
... [Section1]
... Key = Value
...
... [Section2]
... AnotherKey = Value
... """
>>> typical = configparser.ConfigParser()
>>> typical.read_string(config)
>>> list(typical['Section1'].keys())
['key']
>>> list(typical['Section2'].keys())
['anotherkey']
>>> custom = configparser.RawConfigParser()
>>> custom.optionxform = lambda option: option
>>> custom.read_string(config)
>>> list(custom['Section1'].keys())
['Key']
>>> list(custom['Section2'].keys())
['AnotherKey']

```

Note

Option names get mapped into a canonical form by the optionxform function. The function ought to be idempotent: a name that is already canonical should come back unchanged.

 ConfigParser.SECTCRE

A pre-compiled regular expression that parses section headers. By default it maps `[section]` to the name `"section"`. Because whitespace counts as part of the section name, `[ larch ]` is parsed as a section whose name is `" larch "`. If that's not what you want, override this attribute. For instance:

```pycon
>>> import re
>>> config = """
... [Section 1]
... option = value
...
... [  Section 2  ]
... another = val
... """
>>> typical = configparser.ConfigParser()
>>> typical.read_string(config)
>>> typical.sections()
['Section 1', '  Section 2  ']
>>> custom = configparser.ConfigParser()
>>> custom.SECTCRE = re.compile(r"\[ *(?P<header>[^]]+?) *\]")
>>> custom.read_string(config)
>>> custom.sections()
['Section 1', 'Section 2']

```

Note

ConfigParser objects also carry an `OPTCRE` attribute that recognizes option lines, but overriding it is discouraged, as doing so would clash with the constructor options *allow_no_value* and *delimiters*.

[Subject index](INDEX.md) · [Continue](legacy-api-examples-section-introduction-and-initial-examples.md) · [Owning module, declaration or section: configparser](configparser-configuration-file-parser.md) · [Owning module, declaration or section: Customizing Parser Behaviour](parser-customization-overview.md) · [Owning module, declaration or section: ConfigParser.BOOLEAN_STATES](configparser-boolean-states.md) · [Preceding source contract and version conditions](configparser-boolean-states.md)
