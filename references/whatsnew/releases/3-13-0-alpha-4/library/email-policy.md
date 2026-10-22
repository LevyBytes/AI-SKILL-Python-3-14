# Python 3.13.0 alpha 4 / library / email policy

[gh-77749](https://github.com/python/cpython/issues/77749): From now on [`email.policy.EmailPolicy.fold()`](https://docs.python.org/3.14/library/email.policy.html#email.policy.EmailPolicy.fold) encodes every non-ASCII character within headers whenever [`utf8`](https://docs.python.org/3.14/library/email.policy.html#email.policy.EmailPolicy.utf8) evaluates as false.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
