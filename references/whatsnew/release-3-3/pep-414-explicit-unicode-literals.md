# What's New In Python 3.3 / PEP 414: Explicit Unicode literals

### PEP 414: Explicit Unicode literals

So as to smooth the move off Python 2 for Unicode aware Python applications that lean heavily on Unicode literals, Python 3.3 brings back support for the ?`u`? prefix on string literals. Carrying no semantic weight in Python 3, the prefix exists purely to cut down the count of strictly mechanical edits when migrating to Python 3, which lets developers concentrate on the weightier semantic changes (for instance the stricter default split between binary and text data).

See also

[**PEP 414**](https://peps.python.org/pep-0414/) - Explicit Unicode literals

PEP written by Armin Ronacher.

[Subject index](INDEX.md) · [Previous source section](pep-409-suppressing-exception-context.md) · [Next source section](pep-3155-qualified-name-for-classes-and-functions.md) · [Release/subject declaration](summary-release-highlights.md)
