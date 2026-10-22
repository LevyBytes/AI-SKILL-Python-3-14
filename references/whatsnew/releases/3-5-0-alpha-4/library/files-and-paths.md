# Python 3.5.0 alpha 4 / library / files and paths

[bpo-23752](https://bugs.python.org/issue?@action=redirect&bpo=23752): Constructed from an existing file descriptor, io.FileIO() now invokes fstat() a single time. Previously fstat() ran twice, which served no purpose.

[bpo-10395](https://bugs.python.org/issue?@action=redirect&bpo=10395): os.path.commonpath() was added. Both posixpath and ntpath implement it. Rafik Draoui's patch served as the basis.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
