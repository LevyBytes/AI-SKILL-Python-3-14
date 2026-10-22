# Python 3.5.0 alpha 1 / core and builtins / errno

[bpo-22206](https://bugs.python.org/issue?@action=redirect&bpo=22206): When pthread is in use, PyThread_create_key() now sets errno to ENOMEM and gives back -1 (error) upon integer overflow.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
