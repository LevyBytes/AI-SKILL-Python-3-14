# html`html` - HyperText Markup Language support

## html - HyperText Markup Language support

### `html` - HyperText Markup Language support

**Source code:** [Lib/html/__init__.py](https://github.com/python/cpython/tree/3.14/Lib/html/__init__.py)

---

This module defines utilities to manipulate HTML.

 html.escape(*s*, *quote=True*)

Turn the characters `&`, `<` and `>` in string *s* into HTML-safe sequences. Reach for this when you need to render text that may hold such characters inside HTML. When the optional *quote* flag is true (its default), the (`"`) and (`'`) characters get translated as well; that helps when the text goes into an HTML attribute value delimited by quotes, as in `<a href="...">`. With *quote* set to false, the (`"`) and (`'`) characters are left untranslated.

Added in version 3.2.

 html.unescape(*s*)

Turn every named and numeric character reference (e.g. `>`, `>`, `>`) in the string *s* into the matching Unicode characters. This function follows the rules the HTML 5 standard lays down for both valid and invalid character references, plus the [`list of HTML 5 named character references`](https://docs.python.org/3.14/library/html.entities.html#html.entities.html5).

Added in version 3.4.

---

Submodules in the `html` package are:

- [`html.parser`](https://docs.python.org/3.14/library/html.parser.html#module-html.parser) – HTML/XHTML parser with lenient parsing mode

- [`html.entities`](https://docs.python.org/3.14/library/html.entities.html#module-html.entities) – HTML entity definitions

[Subject index](INDEX.md)
