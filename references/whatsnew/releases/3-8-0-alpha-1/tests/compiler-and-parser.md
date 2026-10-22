# Python 3.8.0 alpha 1 / tests / compiler and parser

[bpo-27643](https://bugs.python.org/issue?@action=redirect&bpo=27643): The Test_C case relies on “signed short” bitfields, yet IBM’s XLC compiler (on AIX) lacks that capability. Bypass the code plus the test when both AIX and XLC apply.

Valid for Python2-2.7 onward.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
