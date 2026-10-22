# Python 3.5.0 beta 1 / library / files and paths

[bpo-22107](https://bugs.python.org/issue?@action=redirect&bpo=22107): tempfile.gettempdir() together with tempfile.mkdtemp() now retry whenever a directory already exists under the chosen name, on Windows as well as on Unix. On Windows, tempfile.mkstemp() now fails right away if the parent directory is invalid (missing or a file).

[bpo-9246](https://bugs.python.org/issue?@action=redirect&bpo=9246): Under POSIX, paths beyond 1025 bytes are now handled by os.getcwd(). William Orr authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
