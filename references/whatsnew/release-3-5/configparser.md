# What’s New In Python 3.5 / configparser — configparser

### configparser

[`configparser`](https://docs.python.org/3.14/library/configparser.html#module-configparser) henceforth lets you tailor how values are converted, either by handing a dictionary of converters to the [`ConfigParser`](https://docs.python.org/3.14/library/configparser.html#configparser.ConfigParser) constructor or by declaring them as methods within `ConfigParser` subclasses. Whatever converters a parser instance defines get inherited by its section proxies.

Example:

```python
>>> import configparser
>>> conv = {}
>>> conv['list'] = lambda v: [e.strip() for e in v.split() if e.strip()]
>>> cfg = configparser.ConfigParser(converters=conv)
>>> cfg.read_string("""
... [s]
... list = a b c d e f g
... """)
>>> cfg.get('s', 'list')
'a b c d e f g'
>>> cfg.getlist('s', 'list')
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> section = cfg['s']
>>> section.getlist('list')
['a', 'b', 'c', 'd', 'e', 'f', 'g']

```

(Contributed by ?ukasz Langa in [bpo-18159](https://bugs.python.org/issue?@action=redirect&bpo=18159).)

[Subject index](INDEX.md) · [Previous source section](concurrent-futures.md) · [Next source section](contextlib.md) · [Release/subject declaration](summary-release-highlights.md)
