# Python 3.7.0 alpha 2 / library / argparse

[bpo-26510](https://bugs.python.org/issue?@action=redirect&bpo=26510): By default, argparse subparsers are now mandatory. That mirrors how Python 2 behaved. Where optional subparsers are wanted, supply the new `add_subparsers(required=False)` parameter. Anthony Sottile wrote the patch. (Starting with 3.7.0rc1, the default reverted to not required, matching the behavior since Python 3.3.)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
