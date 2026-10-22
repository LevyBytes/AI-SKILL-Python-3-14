# Python 3.11.0 alpha 3 / library / argparse

[bpo-45235](https://bugs.python.org/issue?@action=redirect&bpo=45235): Backed out an argparse bugfix that introduced a regression in how default arguments for subparsers were handled. The regression stopped leaf level arguments from overriding root level arguments.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
