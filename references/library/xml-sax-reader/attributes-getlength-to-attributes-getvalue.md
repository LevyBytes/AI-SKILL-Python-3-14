# xml.sax.xmlreader — The `Attributes` Interface

### The `Attributes` Interface

`Attributes` objects realize part of the [mapping protocol](https://docs.python.org/3.14/glossary.html#term-mapping), namely the methods `copy()`, `get()`, [`__contains__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__contains__), `items()`, `keys()`, and `values()`. Beyond those, the methods below are supplied:

 Attributes.getLength()

Return the number of attributes.

 Attributes.getNames()

Return the names of the attributes.

 Attributes.getType(*name*)

Returns the type of the attribute *name*, which is normally `'CDATA'`.

 Attributes.getValue(*name*)

Return the value of attribute *name*.

[Subject index](INDEX.md) · [Previous](inputsource-setpublicid-to-inputsource-getcharacterstream.md) · [Continue](attributesns-getvaluebyqname-to-attributesns-getqnames.md)
