# Python 3.11.0 alpha 7 / core and builtins / drop f state field out pyinterpreterframe struct

[bpo-47045](https://bugs.python.org/issue?@action=redirect&bpo=47045): Drop the `f_state` field out of the _PyInterpreterFrame struct. A new `owner` field on the _PyInterpreterFrame struct spells out ownership explicitly, which eases the clearing and deallocation of frames and generators.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
