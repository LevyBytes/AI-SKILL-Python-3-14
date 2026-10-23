# configparser - Customizing Parser Behaviour - Section introduction and initial examples

### Customizing Parser Behaviour

INI format variants are almost as numerous as the applications that rely on the format. `configparser` works hard to cover the broadest reasonable range of INI styles around. Its default behavior largely stems from historical reasons, and odds are good you'll want to adjust a few of its features.

Reaching for the `__init__()` options is the usual route to altering how a given config parser operates:

- *defaults*, default value: `None`

A dictionary of key-value pairs is what this option takes, and those pairs land in the `DEFAULT` section right away. It's a tidy means of backing compact configuration files that skip values matching the documented default.

Hint: when you need default values targeting one particular section, call `read_dict()` ahead of reading the real file.

- *dict_type*, default value: [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict)

This option weighs heavily on both how the mapping protocol acts and the appearance of the configuration files written out. Using the standard dictionary, each section is held in whatever order it joined the parser. The same applies to options inside sections.

You might supply a different dictionary type, for instance, to have sections and options sorted as they're written back.

Please note: a single operation can add a whole batch of key-value pairs at once. Supply a regular dictionary to those operations and the keys come out in order. For example:

```pycon
>>> parser = configparser.ConfigParser()
>>> parser.read_dict({'section1': {'key1': 'value1',
...                                'key2': 'value2',
...                                'key3': 'value3'},
...                   'section2': {'keyA': 'valueA',
...                                'keyB': 'valueB',
...                                'keyC': 'valueC'},
...                   'section3': {'foo': 'x',
...                                'bar': 'y',
...                                'baz': 'z'}
... })
>>> parser.sections()
['section1', 'section2', 'section3']
>>> [option for option in parser['section3']]
['foo', 'bar', 'baz']

```

- *allow_no_value*, default value: `False`

Certain configuration files famously carry settings that lack values while otherwise matching the syntax `configparser` accepts. To signal that such values ought to be tolerated, hand the constructor the *allow_no_value* parameter:

```pycon
>>> import configparser

>>> sample_config = """
... [mysqld]
...   user = mysql
...   pid-file = /var/run/mysqld/mysqld.pid
...   skip-external-locking
...   old_passwords = 1
...   skip-bdb
...   # we don't need ACID today
...   skip-innodb
... """
>>> config = configparser.ConfigParser(allow_no_value=True)
>>> config.read_string(sample_config)

>>> # Settings with values are treated as before:
>>> config["mysqld"]["user"]
'mysql'

>>> # Settings without values provide None:
>>> config["mysqld"]["skip-bdb"]

>>> # Settings which aren't specified still raise an error:
>>> config["mysqld"]["does-not-exist"]
Traceback (most recent call last):
  ...
KeyError: 'does-not-exist'

```

- *delimiters*, default value: `('=', ':')`

[Subject index](INDEX.md) · [Previous](mapping-protocol-access.md) · [Continue](delimiters-and-comment-prefixes.md) · [Owning module, declaration or section: configparser](configparser-configuration-file-parser.md)
