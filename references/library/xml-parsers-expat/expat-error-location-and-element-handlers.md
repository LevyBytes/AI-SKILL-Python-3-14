# xml.parsers.expat: Error locations and declaration, element and text handlers

xmlparser.ErrorLineNumber

Line number at which an error occurred.

The following attributes hold values about the current parse location within an `xmlparser` object. While a callback is reporting a parse event, they point at the first of the run of characters that produced the event. When invoked outside a callback, the position reported sits just past the last parse event (whether or not a callback was tied to it).

 xmlparser.CurrentByteIndex

Current byte index in the parser input.

 xmlparser.CurrentColumnNumber

Current column number in the parser input.

 xmlparser.CurrentLineNumber

Current line number in the parser input.

What follows is the list of handlers you can set. To set a handler on an `xmlparser` object *o*, use `o.handlername = func`. *handlername* has to come from the following list, and *func* has to be a callable object that accepts the right number of arguments. Unless stated otherwise, the arguments are all strings.

 xmlparser.XmlDeclHandler(*version*, *encoding*, *standalone*)

Called once the XML declaration has been parsed. That XML declaration is the (optional) statement of which version of the XML recommendation is in force, the encoding of the document text, plus an optional "standalone" declaration. *version* and *encoding* arrive as strings, and *standalone* arrives as `1` when the document declares itself standalone, `0` when it declares itself not standalone, or `-1` when the standalone clause was dropped. This works only with Expat version 1.95.0 or newer.

 xmlparser.StartDoctypeDeclHandler(*doctypeName*, *systemId*, *publicId*, *has_internal_subset*)

Called when Expat starts parsing the document type declaration (`<!DOCTYPE ...`). The *doctypeName* is supplied exactly as it appears. The *systemId* and *publicId* parameters give the system and public identifiers when specified, or `None` when omitted. *has_internal_subset* will be true when the document carries an internal document declaration subset. This needs Expat version 1.2 or newer.

 xmlparser.EndDoctypeDeclHandler()

Called once Expat has finished parsing the document type declaration. This needs Expat version 1.2 or newer.

 xmlparser.ElementDeclHandler(*name*, *model*)

Called one time for each element type declaration. *name* holds the element type's name, while *model* holds a representation of the content model.

 xmlparser.AttlistDeclHandler(*elname*, *attname*, *type*, *default*, *required*)

Called for every declared attribute of an element type. When an attribute list declaration declares three attributes, this handler fires three times, once per attribute. *elname* is the name of the element the declaration applies to, and *attname* is the name of the attribute declared. The attribute type comes as a string in *type*; the possible values are `'CDATA'`, `'ID'`, `'IDREF'`, … *default* gives the default value used for the attribute when the document instance does not specify it, or `None` when there is no default value (`#IMPLIED` values). When the document instance is required to supply the attribute, *required* will be true. This needs Expat version 1.95.0 or newer.

 xmlparser.StartElementHandler(*name*, *attributes*)

Called when each element begins. *name* is a string carrying the element name, and *attributes* carries the element's attributes. With `ordered_attributes` true, this comes as a list (the full description lives under `ordered_attributes`). Without it, this comes as a dictionary mapping names to values.

 xmlparser.EndElementHandler(*name*)

Called for the end of every element.

 xmlparser.ProcessingInstructionHandler(*target*, *data*)

Called for every processing instruction.

 xmlparser.CharacterDataHandler(*data*)

Called for character data. It fires for ordinary character data, CDATA marked content, and ignorable whitespace. Applications that have to tell these cases apart can use the `StartCdataSectionHandler`, `EndCdataSectionHandler`, and `ElementDeclHandler` callbacks to gather the needed information. Note that the character data may arrive in chunks even when it is short, so `CharacterDataHandler()` may fire more than once. To prevent that, set the `buffer_text` instance attribute to `True`.

 xmlparser.UnparsedEntityDeclHandler(*entityName*, *base*, *systemId*, *publicId*, *notationName*)

Called for unparsed (NDATA) entity declarations. This is present only for version 1.2 of the Expat library; for newer versions, use `EntityDeclHandler` instead. (The underlying function in the Expat library has been marked obsolete.)

 xmlparser.EntityDeclHandler(*entityName*, *is_parameter_entity*, *value*, *base*, *systemId*, *publicId*, *notationName*)

Called for every entity declaration. With parameter and internal entities, *value* arrives as a string giving the entity's declared contents; with external entities it arrives as `None`. The *notationName* parameter arrives as `None` for parsed entities, and as the notation's name for unparsed entities. *is_parameter_entity* arrives as true for a parameter entity and false for a general one (general entities being all that most applications need to handle). This becomes available only from version 1.95.0 of the Expat library onward.

 xmlparser.NotationDeclHandler(*notationName*, *base*, *systemId*, *publicId*)

Called for notation declarations. *notationName*, *base*, and *systemId*, and *publicId* are strings when given. When the public identifier is omitted, *publicId* will be `None`.

 xmlparser.StartNamespaceDeclHandler(*prefix*, *uri*)

Called when an element carries a namespace declaration. Namespace declarations get processed before the `StartElementHandler` runs for the element on which the declarations sit.

[Subject index](INDEX.md) · [Previous](expat-amplification-protection-and-error-position.md) · [Continue](expat-namespace-doctype-and-entity-handlers.md) · [Owning module, declaration or section: xml.parsers.expat](expat-parser-factory-and-exception.md) · [Owning module, declaration or section: XMLParser Objects](expat-parsing-and-entity-protection-threshold.md)
