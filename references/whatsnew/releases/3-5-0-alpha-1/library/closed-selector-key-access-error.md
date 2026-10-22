# Python 3.5.0 alpha 1 / library / closed selector triggers runtimeerror selectors baseselector get key

[bpo-23209](https://bugs.python.org/issue?@action=redirect&bpo=23209): A closed selector now triggers a RuntimeError from selectors.BaseSelector.get_key(). Meanwhile selectors.BaseSelector.close() drops its internal pointer to the selector mapping so that a reference cycle is broken. Martin Richard authored the first patch. (See also: [bpo-23225](https://bugs.python.org/issue?@action=redirect&bpo=23225))

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
