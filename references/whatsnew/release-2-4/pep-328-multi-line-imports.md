# What’s New in Python 2.4 / PEP 328: Multi-line Imports

### PEP 328: Multi-line Imports

A single language adjustment is a minor syntactic refinement intended to simplify importing numerous names out of one module. Within a `from module import names` statement, *names* is a list of names delimited by commas. When that list grows very long, your options are to write several imports referencing the same module, or to escape the line endings with backslashes in this fashion:

```python
from SimpleXMLRPCServer import SimpleXMLRPCServer,\
            SimpleXMLRPCRequestHandler,\
            CGIXMLRPCRequestHandler,\
            resolve_dotted_attribute

```

Python 2.4's syntactic update merely permits enclosing the names inside parentheses. Because Python disregards newlines inside a parenthesized expression, the backslashes become unnecessary:

```python
from SimpleXMLRPCServer import (SimpleXMLRPCServer,
                                SimpleXMLRPCRequestHandler,
                                CGIXMLRPCRequestHandler,
                                resolve_dotted_attribute)

```

The PEP further proposes that every [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statement become an absolute import, where a leading `.` character signals a relative import. That portion of the PEP went unimplemented in Python 2.4, though it was finished in Python 2.5.

See also

[**PEP 328**](https://peps.python.org/pep-0328/) - Imports: Multi-Line and Absolute/Relative

Written by Aahz. Multi-line imports were implemented by Dima Dorfman.

[Subject index](INDEX.md) · [Previous source section](the-context-type.md) · [Next source section](pep-331-locale-independent-float-string-conversions.md) · [Release/subject declaration](pep-218-built-in-set-objects.md)
