# xml.parsers.expat: CDATA, external entity, encoding and namespace errors

xml.parsers.expat.errors.XML_ERROR_UNCLOSED_CDATA_SECTION

A marked CDATA section was left unclosed.

 xml.parsers.expat.errors.XML_ERROR_EXTERNAL_ENTITY_HANDLING

 xml.parsers.expat.errors.XML_ERROR_NOT_STANDALONE

Even though the XML declaration claimed the document to be “standalone”, the parser found it was not, while the `NotStandaloneHandler` had been installed and returned `0`.

 xml.parsers.expat.errors.XML_ERROR_UNEXPECTED_STATE

 xml.parsers.expat.errors.XML_ERROR_ENTITY_DECLARED_IN_PE

 xml.parsers.expat.errors.XML_ERROR_FEATURE_REQUIRES_XML_DTD

A requested operation depends on DTD support being compiled in, yet Expat had been built without that support. A standard build of the `xml.parsers.expat` module should never surface this.

 xml.parsers.expat.errors.XML_ERROR_CANT_CHANGE_FEATURE_ONCE_PARSING

A behavioral adjustment that may only be made prior to parsing was requested once parsing had already begun. At present `UseForeignDTD()` is the sole source of this.

 xml.parsers.expat.errors.XML_ERROR_UNBOUND_PREFIX

With namespace processing turned on, a prefix that had not been declared was encountered.

 xml.parsers.expat.errors.XML_ERROR_UNDECLARING_PREFIX

The document tried to undo the namespace declaration tied to a prefix.

[Subject index](INDEX.md) · [Previous](expat-processing-instruction-and-encoding-errors.md) · [Continue](parameter-entity-and-reserved-prefix-errors.md) · [Owning module, declaration or section: xml.parsers.expat](expat-parser-factory-and-exception.md) · [Owning module, declaration or section: Expat error constants](expat-parse-and-document-structure-errors.md)
