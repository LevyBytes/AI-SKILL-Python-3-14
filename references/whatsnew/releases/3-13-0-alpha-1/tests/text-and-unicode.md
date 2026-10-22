# Python 3.13.0 alpha 1 / tests / text and unicode

[gh-81005](https://github.com/python/cpython/issues/81005): The String tests got revised to capture that `str` and `unicode` became merged within Python 3. Daniel Fortunov supplied the patch.

[gh-109237](https://github.com/python/cpython/issues/109237): Repaired `test_site.test_underpth_basic()` for the case where the working directory holds one or more non-ASCII characters: encode the `._pth` file as UTF-8 and turn on UTF-8 Mode so the child process stdout uses UTF-8. Victor Stinner authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
