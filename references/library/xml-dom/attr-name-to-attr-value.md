# xml.dom — Attr Objects

### Attr Objects

`Attr` derives from `Node`, and so picks up all of its attributes.

 Attr.name

The name of the attribute. Within a document that uses namespaces it may carry a colon.

 Attr.localName

Whatever trails the colon in the name, if a colon is present, or otherwise the whole name. This is a read-only attribute.

 Attr.prefix

Whatever precedes the colon in the name, if a colon is present, or otherwise the empty string.

 Attr.value

The textual value of the attribute. It is a synonym for the `nodeValue` attribute.

[Subject index](INDEX.md) · [Previous](element-tagname-to-element-setattributens.md) · [Continue](namednodemap-length-to-namednodemap-item.md) · [Owning module, declaration or section: xml.dom](xml-dom-the-document-object-model-api.md)
