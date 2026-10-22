# Python 3.14.0 beta 3 / library / pickle

[gh-135321](https://github.com/python/cpython/issues/135321): Within the C implementation of [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle), a correct exception is now raised for the `BINSTRING` opcode when values exceed 0x7fffffff.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
