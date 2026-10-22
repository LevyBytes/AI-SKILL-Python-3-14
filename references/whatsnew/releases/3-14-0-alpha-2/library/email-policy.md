# Python 3.14.0 alpha 2 / library / email policy

[gh-124452](https://github.com/python/cpython/issues/124452): Repair a problem within [`email.policy.EmailPolicy.header_source_parse()`](https://docs.python.org/3.14/library/email.policy.html#email.policy.EmailPolicy.header_source_parse) plus [`email.policy.Compat32.header_source_parse()`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Compat32.header_source_parse) that added bogus leading whitespace onto header values whenever a header carries a newline following the header name delimiter (`:`) and ahead of the value.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
