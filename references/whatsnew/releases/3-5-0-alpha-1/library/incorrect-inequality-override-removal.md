# Python 3.5.0 alpha 1 / library / stripped out incorrect ne implementations failed return notimplemented whenever

[bpo-21408](https://bugs.python.org/issue?@action=redirect&bpo=21408): Stripped out the incorrect __ne__() implementations that failed to return NotImplemented whenever __eq__() returned NotImplemented. The default __ne__() now behaves correctly.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
