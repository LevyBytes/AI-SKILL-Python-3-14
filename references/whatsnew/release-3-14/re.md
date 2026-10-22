# What's new in Python 3.14 / re — re

### re

- Support `\z` as a synonym for `\Z` in [`regular expressions`](https://docs.python.org/3.14/library/re.html#module-re). Numerous other regular expression engines read it without ambiguity, in contrast to `\Z`, whose behavior differs in subtle ways. (Contributed by Serhiy Storchaka in [gh-133306](https://github.com/python/cpython/issues/133306).)

- `\B` in [`regular expression`](https://docs.python.org/3.14/library/re.html#module-re) now matches the empty input string, so that it now always serves as the exact opposite of `\b`. (Contributed by Serhiy Storchaka in [gh-124130](https://github.com/python/cpython/issues/124130).)

[Subject index](INDEX.md) · [Previous source section](pydoc.md) · [Next source section](socket.md) · [Release/subject declaration](summary-release-highlights.md)
