# tarfile: `TarFile.open()`, `TarFile.getmember()`, `TarFile.getmembers()`, `TarFile.getnames()`, `TarFile.list()`, `TarFile.next()`, `TarFile.extractall()`, `TarFile.extract()`

*classmethod *TarFile.open(*...*)

Alternative constructor. The `tarfile.open()` function is actually a shortcut to this classmethod.

 TarFile.getmember(*name*)

Hand back a `TarInfo` object for the member *name*. When *name* cannot be located in the archive, [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) is raised.

Note

Where the same member shows up several times within the archive, the final appearance is taken to be the freshest version.

 TarFile.getmembers()

Hand back the archive's members as a list of `TarInfo` objects. That list preserves the same ordering the members have in the archive.

 TarFile.getnames()

Hand back the members as a list of their names. Its ordering matches the list that `getmembers()` returns.

 TarFile.list(*verbose=True*, ***, *members=None*)

Print a table of contents onto `sys.stdout`. With *verbose* at [`False`](https://docs.python.org/3.14/library/constants.html#False), nothing but the member names is shown. With it at [`True`](https://docs.python.org/3.14/library/constants.html#True), the output looks much like that of **ls -l**. Where the optional *members* is given, it must be a subset of what `getmembers()` returns.

Changed in version 3.5: Added the *members* parameter.

 TarFile.next()

Hand back the archive's next member as a `TarInfo` object, while `TarFile` is open for reading. Return [`None`](https://docs.python.org/3.14/library/constants.html#None) once nothing more is available.

 TarFile.extractall(*path='.'*, *members=None*, ***, *numeric_owner=False*, *filter=None*)

Draw every member out of the archive into the current working directory, or into directory *path*. Where the optional *members* is given, it must be a subset of what `getmembers()` returns. Directory details like owner, modification time and permissions are set only once all members are out. This sidesteps a pair of problems: creating a file inside a directory resets that directory’s modification time, and a directory whose permissions deny writing cannot receive extracted files at all.

With *numeric_owner* set to [`True`](https://docs.python.org/3.14/library/constants.html#True), the extracted files take their owner/group from the uid and gid numbers stored in the tarfile. Failing that, the named values held in the tarfile apply.

The *filter* argument decides how each of the `members` is reshaped or turned away before extraction. The Extraction filters section spells this out. Reach for an explicit setting only when specific *tar* features matter, or use `filter='data'` to stay safe on Python releases with a weaker default (3.13 and earlier).

Warning

Never extract archives from untrusted sources without prior inspection.

From Python 3.14 onward, the default (`data`) wards off the gravest security problems. It will not, however, stop *every* unintended or insecure behavior. The Extraction filters section spells out the rest.

Changed in version 3.5: Added the *numeric_owner* parameter.

Changed in version 3.6: The *path* parameter accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.12: Added the *filter* parameter.

Changed in version 3.14: The *filter* parameter now defaults to `'data'`.

 TarFile.extract(*member*, *path=''*, *set_attrs=True*, ***, *numeric_owner=False*, *filter=None*)

Draw a single member out of the archive into the current working directory under its full name. Its file information is recreated as accurately as the system allows. The *member* argument may be a filename or a `TarInfo` object. You can point at another directory via *path*, which may be a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object). The file attributes (owner, mtime, mode) get set unless *set_attrs* is false.

The *numeric_owner* and *filter* arguments are the same as for `extractall()`.

Note

Several extraction concerns go unhandled by the `extract()` method. For most situations the `extractall()` method is the better choice to reach for.

Warning

Archives from untrusted sources must never be extracted before you inspect them. The warning on `extractall()` covers the details.

Changed in version 3.2: Added the *set_attrs* parameter.

Changed in version 3.5: Added the *numeric_owner* parameter.

Changed in version 3.6: The *path* parameter accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

Changed in version 3.12: Added the *filter* parameter.

[Subject index](INDEX.md) · [Previous](tarfile-tarfile-class.md) · [Continue](tarfile-extractfile-to-tarfile-addfile.md) · [Owning module, declaration or section: tarfile](tarfile-read-and-write-tar-archive-files.md) · [Owning module, declaration or section: tarfile.TarFile](tarfile-tarfile-class.md) · [Owning module, declaration or section: TarFile Objects](tarfile-tarfile-class.md)
