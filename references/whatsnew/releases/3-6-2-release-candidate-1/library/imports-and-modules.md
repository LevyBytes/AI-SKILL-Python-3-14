# Python 3.6.2 release candidate 1 / library / imports and modules

[bpo-28556](https://bugs.python.org/issue?@action=redirect&bpo=28556): Several changes landed in the typing module: introduce the typing.NoReturn type, employ WrapperDescriptorType, plus small bug-fixes. Jim Fasarakis-Hilliard and Ivan Levkivskyi authored the original PRs.

[bpo-30645](https://bugs.python.org/issue?@action=redirect&bpo=30645): Corrected the path computation within imp.load_package(), repairing the situation where a package arrives carrying only bytecodes. Alexandru Ardelean wrote the patch.

[bpo-28556](https://bugs.python.org/issue?@action=redirect&bpo=28556): typing module updates: a generic AsyncContextManager is added, and ContextManager support reaches every version. Jelle Zijlstra and Ivan Levkivskyi authored the original PRs

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
