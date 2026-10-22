# Python 3.6.2 release candidate 1 / library / files and paths

[bpo-29998](https://bugs.python.org/issue?@action=redirect&bpo=29998): Copying and pickling an ImportError now retains the name and path attributes.

[bpo-25803](https://bugs.python.org/issue?@action=redirect&bpo=25803): Prevent the wrong errors that Path.mkdir(exist_ok=True) raised whenever the OS favors errors like EACCES ahead of EEXIST.

[bpo-25455](https://bugs.python.org/issue?@action=redirect&bpo=25455): Corrected crashes in the repr of buffered file-like objects that are recursive.

[bpo-30177](https://bugs.python.org/issue?@action=redirect&bpo=30177): path.resolve(strict=False) no longer truncates the path past the first element absent from the filesystem. Antoine Pietri contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
