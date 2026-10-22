# What’s New In Python 3.8 / pprint — pprint

### pprint

Several functions in the [`pprint`](https://docs.python.org/3.14/library/pprint.html#module-pprint) module gained a *sort_dicts* parameter. Those functions, by default, keep sorting dictionaries ahead of rendering or printing them. Yet when *sort_dicts* is given the value false, a dictionary preserves whichever order its keys were inserted in. That can help when you compare against JSON inputs while debugging.

On top of that, a handy new [`pprint.pp()`](https://docs.python.org/3.14/library/pprint.html#pprint.pp) function resembles [`pprint.pprint()`](https://docs.python.org/3.14/library/pprint.html#pprint.pprint) except *sort_dicts* defaults to `False`:

```python
>>> from pprint import pprint, pp
>>> d = dict(source='input.txt', operation='filter', destination='output.txt')
>>> pp(d, width=40)                  # Original order
{'source': 'input.txt',
 'operation': 'filter',
 'destination': 'output.txt'}
>>> pprint(d, width=40)              # Keys sorted alphabetically
{'destination': 'output.txt',
 'operation': 'filter',
 'source': 'input.txt'}

```

(Contributed by Rémi Lapeyre in [bpo-30670](https://bugs.python.org/issue?@action=redirect&bpo=30670).)

[Subject index](INDEX.md) · [Previous source section](plistlib.md) · [Next source section](py-compile.md) · [Release/subject declaration](assignment-expressions.md)
