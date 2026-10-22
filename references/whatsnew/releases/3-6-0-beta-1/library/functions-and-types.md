# Python 3.6.0 beta 1 / library / functions and types

[bpo-27866](https://bugs.python.org/issue?@action=redirect&bpo=27866): A new SSLContext.get_ciphers() method returns every enabled cipher.

[bpo-27832](https://bugs.python.org/issue?@action=redirect&bpo=27832): Turn the `_normalize` argument on the `Fraction` constructor keyword-only, which makes `Fraction(2, 3, 4)` raise `TypeError` now.

[bpo-24594](https://bugs.python.org/issue?@action=redirect&bpo=24594): Validates persist parameter when opening MSI database

[bpo-17582](https://bugs.python.org/issue?@action=redirect&bpo=17582): xml.etree.ElementTree now keeps whitespace within attributes (Duane Griffin wrote the patch. Stefan Behnel reviewed and approved it.)

[bpo-28485](https://bugs.python.org/issue?@action=redirect&bpo=28485): Raise ValueError for a negative compileall.compile_dir(workers=…) parameter in every case, including when multithreading isn’t available.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
