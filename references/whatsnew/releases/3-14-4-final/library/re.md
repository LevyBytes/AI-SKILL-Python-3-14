# Python 3.14.4 final / library / re

[gh-143637](https://github.com/python/cpython/issues/143637): Corrected a crash within socket.sendmsg() able to arise if ancillary data is mutated re-entrantly throughout argument parsing.

[gh-143543](https://github.com/python/cpython/issues/143543): Corrects a crash within itertools.groupby able to arise once a user-defined [`__eq__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__eq__) method re-enters the iterator amid key comparison.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
