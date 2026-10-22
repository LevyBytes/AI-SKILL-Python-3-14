# Python 3.6.5 release candidate 1 / core and builtins / hash randomization disabled via pythonhashseed sys flags hash randomization value correctly assigned

[bpo-32329](https://bugs.python.org/issue?@action=redirect&bpo=32329): When hash randomization is disabled via `PYTHONHASHSEED=0`, the `sys.flags.hash_randomization` value is correctly assigned 0.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
