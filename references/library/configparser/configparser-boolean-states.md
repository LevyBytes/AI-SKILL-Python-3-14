# configparser: `ConfigParser.BOOLEAN_STATES`

ConfigParser.BOOLEAN_STATES

Out of the box, `getboolean()` makes config parsers regard these values as `True`: `'1'`, `'yes'`, `'true'`, `'on'` and these as `False`: `'0'`, `'no'`, `'false'`, `'off'`. To change that, supply your own dictionary mapping strings to their Boolean results. For example:

[Subject index](INDEX.md) · [Previous](multiline-value-indentation.md) · [Owning module, declaration or section: configparser](configparser-configuration-file-parser.md) · [Owning module, declaration or section: Customizing Parser Behaviour](parser-customization-overview.md) · [Required continuation of the source contract](configparser-optionxform-to-configparser-sectcre.md)
