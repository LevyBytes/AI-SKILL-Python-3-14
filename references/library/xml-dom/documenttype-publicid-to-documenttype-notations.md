# xml.dom - DocumentType Objects

### DocumentType Objects

Details about the notations and entities a document declares (taking in the external subset when the parser consults it and can surface that data) come from a `DocumentType` object. You reach a document's `DocumentType` via the `Document` object's `doctype` attribute; when the document carries no `DOCTYPE` declaration, its `doctype` attribute is `None` in place of an instance of this interface.

`DocumentType` specializes `Node`, contributing these extra attributes:

 DocumentType.publicId

The public identifier covering the document type definition's external subset. It will be either a string or `None`.

 DocumentType.systemId

The system identifier covering the document type definition's external subset. It will be a URI as a string, or `None`.

 DocumentType.internalSubset

A string holding the whole internal subset taken from the document. The enclosing brackets around the subset are left out. When the document carries no internal subset, this should be `None`.

 DocumentType.name

The name the `DOCTYPE` declaration gives for the root element, when one is present.

 DocumentType.entities

A `NamedNodeMap` listing the definitions of external entities. Where an entity name is declared multiple times, only the earliest definition appears (the rest are dropped, as the XML recommendation demands). This may be `None` when the parser does not surface the data, or when no entities are declared.

 DocumentType.notations

A `NamedNodeMap` listing the definitions of notations. Where a notation name is declared multiple times, only the earliest definition appears (the rest are dropped, as the XML recommendation demands). This may be `None` when the parser does not surface the data, or when no notations are declared.

[Subject index](INDEX.md) · [Previous](nodelist-item-to-nodelist-length.md) · [Continue](document-documentelement-to-document-getelementsbytagnamens.md) · [Owning module, declaration or section: xml.dom](xml-dom-the-document-object-model-api.md)
