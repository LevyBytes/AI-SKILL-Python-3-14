# Python 3.5.4 release candidate 1 / library / imports and modules

[bpo-28556](https://bugs.python.org/issue?@action=redirect&bpo=28556): Assorted typing module updates: a typing.NoReturn type is added, WrapperDescriptorType is used, and minor bugs are fixed. Jim Fasarakis-Hilliard and Ivan Levkivskyi wrote the original PRs.

[bpo-30645](https://bugs.python.org/issue?@action=redirect&bpo=30645): Repair the path calculation in imp.load_package(), making it work for the case where a package ships with bytecodes alone. Alexandru Ardelean contributed the patch.

[bpo-28556](https://bugs.python.org/issue?@action=redirect&bpo=28556): typing module updates: a generic AsyncContextManager is added, and ContextManager support arrives on every version. Jelle Zijlstra and Ivan Levkivskyi wrote the original PRs

[bpo-28556](https://bugs.python.org/issue?@action=redirect&bpo=28556): Several improvements landed in the typing module: typing.Counter, typing.ChainMap, better ABC caching, and more. The initial PRs came from Jelle Zijlstra, Ivan Levkivskyi, Manuel Krebber, and ??ukasz Langa.

[bpo-29011](https://bugs.python.org/issue?@action=redirect&bpo=29011): Close a notable gap by registering Deque within the typing module.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
