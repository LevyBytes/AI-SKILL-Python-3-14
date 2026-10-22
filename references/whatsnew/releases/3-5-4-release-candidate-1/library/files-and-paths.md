# Python 3.5.4 release candidate 1 / library / files and paths

[bpo-29998](https://bugs.python.org/issue?@action=redirect&bpo=29998): Pickling plus copying an ImportError now keeps the name and path attributes intact.

[bpo-25803](https://bugs.python.org/issue?@action=redirect&bpo=25803): Steer clear of the wrong errors raised by Path.mkdir(exist_ok=True) when the OS prioritizes errors like EACCES ahead of EEXIST.

[bpo-25455](https://bugs.python.org/issue?@action=redirect&bpo=25455): Repaired crashes in the repr of recursive buffered file-like objects.

[bpo-29110](https://bugs.python.org/issue?@action=redirect&bpo=29110): Stop aifc.open() from leaking a file object whenever the file is supplied as a filesystem path and turns out not to be a valid AIFF stream. Anthony Zhang supplied the patch.

[bpo-29416](https://bugs.python.org/issue?@action=redirect&bpo=29416): Guard against an endless loop inside pathlib.Path.mkdir

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
