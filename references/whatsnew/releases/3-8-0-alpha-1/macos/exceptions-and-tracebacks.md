# Python 3.8.0 alpha 1 / macos / exceptions and tracebacks

[bpo-33635](https://bugs.python.org/issue?@action=redirect&bpo=33635): Under macOS, calling stat on certain file descriptors (/dev/fd/3 for example) yields a bad file descriptor OSError. A guard against that exception was inserted into is_dir, is_file and comparable methods. Because DirEntry.is_dir may likewise raise this exception, _RecursiveWildcardSelector._iterate_directories was additionally given the same error-suppressing behaviour.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
