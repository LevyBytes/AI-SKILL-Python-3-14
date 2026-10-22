# What's New In Python 3.3 / API changes

### API changes

- The dimension count now has an official ceiling of 64.

- When shape, strides and suboffsets are empty, they are now represented by an empty tuple rather than `None`.

- Reading a memoryview element whose format is ?B? (unsigned bytes) now yields an integer (matching the struct module syntax). To get back a bytes object instead, first cast the view to ?c?.

- memoryview comparisons now rely on the logical structure of their operands and compare every array element by value. The struct module syntax is supported for all format strings. Views carrying unrecognised format strings remain allowed, yet they will invariably compare as unequal no matter what the view holds.

- Consult Build and C API Changes along with Porting C code for additional changes.

(Contributed by Stefan Krah in [bpo-10181](https://bugs.python.org/issue?@action=redirect&bpo=10181).)

See also

[**PEP 3118**](https://peps.python.org/pep-3118/) - Revising the Buffer Protocol

[Subject index](INDEX.md) · [Previous source section](features.md) · [Next source section](pep-393-flexible-string-representation.md) · [Release/subject declaration](summary-release-highlights.md)
