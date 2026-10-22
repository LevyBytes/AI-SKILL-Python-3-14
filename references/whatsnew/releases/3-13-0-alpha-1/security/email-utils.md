# Python 3.13.0 alpha 1 / security / email utils

[gh-102988](https://github.com/python/cpython/issues/102988): The [`email.utils`](https://docs.python.org/3.14/library/email.utils.html#module-email.utils) security hardening shipped in 3.12beta4 was rolled back, since it had accidentally broken [`email.utils.getaddresses`](https://docs.python.org/3.14/library/email.utils.html#email.utils.getaddresses) for addresses whose quoted name field carried a comma. Refer to [gh-106669](https://github.com/python/cpython/issues/106669).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
