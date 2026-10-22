# Python 3.8.0 beta 1 / library / fileinput

[bpo-36952](https://bugs.python.org/issue?@action=redirect&bpo=36952): The **bufsize** argument of [`fileinput.input()`](https://docs.python.org/3.14/library/fileinput.html#fileinput.input) and [`fileinput.FileInput`](https://docs.python.org/3.14/library/fileinput.html#fileinput.FileInput) is gone (it had been deprecated and disregarded ever since Python 3.6), and consequently the **mode** plus **openhook** arguments are now keyword-only.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
