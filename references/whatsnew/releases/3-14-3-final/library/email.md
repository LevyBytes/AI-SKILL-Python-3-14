# Python 3.14.3 final / library / email

[gh-142517](https://github.com/python/cpython/issues/142517): The [`email`](https://docs.python.org/3.14/library/email.html#module-email) policies other than `compat32` now properly refold encoded words holding bytes that cannot be decoded under the character set they declare. That situation used to raise an encoding exception while folding.

[gh-79986](https://github.com/python/cpython/issues/79986): The [`email`](https://docs.python.org/3.14/library/email.html#module-email) library gains parsing of the `References` and `In-Reply-To` headers, treating their content as lists of message id tokens. As a result they are no longer folded the wrong way.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
