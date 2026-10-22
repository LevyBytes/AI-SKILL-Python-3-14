# configparser — Supported Datatypes

### Supported Datatypes

The datatypes of values within configuration files are never inferred by config parsers; instead they are always kept internally as strings. So whenever a different datatype is required, the conversion is yours to perform:

```pycon
>>> int(topsecret['Port'])
50022
>>> float(topsecret['CompressionLevel'])
9.0

```

Because this need crops up constantly, config parsers ship several convenient getter methods covering integers, floats and booleans. Booleans deserve special mention: feeding a value straight to `bool()` accomplishes nothing, given that `bool('False')` still evaluates to `True`. For that reason config parsers add `getboolean()` as well. Ignoring case, it accepts Boolean values drawn from `'yes'`/`'no'`, `'on'`/`'off'`, `'true'`/`'false'` and `'1'`/`'0'` [1]. As an illustration:

```pycon
>>> topsecret.getboolean('ForwardX11')
False
>>> config['forge.example'].getboolean('ForwardX11')
True
>>> config.getboolean('forge.example', 'Compression')
True

```

Beyond `getboolean()`, config parsers expose matching `getint()` and `getfloat()` methods too. The supplied converters can be tweaked, and you may also register converters of your own. [1]

[Subject index](INDEX.md) · [Previous](quick-start-code-example-default.md) · [Continue](fallback-values.md) · [Owning module, declaration or section: configparser](configparser-configuration-file-parser.md)
