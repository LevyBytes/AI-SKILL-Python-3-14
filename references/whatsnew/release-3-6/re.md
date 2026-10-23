# What's New In Python 3.6 / re - re

### re

Modifier spans within regular expressions are now supported. For instance, `'(?i:p)ython'` matches `'python'` and `'Python'`, but not `'PYTHON'`; meanwhile `'(?i)g(?-i:v)r'` matches `'GvR'` and `'gvr'`, but not `'GVR'`. (Contributed by Serhiy Storchaka in [bpo-433028](https://bugs.python.org/issue?@action=redirect&bpo=433028).)

Reaching match object groups via `__getitem__` now works and mirrors `group()`. Thus `mo['name']` is now equivalent to `mo.group('name')`. (Contributed by Eric Smith in [bpo-24454](https://bugs.python.org/issue?@action=redirect&bpo=24454).)

As group indices, [`Match`](https://docs.python.org/3.14/library/re.html#re.Match) objects now accept [`index-like objects`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__). (Contributed by Jeroen Demeyer and Xiang Zhang in [bpo-27177](https://bugs.python.org/issue?@action=redirect&bpo=27177).)

[Subject index](INDEX.md) · [Previous source section](random.md) · [Next source section](readline.md) · [Release/subject declaration](summary-release-highlights.md)
