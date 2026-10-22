# What's New In Python 3.4 / audioop

### audioop

`audioop` has gained handling for 24-bit samples. (Contributed by Serhiy Storchaka in [bpo-12866](https://bugs.python.org/issue?@action=redirect&bpo=12866).)

A new `byteswap()` function flips big-endian samples into little-endian and the other way round. (Contributed by Serhiy Storchaka in [bpo-19641](https://bugs.python.org/issue?@action=redirect&bpo=19641).)

Every `audioop` function will now take any [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object). Strings stay disallowed: they never worked previously, and now they raise an error immediately. (Contributed by Serhiy Storchaka in [bpo-16685](https://bugs.python.org/issue?@action=redirect&bpo=16685).)

[Subject index](INDEX.md) · [Previous source section](argparse.md) · [Next source section](base64.md) · [Release/subject declaration](release-highlights.md)
