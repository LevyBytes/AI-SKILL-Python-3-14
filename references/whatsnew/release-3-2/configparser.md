# What's New In Python 3.2 / configparser — configparser

### configparser

Adjustments were made to the [`configparser`](https://docs.python.org/3.14/library/configparser.html#module-configparser) module so the default parser, plus the INI syntax it understands, behaves more usefully and more predictably. The legacy `ConfigParser` class was dropped in favour of `SafeConfigParser`, which was then itself renamed to [`ConfigParser`](https://docs.python.org/3.14/library/configparser.html#configparser.ConfigParser). Inline comment handling is switched off out of the box, and neither section nor option duplicates may appear inside one configuration source.

Config parsers picked up a fresh API built around the mapping protocol:

```python
>>> parser = ConfigParser()
>>> parser.read_string("""
... [DEFAULT]
... location = upper left
... visible = yes
... editable = no
... color = blue
...
... [main]
... title = Main Menu
... color = green
...
... [options]
... title = Options
... """)
>>> parser['main']['color']
'green'
>>> parser['main']['editable']
'no'
>>> section = parser['options']
>>> section['title']
'Options'
>>> section['title'] = 'Options (editable: %(editable)s)'
>>> section['title']
'Options (editable: no)'

```

Because this fresh API sits on top of the classic one, custom parser subclasses ought to work with it as-is, no edits required.

The INI layout that config parsers will accept is now configurable. You may name alternative option/value delimiters and comment prefixes, rename the *DEFAULT* section, or swap out the interpolation syntax.

Pluggable interpolation is supported, including one extra interpolation handler, [`ExtendedInterpolation`](https://docs.python.org/3.14/library/configparser.html#configparser.ExtendedInterpolation):

```python
>>> parser = ConfigParser(interpolation=ExtendedInterpolation())
>>> parser.read_dict({'buildout': {'directory': '/home/ambv/zope9'},
...                   'custom': {'prefix': '/usr/local'}})
>>> parser.read_string("""
... [buildout]
... parts =
...   zope9
...   instance
... find-links =
...   ${buildout:directory}/downloads/dist
...
... [zope9]
... recipe = plone.recipe.zope9install
... location = /opt/zope
...
... [instance]
... recipe = plone.recipe.zope9instance
... zope9-location = ${zope9:location}
... zope-conf = ${custom:prefix}/etc/zope.conf
... """)
>>> parser['buildout']['find-links']
'\n/home/ambv/zope9/downloads/dist'
>>> parser['instance']['zope-conf']
'/usr/local/etc/zope.conf'
>>> instance = parser['instance']
>>> instance['zope-conf']
'/usr/local/etc/zope.conf'
>>> instance['zope9-location']
'/opt/zope'

```

Several smaller capabilities arrived too, such as letting read operations name an encoding, supplying fallback values to get-functions, or pulling data straight out of dictionaries and strings.

(All changes contributed by Łukasz Langa.)

[Subject index](INDEX.md) · [Previous source section](pdb.md) · [Next source section](urllib-parse.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
