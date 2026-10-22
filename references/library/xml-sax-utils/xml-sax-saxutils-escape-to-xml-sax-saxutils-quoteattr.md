# xml.sax.saxutils: `xml.sax.saxutils.escape()`, `xml.sax.saxutils.unescape()`, `xml.sax.saxutils.quoteattr()`

## xml.sax.saxutils — SAX Utilities??

### `xml.sax.saxutils` — SAX Utilities

**Source code:** [Lib/xml/sax/saxutils.py](https://github.com/python/cpython/tree/3.14/Lib/xml/sax/saxutils.py)

---

The module `xml.sax.saxutils` holds a number of classes and functions that prove commonly useful while building SAX applications, whether through direct use or as base classes.

 xml.sax.saxutils.escape(*data*, *entities={}*)

Escape `'&'`, `'<'`, and `'>'` in a string of data.

Other strings of data can be escaped by passing a dictionary as the optional *entities* parameter. Every key and value must be a string; each key gets replaced with its matching value. The characters `'&'`, `'<'` and `'>'` are always escaped, even when *entities* is supplied.

Note

This function should serve only to escape characters that can't appear directly in XML. Do not employ this function as a general string translation function.

 xml.sax.saxutils.unescape(*data*, *entities={}*)

Unescape `'&'`, `'<'`, and `'>'` in a string of data.

Other strings of data can be unescaped by passing a dictionary as the optional *entities* parameter. Every key and value must be a string; each key gets replaced with its matching value. `'&'`, `'<'`, and `'>'` are always unescaped, even when *entities* is supplied.

 xml.sax.saxutils.quoteattr(*data*, *entities={}*)

Resembles `escape()`, except that it additionally readies *data* to serve as an attribute value. What it gives back is a quoted form of *data* carrying whatever extra replacements are required. `quoteattr()` will pick a quote character according to the content of *data*, trying to dodge encoding any quote characters within the string. When both single- and double-quote characters already occur in *data*, the double-quote characters get encoded and *data* gets wrapped in double-quotes. You can drop the resulting string straight in as an attribute value:

```python
>>> print("<element attr=%s>" % quoteattr("ab ' cd \" ef"))
<element attr="ab ' cd &quot; ef">
```

For producing attribute values in HTML, or in any SGML that relies on the reference concrete syntax, this function proves handy.

[Subject index](INDEX.md) · [Continue](xml-sax-saxutils-xmlgenerator-class.md)
