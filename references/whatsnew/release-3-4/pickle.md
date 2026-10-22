# What's New In Python 3.4 / pickle — pickle

### pickle

[`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) gains (though it does not pick it by default) a fresh pickle protocol, protocol 4. The newcomer tackles several shortcomings found in earlier protocols, including the serialization of nested classes, extremely large strings and containers, plus classes whose [`__new__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__new__) method expects keyword-only arguments. It throws in a few efficiency gains as well.

See also

[**PEP 3154**](https://peps.python.org/pep-3154/) ? Pickle protocol 4

PEP written by Antoine Pitrou and implemented by Alexandre Vassalotti.

[Subject index](INDEX.md) · [Previous source section](pdb.md) · [Next source section](plistlib.md) · [Release/subject declaration](release-highlights.md)
