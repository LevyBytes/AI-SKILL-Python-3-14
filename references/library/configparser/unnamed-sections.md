# configparser — Unnamed Sections

### Unnamed Sections

You may leave off the first (or only) section's name and reach its values through the `UNNAMED_SECTION` attribute.

```pycon
>>> config = """
... option = value
...
... [  Section 2  ]
... another = val
... """
>>> unnamed = configparser.ConfigParser(allow_unnamed_section=True)
>>> unnamed.read_string(config)
>>> unnamed.get(configparser.UNNAMED_SECTION, 'option')
'value'

```

[Subject index](INDEX.md) · [Previous](supported-ini-file-structure.md) · [Continue](configparser-basicinterpolation-class.md) · [Owning module, declaration or section: configparser](configparser-configuration-file-parser.md)
