# xml.sax.xmlreader: `xml.sax.xmlreader.AttributesNSImpl`

*class *xml.sax.xmlreader.AttributesNSImpl(*attrs*, *qnames*)

Namespace-aware variant of `AttributesImpl`, which will be passed to `startElementNS()`. It descends from `AttributesImpl`, but treats attribute names as two-tuples of *namespaceURI* and *localname*. On top of that, it supplies several methods that expect qualified names in the form they take within the original document. The `AttributesNS` interface (see section The AttributesNS Interface) is what this class implements.

[Subject index](INDEX.md) · [Previous](xml-sax-xmlreader-attributesimpl-class.md) · [Continue](xmlreader-parse-to-xmlreader-setproperty.md)
