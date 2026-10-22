# Python 3.10.0 alpha 2 / core and builtins / locale

[bpo-41894](https://bugs.python.org/issue?@action=redirect&bpo=41894): During a native module load that ends in failure, head off a possible UnicodeDecodeError outside of a UTF-8 locale by decoding the load error text through the encoding of the current locale.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
