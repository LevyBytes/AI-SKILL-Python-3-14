# What's New In Python 3.7 / enum — enum

### enum

A fresh `_ignore_` class property on the [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum) lets you spell out the names of properties that ought not turn into enum members. (Contributed by Ethan Furman in [bpo-31801](https://bugs.python.org/issue?@action=redirect&bpo=31801).)

Starting with Python 3.8, testing for non-Enum objects inside [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum) classes raises a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) (for example, `1 in Color`); likewise, testing for non-Flag objects against a [`Flag`](https://docs.python.org/3.14/library/enum.html#enum.Flag) member raises `TypeError` (for example, `1 in Perm.RW`); for now, both of those return [`False`](https://docs.python.org/3.14/library/constants.html#False) and carry a deprecation. (Contributed by Ethan Furman in [bpo-33217](https://bugs.python.org/issue?@action=redirect&bpo=33217).)

### enum

From Python 3.8 onward, testing for non-Enum objects within [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum) classes will trigger a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) (for example `1 in Color`); in the same way, testing for non-Flag objects against a [`Flag`](https://docs.python.org/3.14/library/enum.html#enum.Flag) member will trigger `TypeError` (for example `1 in Perm.RW`); right now each of these checks yields [`False`](https://docs.python.org/3.14/library/constants.html#False) rather than raising. (Contributed by Ethan Furman in [bpo-33217](https://bugs.python.org/issue?@action=redirect&bpo=33217).)

[Subject index](INDEX.md) · [Previous source section](distutils.md) · [Next source section](functools.md) · [Release/subject declaration](summary-release-highlights.md) · [Previous source section](dbm.md) · [Next source section](gettext.md)
