# What's New In Python 3.4 / enum — enum, socket

> Whatsnew note. Reworded narrative; identifiers retained exactly.

The fresh [`enum`](https://docs.python.org/3.14/library/enum.html#module-enum) module (specified in [**PEP 435**](https://peps.python.org/pep-0435/)) ships a canonical implementation of enumeration types. This lets other modules ? for instance [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) ? surface clearer error text and stronger debugging help, swapping out opaque integer constants for enumeration values that stay backwards compatible.

See also

[**PEP 435**](https://peps.python.org/pep-0435/) ? Adding an Enum type to the Python standard library

Authored as a PEP by Barry Warsaw, plus Eli Bendersky and Ethan Furman; the implementation came from Ethan Furman.

[Subject index](INDEX.md) · [Next source section](pathlib.md) · [Release/subject declaration](release-highlights.md) · [Release/subject declaration](ensurepip.md) · [Preceding release/subject continuation](ensurepip.md)
