# Python 3.13.0 alpha 3 / library / email utils

[gh-102988](https://github.com/python/cpython/issues/102988): In a wider range of cases where an invalid email address is found, [`email.utils.getaddresses()`](https://docs.python.org/3.14/library/email.utils.html#email.utils.getaddresses) and [`email.utils.parseaddr()`](https://docs.python.org/3.14/library/email.utils.html#email.utils.parseaddr) now hand back `('', '')` 2-tuples rather than values that might be inaccurate. An optional *strict* parameter joins both functions: pass `strict=False` to restore the former behavior and tolerate malformed inputs. To test whether the *strict* parameter exists, you can use `getattr(email.utils, 'supports_strict_parsing', False)`. To strengthen the [**CVE 2023-27043**](https://www.cve.org/CVERecord?id=CVE-2023-27043) fix, Thomas Dwyer and Victor Stinner supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
