# xml.parsers.expat - ExpatError Exceptions

### ExpatError Exceptions

`ExpatError` exceptions carry a number of interesting attributes:

 ExpatError.code

Expat's own internal error number for that particular error. The `errors.messages` dictionary translates these error numbers into Expat's error messages. As an example:

```python
from xml.parsers.expat import ParserCreate, ExpatError, errors

p = ParserCreate()
try:
    p.Parse(some_xml_document)
except ExpatError as err:
    print("Error:", errors.messages[err.code])

```

The `errors` module also supplies error message constants along with a dictionary `codes` that maps those messages back to the error codes; see below.

 ExpatError.lineno

The line number where the error was spotted. Line numbering starts at `1`.

 ExpatError.offset

The character offset within the line at which the error happened. Column numbering starts at `0`.

[Subject index](INDEX.md) · [Previous](expat-namespace-doctype-and-entity-handlers.md) · [Continue](example.md) · [Owning module, declaration or section: xml.parsers.expat](expat-parser-factory-and-exception.md)
