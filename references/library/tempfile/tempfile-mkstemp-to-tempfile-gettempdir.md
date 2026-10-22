# tempfile: `tempfile.mkstemp()`, `tempfile.mkdtemp()`, `tempfile.gettempdir()`

tempfile.mkstemp(*suffix=None*, *prefix=None*, *dir=None*, *text=False*)

Builds a temporary file as securely as can be managed. Its creation is free of race conditions, provided the platform implements the [`os.O_EXCL`](https://docs.python.org/3.14/library/os.html#os.O_EXCL) flag for [`os.open()`](https://docs.python.org/3.14/library/os.html#os.open) correctly. Read and write access on the file belong to the creating user ID alone. Where the platform signals executability through permission bits, no one is granted execute rights on the file.

The file descriptor is [not inherited by child processes](https://docs.python.org/3.14/library/os.html#fd-inheritance).

In contrast to `TemporaryFile()`, anyone using `mkstemp()` must delete the temporary file once finished with it.

When *suffix* is something other than `None`, the file name closes with that suffix; otherwise no suffix is appended. `mkstemp()` will not insert a dot between the name and the suffix, so if you want one, lead *suffix* with it.

When *prefix* is something other than `None`, the file name opens with that prefix; if not, a default prefix steps in — namely the result of `gettempprefix()` or `gettempprefixb()`, whichever fits.

When *dir* is something other than `None`, the file goes into that directory; otherwise a default directory is used, picked from a platform-dependent list. The application's user can still steer where that lands by setting the *TMPDIR*, *TEMP* or *TMP* environment variables. Consequently there is no promise that the generated filename will be well-behaved — for instance, that it won't need quoting when fed to external commands through `os.popen()`.

When any of *suffix*, *prefix*, and *dir* differ from `None`, they all have to share one type. Should they be bytes, the name returned comes back as bytes rather than str. To force a bytes return value while otherwise keeping the defaults, pass `suffix=b''`.

When *text* is given as true, the file opens in text mode; otherwise, by default, it opens in binary mode.

`mkstemp()` yields a tuple holding an OS-level handle to an open file (such as [`os.open()`](https://docs.python.org/3.14/library/os.html#os.open) would give) followed by that file's absolute pathname, in that sequence.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `tempfile.mkstemp` with argument `fullpath`.

Changed in version 3.5: *suffix*, *prefix*, and *dir* can now be passed as bytes so that a bytes return value results. Before this, str alone was permitted. *suffix* and *prefix* now take, and default to, `None` to trigger a suitable default value.

Changed in version 3.6: The *dir* parameter now accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

 tempfile.mkdtemp(*suffix=None*, *prefix=None*, *dir=None*)

Builds a temporary directory as securely as can be managed. Its creation carries no race conditions. Read, write, and search access on the directory belong to the creating user ID alone.

Whoever uses `mkdtemp()` is responsible for removing the temporary directory along with its contents once finished.

The *prefix*, *suffix*, and *dir* arguments match those of `mkstemp()`.

`mkdtemp()` hands back the absolute pathname of the newly made directory.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `tempfile.mkdtemp` with argument `fullpath`.

Changed in version 3.5: *suffix*, *prefix*, and *dir* can now be passed as bytes so that a bytes return value results. Before this, str alone was permitted. *suffix* and *prefix* now take, and default to, `None` to trigger a suitable default value.

Changed in version 3.6: The *dir* parameter now accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.12: `mkdtemp()` now always returns an absolute path, even when *dir* is relative.

 tempfile.gettempdir()

Hands back the name of the directory where temporary files go. This sets the default for the *dir* argument across every function in this module.

To find a directory the calling user can create files in, Python walks a standard list of candidates. That list runs:

1.

Whatever directory the `TMPDIR` environment variable points to.

2.

Whatever directory the `TEMP` environment variable points to.

3.

Whatever directory the `TMP` environment variable points to.

4.

A location that depends on the platform:

  - On Windows, the directories `C:\TEMP`, `C:\TMP`, `\TEMP`, and `\TMP`, tried in that sequence.

  - Everywhere else, the directories `/tmp`, `/var/tmp`, and `/usr/tmp`, tried in that sequence.

5.

Failing all of those, the current working directory.

What this search turns up gets cached; see the `tempdir` write-up further down.

Changed in version 3.10: Always returns a str. Earlier it would hand back any `tempdir` value of whatever type, so long as it wasn't `None`.

[Subject index](INDEX.md) · [Previous](temporary-directory-lifecycle.md) · [Continue](tempfile-gettempdirb-to-tempfile-tempdir.md) · [Owning module, declaration or section: tempfile](tempfile-generate-temporary-files-and-directories.md)
