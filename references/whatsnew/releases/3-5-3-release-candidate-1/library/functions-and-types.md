# Python 3.5.3 release candidate 1 / library / functions and types

[bpo-28485](https://bugs.python.org/issue?@action=redirect&bpo=28485): Always raise ValueError for a negative `compileall.compile_dir(workers=...)` parameter, even where multithreading is not available.

[bpo-20491](https://bugs.python.org/issue?@action=redirect&bpo=20491): The textwrap.TextWrapper class now respects non-breaking spaces. The work builds on a patch from Kaarle Ritvanen.

[bpo-25651](https://bugs.python.org/issue?@action=redirect&bpo=25651): Permit false values to serve as the msg parameter of subTest().

[bpo-24594](https://bugs.python.org/issue?@action=redirect&bpo=24594): Now validates the persist parameter at MSI database open time.

[bpo-17582](https://bugs.python.org/issue?@action=redirect&bpo=17582): xml.etree.ElementTree now keeps whitespace inside attributes intact. Duane Griffin wrote the patch; Stefan Behnel handled review and sign-off.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
