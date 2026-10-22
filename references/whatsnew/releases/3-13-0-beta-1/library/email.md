# Python 3.13.0 beta 1 / library / email

[gh-117313](https://github.com/python/cpython/issues/117313): Only `'\n'`, `'\r'` and `'\r\n'` count as line separators when re-folding the [`email`](https://docs.python.org/3.14/library/email.html#module-email) messages. The control characters `'\v'`, `'\f'`, `'\x1c'`, `'\x1d'` and `'\x1e'`, plus the Unicode line separators `'\x85'`, `'\u2028'` and `'\u2029'`, are now left untouched.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
