# What's New In Python 3.6 / PEP 520: Preserving Class Attribute Definition Order

### PEP 520: Preserving Class Attribute Definition Order

Within a class definition body the attributes carry an intrinsic sequence: the order their names show up in the source. That sequence is now kept in the resulting class's [`__dict__`](https://docs.python.org/3.14/reference/datamodel.html#type.__dict__) attribute.

On top of that, the working default class *execution* namespace (handed back by [type.__prepare__()](https://docs.python.org/3.14/reference/datamodel.html#prepare)) is now a mapping that keeps insertion order.

See also

[**PEP 520**](https://peps.python.org/pep-0520/): Preserving Class Attribute Definition Order

PEP written and implemented by Eric Snow.

[Subject index](INDEX.md) · [Previous source section](pep-528-change-windows-console-encoding-to-utf-8.md) · [Next source section](pep-468-preserving-keyword-argument-order.md) · [Release/subject declaration](summary-release-highlights.md)
