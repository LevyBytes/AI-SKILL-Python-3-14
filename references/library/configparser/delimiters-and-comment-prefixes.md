# configparser — Customizing Parser Behaviour — Contract: Delimiters are the substrings that mark the boundary between keys and values inside a section.

Delimiters are the substrings that mark the boundary between keys and values inside a section. The earliest appearance of a delimiting substring on a line counts as the delimiter. As a result, values (though not keys) are free to contain the delimiters.

Refer as well to the *space_around_delimiters* argument belonging to `ConfigParser.write()`.

- *comment_prefixes*, default value: `('#', ';')`

- *inline_comment_prefixes*, default value: `None`

Comment prefixes are the strings signaling where a valid comment begins inside a config file. Only on otherwise blank lines (which may be indented) do *comment_prefixes* apply, while *inline_comment_prefixes* may follow any valid value (section names, options and blank lines included). By default inline comments stay off, with `'#'` and `';'` serving as the prefixes for whole-line comments.

Changed in version 3.2: In previous versions of `configparser` behaviour matched `comment_prefixes=('#',';')` and `inline_comment_prefixes=(';',)`.

Be aware that config parsers offer no escaping of comment prefixes, so reaching for *inline_comment_prefixes* might stop users from giving option values characters that double as comment prefixes. Whenever you're unsure, leave *inline_comment_prefixes* unset. Regardless, the lone means of keeping comment-prefix characters at a line's start within multiline values is to interpolate the prefix, like so:

```python
>>> from configparser import ConfigParser, ExtendedInterpolation
>>> parser = ConfigParser(interpolation=ExtendedInterpolation())
>>> # the default BasicInterpolation could be used as well
>>> parser.read_string("""
... [DEFAULT]
... hash = #
...
... [hashes]
... shebang =
...   ${hash}!/usr/bin/env python
...   ${hash} -*- coding: utf-8 -*-
...
... extensions =
...   enabled_extension
...   another_extension
...   #disabled_by_comment
...   yet_another_extension
...
... interpolation not necessary = if # is not at line start
... even in multiline values = line #1
...   line #2
...   line #3
... """)
>>> print(parser['hashes']['shebang'])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
>>> print(parser['hashes']['extensions'])

enabled_extension
another_extension
yet_another_extension
>>> print(parser['hashes']['interpolation not necessary'])
if # is not at line start
>>> print(parser['hashes']['even in multiline values'])
line #1
line #2
line #3

```

- *strict*, default value: `True`

Set to `True`, the parser refuses any duplicate section or option while reading from one source (through `read_file()`, `read_string()` or `read_dict()`). Fresh applications are advised to keep their parsers strict.

Changed in version 3.2: In previous versions of `configparser` behaviour matched `strict=False`.

- *empty_lines_in_values*, default value: `True`

Within config parsers, a value can span several lines so long as it sits more deeply indented than the key owning it. By default the parsers further allow blank lines to count as part of values. Keys, meanwhile, may carry whatever indentation you like to aid readability. The upshot is that as configuration files grow large and intricate, the user readily loses the thread of the file's structure. Consider this:

```ini
[Section]
key = multiline
  value with a gotcha

 this = is still a part of the multiline value of 'key'

```

[Subject index](INDEX.md) · [Previous](parser-customization-overview.md) · [Continue](multiline-value-indentation.md) · [Owning module, declaration or section: configparser](configparser-configuration-file-parser.md) · [Owning module, declaration or section: Customizing Parser Behaviour](parser-customization-overview.md)
