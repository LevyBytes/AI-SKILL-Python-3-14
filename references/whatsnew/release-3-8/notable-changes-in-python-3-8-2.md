# What’s New In Python 3.8 / Notable changes in Python 3.8.2 — shutil

### Notable changes in Python 3.8.2

A regression affecting the `ignore` callback belonging to [`shutil.copytree()`](https://docs.python.org/3.14/library/shutil.html#shutil.copytree) was corrected. Its argument types have reverted to str and List[str]. (The work here came from Manuel Barkhau and Giampaolo Rodola under [gh-83571](https://github.com/python/cpython/issues/83571).)

[Subject index](INDEX.md) · [Previous source section](notable-changes-in-python-3-8-1.md) · [Next source section](notable-changes-in-python-3-8-3.md) · [Release/subject declaration](assignment-expressions.md)
