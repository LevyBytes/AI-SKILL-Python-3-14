# Python 3.14.3 final / library / email policy

[gh-142006](https://github.com/python/cpython/issues/142006): Correct a defect in the [`email.policy.default`](https://docs.python.org/3.14/library/email.policy.html#email.policy.default) folding logic that wrongly produced a doubled newline whenever a line that ended precisely at max_line_length was trailed by an unfoldable token.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
