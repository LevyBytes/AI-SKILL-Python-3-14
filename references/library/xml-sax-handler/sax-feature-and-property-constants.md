# xml.sax.handler: SAX namespace, validation and parser feature constants

xml.sax.handler.feature_namespaces

 value: `"http://xml.org/sax/features/namespaces"`. true: Carry out Namespace processing. false: Optionally skip Namespace processing (this implies namespace-prefixes; default). access: read-only while (parsing); read/write while (not parsing).

 xml.sax.handler.feature_namespace_prefixes

 value: `"http://xml.org/sax/features/namespace-prefixes"`. true: Report the original prefixed names plus the attributes that Namespace declarations use. false: Withhold the attributes that Namespace declarations use, and optionally withhold original prefixed names (default). access: read-only while (parsing); read/write while (not parsing).

 xml.sax.handler.feature_string_interning

 value: `"http://xml.org/sax/features/string-interning"`. true: Every element name, prefix, attribute name, Namespace URI, and local name gets interned through the built-in intern function. false: Names need not be interned, though they might be (default). access: read-only while (parsing); read/write while (not parsing).

 xml.sax.handler.feature_validation

 value: `"http://xml.org/sax/features/validation"`. true: Report every validation error (this implies external-general-entities and external-parameter-entities). false: Suppress validation errors. access: read-only while (parsing); read/write while (not parsing).

 xml.sax.handler.feature_external_ges

Warning

Turning this on exposes a vulnerability to [external entity attacks](https://en.wikipedia.org/wiki/XML_external_entity_attack) when the parser handles user-provided XML content. Please weigh your [threat model](https://en.wikipedia.org/wiki/Threat_model) before enabling this feature.

   value: `"http://xml.org/sax/features/external-general-entities"`. true: Pull in every external general (text) entity. false: Leave out external general entities. access: read-only while (parsing); read/write while (not parsing).

 xml.sax.handler.feature_external_pes

 value: `"http://xml.org/sax/features/external-parameter-entities"`. true: Pull in every external parameter entity, the external DTD subset included. false: Leave out all external parameter entities, even the external DTD subset. access: read-only while (parsing); read/write while (not parsing).

 xml.sax.handler.all_features

List of all features.

 xml.sax.handler.property_lexical_handler

 Its value is `"http://xml.org/sax/properties/lexical-handler"`. Its data type, xml.sax.handler.LexicalHandler, is unsupported under Python 2. Purpose: an optional extension handler that covers lexical events such as comments. Its access is read/write.

 xml.sax.handler.property_declaration_handler

 Its value is `"http://xml.org/sax/properties/declaration-handler"`. Its data type, xml.sax.sax2lib.DeclHandler, is unsupported under Python 2. Purpose: an optional extension handler that covers DTD-related events apart from notations and unparsed entities. Its access is read/write.

 xml.sax.handler.property_dom_node

 Its value is `"http://xml.org/sax/properties/dom-node"`. Its data type, org.w3c.dom.Node, is unsupported under Python 2. Purpose: while parsing, the current DOM node under visit when this is a DOM iterator; while not parsing, the root DOM node used for iteration. Its access is read-only while (parsing) and read/write while (not parsing).

 xml.sax.handler.property_xml_string

 Its value is `"http://xml.org/sax/properties/xml-string"`. Its data type is Bytes. Purpose: the literal run of characters that served as the source for the current event. Its access is read-only.

 xml.sax.handler.all_properties

List of all known property names.

[Subject index](INDEX.md) · [Previous](xml-sax-handler-lexicalhandler-class.md) · [Continue](sax-locator-document-and-character-events.md) · [Owning module, declaration or section: xml.sax.handler](xml-sax-handler-contenthandler-class.md)
