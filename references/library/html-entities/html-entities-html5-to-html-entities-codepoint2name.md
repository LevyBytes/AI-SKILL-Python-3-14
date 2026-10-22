# html.entities — `html.entities` — Definitions of HTML general entities

## html.entities — Definitions of HTML general entities

### `html.entities` — Definitions of HTML general entities

**Source code:** [Lib/html/entities.py](https://github.com/python/cpython/tree/3.14/Lib/html/entities.py)

---

Four dictionaries are defined by this module: `html5`, `name2codepoint`, `codepoint2name`, and `entitydefs`.

 html.entities.html5

A dictionary mapping HTML5 named character references [1] onto the matching Unicode character(s), e.g. `html5['gt;'] == '>'`. Be aware that the name keeps its trailing semicolon (for example `'gt;'`); still, the standard accepts a number of these names without it, and the name then appears both with and without the `';'`. See also [`html.unescape()`](https://docs.python.org/3.14/library/html.html#html.unescape).

Added in version 3.3.

 html.entities.entitydefs

A dictionary that pairs each XHTML 1.0 entity definition with its ISO Latin-1 replacement text.

 html.entities.name2codepoint

A dictionary that maps HTML4 entity names to the Unicode code points.

 html.entities.codepoint2name

A dictionary that maps Unicode code points to HTML4 entity names.

Footnotes

[Subject index](INDEX.md) · [Continue](../html/html-escape-to-html-unescape.md)
