# html.parser — `html.parser` — Simple HTML and XHTML parser

# Html.Parser

### `html.parser` — Simple HTML and XHTML parser

**Source code:** [Lib/html/parser.py](https://github.com/python/cpython/tree/3.14/Lib/html/parser.py)

---

Within this module lives a class called `HTMLParser`, the foundation on which reading of text documents written in HTML (HyperText Mark-up Language) and XHTML is built.

 *class *html.parser.HTMLParser(***, *convert_charrefs=True*, *scripting=False*)

Builds a parser object that copes with reading malformed markup.

When *convert_charrefs* holds its default value of true, every character reference — aside from those sitting inside elements such as `script` and `style` — is turned automatically into its matching Unicode character.

With *scripting* left at its default of false, whatever sits inside the `noscript` element gets parsed as usual; flip it to true and that content comes back untouched, with no parsing applied.

You supply HTML data to an `HTMLParser` object, and it invokes handler methods as it runs across start tags, end tags, text, comments, and the rest of the markup. To get the behavior you want, derive your own class from `HTMLParser` and replace its methods.

No verification happens here that an end tag lines up with its start tag, nor is the end-tag handler triggered for elements that get closed implicitly when some enclosing element is closed.

Changed in version 3.4: *convert_charrefs* keyword argument added.

Changed in version 3.5: For the *convert_charrefs* argument, the default has become `True`.

Changed in version 3.14.1: Added the *scripting* parameter.

[Subject index](INDEX.md) · [Continue](example-html-parser-application.md)
