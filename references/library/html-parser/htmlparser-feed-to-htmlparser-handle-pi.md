# html.parser: HTML input feeding and event callbacks

### `HTMLParser` Methods

These are the methods available on an `HTMLParser` object:

 HTMLParser.feed(*data*)

Hand a chunk of text over to the parser. Processing covers only whatever amounts to complete elements; anything partial is held in a buffer until further text arrives or `close()` gets invoked. The *data* value has to be a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str).

 HTMLParser.close()

Compel every buffered byte to be processed, treating it as though an end-of-file marker came right after. A subclass may override this to tack on extra work once the input ends, yet any such override ought always to invoke the `close()` method on the `HTMLParser` base class.

 HTMLParser.reset()

Return the object to its initial state, discarding any data not yet processed. It runs automatically when the instance is created.

 HTMLParser.getpos()

Give back the present line number together with the offset.

 HTMLParser.get_starttag_text()

Hand back the literal text of the start tag opened most recently. Structured processing rarely calls for this, though it can come in handy when working with HTML “as deployed” or when reproducing input with only small edits (for instance, the spacing between attributes stays intact).

The methods below fire as data or markup elements turn up, and they exist to be overridden within a subclass. In the base class each one is a no-op (the sole exception being `handle_startendtag()`):

 HTMLParser.handle_starttag(*tag*, *attrs*)

Invoked to deal with an element's start tag (for example, `<div id="main">`).

Here the *tag* argument carries the tag's name lowercased. The *attrs* argument supplies a list of `(name, value)` pairs holding whatever attributes sat within the tag's `<>` brackets. Each *name* gets lowercased, any quotes around the *value* are dropped, and character plus entity references are substituted. Where an attribute has no value, *value* comes through as `None`.

Take the tag `<A HREF="https://www.cwi.nl/">` as a case in point: the call would arrive as `handle_starttag('a', [('href', 'https://www.cwi.nl/')])`.

Inside the attribute values, every entity reference drawn from [`html.entities`](https://docs.python.org/3.14/library/html.entities.html#module-html.entities) is swapped out.

 HTMLParser.handle_endtag(*tag*)

Invoked to take care of an element's end tag (for example, `</div>`).

The *tag* argument holds the tag's name in lowercase form.

 HTMLParser.handle_startendtag(*tag*, *attrs*)

Much like `handle_starttag()`, except it fires when the parser meets an empty tag in the XHTML style (`<img ... />`). Subclasses that need this specific lexical detail can override it; by default it merely chains `handle_starttag()` followed by `handle_endtag()`.

 HTMLParser.handle_data(*data*)

Invoked to deal with free-form data (text nodes, say, along with what sits inside elements such as `script` and `style`).

 HTMLParser.handle_entityref(*name*)

Invoked to handle a named character reference shaped like `&name;` (`>`, for example), in which *name* stands for a general entity reference (such as `'gt'`). It runs only when *convert_charrefs* is false.

 HTMLParser.handle_charref(*name*)

Invoked to handle numeric character references in decimal and hexadecimal form, written as `&#*NNN*;` and `&#x*NNN*;`. To illustrate, the decimal stand-in for `>` is `>` while the hexadecimal one is `>`; in that situation the method gets handed `'62'` or `'x3E'`. It runs only when *convert_charrefs* is false.

 HTMLParser.handle_comment(*data*)

Invoked the moment a comment turns up (for example, ``).

As an illustration, the comment `` will cause this method to be called with the argument `' comment '`.

Whatever sits inside Internet Explorer conditional comments (condcoms) reaches this method too; thus, given ``, this method will receive `'[if IE 9]>IE9-specific content<![endif]'`.

 HTMLParser.handle_decl(*decl*)

Invoked to take care of an HTML doctype declaration (for example, `<!DOCTYPE html>`).

Everything the declaration holds within the `<!...>` markup arrives as the *decl* parameter (for example, `'DOCTYPE html'`).

 HTMLParser.handle_pi(*data*)

Fires whenever a processing instruction shows up. The whole processing instruction lands in the *data* parameter. To illustrate, given the processing instruction `<?proc color='red'>`, the call arrives as `handle_pi("proc color='red'")`. A subclass is meant to override it; in the base class it does nothing at all.

Note

For processing instructions, the `HTMLParser` class follows the SGML syntax rules. Should an XHTML processing instruction carry the trailing `'?'`, that `'?'` ends up part of *data*.

[Subject index](INDEX.md) · [Previous](example-html-parser-application.md) · [Continue](htmlparser-unknown-decl.md) · [Owning module, declaration or section: html.parser](html-parser-htmlparser-class.md)
