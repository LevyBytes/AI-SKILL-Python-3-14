# What’s New In Python 3.5 / Other Language Changes - codecs, collections

> PEP written by Petr Viktorin, Stefan Behnel, and Nick Coghlan; implemented by Petr Viktorin.

### Other Language Changes

A handful of more modest adjustments landed in the core Python language:

- Introduced the `"namereplace"` error handlers. Meanwhile the `"backslashreplace"` error handlers gained support for decoding alongside translating. (Contributed by Serhiy Storchaka in [bpo-19676](https://bugs.python.org/issue?@action=redirect&bpo=19676) and [bpo-22286](https://bugs.python.org/issue?@action=redirect&bpo=22286).)

- The [`-b`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-b) option henceforth influences how [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) values compare against [`int`](https://docs.python.org/3.14/library/functions.html#int) values. (Contributed by Serhiy Storchaka in [bpo-23681](https://bugs.python.org/issue?@action=redirect&bpo=23681).)

- Fresh Kazakh `kz1048` plus Tajik `koi8_t` [codecs](https://docs.python.org/3.14/library/codecs.html#standard-encodings) arrived. (Contributed by Serhiy Storchaka in [bpo-22682](https://bugs.python.org/issue?@action=redirect&bpo=22682) and [bpo-22681](https://bugs.python.org/issue?@action=redirect&bpo=22681).)

- Property docstrings can now be assigned to. That proves particularly handy for [`collections.namedtuple()`](https://docs.python.org/3.14/library/collections.html#collections.namedtuple) docstrings. (Contributed by Berker Peksag in [bpo-24064](https://bugs.python.org/issue?@action=redirect&bpo=24064).)

- Circular imports that rely on relative imports now function correctly. (Contributed by Brett Cannon and Antoine Pitrou in [bpo-17636](https://bugs.python.org/issue?@action=redirect&bpo=17636).)

[Subject index](INDEX.md) · [Previous source section](pep-489-multi-phase-extension-module-initialization.md) · [Next source section](typing.md) · [Release/subject declaration](summary-release-highlights.md)
