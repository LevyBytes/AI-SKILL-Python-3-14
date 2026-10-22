# 3.2.2. NotImplemented

### 3.2.2. NotImplemented

A single value belongs to this type. Exactly one object holds that value. You reach this object via the built-in name [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented). When numeric methods and rich comparison methods cannot perform the operation for the given operands, they should hand back this value. (The interpreter will then attempt the reflected operation, or fall back some other way, according to the operator.) It must not be assessed in a boolean context.

For fuller treatment, consult [Implementing the arithmetic operations](https://docs.python.org/3.14/library/numbers.html#implementing-the-arithmetic-operations).

Changed in version 3.9: Assessing [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented) within a boolean context became deprecated.

Changed in version 3.14: Assessing [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented) within a boolean context will now raise a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). Formerly it yielded [`True`](https://docs.python.org/3.14/library/constants.html#True) while issuing a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning), as it had done from Python 3.9 onward.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Previous source section](none.md) · [Following source section](ellipsis.md)
