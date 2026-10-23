# xml.sax.xmlreader - The `AttributesNS` Interface

### The `AttributesNS` Interface

Acting as a subtype of the `Attributes` interface (see section The Attributes Interface), this interface exposes every method that one supports on `AttributesNS` objects as well.

The following methods are also available:

 AttributesNS.getValueByQName(*name*)

Return the value for a qualified name.

 AttributesNS.getNameByQName(*name*)

Return the `(namespace, localname)` pair for a qualified *name*.

 AttributesNS.getQNameByName(*name*)

Return the qualified name for a `(namespace, localname)` pair.

 AttributesNS.getQNames()

Return the qualified names of all attributes.

[Subject index](INDEX.md) · [Previous](attributes-getlength-to-attributes-getvalue.md) · [Continue](../xml-sax-utils/xml-sax-saxutils-escape-to-xml-sax-saxutils-quoteattr.md)
