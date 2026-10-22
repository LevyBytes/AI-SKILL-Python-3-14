# What’s New in Python 2.2 / PEP 234: Iterators

Keep in mind that iterators move in one direction only; you cannot step back to a prior element, restart the iterator, or duplicate it. While an iterator object is free to offer extra abilities like these, the protocol itself demands only a [`next()`](https://docs.python.org/3.14/library/functions.html#next) method.

See also

[**PEP 234**](https://peps.python.org/pep-0234/) - Iterators

Authored by Ka-Ping Yee and GvR; the Python Labs crew built it, chiefly GvR alongside Tim Peters.

[Subject index](INDEX.md) · [Next source section](pep-255-simple-generators.md) · [Release/subject declaration](introduction.md) · [Release/subject declaration](pep-234-iterators.md) · [Preceding release/subject continuation](pep-234-iterators.md)
