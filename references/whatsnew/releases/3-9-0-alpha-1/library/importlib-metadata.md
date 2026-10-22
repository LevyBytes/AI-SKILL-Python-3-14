# Python 3.9.0 alpha 1 / library / importlib metadata

[bpo-38121](https://bugs.python.org/issue?@action=redirect&bpo=38121): Parameter names on importlib.metadata functions were updated to track the changes from the 0.22 release of importlib_metadata.

[bpo-38086](https://bugs.python.org/issue?@action=redirect&bpo=38086): Brought importlib.metadata up to date with changes from [importlib_metadata 0.21](https://gitlab.com/python-devs/importlib_metadata/blob/0.21/importlib_metadata/docs/changelog.rst).

[bpo-37697](https://bugs.python.org/issue?@action=redirect&bpo=37697): Brought `importlib.metadata` into line with [importlib_metadata 0.19](https://gitlab.com/python-devs/importlib_metadata/-/milestones/20); this betters the treatment of EGG-INFO files and clears up a crash arising when colons appeared inside entry point names.

[bpo-38010](https://bugs.python.org/issue?@action=redirect&bpo=38010): Synced `importlib.metadata` with `importlib_metadata` 0.20, which clarifies how `files()` behaves and fixes a case where `requires()` returned only one requirement on `dist-info` packages.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
