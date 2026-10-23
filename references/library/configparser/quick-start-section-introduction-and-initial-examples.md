# configparser - Quick Start - Section introduction and initial examples

### Quick Start

Consider a configuration file kept this simple:

```ini
[DEFAULT]
ServerAliveInterval = 45
Compression = yes
CompressionLevel = 9
ForwardX11 = yes

[forge.example]
User = hg

[topsecret.server.example]
Port = 50022
ForwardX11 = no

```

A later section lays out how INI files are organized. In short, the file holds sections, and every section carries keys paired with values. Files of this kind are both readable and writable through the `configparser` classes. To begin, we'll generate the configuration file shown above from code.

```pycon
>>> import configparser
>>> config = configparser.ConfigParser()
>>> config['DEFAULT'] = {'ServerAliveInterval': '45',
...                      'Compression': 'yes',
...                      'CompressionLevel': '9'}
>>> config['forge.example'] = {}
>>> config['forge.example']['User'] = 'hg'
>>> config['topsecret.server.example'] = {}
>>> topsecret = config['topsecret.server.example']
>>> topsecret['Port'] = '50022'     # mutates the parser
>>> topsecret['ForwardX11'] = 'no'  # same here
>>> config['DEFAULT']['ForwardX11'] = 'yes'
>>> with open('example.ini', 'w') as configfile:
...   config.write(configfile)
...

```

Notice that working with a config parser resembles working with a dictionary. A few distinctions exist, discussed further on, yet the behavior tracks dictionary expectations very closely.

Having built and stored a configuration file, we'll now load it again and inspect the contents it carries.

```pycon
>>> config = configparser.ConfigParser()
>>> config.sections()
[]
>>> config.read('example.ini')
['example.ini']
>>> config.sections()
['forge.example', 'topsecret.server.example']
>>> 'forge.example' in config
True
>>> 'python.org' in config
False
>>> config['forge.example']['User']
'hg'
>>> config['DEFAULT']['Compression']
'yes'
>>> topsecret = config['topsecret.server.example']
>>> topsecret['ForwardX11']
'no'
>>> topsecret['Port']
'50022'
>>> for key in config['forge.example']:
...     print(key)
user
compressionlevel
serveraliveinterval
compression
forwardx11
>>> config['forge.example']['ForwardX11']
'yes'

```

The snippet above shows how plain the API is. Its single piece of cleverness is the `DEFAULT` section, whose entries supply fallback defaults to every other section [1]. Keep in mind too that section keys ignore case and end up saved in lowercase [1].

You can pull more than one configuration into a single `ConfigParser`; whichever configuration was added latest carries the greatest weight. Where keys collide, the value comes from the newer configuration, yet keys that already existed stay put. In the snippet below an `override.ini` file is loaded, and it supersedes any clashing keys coming from `example.ini`.

[Subject index](INDEX.md) · [Previous](configparser-configuration-file-parser.md) · [Continue](quick-start-code-example-default.md) · [Owning module, declaration or section: configparser](configparser-configuration-file-parser.md)
