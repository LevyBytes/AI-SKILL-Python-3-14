# What's New In Python 3.13 / email - email.generator, email.policy, email.utils

### email

- Headers carrying embedded newlines are henceforth quoted as they are emitted. The [`generator`](https://docs.python.org/3.14/library/email.generator.html#module-email.generator) henceforth declines to serialize (write) any header folded or delimited so badly that it would read back as several headers or merge with neighboring data. Should you wish to disable this safeguard, set [`verify_generated_headers`](https://docs.python.org/3.14/library/email.policy.html#email.policy.Policy.verify_generated_headers). (Contributed by Bas Bloemsaat and Petr Viktorin in [gh-121650](https://github.com/python/cpython/issues/121650).)

- [`getaddresses()`](https://docs.python.org/3.14/library/email.utils.html#email.utils.getaddresses) plus [`parseaddr()`](https://docs.python.org/3.14/library/email.utils.html#email.utils.parseaddr) henceforth yield `('', '')` pairs across a wider set of cases involving invalid email addresses, rather than handing back values that might mislead. Both functions gained a fresh optional *strict* parameter (defaulting to `True`). For the former behavior, which tolerated malformed input, pass `strict=False`. Use `getattr(email.utils, 'supports_strict_parsing', False)` to detect whether the *strict* parameter exists. (Contributed by Thomas Dwyer and Victor Stinner for [gh-102988](https://github.com/python/cpython/issues/102988) to improve the [**CVE 2023-27043**](https://www.cve.org/CVERecord?id=CVE-2023-27043) fix.)

[Subject index](INDEX.md) · [Previous source section](doctest.md) · [Next source section](enum.md) · [Release/subject declaration](summary-release-highlights.md)
