# Python 3.14.3 final / security / email generator

[gh-144125](https://github.com/python/cpython/issues/144125): Headers that are unsafely folded or delimited will no longer be serialized (written) by [`BytesGenerator`](https://docs.python.org/3.14/library/email.generator.html#email.generator.BytesGenerator); consult [`verify_generated_headers`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Policy.verify_generated_headers). Bas Bloemsaat and Petr Viktorin contributed this — see [gh-121650](https://github.com/python/cpython/issues/121650).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
