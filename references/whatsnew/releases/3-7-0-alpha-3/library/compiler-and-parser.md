# Python 3.7.0 alpha 3 / library / compiler and parser

[bpo-32037](https://bugs.python.org/issue?@action=redirect&bpo=32037): Any integer that fits within a signed 32-bit integer will now be pickled under protocol 0 through the INT opcode. The result is a smaller pickle, quicker pickling and unpickling, and these integers unpickling as int instances on Python 2.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
