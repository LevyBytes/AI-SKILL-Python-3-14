# Python 3.11.0 alpha 1 / core and builtins / constants

[bpo-45056](https://bugs.python.org/issue?@action=redirect&bpo=45056): The compiler now strips trailing unused constants out of co_consts.

[bpo-45000](https://bugs.python.org/issue?@action=redirect&bpo=45000): Trying to delete [`__debug__`](https://docs.python.org/3.14/library/constants.html#debug__) now triggers a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError). Donghee Na contributed the patch.

[bpo-44633](https://bugs.python.org/issue?@action=redirect&bpo=44633): Substituting wrong types into the union type's parameters now raises `TypeError` rather than handing back [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
