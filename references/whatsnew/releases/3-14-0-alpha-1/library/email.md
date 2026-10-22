# Python 3.14.0 alpha 1 / library / email

[gh-118643](https://github.com/python/cpython/issues/118643): Resolve an AttributeError within the [`email`](https://docs.python.org/3.14/library/email.html#module-email) module that arose while re-folding a lengthy address list. Also correct further cases where the address separator within the address list was encoded wrongly.

[gh-92081](https://github.com/python/cpython/issues/92081): Spaces that go missing from email headers when they are interleaved with encoded 8-bit characters are now restored.

[gh-121650](https://github.com/python/cpython/issues/121650): [`email`](https://docs.python.org/3.14/library/email.html#module-email) headers carrying embedded newlines now get quoted on output. The [`generator`](https://docs.python.org/3.14/library/email.generator.html#module-email.generator) will decline to serialize (write) any header folded or delimited in an unsafe way; refer to [`verify_generated_headers`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Policy.verify_generated_headers). Bas Bloemsaat and Petr Viktorin contributed this work ([gh-121650](https://github.com/python/cpython/issues/121650)).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
