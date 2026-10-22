# html.parser: `HTMLParser.unknown_decl()`

HTMLParser.unknown_decl(*data*)

Fires when the parser reads a declaration it cannot recognize.

All that the declaration contains within the `<![...]>` markup arrives in the *data* parameter. Overriding it in a subclass is occasionally worthwhile. Within the base class it does nothing.

[Subject index](INDEX.md) · [Previous](htmlparser-feed-to-htmlparser-handle-pi.md) · [Continue](examples-section-introduction-and-initial-examples.md) · [Owning module, declaration or section: html.parser](html-parser-htmlparser-class.md) · [Owning module, declaration or section: `HTMLParser` Methods](htmlparser-feed-to-htmlparser-handle-pi.md)
