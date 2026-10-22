# What's New In Python 3.11 / os — os

### os

- Under Windows, [`os.urandom()`](https://docs.python.org/3.14/library/os.html#os.urandom) now calls `BCryptGenRandom()` in place of the deprecated `CryptGenRandom()`. (Contributed by Donghee Na in [bpo-44611](https://bugs.python.org/issue?@action=redirect&bpo=44611).)

[Subject index](INDEX.md) · [Previous source section](operator.md) · [Next source section](pathlib.md) · [Release/subject declaration](summary-release-highlights.md)
