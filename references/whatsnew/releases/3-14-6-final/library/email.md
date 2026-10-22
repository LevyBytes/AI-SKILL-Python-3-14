# Python 3.14.6 final / library / email

[gh-88726](https://github.com/python/cpython/issues/88726): The [`email`](https://docs.python.org/3.14/library/email.html#module-email) package now adopts the standard MIME charset names “gb2312” and “big5” in place of the non-standard “eucgb2312_cn” and “big5_tw”.

[gh-128110](https://github.com/python/cpython/issues/128110): Repair a defect in parsing [`email`](https://docs.python.org/3.14/library/email.html#module-email) address headers that, under a modern email policy, could leave stray spaces inside the decoded text. Whitespace separating two adjacent [**RFC 2047**](https://datatracker.ietf.org/doc/html/rfc2047.html) encoded-words is now dropped, in line with section 6.2 (and matching the existing handling of unstructured headers such as *Subject*).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
