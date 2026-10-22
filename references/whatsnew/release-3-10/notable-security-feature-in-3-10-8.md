# What's New In Python 3.10 / Notable security feature in 3.10.8

### Notable security feature in 3.10.8

No longer will the deprecated `mailcap` module pass unsafe text — filenames, MIME types, parameters — through into shell commands. Rather than feeding such text along, it issues a warning and proceeds as though no match turned up (or, with test commands, as though the test came back unsuccessful). (Contributed by Petr Viktorin in [gh-98966](https://github.com/python/cpython/issues/98966).)

[Subject index](INDEX.md) · [Previous source section](notable-security-feature-in-3-10-7.md) · [Next source section](tarfile.md) · [Release/subject declaration](summary-release-highlights.md)
