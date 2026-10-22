# Python 3.13.0 alpha 1 / library / email utils

[gh-109653](https://github.com/python/cpython/issues/109653): Cut the import time of [`email.utils`](https://docs.python.org/3.14/library/email.utils.html#module-email.utils) by roughly 43%. As a knock-on effect the import time of [`email.message`](https://docs.python.org/3.14/library/email.message.html#module-email.message) drops by roughly 18%, which then shaves the import time of [`importlib.metadata`](https://docs.python.org/3.14/library/importlib.metadata.html#module-importlib.metadata) by roughly 6%. Alex Waygood supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
