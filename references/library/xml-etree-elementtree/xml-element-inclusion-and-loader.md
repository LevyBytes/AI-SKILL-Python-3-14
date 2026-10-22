# xml.etree.ElementTree: `xml.etree.ElementInclude.default_loader()`, `xml.etree.ElementInclude.include()`

### Reference

### Functions

 xml.etree.ElementInclude.default_loader(*href*, *parse*, *encoding=None*)

Default loader. This stock loader pulls an included resource off disk. *href* is a URL. *parse* picks the parse mode, either "xml" or "text". *encoding* is an optional text encoding; absent one, the encoding is `utf-8`. The return value is the expanded resource. For a parse mode of `"xml"`, that is an `Element` instance; for a parse mode of `"text"`, it is a string. Should the loader fail, it may hand back `None` or throw an exception.

 xml.etree.ElementInclude.include(*elem*, *loader=None*, *base_url=None*, *max_depth=6*)

This routine expands XInclude directives in-place within the tree referenced by *elem*. *elem* is either the root `Element` or an `ElementTree` instance from which to locate that element. *loader* is an optional resource loader; when left out, it falls back to `default_loader()`. When supplied, it must be a callable presenting the same interface as `default_loader()`. *base_url* is the base URL of the original file, used to resolve relative include file references. *max_depth* caps the number of recursive inclusions. The cap is in place to lower the danger of a malicious content explosion. Hand it `None` to switch the limit off.

Changed in version 3.9: Added the *base_url* and *max_depth* parameters.

[Subject index](INDEX.md) · [Continue](xml-etree-elementtree-element-class.md) · [Owning module, declaration or section: xml.etree.ElementTree](xml-etree-elementtree-the-elementtree-xml-api.md)
