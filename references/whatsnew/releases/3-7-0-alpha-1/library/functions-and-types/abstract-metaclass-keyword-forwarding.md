# Python 3.7.0 alpha 1 / library / abcmeta new takes kwargs lets abstract base classes pass keyword

[bpo-29581](https://bugs.python.org/issue?@action=redirect&bpo=29581): ABCMeta.__new__ now takes `**kwargs`, which lets abstract base classes pass keyword parameters along to __init_subclass__. Nate Soares provided the patch.

[Subject index](INDEX.md) · [Release version, date and status](../../release-overview/overview.md)
