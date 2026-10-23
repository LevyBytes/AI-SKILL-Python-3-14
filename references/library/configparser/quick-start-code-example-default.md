# configparser - Quick Start - Code example: [DEFAULT]

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

You get the same result by invoking `ConfigParser.read()` and handing it multiple files through the *filenames* parameter.

[Subject index](INDEX.md) · [Previous](quick-start-section-introduction-and-initial-examples.md) · [Continue](supported-datatypes.md) · [Owning module, declaration or section: configparser](configparser-configuration-file-parser.md) · [Owning module, declaration or section: Quick Start](quick-start-section-introduction-and-initial-examples.md)
