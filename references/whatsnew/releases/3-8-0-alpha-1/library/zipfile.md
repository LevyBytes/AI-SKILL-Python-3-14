# Python 3.8.0 alpha 1 / library / zipfile

[bpo-34472](https://bugs.python.org/issue?@action=redirect&bpo=34472): Better compatibility for streamed files in [`zipfile`](https://docs.python.org/3.14/library/zipfile.html#module-zipfile). An optional signature had not been written before, and some ZIP applications went unsupported. Silas Sewell wrote the patch.

[bpo-34035](https://bugs.python.org/issue?@action=redirect&bpo=34035): Several AttributeError problems in zipfile seek() methods have been corrected. Patch by Mickaël Schoentgen.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
