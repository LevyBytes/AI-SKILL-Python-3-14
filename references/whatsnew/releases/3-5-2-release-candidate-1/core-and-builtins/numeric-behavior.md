# Python 3.5.2 release candidate 1 / core and builtins / numeric behavior

[bpo-24731](https://bugs.python.org/issue?@action=redirect&bpo=24731): A crash is fixed that happened while converting objects whose special methods __bytes__, __trunc__, and __float__ return instances of subclasses of bytes, int, and float into subclasses of bytes, int, and float respectively.

[bpo-26171](https://bugs.python.org/issue?@action=redirect&bpo=26171): A potential integer overflow plus heap corruption inside zipimporter.get_data() has been addressed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
