# xml.parsers.expat: Namespace, comment, CDATA and external-entity handlers

xmlparser.EndNamespaceDeclHandler(*prefix*)

Called once the closing tag is reached for an element that carried a namespace declaration. It fires once per namespace declaration on the element, in the reverse of the order in which `StartNamespaceDeclHandler` was called to mark the start of each namespace declaration's scope. Calls to this handler happen after the matching `EndElementHandler` for the end of the element.

 xmlparser.CommentHandler(*data*)

Called for comments. *data* holds the comment text, leaving off the leading `'<!-``-'` and trailing `'-``->'`.

 xmlparser.StartCdataSectionHandler()

Called at the start of a CDATA section. This and `EndCdataSectionHandler` are needed in order to pin down the syntactical start and end of CDATA sections.

 xmlparser.EndCdataSectionHandler()

Called at the end of a CDATA section.

 xmlparser.DefaultHandler(*data*)

Called for any characters in the XML document that no applicable handler has been set for. These are characters belonging to a construct that could be reported, yet whose handler was never supplied.

 xmlparser.DefaultHandlerExpand(*data*)

This works the same as `DefaultHandler()`, except that it does not hold back expansion of internal entities. The entity reference will not be handed to the default handler.

 xmlparser.NotStandaloneHandler()

Called when the XML document has not been declared a standalone document. This comes up whenever an external subset exists or a parameter entity is referenced, yet the XML declaration fails to set standalone to `yes` in an XML declaration. When this handler returns `0`, the parser raises an `XML_ERROR_NOT_STANDALONE` error. When this handler is left unset, the parser raises no exception for this situation.

 xmlparser.ExternalEntityRefHandler(*context*, *base*, *systemId*, *publicId*)

Warning

Should a handler you implement reach local files and/or the network, it can open a vulnerability to [external entity attacks](https://en.wikipedia.org/wiki/XML_external_entity_attack) when `xmlparser` runs on user-provided XML content. Do weigh your [threat model](https://en.wikipedia.org/wiki/Threat_model) before you implement this handler.

Called whenever an external entity is referenced. *base* is the current base, as set by an earlier call to `SetBase()`. The public and system identifiers, *systemId* and *publicId*, come as strings when supplied; should the public identifier be missing, *publicId* comes as `None`. Treat the *context* value as opaque, putting it to use solely in the manner laid out below.

To have external entities parsed, you must implement this handler. Its job is to build the sub-parser through `ExternalEntityParserCreate(context)`, hook it up to the right callbacks, and parse the entity. The handler ought to return an integer; a return of `0` makes the parser raise an `XML_ERROR_EXTERNAL_ENTITY_HANDLING` error, while otherwise parsing keeps going.

When this handler is not supplied, external entities get reported through the `DefaultHandler` callback, when one is supplied.

[Subject index](INDEX.md) · [Previous](expat-error-location-and-element-handlers.md) · [Continue](expaterror-code-to-expaterror-offset.md) · [Owning module, declaration or section: xml.parsers.expat](expat-parser-factory-and-exception.md) · [Owning module, declaration or section: XMLParser Objects](expat-parsing-and-entity-protection-threshold.md)
