# Python 3.5.0 alpha 3 / library / tests and documentation

[bpo-2211](https://bugs.python.org/issue?@action=redirect&bpo=2211): Reworked how the http.cookies.Morsel class is implemented. Assigning the attributes key, value and coded_value directly is now deprecated. Both update() and setdefault() now transform plus check keys. Equality comparison now factors in the attributes key, value and coded_value. copy() now hands back a Morsel rather than a dict. repr() now holds every attribute. Key checking and value quoting were optimized. New tests were added. Demian Brecht supplied the original patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
