# Python 3.8.0 beta 1 / library / text and unicode

[bpo-36778](https://bugs.python.org/issue?@action=redirect&bpo=36778): The `cp65001` encoding (that is, Windows code page 65001) now serves as an alias pointing at the `utf_8` encoding.

[bpo-36748](https://bugs.python.org/issue?@action=redirect&bpo=36748): Tuned write buffering within the C implementation of `TextIOWrapper`. Pushing an ASCII string into `TextIOWrapper` under ascii, latin1, or utf-8 encoding runs roughly 20% quicker. Inada Naoki authored the patch.

[bpo-34424](https://bugs.python.org/issue?@action=redirect&bpo=34424): Corrects serialization of messages holding encoded strings whenever policy.linesep carries a multi-character string. Jens Troeger supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
