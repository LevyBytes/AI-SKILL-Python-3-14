# What's New In Python 3.2 / Other Language Changes — collections, configparser, dbm, shelve, sys

### Other Language Changes

A selection of more modest tweaks landed in the core Python language:

- The string-formatting behavior of [`format()`](https://docs.python.org/3.14/library/functions.html#format) and [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) acquired extra behavior tied to the format character **#**. Formerly, with binary, octal, or hexadecimal integers, it prefixed the result with "0b", "0o", or "0x" in turn. It now copes with floats, complex, and Decimal too, forcing the output to always carry a decimal point even where no digits trail it.

```python
>>> format(20, '#o')
'0o24'
>>> format(12.34, '#5.0f')
'  12.'

```

(Suggested by Mark Dickinson and implemented by Eric Smith in [bpo-7094](https://bugs.python.org/issue?@action=redirect&bpo=7094).)

- A new [`str.format_map()`](https://docs.python.org/3.14/library/stdtypes.html#str.format_map) method broadens what the existing [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) method can do by taking arbitrary [mapping](https://docs.python.org/3.14/glossary.html#term-mapping) objects. With it, string formatting becomes usable against any of Python's numerous dictionary-style objects, including [`defaultdict`](https://docs.python.org/3.14/library/collections.html#collections.defaultdict), [`Shelf`](https://docs.python.org/3.14/library/shelve.html#shelve.Shelf), [`ConfigParser`](https://docs.python.org/3.14/library/configparser.html#configparser.ConfigParser), or [`dbm`](https://docs.python.org/3.14/library/dbm.html#module-dbm). The method also helps with custom [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) subclasses that canonicalize keys ahead of lookup or that furnish a [`__missing__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__missing__) method covering unknown keys:

```python
>>> import shelve
>>> d = shelve.open('tmp.shl')
>>> 'The {project_name} status is {status} as of {date}'.format_map(d)
'The testing project status is green as of February 15, 2011'

>>> class LowerCasedDict(dict):
...     def __getitem__(self, key):
...         return dict.__getitem__(self, key.lower())
...
>>> lcd = LowerCasedDict(part='widgets', quantity=10)
>>> 'There are {QUANTITY} {Part} in stock'.format_map(lcd)
'There are 10 widgets in stock'

>>> class PlaceholderDict(dict):
...     def __missing__(self, key):
...         return '<{}>'.format(key)
...
>>> 'Hello {name}, welcome to {location}'.format_map(PlaceholderDict())
'Hello <name>, welcome to <location>'

```

>

(Suggested by Raymond Hettinger and implemented by Eric Smith in [bpo-6081](https://bugs.python.org/issue?@action=redirect&bpo=6081).)

- Launching the interpreter now accepts a quiet flag, `-q`, suppressing the copyright and version banner that otherwise appears in interactive mode. You can examine whether it is set via the [`sys.flags`](https://docs.python.org/3.14/library/sys.html#sys.flags) attribute:

```shell
$ python -q
>>> sys.flags
sys.flags(debug=0, division_warning=0, inspect=0, interactive=0,
optimize=0, dont_write_bytecode=0, no_user_site=0, no_site=0,
ignore_environment=0, verbose=0, bytes_warning=0, quiet=1)

```

(Contributed by Marcin Wojdyr in [bpo-1772833](https://bugs.python.org/issue?@action=redirect&bpo=1772833)).

- The way [`hasattr()`](https://docs.python.org/3.14/library/functions.html#hasattr) operates is by invoking [`getattr()`](https://docs.python.org/3.14/library/functions.html#getattr) and watching for a raised exception. That mechanism lets it spot methods conjured on the fly by [`__getattr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__) or [`__getattribute__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattribute__) which would otherwise not appear in the class dictionary. Earlier, *hasattr* would swallow every exception, potentially hiding real bugs. It has since been narrowed so that it traps only [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) and permits all other exceptions to propagate:

```python
>>> class A:
...     @property
...     def f(self):
...         return 1 // 0
...
>>> a = A()
>>> hasattr(a, 'f')
Traceback (most recent call last):
  ...
ZeroDivisionError: integer division or modulo by zero

```

(Discovered by Yury Selivanov and fixed by Benjamin Peterson; [bpo-9666](https://bugs.python.org/issue?@action=redirect&bpo=9666).)

[Subject index](INDEX.md) · [Previous source section](pep-3333-python-web-server-gateway-interface-v1-0-1.md) · [Next source section](other-language-changes-outer.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
