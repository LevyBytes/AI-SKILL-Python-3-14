# Python 3.9.0 alpha 1 / library / exceptions and tracebacks

[bpo-36993](https://bugs.python.org/issue?@action=redirect&bpo=36993): Better error reporting now applies to corrupt zip files carrying bad zip64 extra data. Daniel Hillier contributed the patch.

[bpo-36991](https://bugs.python.org/issue?@action=redirect&bpo=36991): Addresses a possible spurious AttributeError exception leaking out of ZipFile.extract() under some unsupported input error conditions.

[bpo-37834](https://bugs.python.org/issue?@action=redirect&bpo=37834): Stopped a shutil.rmtree exception on non-Windows builds that lack fd system call support, such as older macOS releases.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
