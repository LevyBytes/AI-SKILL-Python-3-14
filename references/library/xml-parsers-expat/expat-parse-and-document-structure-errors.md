# xml.parsers.expat: Expat syntax and document-structure errors

### Expat error constants

You will find the constants below inside the `xml.parsers.expat.errors` module. They help when you need to make sense of certain attributes carried by the `ExpatError` exception objects that get raised once an error happens. Because, to stay backward compatible, each constant holds the error *message* string rather than the numeric error *code*, the way to do this is to match its [`code`](https://docs.python.org/3.14/library/pyexpat.html#xml.parsers.expat.ExpatError.code) attribute against `errors.codes[errors.XML_ERROR_*CONSTANT_NAME*]`.

These are the attributes exposed by the `errors` module:

 xml.parsers.expat.errors.codes

A dictionary that pairs each string description with its matching error code.

Added in version 3.2.

 xml.parsers.expat.errors.messages

A dictionary that pairs each numeric error code with its string description.

Added in version 3.2.

 xml.parsers.expat.errors.XML_ERROR_ASYNC_ENTITY

 xml.parsers.expat.errors.XML_ERROR_ATTRIBUTE_EXTERNAL_ENTITY_REF

Inside an attribute value, an entity reference pointed at an external entity rather than at an internal one.

 xml.parsers.expat.errors.XML_ERROR_BAD_CHAR_REF

A character reference named a character that XML forbids (such as character `0`, or ‘`&#0;`’).

 xml.parsers.expat.errors.XML_ERROR_BINARY_ENTITY_REF

An entity reference pointed to an entity declared with a notation, which therefore can't be parsed.

 xml.parsers.expat.errors.XML_ERROR_DUPLICATE_ATTRIBUTE

The same attribute appeared two or more times within one start tag.

 xml.parsers.expat.errors.XML_ERROR_INCORRECT_ENCODING

 xml.parsers.expat.errors.XML_ERROR_INVALID_TOKEN

Triggered when some input byte cannot be mapped correctly onto a character — for instance, a NUL byte (value `0`) appearing in a UTF-8 input stream.

 xml.parsers.expat.errors.XML_ERROR_JUNK_AFTER_DOC_ELEMENT

Past the document element, content other than whitespace showed up.

[Subject index](INDEX.md) · [Previous](expat-content-model-types-and-quantifiers.md) · [Continue](expat-processing-instruction-and-encoding-errors.md) · [Owning module, declaration or section: xml.parsers.expat](expat-parser-factory-and-exception.md)
