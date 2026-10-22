# Python 3.13.0 alpha 1 / windows / os path

[gh-82367](https://github.com/python/cpython/issues/82367): [`os.path.realpath()`](https://docs.python.org/3.14/library/os.path.html#os.path.realpath) henceforth resolves MS-DOS style file names even where the file cannot be accessed. Moonsik Park supplied the patch.

[gh-106242](https://github.com/python/cpython/issues/106242): Makes [`realpath()`](https://docs.python.org/3.14/library/os.path.html#os.path.realpath) act consistently once it gets a path holding an embedded null character on Windows. Under strict mode it now throws [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) in place of the surprising [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError), and outside strict mode it will turn the path absolute.

[gh-104803](https://github.com/python/cpython/issues/104803): A new [`os.path.isdevdrive()`](https://docs.python.org/3.14/library/os.path.html#os.path.isdevdrive) reports whether a given path sits on a Windows Dev Drive. Where Dev Drive support is missing the call yields `False`, and the function does not exist at all away from Windows.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
