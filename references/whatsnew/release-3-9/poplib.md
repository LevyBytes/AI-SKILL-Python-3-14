# What's New In Python 3.9 / poplib — poplib

### poplib

When the constructor of [`POP3`](https://docs.python.org/3.14/library/poplib.html#poplib.POP3) or [`POP3_SSL`](https://docs.python.org/3.14/library/poplib.html#poplib.POP3_SSL) is given a timeout of zero, it now raises a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) to avoid producing a non-blocking socket. (Contributed by Donghee Na in [bpo-39259](https://bugs.python.org/issue?@action=redirect&bpo=39259).)

[Subject index](INDEX.md) · [Previous source section](pdb.md) · [Next source section](pprint.md) · [Release/subject declaration](summary-release-highlights.md)
