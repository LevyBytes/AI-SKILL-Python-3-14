# Python 3.11.0 alpha 7 / library / files and paths

[bpo-20392](https://bugs.python.org/issue?@action=redirect&bpo=20392): Uppercase file-extension inconsistency in `MimeTypes.guess_type()` is now fixed. Kumar Aditya supplied the patch.

[bpo-44439](https://bugs.python.org/issue?@action=redirect&bpo=44439): The `.write()` method on a member file inside `ZipFile` is corrected: previously, when the supplied data was an object supporting the buffer protocol, the recorded file length could come out wrong.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
