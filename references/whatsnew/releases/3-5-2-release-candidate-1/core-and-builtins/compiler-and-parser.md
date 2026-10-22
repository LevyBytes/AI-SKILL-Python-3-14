# Python 3.5.2 release candidate 1 / core and builtins / compiler and parser

[bpo-20120](https://bugs.python.org/issue?@action=redirect&bpo=20120): Switched .pypirc parsing over to RawConfigParser, removing the interpolation support that the move to Python 3 had added unintentionally. Behaviour now performs no interpolation across .pypirc files, lining up with how Python 2.7 and Setuptools 19.0 behave.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
