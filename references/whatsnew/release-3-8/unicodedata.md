# What’s New In Python 3.8 / unicodedata — unicodedata

### unicodedata

The [`unicodedata`](https://docs.python.org/3.14/library/unicodedata.html#module-unicodedata) module was bumped to adopt the [Unicode 12.1.0](https://blog.unicode.org/2019/05/unicode-12-1-en.html) release.

A new [`is_normalized()`](https://docs.python.org/3.14/library/unicodedata.html#unicodedata.is_normalized) function lets you confirm that a string sits in a given normal form, frequently a good deal quicker than performing the normalization itself. (Contributed by Max Belanger, David Euresti, and Greg Price in [bpo-32285](https://bugs.python.org/issue?@action=redirect&bpo=32285) and [bpo-37966](https://bugs.python.org/issue?@action=redirect&bpo=37966)).

[Subject index](INDEX.md) · [Previous source section](typing.md) · [Next source section](unittest.md) · [Release/subject declaration](assignment-expressions.md)
