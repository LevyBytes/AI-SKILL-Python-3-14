# What's New In Python 3.3 / PEP 412: Key-Sharing Dictionary

### PEP 412: Key-Sharing Dictionary

The dictionaries that hold objects? attributes can now share a slice of their internal storage with one another (specifically the slice that keeps the keys together with their respective hashes). This trims the memory footprint of programs that spin up many instances of non-builtin types.

See also

[**PEP 412**](https://peps.python.org/pep-0412/) - Key-Sharing Dictionary

PEP written and implemented by Mark Shannon.

[Subject index](INDEX.md) · [Previous source section](pep-3155-qualified-name-for-classes-and-functions.md) · [Next source section](pep-362-function-signature-object.md) · [Release/subject declaration](summary-release-highlights.md)
