# Python 3.6.0 beta 1 / library / mmap

[bpo-27137](https://bugs.python.org/issue?@action=redirect&bpo=27137): For subclassing, pickling and text-representation behavior, the pure Python fallback of `functools.partial` now lines up with its accelerated C version. Emanuel Barry and Serhiy Storchaka wrote the patch.

- Heads off possible integer overflows and crashes within the mmap module under unusual usage patterns.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
